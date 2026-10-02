#!/usr/bin/env python3
"""Adapt multi-material URDF links for the ROS 2 Jazzy RViz renderer.

Jazzy's RobotLink passes an empty material name while creating every entry in
``visual_array``. RViz consequently resolves every mesh in one link to that
link's first material. Moving the additional visuals to fixed child links
keeps the same meshes, poses, and shared URDF colours while giving RViz one
unambiguous material per rendered link.

The transformation only changes the URDF written to stdout. The input file is
never modified.
"""

import re
import sys
from pathlib import Path
from xml.etree import ElementTree as ET


_RVIZ_COLOR_OVERRIDES = {
    # RViz/Ogre renders the source RS blacks nearly featureless. Use a lighter
    # presentation value without changing the source URDF or Web/MJCF RGBs.
    "rs_base_black": "0.140 0.160 0.150 1",
    "rs_motor_black": "0.140 0.160 0.150 1",
    "rs_pla_black": "0.140 0.160 0.150 1",
}


def _visual_suffix(visual: ET.Element, index: int) -> str:
    mesh = visual.find("geometry/mesh")
    filename = mesh.get("filename", "") if mesh is not None else ""
    stem = Path(filename).stem or f"part_{index}"
    return re.sub(r"[^A-Za-z0-9_]+", "_", stem).strip("_") or f"part_{index}"


def make_rviz_compatible(urdf_xml: str) -> str:
    """Return an equivalent URDF with at most one visual per link."""
    root = ET.fromstring(urdf_xml)

    for material in root.findall("material"):
        rgba = _RVIZ_COLOR_OVERRIDES.get(material.get("name", ""))
        color = material.find("color")
        if rgba is not None and color is not None:
            color.set("rgba", rgba)

    additions = []
    used_links = {link.get("name", "") for link in root.findall("link")}
    used_joints = {joint.get("name", "") for joint in root.findall("joint")}

    for link in list(root.findall("link")):
        visuals = link.findall("visual")
        if len(visuals) <= 1:
            continue

        parent_name = link.get("name", "")
        for index, visual in enumerate(visuals[1:], start=1):
            suffix = _visual_suffix(visual, index)
            child_name = f"{parent_name}__rviz_visual_{suffix}"
            joint_name = f"{child_name}__fixed_joint"
            serial = 2
            while child_name in used_links or joint_name in used_joints:
                child_name = f"{parent_name}__rviz_visual_{suffix}_{serial}"
                joint_name = f"{child_name}__fixed_joint"
                serial += 1

            used_links.add(child_name)
            used_joints.add(joint_name)
            link.remove(visual)

            child_link = ET.Element("link", {"name": child_name})
            child_link.append(visual)
            fixed_joint = ET.Element(
                "joint", {"name": joint_name, "type": "fixed"}
            )
            ET.SubElement(fixed_joint, "origin", {"xyz": "0 0 0", "rpy": "0 0 0"})
            ET.SubElement(fixed_joint, "parent", {"link": parent_name})
            ET.SubElement(fixed_joint, "child", {"link": child_name})
            additions.extend((child_link, fixed_joint))

    root.extend(additions)
    return ET.tostring(root, encoding="unicode")


def main() -> int:
    if len(sys.argv) != 2:
        print(f"usage: {Path(sys.argv[0]).name} ROBOT.urdf", file=sys.stderr)
        return 2
    source = Path(sys.argv[1])
    print(make_rviz_compatible(source.read_text(encoding="utf-8")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
