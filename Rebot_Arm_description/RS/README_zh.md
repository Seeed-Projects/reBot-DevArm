# ReBot Arm RS 机械描述包

<p align="center">
  <strong>
    <a href="./README_zh.md">简体中文</a> &nbsp;|&nbsp;
    <a href="./README.md">English</a>
  </strong>
</p>

本目录是可独立复制的 B601-RS 机械描述资源。RS/DM 总体差异及跨引擎复用说明见上一级 [`README_zh.md`](../README_zh.md)。

```text
RS/
├── mjcf/                 # MJCF XML 与来源元数据
├── urdf/
│   └── ReBot_Arm_RS.urdf
└── meshes/
    ├── visual/             # 机械臂与腕部相机视觉件
    ├── shared/             # 同时用于渲染和 URDF 碰撞的整件网格
    └── mujoco_collision/   # MuJoCo 夹指精细碰撞网格
```

- 当前 RS URDF 使用实测质量和质心。模型总质量为 6.5503 kg，每侧夹爪手指为 55.9 g，滑动行程各为 0–50 mm。 [URDF 源文件](urdf/ReBot_Arm_RS.urdf)
- 每侧 55.9 g 由 43.9 g 金属件及 12.0 g 3D 打印件组成。Pinocchio 中包含六个旋转关节与两个夹爪滑动关节，`nq = nv = 8`。
- `meshes/visual/` 包含 54 个仅用于渲染和配色的 STL（含腕部相机视觉件）。
- `meshes/shared/` 包含 10 个同时用于渲染和碰撞的 STL；RS 当前没有只用于 URDF 碰撞的独立网格。
- `meshes/mujoco_collision/` 包含 10 个 MuJoCo 使用的夹指前、中、后段以及滑块、限位块碰撞网格。
- URDF 使用 `../meshes/...` 相对路径，不依赖 ROS package URI，复制整个 `RS/` 目录即可使用。
- ROS 2 运行时模型仍位于 `rebotarm_ros2_RS/src/rebotarm_bringup/description/`，两处模型更新后应同步核对。

例如，从仓库根目录加载：

```python
from pathlib import Path

urdf_path = Path("Rebot_Arm_description/RS/urdf/ReBot_Arm_RS.urdf")
```

## MJCF / MuJoCo

完整模型和场景 XML 位于 [`mjcf/`](mjcf/)。复制整个机械臂目录即可保留网格相对路径。模型选择、加载和校验方法见上一级 [MuJoCo 说明](../README_zh.md#mujoco)，来源提交与哈希见 [`../source.json`](../source.json)。现有数字孪生运行工程保持原样。

RS 运行时来源注明原始模型来自 `LAN-GER/reBot-B601-RS-for-mujoco_sim` 的 `1249cb6efdf393ba636056fc41df30dc6ba389aa` 版本，并记载该上游版本没有 LICENSE 文件。本次归档保留这一来源记录。相机资源署名和许可证原文见 [`mjcf/THIRD_PARTY_MODELS.md`](mjcf/THIRD_PARTY_MODELS.md) 与 [`mjcf/licenses/`](mjcf/licenses/)。
