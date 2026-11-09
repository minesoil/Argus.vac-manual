"""Validate saved assemblies and produce ROS models.

This module has no ROS or browser dependency. JSON uses metres and radians;
the editor converts those values to millimetres and degrees. The template keeps
the tested sensors/control plugins while editable parts change their geometry.
"""

import base64
import copy
import math
from pathlib import Path
import re
import xml.etree.ElementTree as ET

IDENTIFIER = re.compile(r"^[A-Za-z][A-Za-z0-9_]{0,63}$")
SHAPES = {"assembly", "box", "cylinder", "sphere", "mesh"}
ROLES = {"fixed", "left_wheel", "right_wheel", "lidar", "camera"}
MAX_PARTS = 200
TEMPLATE = Path(__file__).parent / "templates/reference.urdf"


def vector(value, name, lower, upper, length=3):
    if not isinstance(value, list) or len(value) != length:
        raise ValueError(f"{name} must contain {length} numbers.")
    if any(
        isinstance(x, bool)
        or not isinstance(x, (int, float))
        or not math.isfinite(x)
        or not lower <= x <= upper
        for x in value
    ):
        raise ValueError(
            f"{name} must contain finite numbers between {lower} and {upper}."
        )


def validate(design):
    """Reject bad names, nonfinite transforms and oversized/imported data."""
    if not isinstance(design, dict) or design.get("schema_version") != 1:
        raise ValueError("Unsupported design version. Expected schema_version 1.")
    if not isinstance(design.get("name"), str) or not 1 <= len(design["name"]) <= 100:
        raise ValueError("Give this design a name of 1–100 characters.")
    parts = design.get("parts")
    if not isinstance(parts, list) or not 1 <= len(parts) <= MAX_PARTS:
        raise ValueError(f"A design must contain 1–{MAX_PARTS} parts.")
    ids = set()
    reference = ET.parse(TEMPLATE).getroot()
    links = {x.get("name") for x in reference.findall("link")}
    targets = set()
    for p in parts:
        if (
            not isinstance(p, dict)
            or not IDENTIFIER.fullmatch(str(p.get("id", "")))
            or p["id"] in ids
        ):
            raise ValueError(
                "Part IDs must be unique letters/numbers/underscores starting with a letter."
            )
        ids.add(p["id"])
        if not isinstance(p.get("label"), str) or not 1 <= len(p["label"]) <= 100:
            raise ValueError(f"{p['id']}: label must contain 1–100 characters.")
        if p.get("shape") not in SHAPES or p.get("role", "fixed") not in ROLES:
            raise ValueError(f"{p['id']}: unsupported shape or role.")
        vector(p.get("xyz_m"), "Position", -5, 5)
        vector(p.get("rpy_rad"), "Rotation", -100, 100)
        vector(p.get("size_m"), "Size", 0.0001, 5)
        vector(p.get("rgba"), "Colour", 0, 1, 4)
        mass = p.get("mass_kg")
        if (
            isinstance(mass, bool)
            or not isinstance(mass, (float, int))
            or not math.isfinite(mass)
            or not 0.001 <= mass <= 100
        ):
            raise ValueError(f"{p['id']}: mass must be between 0.001 and 100 kg.")
        if not isinstance(p.get("collision"), bool):
            raise ValueError("Collision must be true or false.")
        target = p.get("target")
        if target:
            key = (target.get("link"), target.get("visual"))
            if key in targets or key[0] not in links:
                raise ValueError("Duplicate or unknown template attachment.")
            targets.add(key)
            if (
                key[1]
                and reference.find(f"link[@name='{key[0]}']/visual[@name='{key[1]}']")
                is None
            ):
                raise ValueError("Unknown chassis visual attachment.")
        elif p.get("role", "fixed") != "fixed":
            raise ValueError(
                "New parts are fixed attachments. Keep the supplied functional wheels and sensors."
            )
        if (
            p["shape"] in ("cylinder", "sphere")
            and abs(p["size_m"][0] - p["size_m"][1]) > 1e-7
        ):
            raise ValueError("Cylinder and sphere diameters must match on X and Y.")
        if p["shape"] == "sphere" and abs(p["size_m"][0] - p["size_m"][2]) > 1e-7:
            raise ValueError("Sphere diameters must match on all three axes.")
        if p["shape"] == "mesh":
            mesh = p.get("mesh", {})
            try:
                data = base64.b64decode(mesh["base64"], validate=True)
            except (KeyError, ValueError) as exc:
                raise ValueError("Invalid STL data.") from exc
            if not 1 <= len(data) <= 8 * 1024 * 1024:
                raise ValueError("STL files must be no larger than 8 MB.")
            vector(mesh.get("scale"), "Mesh scale", 0.000001, 100)
        for v in p.get("visuals", []):
            if v.get("shape") not in {"box", "cylinder", "sphere"}:
                raise ValueError("Unsupported assembly geometry.")
            vector(v.get("size_m"), "Assembly size", 0.00001, 5)
            vector(v.get("xyz_m"), "Assembly position", -5, 5)
            vector(v.get("rpy_rad"), "Assembly rotation", -100, 100)
            vector(v.get("rgba"), "Assembly colour", 0, 1, 4)
        if p["shape"] == "assembly" and not p.get("visuals"):
            raise ValueError("Assemblies must include their visual geometry.")
    return design


def drive_geometry(design):
    """Return usable wheel geometry; layout/export remains available without it."""
    validate(design)

    def role(name):
        found = [p for p in design["parts"] if p["role"] == name]
        if len(found) != 1:
            raise ValueError(
                f'Simulation requires exactly one {name.replace("_", " ")}.'
            )
        return found[0]

    left, right = role("left_wheel"), role("right_wheel")
    role("lidar")
    if (
        left["target"].get("link") != "left_wheel"
        or right["target"].get("link") != "right_wheel"
    ):
        raise ValueError("Keep each functional role on its supplied wheel.")
    if any(abs(a - b) > 0.0005 for a, b in zip(left["size_m"], right["size_m"])):
        raise ValueError("Drive wheels must have matching diameter and width.")
    for p in (left, right):
        if any(abs(a) > 0.001 for a in p["rpy_rad"]):
            raise ValueError(
                "Drive wheel axles must stay parallel to Y (wheel rotation 0, 0, 0)."
            )
        if abs(p["size_m"][0] - p["size_m"][1]) > 0.0005:
            raise ValueError("Drive wheels must be round.")
        if abs(p["xyz_m"][2] - p["size_m"][0] / 2) > 0.001:
            raise ValueError(
                "Set wheel centre Z to half its diameter so it touches the floor."
            )
    if abs(left["xyz_m"][0] - right["xyz_m"][0]) > 0.001:
        raise ValueError("The two drive wheels must share the same X coordinate.")
    separation = left["xyz_m"][1] - right["xyz_m"][1]
    if not 0.04 <= separation <= 2:
        raise ValueError(
            "Left wheel must be to the left of the right wheel, separated by at least 40 mm."
        )
    lidar = role("lidar")
    if lidar["target"].get("link") != "lidar_link":
        raise ValueError("Keep the lidar role on the supplied C1.")
    return {"wheel_radius_m": left["size_m"][0] / 2, "wheel_separation_m": separation}


def text(values):
    return " ".join(f"{x:.9g}" for x in values)


def geometry(parent, shape, size, mesh=None):
    node = ET.SubElement(parent, "geometry")
    if shape == "box":
        ET.SubElement(node, "box", size=text(size))
    elif shape == "cylinder":
        ET.SubElement(node, "cylinder", radius=str(size[0] / 2), length=str(size[2]))
    elif shape == "sphere":
        ET.SubElement(node, "sphere", radius=str(size[0] / 2))
    elif shape == "mesh":
        ET.SubElement(node, "mesh", filename=mesh["uri"], scale=text(mesh["scale"]))


def add_visual(link, p, xyz=None, rpy=None, name=None, mesh_uri=None):
    v = ET.SubElement(link, "visual", name=name or p["id"])
    ET.SubElement(v, "origin", xyz=text(xyz or [0, 0, 0]), rpy=text(rpy or [0, 0, 0]))
    geometry(
        v,
        p["shape"],
        p["size_m"],
        (
            {"uri": mesh_uri, "scale": p.get("mesh", {}).get("scale")}
            if mesh_uri
            else None
        ),
    )
    material = ET.SubElement(v, "material", name=p["id"] + "_colour")
    ET.SubElement(material, "color", rgba=text(p["rgba"]))
    return v


def inertia(link, mass, size):
    old = link.find("inertial")
    if old is not None:
        link.remove(old)
    node = ET.SubElement(link, "inertial")
    ET.SubElement(node, "mass", value=str(mass))
    x, y, z = size
    ET.SubElement(
        node,
        "inertia",
        ixx=str(mass * (y * y + z * z) / 12),
        iyy=str(mass * (x * x + z * z) / 12),
        izz=str(mass * (x * x + y * y) / 12),
        ixy="0",
        ixz="0",
        iyz="0",
    )


def bounds(p):
    """Conservative XY bounds of a rotated component, including assembly details."""
    r, pitch, yaw = p["rpy_rad"]
    cr, sr, cp, sp, cy, sy = (
        math.cos(r),
        math.sin(r),
        math.cos(pitch),
        math.sin(pitch),
        math.cos(yaw),
        math.sin(yaw),
    )
    matrix = [
        [cy * cp, cy * sp * sr - sy * cr, cy * sp * cr + sy * sr],
        [sy * cp, sy * sp * sr + cy * cr, sy * sp * cr - cy * sr],
        [-sp, cp * sr, cp * cr],
    ]
    dimensions = list(p["size_m"])
    if p["role"] in ("left_wheel", "right_wheel"):
        dimensions = [p["size_m"][0], p["size_m"][2], p["size_m"][0]]
    if (
        p["shape"] == "assembly"
        and p.get("visuals")
        and p["role"] not in ("left_wheel", "right_wheel")
    ):
        dimensions = [
            max(abs(v["xyz_m"][i]) + max(v["size_m"]) / 2 for v in p["visuals"]) * 2
            for i in range(3)
        ]
    half = [
        sum(abs(matrix[i][j]) * dimensions[j] / 2 for j in range(3)) for i in range(3)
    ]
    return [
        p["xyz_m"][0] - half[0],
        p["xyz_m"][1] - half[1],
        p["xyz_m"][0] + half[0],
        p["xyz_m"][1] + half[1],
    ]


def footprint(design):
    boxes = [bounds(p) for p in design["parts"]]
    # Coordinates in base_link, matching Collision Monitor and Nav2.
    base = [-0.03, 0, 0.116]
    xmin = min(x[0] for x in boxes) - base[0]
    ymin = min(x[1] for x in boxes) - base[1]
    xmax = max(x[2] for x in boxes) - base[0]
    ymax = max(x[3] for x in boxes) - base[1]
    return [[xmin, ymin], [xmax, ymin], [xmax, ymax], [xmin, ymax]]


def compile_model(design, mesh_prefix="package://vacuum_sim/meshes/design"):
    """Generate a full simulation URDF plus mesh files without mutating inputs."""
    validate(design)
    root = ET.parse(TEMPLATE).getroot()
    base = [-0.03, 0, 0.116]
    parts = design["parts"]
    retained_links = {p["target"]["link"] for p in parts if p.get("target")}
    editable_links = {
        "left_wheel",
        "right_wheel",
        "caster",
        "lidar_link",
        "camera_link",
        "left_nema17",
        "right_nema17",
        "left_tb6600",
        "right_tb6600",
        "arduino_mega",
        "orange_pi5",
    }
    removed = editable_links - retained_links
    # Remove descendants (for example the camera optical frame) with their parent.
    changed = True
    while changed:
        changed = False
        for joint in root.findall("joint"):
            if (
                joint.find("parent").get("link") in removed
                and joint.find("child").get("link") not in removed
            ):
                removed.add(joint.find("child").get("link"))
                changed = True
    for node in list(root):
        if node.tag == "link" and node.get("name") in removed:
            root.remove(node)
        elif node.tag == "joint" and node.find("child").get("link") in removed:
            root.remove(node)
        elif (
            node.tag == "gazebo"
            and node.get("reference", "").replace("_joint", "") in removed
        ):
            root.remove(node)
    body = root.find("link[@name='base_link']")
    for visual in list(body.findall("visual")):
        body.remove(visual)
    meshes = {}
    for p in parts:
        target = p.get("target", {})
        xyz = [p["xyz_m"][i] - base[i] for i in range(3)]
        if target.get("visual"):
            add_visual(body, p, xyz, p["rpy_rad"], target["visual"])
            continue
        if target.get("link"):
            link = root.find(f"link[@name='{target['link']}']")
            joint = next(
                j
                for j in root.findall("joint")
                if j.find("child").get("link") == target["link"]
            )
            origin = joint.find("origin")
            origin.set("xyz", text(xyz))
            origin.set("rpy", text(p["rpy_rad"]))
            first = link.find("visual/geometry")[0]
            original_size = (
                [float(x) for x in first.get("size").split()]
                if first.tag == "box"
                else [float(first.get("radius")) * 2]
                * (3 if first.tag == "sphere" else 2)
                + ([] if first.tag == "sphere" else [float(first.get("length"))])
            )
            scale = [p["size_m"][i] / original_size[i] for i in range(3)]
            if any(abs(x - 1) > 1e-9 for x in scale):
                for node in list(link.findall("visual")) + list(
                    link.findall("collision")
                ):
                    geom = node.find("geometry")[0]
                    if geom.tag == "box":
                        geom.set(
                            "size",
                            text(
                                [
                                    float(x) * scale[i]
                                    for i, x in enumerate(geom.get("size").split())
                                ]
                            ),
                        )
                    elif geom.tag in ("sphere", "cylinder"):
                        geom.set("radius", str(float(geom.get("radius")) * scale[0]))
                        if geom.tag == "cylinder":
                            geom.set(
                                "length", str(float(geom.get("length")) * scale[2])
                            )
                    v_origin = node.find("origin")
                    if v_origin is not None and v_origin.get("xyz"):
                        v_origin.set(
                            "xyz",
                            text(
                                [
                                    float(x) * scale[i]
                                    for i, x in enumerate(v_origin.get("xyz").split())
                                ]
                            ),
                        )
                inertia(link, p["mass_kg"], p["size_m"])
            else:
                link.find("inertial/mass").set("value", str(p["mass_kg"]))
            for visual, editable in zip(link.findall("visual"), p.get("visuals", [])):
                material = visual.find("material")
                if material is not None:
                    visual.remove(material)
                material = ET.SubElement(
                    visual, "material", name=p["id"] + "_edited_" + str(len(visual))
                )
                ET.SubElement(material, "color", rgba=text(editable["rgba"]))
            if not p["collision"]:
                for node in list(link.findall("collision")):
                    link.remove(node)
            continue
        if root.find(f"link[@name='{p['id']}']") is not None:
            raise ValueError("A new part ID conflicts with a reserved ROS link.")
        link = ET.SubElement(root, "link", name=p["id"])
        joint = ET.SubElement(root, "joint", name=p["id"] + "_mount", type="fixed")
        ET.SubElement(joint, "parent", link="base_link")
        ET.SubElement(joint, "child", link=p["id"])
        ET.SubElement(joint, "origin", xyz=text(xyz), rpy=text(p["rpy_rad"]))
        inertia(link, p["mass_kg"], p["size_m"])
        if p["shape"] == "assembly":
            scale = [p["size_m"][i] / p["visuals"][0]["size_m"][i] for i in range(3)]
            for i, v in enumerate(p.get("visuals", [])):
                editable = copy.deepcopy(v)
                editable["size_m"] = [v["size_m"][i] * scale[i] for i in range(3)]
                add_visual(
                    link,
                    dict(editable, id=p["id"]),
                    [v["xyz_m"][i] * scale[i] for i in range(3)],
                    v["rpy_rad"],
                    f"{p['id']}_{i}",
                )
        else:
            uri = None
            if p["shape"] == "mesh":
                filename = p["id"] + ".stl"
                meshes[filename] = base64.b64decode(p["mesh"]["base64"])
                uri = mesh_prefix + "/" + filename
            add_visual(link, p, mesh_uri=uri)
        if p["collision"]:
            c = ET.SubElement(link, "collision")
            # Imported meshes use a measured bounding box for stable collisions.
            geometry(
                c,
                "box" if p["shape"] in ("mesh", "assembly") else p["shape"],
                p["size_m"],
            )
    # The chassis envelope follows edited plates; boards remain within it by default.
    plates = [p for p in parts if p.get("target", {}).get("visual") and p["collision"]]
    if plates:
        xy = [bounds(p) for p in plates]
        lo = [
            min(x[0] for x in xy),
            min(x[1] for x in xy),
            min(p["xyz_m"][2] - p["size_m"][2] / 2 for p in plates),
        ]
        hi = [
            max(x[2] for x in xy),
            max(x[3] for x in xy),
            max(p["xyz_m"][2] + p["size_m"][2] / 2 for p in plates),
        ]
        c = body.find("collision")
        c.clear()
        ET.SubElement(
            c, "origin", xyz=text([(lo[i] + hi[i]) / 2 - base[i] for i in range(3)])
        )
        geometry(c, "box", [hi[i] - lo[i] for i in range(3)])
    # Non-driving exports must not advertise absent control joints.
    for control in root.findall("ros2_control"):
        for joint in list(control.findall("joint")):
            if root.find(f"joint[@name='{joint.get('name')}']") is None:
                control.remove(joint)
    for parameters in root.findall("gazebo/plugin/parameters"):
        parameters.text = "$(find vacuum_sim)/config/controllers.yaml"
    ET.indent(root, space="  ")
    return ET.tostring(root, encoding="unicode") + "\n", meshes


def hardware_description(urdf):
    """Remove Gazebo/control plugins; retain sensor frames and movable joints."""
    root = ET.fromstring(urdf)
    for node in list(root):
        if node.tag in ("gazebo", "ros2_control"):
            root.remove(node)
    for mesh in root.findall("link/visual/geometry/mesh"):
        mesh.set(
            "filename",
            mesh.get("filename").replace(
                "package://vacuum_sim/", "package://vacuum_hardware/"
            ),
        )
    ET.indent(root, space="  ")
    return ET.tostring(root, encoding="unicode") + "\n"
