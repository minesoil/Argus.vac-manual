#!/usr/bin/env python3
"""
vaultsync.py - fast bulk editor for the Argus Vac vault.

Why: doc syncs used to need a hand-written one-off script per change, each with
exact-match anchors that broke when wording moved. This tool makes those passes
single commands, with dry-run previews and hit counts so nothing silently misses.

Ops
---
  replace   literal text swap in one file or every file under a folder
  rename    rename a vault file AND update references to it across md/py files
  registry  rewrite one row of the changelog's Master Registry table by name
  bump      convenience: registry + a history bullet in one call

Examples
--------
  python tools/vaultsync.py replace 4-Software --ext .py --find v10.3 --replace v10.4 --dry-run
  python tools/vaultsync.py rename obstacle-detector-mediapipe-v10.4.py obstacle-detector-mediapipe-v10.4.py
  python tools/vaultsync.py registry --doc "Electrical Wiring" --version 1.4 --date 2026-08-25 --status "Active reference. Fuse now 10 A."
  python tools/vaultsync.py replace HANDOFF.md --find "fuse 7.5 A" --replace "fuse 10 A"

Notes: utf-8 everywhere; skips .obsidian/.git/caches/conversations; literal
matching (no regex surprises); every op prints exactly what it touched.
"""
import argparse
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".obsidian", ".git", ".smart-env", "__pycache__", "node_modules",
             ".claude", ".opencode", ".agents", ".copilot",
             "copilot-conversations"}
SKIP_EXT = {".png", ".jpg", ".jpeg", ".fzz", ".xml", ".base", ".pyc", ".exe",
            ".zip", ".ico", ".tflite", ".run"}


def iter_files(subpath="", exts=None):
    base = os.path.join(ROOT, subpath) if subpath else ROOT
    if os.path.isfile(base):
        yield base
        return
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            ext = os.path.splitext(fn)[1].lower()
            if ext in SKIP_EXT:
                continue
            if exts and ext not in exts:
                continue
            yield os.path.join(dirpath, fn)


def read(p, errors="strict"):
    with io.open(p, encoding="utf-8", errors=errors) as f:
        return f.read()


def write(p, t):
    with io.open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)


def op_replace(args):
    exts = set(args.ext) if args.ext else None
    hits_total = 0
    files_touched = 0
    for p in iter_files(args.path, exts):
        try:
            t = read(p)
        except UnicodeDecodeError:
            continue  # binary/utf16 file - no literal text swap possible
        n = t.count(args.find)
        if n == 0:
            continue
        hits_total += n
        files_touched += 1
        rel = os.path.relpath(p, ROOT)
        if args.dry_run:
            print(f"[dry] {rel}: {n} hit(s)")
        else:
            write(p, t.replace(args.find, args.replace))
            print(f"[ok ] {rel}: {n} replaced")
    print(f"== {'would touch' if args.dry_run else 'touched'} "
          f"{files_touched} file(s), {hits_total} occurrence(s)")
    return 0


def op_rename(args):
    src = None
    dst_exists = False
    for p in iter_files():
        base = os.path.basename(p)
        if base == args.from_name:
            src = p
        elif base == args.to_name:
            dst_exists = True
    if src is None:
        if dst_exists:
            print(f"[WARN] {args.from_name} not on disk but {args.to_name} is - "
                  "updating references only.")
        else:
            print(f"[ERR] '{args.from_name}' not found anywhere under the vault")
            return 1
    else:
        dst = os.path.join(os.path.dirname(src), args.to_name)
        if not args.dry_run:
            os.rename(src, dst)
    print(f"[{'dry' if args.dry_run else 'ok '}] rename step: "
          f"{args.from_name} -> {args.to_name}")

    # update references (stem match so .ino/.py variants both work)
    old_ref = args.from_name
    new_ref = args.to_name
    ref_files = ref_hits = 0
    for p in iter_files():
        if os.path.basename(p) in (args.from_name, args.to_name):
            continue  # never rewrite the renamed file itself
        try:
            t = read(p)
        except UnicodeDecodeError:
            continue  # binary/utf16 file - no text refs to update
        n = t.count(old_ref)
        if n == 0:
            continue
        ref_files += 1
        ref_hits += n
        if not args.dry_run:
            write(p, t.replace(old_ref, new_ref))
    print(f"== references: {'would update' if args.dry_run else 'updated'} "
          f"{ref_hits} occurrence(s) in {ref_files} file(s)")
    return 0


def op_registry(args):
    cl_path = os.path.join(ROOT, args.changelog)
    lines = read(cl_path).splitlines(keepends=True)
    row_idx = None
    for i, line in enumerate(lines):
        if line.startswith("| **") and args.doc.lower() in line.lower() \
                and "---" not in line:
            row_idx = i
            break
    if row_idx is None:
        print(f"[ERR] no registry row matching '{args.doc}'")
        return 1

    cells = [c.strip() for c in lines[row_idx].strip().strip("|").split("|")]
    if len(cells) != 5:
        print(f"[ERR] unexpected column count ({len(cells)}) in row: {cells[:2]}")
        return 1
    cells[2] = f"**{args.version}**"
    if args.date:
        cells[3] = args.date
    if args.status:
        cells[4] = args.status
    lines[row_idx] = "| " + " | ".join(cells) + " |\n"
    if not args.dry_run:
        write(cl_path, "".join(lines))
    print(f"[{'dry' if args.dry_run else 'ok '}] registry row for '{args.doc}' -> "
          f"v{args.version} ({args.date})")
    return 0


def op_bullet(args):
    """Append a dated bullet at the end of the '### <anchor>' section in the
    changelog, or replace the existing bullet for the same version+date.

    Bug fixed 2026-08-25: when no existing bullet matched, this used
    t.find("\\n### ", i) with i == -1, so nxt came back -1 and the new bullet
    was PREPENDED to the top of the whole changelog instead of landing in its
    section. That is how the 10.4 detector bullet ended up above the title.
    Now an append always requires a real section anchor and inserts before the
    next '### ' heading after it."""
    cl_path = os.path.join(ROOT, args.changelog)
    t = read(cl_path)
    bullet = f"*   **{args.version} ({args.date}):** {args.text}\n"
    i = t.find(f"*   **{args.version} ({args.date}):**")
    if i != -1 and not args.append_new:
        # replace existing bullet line
        line_end = t.find("\n", i)
        t = t[:i] + bullet.rstrip() + t[line_end:]
        action = "replaced"
    else:
        if not args.section_anchor.strip() or args.section_anchor.strip() == "###":
            print("[ERR] refusing to guess the section: pass a specific "
                  "--section-anchor such as 'detector-mediapipe (software)'")
            return 1
        j = t.find(args.section_anchor)
        if j == -1:
            print(f"[ERR] section anchor not found: {args.section_anchor}")
            return 1
        nxt = t.find("\n### ", j)
        if nxt == -1:
            # section runs to end of file: append after the last non-empty line
            body = t.rstrip("\n")
            t = body + "\n" + bullet
        else:
            t = t[:nxt + 1] + bullet + t[nxt + 1:]
        action = "appended new"
    if not args.dry_run:
        write(cl_path, t)
    print(f"[{'dry' if args.dry_run else 'ok '}] bullet for '{args.version}' {action}")
    return 0


def op_batch(args):
    """Run a list of steps from a JSON spec. Steps use the same fields as the
    CLI flags of each op (no dashes). Example spec:
    {"steps": [
       {"op":"replace","path":"HANDOFF.md","find":"a","replace":"b"},
       {"op":"rename","from_name":"x.py","to_name":"y.py"},
       {"op":"registry","doc":"Obstacle Risk","version":"10.4"}
    ]}
    """
    import json
    with io.open(args.spec, encoding="utf-8") as f:
        spec = json.load(f)
    dispatch = {"replace": op_replace, "rename": op_rename,
                "registry": op_registry, "bullet": op_bullet}
    rc = 0
    for n, step in enumerate(spec.get("steps", []), 1):
        op = step.pop("op")
        if args.dry_run:
            step["dry_run"] = True
        ns = argparse.Namespace(**step)
        print(f"-- step {n}: {op}")
        rc |= dispatch[op](ns) or 0
    return rc


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="op", required=True)

    p = sub.add_parser("replace")
    p.add_argument("path", help="file or folder (relative to vault root)")
    p.add_argument("--find", required=True)
    p.add_argument("--replace", required=True)
    p.add_argument("--ext", nargs="*", help="only these extensions, e.g. .md .py")
    p.add_argument("--dry-run", action="store_true")
    p.set_defaults(func=op_replace)

    p = sub.add_parser("rename")
    p.add_argument("--from-name", required=True)
    p.add_argument("--to-name", required=True)
    p.add_argument("--dry-run", action="store_true")
    p.set_defaults(func=op_rename)

    p = sub.add_parser("registry")
    p.add_argument("--doc", required=True, help="case-insensitive substring of the row name")
    p.add_argument("--version", required=True)
    p.add_argument("--date", default=None)
    p.add_argument("--status", default=None)
    p.add_argument("--changelog", default=r"3-Logs\argus-vac-version-control-and-change-log-v25.md")
    p.add_argument("--dry-run", action="store_true")
    p.set_defaults(func=op_registry)

    p = sub.add_parser("bullet")
    p.add_argument("--version", required=True)
    p.add_argument("--date", required=True)
    p.add_argument("--text", required=True)
    p.add_argument("--append-new", action="store_true")
    p.add_argument("--section-anchor", default="### ")
    p.add_argument("--changelog", default=r"3-Logs\argus-vac-version-control-and-change-log-v25.md")
    p.add_argument("--dry-run", action="store_true")
    p.set_defaults(func=op_bullet)

    p = sub.add_parser("batch")
    p.add_argument("spec", help="JSON file with a steps[] list")
    p.add_argument("--dry-run", action="store_true",
                   help="force every step into preview mode")
    p.set_defaults(func=op_batch)

    args = ap.parse_args()
    sys.exit(args.func(args))


if __name__ == "__main__":
    main()
