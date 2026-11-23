# ReBot Arm RS Mechanical Description Package

<p align="center">
  <strong>
    <a href="./README_zh.md">简体中文</a> &nbsp;|&nbsp;
    <a href="./README.md">English</a>
  </strong>
</p>

This directory contains the self-contained B601-RS mechanical description resources. See the parent [`README.md`](../README.md) for the overall RS/DM differences and cross-engine reuse guidance.

```text
RS/
├── mjcf/                 # MJCF XML and source metadata
├── urdf/
│   └── ReBot_Arm_RS.urdf
└── meshes/
    ├── visual/             # Arm and wrist-camera parts used only for rendering
    ├── shared/             # Complete meshes shared by rendering and URDF collision
    └── mujoco_collision/   # Detailed MuJoCo finger-collision meshes
```

- The current RS URDF uses measured masses and centers of mass. The model totals 6.5503 kg. Each gripper finger weighs 55.9 g and has 0–50 mm of travel. [URDF source](urdf/ReBot_Arm_RS.urdf)
- Each 55.9 g finger consists of 43.9 g of metal hardware and a 12.0 g 3D-printed finger. Pinocchio has six revolute joints and two prismatic finger joints, with `nq = nv = 8`.
- `meshes/visual/` contains 54 STL files used only for rendering and colors, including wrist-camera visuals.
- `meshes/shared/` contains 10 STL files used for both rendering and collision. RS currently has no independent meshes used only for URDF collision.
- `meshes/mujoco_collision/` contains 10 MuJoCo collision meshes for the front, middle, and rear finger segments, carriages, and travel stops.
- The URDF uses `../meshes/...` relative paths and does not depend on ROS package URIs. Copy the complete `RS/` directory to use it.
- The ROS 2 runtime model remains in `rebotarm_ros2_RS/src/rebotarm_bringup/description/`. Compare and synchronize the two locations after model updates.

For example, load it from the repository root with:

```python
from pathlib import Path

urdf_path = Path("Rebot_Arm_description/RS/urdf/ReBot_Arm_RS.urdf")
```

## MJCF / MuJoCo

The complete model and scene XML files are in [`mjcf/`](mjcf/). Copy this entire arm directory to preserve relative mesh references. See the parent [MuJoCo instructions](../README.md#mujoco) for model selection, loading and validation. Source commits and hashes are in [`../source.json`](../source.json). Existing DigitalTwin runtime projects are unchanged.

The RS runtime source identifies `LAN-GER/reBot-B601-RS-for-mujoco_sim` revision `1249cb6efdf393ba636056fc41df30dc6ba389aa` as its original model source and records that no upstream LICENSE file existed at that revision. The archived files retain this provenance. Camera asset attribution and license texts are in [`mjcf/THIRD_PARTY_MODELS.md`](mjcf/THIRD_PARTY_MODELS.md) and [`mjcf/licenses/`](mjcf/licenses/).
