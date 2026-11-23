#!/usr/bin/env python3
"""Check archived model references and provenance; optionally load/step MuJoCo."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import xml.etree.ElementTree as ET


def contained(base, relative):
    path = (base / relative).resolve()
    if not path.is_relative_to(base.resolve()) or not path.is_file():
        raise ValueError(f'Missing or external asset: {relative} (under {base})')
    return path


def verify_rs_inertials(arm):
    urdf = ET.parse(arm / 'urdf/ReBot_Arm_RS.urdf')
    mjcf = ET.parse(arm / 'mjcf/rs_arm.xml')
    for link in urdf.findall('link'):
        name = link.attrib['name']
        expected = link.find('inertial')
        actual = mjcf.find(f'.//body[@name="{name}"]/inertial')
        if actual is None:
            raise ValueError(f'Missing RS MJCF inertial: {name}')
        tensor = expected.find('inertia').attrib
        expected_values = [
            float(expected.find('mass').attrib['value']),
            *map(float, expected.find('origin').attrib['xyz'].split()),
            *(float(tensor[key]) for key in ('ixx', 'iyy', 'izz', 'ixy', 'ixz', 'iyz')),
        ]
        values = [float(actual.attrib['mass']), *map(float, actual.attrib['pos'].split())]
        if 'fullinertia' in actual.attrib:
            values.extend(map(float, actual.attrib['fullinertia'].split()))
        else:
            values.extend([*map(float, actual.attrib['diaginertia'].split()), 0.0, 0.0, 0.0])
        if len(values) != len(expected_values) or not all(
            math.isclose(a, b, rel_tol=0.0, abs_tol=1e-8)
            for a, b in zip(expected_values, values)
        ):
            raise ValueError(f'RS URDF and MJCF inertials differ: {name}')
    for name in ('joint7', 'joint_left', 'joint_right'):
        joint = mjcf.find(f'.//joint[@name="{name}"]')
        if joint is None or list(map(float, joint.attrib['range'].split())) != [0.0, 0.05]:
            raise ValueError(f'Invalid RS MJCF finger range: {name}')


def verify(description, simulate=False):
    manifest = json.loads((description / 'source.json').read_text())
    for entry in manifest['files']:
        path = contained(description, entry['path'])
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != entry['sha256']:
            raise ValueError(f"Hash mismatch: {entry['path']}; update provenance after an intentional change")
    models = []
    for arm in ('RS', 'DM'):
        base = description / arm
        contained(base, f'urdf/ReBot_Arm_{arm}.urdf')
        required = ('rs_arm.xml', 'rs_grasp_scene.xml') if arm == 'RS' else (
            'rebotarm_b601_colored.xml', 'rebotarm_b601_stl.xml',
            'rebotarm_b601_kinematic.xml', 'simple_rebotarm.xml',
        )
        for filename in required:
            contained(base, f'mjcf/{filename}')
        for urdf in sorted((base / 'urdf').glob('*.urdf')):
            for mesh in ET.parse(urdf).findall('.//mesh'):
                filename = mesh.get('filename')
                if filename:
                    asset = (urdf.parent / filename).resolve()
                    if not asset.is_relative_to(base.resolve()) or not asset.is_file():
                        raise ValueError(f'Missing URDF mesh: {urdf}: {filename}')
        for model in sorted((base / 'mjcf').glob('*.xml')):
            tree = ET.parse(model)
            if tree.getroot().tag != 'mujoco':
                raise ValueError(f'Not an MJCF model: {model}')
            compiler = tree.find('compiler')
            meshdir = compiler.get('meshdir', '') if compiler is not None else ''
            for include in tree.findall('.//include'):
                contained(base, (model.parent / include.attrib['file']).relative_to(base))
            for mesh in tree.findall('.//asset/mesh'):
                if mesh.get('file'):
                    contained(base, (model.parent / meshdir / mesh.attrib['file']).resolve().relative_to(base.resolve()))
            models.append(model)
    verify_rs_inertials(description / 'RS')
    if simulate:
        import mujoco
        import numpy as np
        for path in models:
            model = mujoco.MjModel.from_xml_path(str(path))
            data = mujoco.MjData(model)
            for _ in range(200):
                mujoco.mj_step(model, data)
            if not np.isfinite(data.qpos).all() or not np.isfinite(data.qvel).all():
                raise ValueError(f'Non-finite simulation state: {path}')
            print(f'{path.relative_to(description)}: loaded and stepped 200 times')
    print(f'PASS: 2 arm packages, {len(models)} MJCF files, {len(manifest["files"])} pinned resources')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mujoco', action='store_true', help='also load and step each model; requires mujoco and numpy')
    args = parser.parse_args()
    verify(Path(__file__).resolve().parents[1], args.mujoco)
