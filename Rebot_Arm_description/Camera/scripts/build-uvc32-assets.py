#!/usr/bin/env python3
"""Derive the UVC bracket from STEP and create a schematic 32 mm camera board.

Developer dependencies: cadquery 2.5.2, numpy, scipy. No CAD dependency is
required to load the generated URDFs or run either simulator.
SPDX-License-Identifier: Apache-2.0
"""
from pathlib import Path
import hashlib
import json
import struct
import xml.etree.ElementTree as ET

import cadquery as cq
import numpy as np
from scipy.spatial.transform import Rotation

ROOT = Path(__file__).resolve().parents[1]
CAD = ROOT / "source/seeed_projects/hardware/camera-mounts/b601-camera-mounts"


def circle_centers(shape, radius):
    return np.unique(np.array([
        np.round(edge.arcCenter().toTuple(), 7)
        for edge in shape.Edges()
        if edge.geomType() == "CIRCLE" and abs(edge.radius() - radius) < 1e-6
    ]), axis=0)


def clamp_center(shape):
    # The common B601 clamp has 3.3 mm bolt holes and a 20.4 mm cavity.
    holes = circle_centers(shape, 1.65)
    holes = holes[np.abs(holes[:, 1] - holes[:, 1].min()) < 1e-4]
    levels = np.unique(holes[:, 2])
    assert len(levels) == 4 and abs(levels[2] - levels[1] - 20.4) < 1e-5
    return np.array([holes[:, 0].mean(), holes[:, 1].mean(), levels[1:3].mean()])


def write_stl(shape, path):
    vertices, indices = shape.tessellate(0.05, 0.1)
    triangles = np.array([v.toTuple() for v in vertices], dtype=np.float32)[indices]
    normals = np.cross(triangles[:, 1] - triangles[:, 0], triangles[:, 2] - triangles[:, 0])
    norms = np.linalg.norm(normals, axis=1)
    normals /= np.maximum(norms[:, None], 1e-12)
    records = np.zeros(len(triangles), dtype=[("normal", "<f4", (3,)),
                       ("vertices", "<f4", (3, 3)), ("attribute", "<u2")])
    records["normal"], records["vertices"] = normals, triangles
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(b"UVC32 derived geometry; see source.json".ljust(80, b"\0")
                     + struct.pack("<I", len(records)) + records.tobytes())


def numbers(values):
    return " ".join(f"{value:.12g}" for value in values)


def build():
    bracket = cq.importers.importStep(str(CAD / "UVC32_mount.step")).val()
    reference = cq.importers.importStep(str(CAD / "D435_Gemini2_Mount.step")).val()
    center = clamp_center(bracket)
    reference_center = clamp_center(reference)
    candidates = [face for face in bracket.Faces() if face.geomType() == "PLANE"
                  and face.normalAt().z > 0.5 and len(circle_centers(face, 0.95)) == 4]
    assert len(candidates) == 1, "Expected one front camera-board mounting plane"
    plate = candidates[0]
    holes = circle_centers(plate, 0.95)
    board_center = holes.mean(axis=0)
    forward = np.array(plate.normalAt().toTuple())
    # +Z optical forward, +X right, +Y down on the upright camera plate.
    right = np.array([-1.0, 0.0, 0.0])
    down = np.cross(forward, right)
    camera_rotation = np.column_stack((right, down, forward))
    board_holes = (holes - board_center) @ camera_rotation
    np.testing.assert_allclose(np.abs(board_holes[:, :2]), 14.0, atol=1e-5)
    np.testing.assert_allclose(board_holes[:, 2], 0, atol=1e-5)

    # Put the UVC mesh origin at its clamp center. The D435 CAD clamp center
    # anchors it to the already validated B601 wrist attachment transform.
    reference_urdf = ET.parse(ROOT / "urdf/d435i.urdf").getroot()
    origin = reference_urdf.find("joint[@name='gripper_to_mount']/origin")
    rpy = np.fromstring(origin.get("rpy"), sep=" ")
    mount_xyz = np.fromstring(origin.get("xyz"), sep=" ") + Rotation.from_euler(
        "xyz", rpy).apply(reference_center * 0.001)
    camera_xyz = (board_center - center) * 0.001
    camera_rpy = Rotation.from_matrix(camera_rotation).as_euler("xyz")

    outputs = [ROOT / "meshes/mounts/UVC32_mount.stl"]
    write_stl(bracket.translate(tuple(-center)), outputs[0])
    board = cq.Workplane("XY").box(32, 32, 1.6, centered=(True, True, False))
    board = board.faces(">Z").workplane().pushPoints(
        [tuple(point[:2]) for point in board_holes]).hole(1.9).val()
    # Board thickness and lens dimensions are schematic simulation choices;
    # the supplied STEP contains only the bracket, not a vendor camera body.
    lens = cq.Workplane("XY").circle(4).extrude(8).translate((0, 0, 1.6)).val()
    glass = cq.Workplane("XY").circle(3.4).extrude(0.3).translate((0, 0, 9.6)).val()
    for name, shape in (("board", board), ("lens", lens), ("glass", glass)):
        path = ROOT / "meshes/uvc32" / f"{name}.stl"
        write_stl(shape, path)
        outputs.append(path)

    robot = ET.Element("robot", {"xmlns:xacro": "http://www.ros.org/wiki/xacro",
                                "name": "rebotarm_rs_uvc32"})
    robot.append(ET.Comment("Official STEP bracket; generic board/lens are schematic, not calibrated."))
    ET.SubElement(robot, "link", name="gripper_end")

    def visual(link, uri, color):
        node = ET.SubElement(link, "visual")
        geometry = ET.SubElement(node, "geometry")
        ET.SubElement(geometry, "mesh", filename=uri, scale="0.001 0.001 0.001")
        material = ET.SubElement(node, "material", name=f"{link.get('name')}_uvc32_{len(link)}")
        ET.SubElement(material, "color", rgba=color)

    def joint(name, parent, child, xyz, angles):
        node = ET.SubElement(robot, "joint", name=name, type="fixed")
        ET.SubElement(node, "parent", link=parent)
        ET.SubElement(node, "child", link=child)
        ET.SubElement(node, "origin", xyz=numbers(xyz), rpy=numbers(angles))

    mount = ET.SubElement(robot, "link", name="camera_mount_link")
    visual(mount, "package://uvc32_description/meshes/mounts/UVC32_mount.stl", "0.7 0.73 0.75 1")
    joint("gripper_to_mount", "gripper_end", "camera_mount_link", mount_xyz, rpy)
    camera = ET.SubElement(robot, "link", name="camera_link")
    for name, color in (("board", "0.06 0.32 0.14 1"), ("lens", "0.035 0.035 0.04 1"),
                        ("glass", "0.04 0.14 0.22 1")):
        visual(camera, f"package://uvc32_description/meshes/uvc32/{name}.stl", color)
    joint("mount_to_camera", "camera_mount_link", "camera_link", camera_xyz, camera_rpy)
    ET.SubElement(robot, "link", name="camera_color_frame")
    joint("camera_color_joint", "camera_link", "camera_color_frame", [0, 0, 0.0099], [0, 0, 0])
    ET.SubElement(robot, "link", name="camera_color_optical_frame")
    joint("camera_color_optical_joint", "camera_color_frame", "camera_color_optical_frame", [0, 0, 0], [0, 0, 0])
    ET.indent(robot, space="  ")
    xacro = ROOT / "source/uvc32_description/urdf/rebotarm_rs_with_uvc32.urdf.xacro"
    xacro.parent.mkdir(parents=True, exist_ok=True)
    xacro.write_text('<?xml version="1.0"?>\n' + ET.tostring(robot, encoding="unicode") + "\n")
    outputs.append(xacro)

    manifest_path = ROOT / "source.json"
    manifest = json.loads(manifest_path.read_text())
    manifest["uvc32"] = {"body": "generic 32x32 mm schematic; not a vendor camera model",
                         "board_size_mm": [32, 32, 1.6], "board_hole_pitch_mm": [28, 28],
                         "mount_xyz": mount_xyz.tolist(), "mount_rpy": rpy.tolist(),
                         "camera_xyz": camera_xyz.tolist(), "camera_rpy": camera_rpy.tolist(),
                         "cad_clamp_center_mm": center.tolist(),
                         "cad_board_contact_center_mm": board_center.tolist(),
                         "cad_plate_normal": forward.tolist(), "cadquery_version": cq.__version__,
                         "optical_frame": "nominal lens-front origin; simulation FOV is not calibrated"}
    manifest["generated_assets"] = [{"file": str(path.relative_to(ROOT)),
                                    "bytes": path.stat().st_size,
                                    "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
                                   for path in outputs]
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps(manifest["uvc32"], indent=2))


if __name__ == "__main__":
    build()
