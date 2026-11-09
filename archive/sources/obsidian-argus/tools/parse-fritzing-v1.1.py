#!/usr/bin/env python3
"""
parse-fritzing-v1.1.py - extract the real wiring from an Argus Vac .fzz
(Fritzing sketch zip) without opening Fritzing or trusting exported images.

v1.1 changes (2026-08-26)
-------------------------
- FIX: a wire's two endpoints are now unioned together. In the .fz XML a wire
  stores its ends as separate <connector> nodes; v1.0 never joined them, so
  every chain broke at every wire and the tool reported 0 connected parts.
- Removed the --from-netlist crutch (that netlist XML was deleted from the
  vault as inaccurate). Pin names now come from, in order:
    1. part definitions embedded in the .fzz itself ('part.<moduleId>.fzp')
    2. tools/fzp_cache/<moduleId>.fzp (downloaded from the official
       fritzing-parts GitHub repo)
    3. raw connector id fallback
- Added --fetch-missing: resolves unknown moduleIds against the fritzing-parts
  git tree API (via curl.exe, since Python SSL is broken on this machine) and
  caches the .fzp files locally. Run it once whenever a sketch gains a new
  standard part; custom parts imported in Fritzing are already embedded in
  the .fzz and need nothing.

Usage
-----
  python tools/parse-fritzing-v1.1.py "5-Hardware/Argus Vac Final.fzz"
  python tools/parse-fritzing-v1.1.py "5-Hardware/Argus Vac Final.fzz" --fetch-missing
"""
import argparse
import io
import json
import os
import subprocess
import sys
import zipfile
import xml.etree.ElementTree as ET
from collections import defaultdict

VAULT_TOOLS = os.path.dirname(os.path.abspath(__file__))
CACHE_DIR = os.path.join(VAULT_TOOLS, "fzp_cache")
REPO = "fritzing/fritzing-parts"
BRANCH = "master"
# Legacy part ids whose files are named differently in fritzing-parts
# (both live under obsolete/ there).
LEGACY_FILENAMES = {
    "7d0bc366bcac9395c747f3a92e2ff843leg": "stepper_motor_bipolar",
    "1000FADF10011leg": "dc_motor",
}


def load_fzp_labels(text):
    """connectorId -> human label ("NAME (description)") from a .fzp definition."""
    root = ET.fromstring(text)
    out = {}
    conns = root.find("connectors")
    if conns is None:
        return out
    for c in conns:
        cid = c.get("id")
        name = c.get("name") or cid
        desc = c.findtext("description")
        desc = desc.strip() if desc else ""
        junk = ("none", "no description yet", name.lower())
        if desc and desc.lower() not in junk and desc != name:
            out[cid] = "%s (%s)" % (name, desc) if name != desc else name
        else:
            out[cid] = name
    return out


class UF:
    def __init__(self):
        self.p = {}

    def find(self, x):
        self.p.setdefault(x, x)
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[rb] = ra


def parse_sketch(fzz_path):
    z = zipfile.ZipFile(fzz_path)
    fz_names = [n for n in z.namelist() if n.endswith(".fz")]
    if not fz_names:
        sys.exit("[ERR] no .fz sketch inside " + fzz_path)
    root = ET.fromstring(z.read(fz_names[0]).decode("utf-8"))

    embedded = {}
    for n in z.namelist():
        if n.startswith("part.") and n.endswith(".fzp"):
            mid = n[len("part."):-len(".fzp")]
            embedded[mid] = load_fzp_labels(z.read(n).decode("utf-8"))

    parts = {}
    uf = UF()
    for inst in root.find("instances"):
        mi = inst.get("modelIndex")
        mod = inst.get("moduleIdRef")
        if mod == "WireModuleID":
            # A wire IS a connection: its own endpoints are one electrical node.
            bb = inst.find("views/breadboardView")
            conns = bb.find("connectors") if bb is not None else None
            if conns is None:
                continue
            ends = []
            for c in conns.findall("connector"):
                mine = (mi, c.get("connectorId"))
                ends.append(mine)
                for cn in c.findall("connects/connect"):
                    uf.union(mine, (cn.get("modelIndex"), cn.get("connectorId")))
            for e in ends[1:]:
                uf.union(ends[0], e)
        else:
            # Parts can also carry direct <connects> (pin-to-pin contact, no wire).
            bb = inst.find("views/breadboardView")
            if bb is not None:
                conns = bb.find("connectors")
                if conns is not None:
                    for c in conns.findall("connector"):
                        mine = (mi, c.get("connectorId"))
                        for cn in c.findall("connects/connect"):
                            uf.union(mine, (cn.get("modelIndex"), cn.get("connectorId")))
            title = (inst.findtext("title") or "").strip() or mod
            parts[mi] = {"title": title, "moduleId": mod}

    nets = defaultdict(set)
    for node in list(uf.p):
        nets[uf.find(node)].add(node)

    real_nets, floating = [], []
    for members in nets.values():
        real = [(mi, cid) for (mi, cid) in members if mi in parts]
        if len(real) >= 2:
            real_nets.append(real)
        elif len(real) == 1:
            floating.append(real[0])
    return parts, embedded, real_nets, floating


def curl(url, dest=None):
    cmd = ["curl.exe", "-fsSL", url]
    if dest:
        cmd += ["-o", dest]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit("[ERR] curl failed (%d) for %s\n%s" % (r.returncode, url, r.stderr.strip()))
    return r.stdout if not dest else None


def fetch_missing(needed):
    """Download .fzp definitions for moduleIds missing from the local cache."""
    os.makedirs(CACHE_DIR, exist_ok=True)
    todo = [m for m in needed if not os.path.exists(os.path.join(CACHE_DIR, m + ".fzp"))]
    if not todo:
        print("[ok ] cache already has all %d needed part definitions" % len(needed))
        return
    idx_path = os.path.join(CACHE_DIR, "index.json")
    if os.path.exists(idx_path):
        index = json.load(io.open(idx_path, encoding="utf-8"))
    else:
        print("[.. ] listing %s file tree (one-time) ..." % REPO)
        data = json.loads(curl("https://api.github.com/repos/%s/git/trees/%s?recursive=1"
                               % (REPO, BRANCH)))
        index = {os.path.basename(t["path"]): t["path"]
                 for t in data.get("tree", []) if t["path"].endswith(".fzp")}
        json.dump(index, io.open(idx_path, "w", encoding="utf-8"), indent=1)
    lower = {k.lower(): v for k, v in index.items()}

    def resolve(mid):
        """repo path for a moduleId: exact name, case-insensitive, or legacy alias."""
        cands = [mid + ".fzp"]
        if mid in LEGACY_FILENAMES:
            cands.append(LEGACY_FILENAMES[mid] + ".fzp")
        for cand in cands:
            if cand in index:
                return index[cand]
        for cand in cands:
            if cand.lower() in lower:
                return lower[cand.lower()]
        return None

    got, missed = [], []
    for mid in todo:
        path = resolve(mid)
        if not path:
            missed.append(mid)
            continue
        dest = os.path.join(CACHE_DIR, mid + ".fzp")
        curl("https://raw.githubusercontent.com/%s/%s/%s" % (REPO, BRANCH, path), dest=dest)
        # sanity: the downloaded definition should carry the moduleId we expect
        root = ET.parse(dest).getroot()
        real_id = root.get("moduleId")
        if real_id and real_id != mid:
            print("[warn] %s: file %s has moduleId '%s' - labels may be wrong"
                  % (mid, path, real_id))
        got.append(mid)
        print("[got] %s  <-  %s" % (mid, path))
    if missed:
        print("[warn] not found in %s (custom parts - embed them by saving from"
              " Fritzing, or drop the .fzp into %s manually):" % (REPO, CACHE_DIR))
        for m in missed:
            print("      " + m)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("fzz", help="path to the .fzz sketch")
    ap.add_argument("--fetch-missing", action="store_true",
                    help="download missing .fzp pin definitions from fritzing-parts")
    ap.add_argument("--quiet", action="store_true", help="skip the console pin table")
    args = ap.parse_args()

    parts, embedded, real_nets, floating = parse_sketch(args.fzz)

    used_mods = {p["moduleId"] for p in parts.values()
                 if p["moduleId"] != "WireModuleID"}
    unlabelled = sorted(m for m in used_mods if m not in embedded)
    if args.fetch_missing:
        fetch_missing(unlabelled)

    cache = {}
    if os.path.isdir(CACHE_DIR):
        for fn in os.listdir(CACHE_DIR):
            if fn.endswith(".fzp"):
                cache[fn[:-len(".fzp")]] = load_fzp_labels(
                    io.open(os.path.join(CACHE_DIR, fn), encoding="utf-8").read())

    def pin_label(mi, cid):
        mod = parts[mi]["moduleId"]
        src = embedded.get(mod) or cache.get(mod) or {}
        return src.get(cid, cid)

    comp = defaultdict(lambda: defaultdict(list))
    for real in real_nets:
        for i, (mi, cid) in enumerate(real):
            others = [(parts[m2]["title"], pin_label(m2, c2))
                      for j, (m2, c2) in enumerate(real) if j != i]
            comp[mi][pin_label(mi, cid)].extend(others)

    if not args.quiet:
        print("=== COMPONENT PIN TABLE (%d connected parts) ===" % len(comp))
        for mi in sorted(comp, key=lambda k: parts[k]["title"].lower()):
            print("\n--- %s (%s) [modelIndex %s] ---"
                  % (parts[mi]["title"], parts[mi]["moduleId"], mi))
            for pin, conns in sorted(comp[mi].items()):
                print("  %-32s -> %s" % (pin, "; ".join("%s [%s]" % t for t in conns)))
        print("\n=== dangling wire ends (no second real pin) ===")
        if not floating:
            print("  (none)")
        for mi, cid in sorted(floating, key=lambda k: parts[k[0]]["title"].lower()):
            print("  %s [%s]" % (parts[mi]["title"], cid))
    still_missing = sorted(m for m in used_mods
                           if m not in embedded and m not in cache)
    if still_missing:
        print("\n[note] parts without pin definitions (raw connector ids shown): %s"
              % ", ".join(still_missing))
        print("       run again with --fetch-missing to pull them from %s" % REPO)
    return 0


if __name__ == "__main__":
    sys.exit(main())
