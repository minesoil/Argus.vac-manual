/** Offline assembly editor. ROS axes are retained throughout: X forward, Y left, Z up. */
import * as THREE from "three";
import { OrbitControls } from "./vendor/OrbitControls.js";
import { TransformControls } from "./vendor/TransformControls.js";
import { STLLoader } from "./vendor/STLLoader.js";

const $ = (id) => document.getElementById(id);
const clone = (value) => JSON.parse(JSON.stringify(value));
const token = new URLSearchParams(location.search).get("token") || "";
const scene = new THREE.Scene();
scene.background = new THREE.Color("#0c111b");
THREE.Object3D.DEFAULT_UP.set(0, 0, 1);
const camera = new THREE.PerspectiveCamera(40, 1, 0.001, 100);
camera.up.set(0, 0, 1);
camera.position.set(0.6, -0.65, 0.5);
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.outputColorSpace = THREE.SRGBColorSpace;
$("canvas").appendChild(renderer.domElement);
scene.add(new THREE.HemisphereLight(0xe7f2ff, 0x354754, 2.6));
const light = new THREE.DirectionalLight(0xffffff, 3);
light.position.set(0.4, -0.2, 0.8);
scene.add(light);
const grid = new THREE.GridHelper(2, 40, 0x49677b, 0x1d2d3d);
grid.rotation.x = Math.PI / 2;
scene.add(grid);
scene.add(new THREE.AxesHelper(0.22));
const orbit = new OrbitControls(camera, renderer.domElement);
orbit.target.set(0, 0, 0.09);
orbit.enableDamping = true;
orbit.dampingFactor = 0.12;
orbit.mouseButtons = {
  LEFT: null,
  MIDDLE: THREE.MOUSE.PAN,
  RIGHT: THREE.MOUSE.ROTATE,
};
const transform = new TransformControls(camera, renderer.domElement);
transform.setSpace("world");
transform.setSize(0.85);
scene.add(transform.getHelper());
const root = new THREE.Group();
scene.add(root);
const objects = new Map();
let state = null,
  selected = null,
  revision = null,
  currentFile = "default",
  dirty = false;
let history = [],
  future = [],
  dragging = false,
  pointerStart = null,
  meshFile = null;
const stlLoader = new STLLoader();
const raycaster = new THREE.Raycaster();

async function api(path, value) {
  const response = await fetch("/api/" + path, {
    method: value ? "POST" : "GET",
    headers: {
      "X-Robot-Lab-Token": token,
      ...(value ? { "Content-Type": "application/json" } : {}),
    },
    body: value ? JSON.stringify(value) : undefined,
  });
  if (!response.ok) {
    const data = await response.json();
    throw new Error(data.error || `HTTP ${response.status}`);
  }
  return path === "export" ? response.blob() : response.json();
}
function status(text, type = "") {
  $("status").textContent = text;
  $("status").className = type;
}
function changed() {
  dirty = true;
  $("saved").textContent = "Unsaved changes";
  $("saved").className = "tag dirty";
}
function remember() {
  history.push(clone(state));
  if (history.length > 30) history.shift();
  future = [];
}
function part() {
  return state?.parts.find((p) => p.id === selected);
}
function safe(operation) {
  return async () => {
    try {
      await operation();
    } catch (error) {
      status(error.message, "error");
    }
  };
}

function shapeGeometry(shape, size) {
  if (shape === "box") return new THREE.BoxGeometry(...size);
  if (shape === "sphere") return new THREE.SphereGeometry(size[0] / 2, 32, 20);
  const geometry = new THREE.CylinderGeometry(
    size[0] / 2,
    size[0] / 2,
    size[2],
    40,
  );
  geometry.rotateX(Math.PI / 2);
  return geometry;
}
function material(rgba) {
  return new THREE.MeshStandardMaterial({
    color: new THREE.Color(...rgba.slice(0, 3)),
    roughness: 0.55,
    metalness: 0.18,
    transparent: rgba[3] < 1,
    opacity: rgba[3],
    depthWrite: rgba[3] > 0.9,
  });
}
function addGeometry(group, v, scaling = [1, 1, 1]) {
  const mesh = new THREE.Mesh(
    shapeGeometry(v.shape, v.size_m),
    material(v.rgba),
  );
  mesh.position.set(...v.xyz_m);
  mesh.rotation.set(...v.rpy_rad, "ZYX");
  const scaled = new THREE.Group();
  scaled.scale.set(...scaling);
  scaled.add(mesh);
  group.add(scaled);
}
function rebuild() {
  transform.detach();
  while (root.children.length) {
    const node = root.children[0];
    node.traverse((n) => {
      n.geometry?.dispose();
      n.material?.dispose();
    });
    root.remove(node);
  }
  objects.clear();
  for (const p of state.parts) {
    const group = new THREE.Group();
    group.name = p.label;
    group.userData.partId = p.id;
    group.position.set(...p.xyz_m);
    group.rotation.set(...p.rpy_rad, "ZYX");
    if (p.shape === "assembly") {
      const scaling = p.size_m.map((x, i) => x / p.visuals[0].size_m[i]);
      for (const v of p.visuals) addGeometry(group, v, scaling);
    } else if (p.shape === "mesh") {
      const bytes = Uint8Array.from(atob(p.mesh.base64), (x) =>
        x.charCodeAt(0),
      );
      const geometry = stlLoader.parse(bytes.buffer);
      geometry.computeVertexNormals();
      const mesh = new THREE.Mesh(geometry, material(p.rgba));
      mesh.scale.set(...p.mesh.scale);
      group.add(mesh);
    } else addGeometry(group, { ...p, xyz_m: [0, 0, 0], rpy_rad: [0, 0, 0] });
    root.add(group);
    objects.set(p.id, group);
  }
  renderList();
  select(selected);
  updateHistory();
}
function renderList() {
  $("parts").replaceChildren();
  $("count").textContent = `${state.parts.length} parts`;
  for (const p of state.parts) {
    const button = document.createElement("button");
    button.className = "part" + (p.id === selected ? " selected" : "");
    button.setAttribute("role", "option");
    button.setAttribute("aria-selected", p.id === selected);
    const dot = document.createElement("span");
    dot.className = "swatch";
    dot.style.background =
      "#" + new THREE.Color(...p.rgba.slice(0, 3)).getHexString();
    const label = document.createElement("span");
    label.className = "part-name";
    label.textContent = p.label;
    const role = document.createElement("span");
    role.className = "part-role";
    role.textContent = p.role === "fixed" ? "" : p.role.replaceAll("_", " ");
    button.append(dot, label, role);
    button.onclick = () => select(p.id);
    $("parts").append(button);
  }
}
function select(id) {
  selected = id;
  const p = part();
  transform.detach();
  $("properties").hidden = !p;
  $("selection-note").hidden = !!p;
  $("duplicate").disabled = !p;
  $("delete").disabled = !p;
  if (p) {
    transform.attach(objects.get(p.id));
    refreshProperties();
  }
  renderList();
}
function refreshProperties() {
  const p = part();
  if (!p) return;
  $("label").value = p.label;
  $("role").textContent = `${p.id} · ${p.role.replaceAll("_", " ")}`;
  for (const input of document.querySelectorAll("[data-group]")) {
    const value = p[input.dataset.group][Number(input.dataset.index)];
    input.value = Number(
      (
        value * (input.dataset.group === "rpy_rad" ? 180 / Math.PI : 1000)
      ).toFixed(3),
    );
  }
  $("mass").value = p.mass_kg;
  $("colour").value =
    "#" + new THREE.Color(...p.rgba.slice(0, 3)).getHexString();
  $("collision").checked = p.collision;
}
function updateHistory() {
  $("undo").disabled = !history.length;
  $("redo").disabled = !future.length;
}
function undo() {
  if (!history.length) return;
  future.push(clone(state));
  state = history.pop();
  rebuild();
  syncDesign();
  changed();
}
function redo() {
  if (!future.length) return;
  history.push(clone(state));
  state = future.pop();
  rebuild();
  syncDesign();
  changed();
}
function syncDesign() {
  $("design-name").value = state.name;
  $("notes").value = state.notes || "";
}

transform.addEventListener("dragging-changed", (event) => {
  dragging = event.value;
  orbit.enabled = !event.value;
  if (event.value) remember();
  else {
    changed();
    updateHistory();
  }
});
transform.addEventListener("objectChange", () => {
  const p = part();
  if (!p) return;
  const node = objects.get(p.id);
  p.xyz_m = node.position.toArray();
  p.rpy_rad = [node.rotation.x, node.rotation.y, node.rotation.z];
  refreshProperties();
});
renderer.domElement.addEventListener("pointerdown", (event) => {
  pointerStart = [event.clientX, event.clientY];
});
renderer.domElement.addEventListener("pointerup", (event) => {
  if (
    event.button ||
    dragging ||
    transform.axis ||
    !pointerStart ||
    Math.hypot(
      event.clientX - pointerStart[0],
      event.clientY - pointerStart[1],
    ) > 4
  )
    return;
  const bounds = renderer.domElement.getBoundingClientRect();
  raycaster.setFromCamera(
    new THREE.Vector2(
      ((event.clientX - bounds.left) / bounds.width) * 2 - 1,
      (-(event.clientY - bounds.top) / bounds.height) * 2 + 1,
    ),
    camera,
  );
  const hit = raycaster.intersectObjects(root.children, true)[0];
  if (hit) {
    let object = hit.object;
    while (!object.userData.partId && object.parent) object = object.parent;
    select(object.userData.partId);
  } else select(null);
});
$("properties").onsubmit = (event) => event.preventDefault();
for (const input of document.querySelectorAll("[data-group]"))
  input.onchange = () => {
    const p = part(),
      value = Number(input.value),
      group = input.dataset.group;
    if (!p || !Number.isFinite(value) || (group === "size_m" && value <= 0)) {
      refreshProperties();
      return;
    }
    remember();
    p[group][Number(input.dataset.index)] =
      value / (group === "rpy_rad" ? 180 / Math.PI : 1000);
    // A cylinder/sphere remains round. Wheels have an inner 90-degree geometry rotation.
    if (
      group === "size_m" &&
      (p.shape === "cylinder" ||
        p.shape === "sphere" ||
        p.role.includes("wheel")) &&
      Number(input.dataset.index) < 2
    )
      p.size_m[0] = p.size_m[1] = value / 1000;
    if (p.shape === "sphere")
      p.size_m = [p.size_m[0], p.size_m[0], p.size_m[0]];
    rebuild();
    changed();
  };
$("label").onchange = () => {
  if (part() && $("label").value.trim()) {
    remember();
    part().label = $("label").value.trim();
    renderList();
    changed();
  }
};
$("mass").onchange = () => {
  if (
    !part() ||
    !Number.isFinite(Number($("mass").value)) ||
    Number($("mass").value) < 0.001
  )
    return;
  remember();
  part().mass_kg = Number($("mass").value);
  changed();
};
$("colour").onchange = () => {
  if (!part()) return;
  remember();
  const c = new THREE.Color($("colour").value);
  part().rgba = [c.r, c.g, c.b, part().rgba[3]];
  if (part().shape === "assembly")
    for (const v of part().visuals) v.rgba = part().rgba.slice();
  rebuild();
  changed();
};
$("collision").onchange = () => {
  if (!part()) return;
  remember();
  part().collision = $("collision").checked;
  changed();
};
for (const id of ["design-name", "notes"])
  $(id).onchange = () => {
    remember();
    state[id === "notes" ? "notes" : "name"] = $(id).value;
    changed();
  };
function mode(value) {
  transform.setMode(value);
  $("move").classList.toggle("active", value === "translate");
  $("rotate").classList.toggle("active", value === "rotate");
}
$("move").onclick = () => mode("translate");
$("rotate").onclick = () => mode("rotate");
$("snap").onchange = () => {
  transform.setTranslationSnap(
    Number($("snap").value) > 0 ? Number($("snap").value) / 1000 : null,
  );
  transform.setRotationSnap(
    Number($("snap").value) > 0 ? THREE.MathUtils.degToRad(5) : null,
  );
};
$("snap").onchange();
$("undo").onclick = undo;
$("redo").onclick = redo;
function fit(view = "iso") {
  const box = new THREE.Box3().setFromObject(root),
    centre = box.getCenter(new THREE.Vector3());
  const size = Math.max(0.3, box.getSize(new THREE.Vector3()).length());
  orbit.target.copy(centre);
  const delta =
    view === "top"
      ? [0, -0.001, size * 1.7]
      : view === "front"
        ? [size * 1.7, 0, 0.03]
        : [size, -size * 1.15, size * 0.85];
  camera.position.copy(centre).add(new THREE.Vector3(...delta));
  orbit.update();
}
$("fit").onclick = () => fit();
$("top").onclick = () => fit("top");
$("front").onclick = () => fit("front");

const presets = [
  [
    "nema17",
    "NEMA 17 motor",
    "box",
    [0.0423, 0.04, 0.0423],
    [0.2, 0.25, 0.3, 1],
    0.25,
  ],
  [
    "tb6600",
    "TB6600 driver",
    "box",
    [0.077, 0.038, 0.026],
    [0.12, 0.17, 0.23, 1],
    0.1,
  ],
  [
    "mega",
    "Arduino Mega 2560",
    "box",
    [0.10152, 0.0533, 0.006],
    [0.04, 0.3, 0.65, 1],
    0.037,
  ],
  [
    "orange",
    "Orange Pi 5",
    "box",
    [0.1, 0.062, 0.006],
    [0.05, 0.5, 0.3, 1],
    0.046,
  ],
  [
    "c1",
    "RPLIDAR C1 housing",
    "cylinder",
    [0.054, 0.054, 0.03],
    [0.13, 0.17, 0.24, 1],
    0.1,
  ],
  [
    "wheel",
    "Wheel (visual attachment)",
    "cylinder",
    [0.07, 0.07, 0.025],
    [0.06, 0.075, 0.09, 1],
    0.12,
  ],
  [
    "plate",
    "Chassis plate",
    "cylinder",
    [0.3, 0.3, 0.004],
    [0.17, 0.7, 0.77, 0.55],
    0.15,
  ],
  [
    "battery",
    "Battery pack",
    "box",
    [0.09, 0.055, 0.035],
    [0.7, 0.22, 0.18, 1],
    0.3,
  ],
  [
    "caster",
    "Caster ball",
    "sphere",
    [0.04, 0.04, 0.04],
    [0.1, 0.12, 0.15, 1],
    0.08,
  ],
  ["box", "Custom box", "box", [0.04, 0.04, 0.04], [0.65, 0.47, 0.21, 1], 0.1],
  [
    "cylinder",
    "Custom cylinder",
    "cylinder",
    [0.04, 0.04, 0.04],
    [0.35, 0.45, 0.65, 1],
    0.1,
  ],
  [
    "sphere",
    "Custom sphere",
    "sphere",
    [0.04, 0.04, 0.04],
    [0.6, 0.3, 0.45, 1],
    0.1,
  ],
];
for (const preset of presets) {
  const option = document.createElement("option");
  option.value = preset[0];
  option.textContent = preset[1];
  $("catalog").append(option);
}
function newId(kind) {
  let i = 1;
  while (state.parts.some((p) => p.id === `${kind}_${i}`)) i++;
  return `${kind}_${i}`;
}
$("add").onclick = () => {
  if (!state) return;
  const [kind, label, shape, size, rgba, mass] = presets.find(
    (p) => p[0] === $("catalog").value,
  );
  remember();
  const id = newId(kind);
  state.parts.push({
    id,
    label,
    kind,
    shape,
    size_m: size.slice(),
    xyz_m: [0, 0, 0.2],
    rpy_rad: [0, 0, 0],
    rgba: rgba.slice(),
    mass_kg: mass,
    collision: true,
    role: "fixed",
    visuals: [],
  });
  selected = id;
  rebuild();
  changed();
};
$("duplicate").onclick = () => {
  const p = part();
  if (!p) return;
  remember();
  const copy = clone(p);
  copy.id = newId(p.kind.replace(/[^A-Za-z0-9_]/g, "_"));
  copy.label += " copy";
  copy.role = "fixed";
  delete copy.target;
  copy.xyz_m[1] += 0.06;
  state.parts.push(copy);
  selected = copy.id;
  rebuild();
  changed();
};
$("delete").onclick = () => {
  if (!part()) return;
  remember();
  state.parts = state.parts.filter((p) => p.id !== selected);
  selected = null;
  rebuild();
  changed();
};

async function load(name, discard = false) {
  if (
    dirty &&
    !discard &&
    !confirm("Discard unsaved changes and open this design?")
  )
    return;
  const result = await api("state?name=" + encodeURIComponent(name));
  state = result.design;
  currentFile = result.file;
  revision = result.revision;
  selected = state.parts[0]?.id;
  history = [];
  future = [];
  dirty = false;
  $("filename").value = currentFile;
  $("files").replaceChildren();
  for (const name of result.files) {
    const option = document.createElement("option");
    option.value = name;
    option.textContent = name;
    $("files").append(option);
  }
  $("files").value = currentFile;
  $("data-dir").textContent = result.data_dir;
  $("apply").disabled = !result.can_apply;
  $("saved").textContent = "Saved";
  $("saved").className = "tag";
  syncDesign();
  rebuild();
  fit();
  status(
    "Select a part to edit. Changes stay in the design until you apply them.",
  );
}
async function save() {
  const file = $("filename").value.trim();
  const result = await api("save", {
    file,
    design: state,
    revision: file === currentFile ? revision : null,
  });
  revision = result.revision;
  currentFile = file;
  dirty = false;
  $("saved").textContent = "Saved";
  $("saved").className = "tag";
  if (![...$("files").options].some((o) => o.value === file)) {
    const option = document.createElement("option");
    option.value = file;
    option.textContent = file;
    $("files").append(option);
  }
  $("files").value = file;
  status(
    `Saved ${file}.json. Previous versions are kept in history.`,
    "success",
  );
}
$("open").onclick = safe(() => load($("files").value));
$("save").onclick = safe(save);
$("export").onclick = safe(async () => {
  const blob = await api("export", { design: state });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = ($("filename").value || "robot") + "-export.zip";
  a.click();
  setTimeout(() => URL.revokeObjectURL(url), 10000);
  status("Exported design, ROS models and mesh files.", "success");
});
$("import").onclick = () => $("import-file").click();
$("import-file").onchange = safe(async () => {
  const file = $("import-file").files[0];
  if (!file) return;
  if (file.size > 16 * 1024 * 1024) throw Error("Design exceeds 16 MB.");
  const design = JSON.parse(await file.text());
  await api("validate", { design });
  if (dirty && !confirm("Replace unsaved changes with the imported design?"))
    return;
  remember();
  state = design;
  selected = state.parts[0]?.id;
  syncDesign();
  rebuild();
  changed();
  status("Imported design. Choose a new file name before saving.");
  $("import-file").value = "";
});
$("stl").onclick = () => $("stl-file").click();
$("stl-file").onchange = safe(async () => {
  meshFile = $("stl-file").files[0];
  if (!meshFile) return;
  if (meshFile.size > 8 * 1024 * 1024) throw Error("STL exceeds 8 MB.");
  $("stl-dialog").showModal();
});
$("stl-cancel").onclick = () => {
  $("stl-dialog").close();
  meshFile = null;
};
$("stl-confirm").onclick = safe(async () => {
  const bytes = await meshFile.arrayBuffer(),
    unit = Number($("stl-unit").value);
  const geometry = stlLoader.parse(bytes);
  geometry.computeBoundingBox();
  const min = geometry.boundingBox.min,
    max = geometry.boundingBox.max;
  const size = max.clone().sub(min).multiplyScalar(unit).toArray();
  if (size.some((x) => !Number.isFinite(x) || x < 0.0001 || x > 5))
    throw Error("Mesh dimensions must be 0.1 mm–5 m. Check the units.");
  // Preserve the STL origin; the editor shows its imported geometry as authored.
  let raw = "";
  for (const value of new Uint8Array(bytes)) raw += String.fromCharCode(value);
  remember();
  const id = newId("mesh");
  state.parts.push({
    id,
    label: meshFile.name.replace(/\.stl$/i, ""),
    kind: "mesh",
    shape: "mesh",
    size_m: size,
    xyz_m: [0, 0, 0.2],
    rpy_rad: [0, 0, 0],
    rgba: [0.55, 0.65, 0.75, 1],
    mass_kg: 0.1,
    collision: true,
    role: "fixed",
    mesh: { name: meshFile.name, base64: btoa(raw), scale: [unit, unit, unit] },
    visuals: [],
  });
  selected = id;
  geometry.dispose();
  rebuild();
  changed();
  $("stl-dialog").close();
  $("stl-file").value = "";
  status("Imported STL. Set its mass and check the collision box.");
});
$("check").onclick = safe(async () => {
  const result = await api("validate", { design: state });
  status(
    result.drive_valid
      ? "Wheel alignment is valid. Verify clearances and measured masses before hardware use."
      : result.reason,
    result.drive_valid ? "success" : "error",
  );
});
$("apply").onclick = safe(async () => {
  await save();
  await api("apply", { design: state });
  $("apply").disabled = true;
  status("Updating simulator…");
  const timer = setInterval(async () => {
    try {
      const job = await api("job");
      status(job.stage);
      if (!job.running) {
        clearInterval(timer);
        $("apply").disabled = false;
        status(
          job.error || "Design applied. Open Drive now in the launcher.",
          job.error ? "error" : "success",
        );
      }
    } catch (error) {
      clearInterval(timer);
      $("apply").disabled = false;
      status(error.message, "error");
    }
  }, 1000);
});
document.addEventListener("keydown", (event) => {
  if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === "s") {
    event.preventDefault();
    safe(save)();
    return;
  }
  if (["INPUT", "TEXTAREA", "SELECT"].includes(document.activeElement.tagName))
    return;
  if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === "z") {
    event.preventDefault();
    event.shiftKey ? redo() : undo();
  } else if (
    (event.ctrlKey || event.metaKey) &&
    event.key.toLowerCase() === "y"
  ) {
    event.preventDefault();
    redo();
  } else if (event.key.toLowerCase() === "w") mode("translate");
  else if (event.key.toLowerCase() === "e") mode("rotate");
  else if (event.key === "Delete") $("delete").click();
  else if (event.key === "Escape") select(null);
});
window.addEventListener("beforeunload", (event) => {
  if (dirty) {
    event.preventDefault();
    event.returnValue = "";
  }
});
new ResizeObserver(() => {
  const area = $("canvas");
  camera.aspect = area.clientWidth / area.clientHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(area.clientWidth, area.clientHeight);
}).observe($("canvas"));
renderer.setAnimationLoop(() => {
  orbit.update();
  renderer.render(scene, camera);
});
safe(() => load("default", true))();
