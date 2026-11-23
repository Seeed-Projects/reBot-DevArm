# ReBot Arm B601 机械描述复用包

<p align="center">
  <strong>
    <a href="./README_zh.md">简体中文</a> &nbsp;|&nbsp;
    <a href="./README.md">English</a>
  </strong>
</p>

`Rebot_Arm_description/` 汇总了 B601-RS 与 B601-DM 当前使用的 URDF、MJCF、STL，以及 32×32 UVC、D405、D435i、Gemini 2 腕部相机装配资源，供 Web、RViz、ROS 2、MuJoCo 或其他机器人项目复用。

本目录采用相对路径，自带模型显示、URDF 碰撞和 MuJoCo 夹爪精细碰撞所需的网格。复制时建议保留整个版本目录，不要把 STL 全部摊平到同一层。

> 本目录是便于分发和复用的模型包，不是当前程序自动读取的唯一运行时目录。RS、DM 工程中的 ROS 2 和 MuJoCo 运行时资源位置见本文末尾“来源与同步”。

## 目录结构

```text
Rebot_Arm_description/
├── README.md
├── README_zh.md
├── source.json               # MJCF 来源版本与文件哈希
├── tools/
│   ├── verify_models.py      # 引用、哈希及可选 MuJoCo 检查
│   └── rviz_urdf_compat.py  # ROS 2 Jazzy RViz 多材质显示兼容处理
├── Camera/
│   ├── README.md             # 简体中文 / English
│   ├── images/               # MuJoCo screenshots
│   ├── urdf/                 # UVC32 / D405 / D435i / Gemini 2 相机装配 URDF
│   ├── meshes/               # 支架、相机本体 STL / Collada
│   ├── source/               # 上游装配和厂家 Xacro
│   ├── source.json           # 来源版本和文件哈希
│   ├── licenses/
│   └── scripts/              # 离线重新生成 URDF
├── RS/
│   ├── README.md
│   ├── README_zh.md
│   ├── mjcf/                 # 机械臂、场景 XML 与来源说明
│   ├── urdf/
│   │   └── ReBot_Arm_RS.urdf
│   └── meshes/
│       ├── visual/             # 54 个：机械臂与腕部相机视觉件
│       ├── shared/             # 10 个：RS URDF 显示与碰撞共用
│       └── mujoco_collision/   # 10 个：RS MuJoCo 夹爪精细碰撞
└── DM/
    ├── README.md
    ├── README_zh.md
    ├── mjcf/                 # 彩色、STL、运动学及简化 XML
    ├── urdf/
    │   └── ReBot_Arm_DM.urdf
    └── meshes/
        ├── visual/             # 30 个：仅用于 DM 显示和配色
        ├── collision/          # 10 个：仅用于 DM URDF 碰撞
        ├── shared/             # 4 个：DM 显示与 MuJoCo 碰撞共用
        └── mujoco_collision/   # 6 个：仅用于 DM MuJoCo 夹指碰撞
```

腕部相机资源、安装位置和 MuJoCo 装配截图见中英文说明 [`Camera/README.md`](Camera/README.md)。32×32 UVC、D405、D435i、Gemini 2 的相机本体、支架、网格和装配 URDF 供 B601-RS 与 B601-DM 共用。相机装配以空的 `gripper_end` 为根参考系；RS 可挂到同名 link，DM 使用 `end_link`，需通过固定安装变换对齐参考系。复用时请保留整个 `Camera/` 目录。

## 分类含义

| 目录 | 含义 | 修改后的影响 |
| --- | --- | --- |
| `visual/` | 只用于外观、颜色和结构细节 | 影响 Web/RViz/MuJoCo 外观，不应改变物理接触 |
| `collision/` | 只用于 URDF 碰撞检测 | 影响 MoveIt、碰撞检测及使用 URDF 碰撞体的仿真 |
| `shared/` | 在该版本中承担两种用途 | 修改前必须同时检查显示和碰撞结果 |
| `mujoco_collision/` | MuJoCo 夹爪精细接触网格 | 影响夹持、穿模、摩擦和抓取稳定性 |

分类依据是“文件在当前版本中的实际用途”，不是零件是否相同。因此，同一个 STL 在 RS 中可能位于 `mujoco_collision/`，在 DM 中可能位于 `shared/`。

## RS 与 DM 方案对比

当前 RS URDF 使用实测质量和质心。模型总质量为 6.5503 kg，每侧夹爪手指为 55.9 g，滑动行程各为 0–50 mm。 [URDF 源文件](RS/urdf/ReBot_Arm_RS.urdf)

| 项目 | B601-RS | B601-DM |
| --- | --- | --- |
| 主 URDF | `RS/urdf/ReBot_Arm_RS.urdf` | `DM/urdf/ReBot_Arm_DM.urdf` |
| 机械臂本体 | RS 专用连杆、CNC、电机和 PLA 网格 | DM 专用连杆及按材质拆分的网格 |
| 夹爪物理结构 | 与 DM 相同 | 与 RS 相同 |
| 夹爪 URDF 显示 | 每侧采用 `PLA + CNC` 两个较大的视觉件 | 每侧拆成黑色指爪、灰色滑块、黄色限位块、金属齿条 4 个材质件 |
| 夹爪 MuJoCo 精细碰撞 | 10 个 STL 全部只用于 MuJoCo | 同一套 10 个 STL，其中 6 个仅用于 MuJoCo，4 个同时参与 URDF 显示 |
| URDF 碰撞策略 | 10 个整件网格同时用于显示和碰撞，放在 `shared/` | 10 个独立碰撞整件，放在 `collision/` |
| 左右命名 | RS MJCF 因局部坐标约定，将 RS left 映射到 DM right 文件，反之亦然 | 使用 DM 的原始 left/right 命名 |

### 为什么 RS 是 10 个 `mujoco_collision`，DM 是 6 + 4

两端实际使用的是同一套 10 个夹爪精细碰撞 STL，文件内容已逐一校验一致：

- 6 个夹指分段：左右两侧各 `front / mid / rear`；
- 4 个滑块与限位块：左右两侧各 `carriage_grey / travel_stop_yellow`。

在 RS 中，这 10 个文件都不参与 URDF 外观，因此全部放在 `RS/meshes/mujoco_collision/`。

在 DM 中，4 个滑块和限位块还会作为 URDF 可见模型，所以放在 `DM/meshes/shared/`；剩余 6 个夹指分段只用于 MuJoCo，放在 `DM/meshes/mujoco_collision/`。这是用途分类差异，不是夹爪几何差异。

## URDF 路径约定

两个主 URDF 都使用相对路径，例如：

```xml
<mesh filename="../meshes/visual/example.stl" />
```

因此：

- 必须保留 `urdf/` 与 `meshes/` 的相对层级；
- 移动或重命名网格目录时，必须同步修改 URDF；
- Linux 文件名区分大小写，`.STL` 与 `.stl` 不应随意互换；
- 模型尺寸以米为单位，关节角以弧度为单位，不要在加载器中重复缩放。

## 如何复用

### Web / Three.js

将整个 `RS/` 或 `DM/` 目录放到静态服务器可访问的位置，从对应的 `urdf/ReBot_Arm_*.urdf` 加载。服务器必须允许继续访问相邻的 `meshes/` 子目录。

只做显示时，URDF 会自动加载 `visual/` 和 `shared/` 中引用的网格。不要把 DM 的材质分件直接叠加到 RS 的 `PLA + CNC` 视觉件上，否则可能出现重叠闪烁、颜色变亮和重复面。

### ROS 2 / RViz / MoveIt

建议把所选版本复制到 ROS package 的 `description/` 下，并将相对路径改成：

```text
package://<package_name>/description/meshes/...
```

同时确认 `setup.py` 或 `CMakeLists.txt` 会安装所有 URDF 和 STL。RViz 只负责显示；MoveIt 是否使用碰撞网格取决于加载的 robot description。

> [!IMPORTANT]
> ROS 2 Jazzy 的 RViz 在显示“同一 link 包含多个不同材质的 visual”时，可能把该 link 的所有网格渲染成第一个材质的颜色。启动 RViz 或 MoveIt 前，请用 [`tools/rviz_urdf_compat.py`](tools/rviz_urdf_compat.py) 处理传给 `robot_description` 的 URDF。脚本只向标准输出写入转换结果，不会修改源 URDF。

该脚本会将额外的 visual 移到零偏移的 fixed 子 link，保留网格位姿、材质和碰撞定义。它还会针对 RViz/Ogre 单独提亮 RS 的黑色材质，不会改动源 URDF 及 Web/MuJoCo 使用的颜色。DM 没有匹配这些 `rs_*` 材质名，因此只会应用多 visual 拆分。

可先在命令行查看转换结果：

```bash
python3 tools/rviz_urdf_compat.py RS/urdf/ReBot_Arm_RS.urdf > /tmp/ReBot_Arm_RS_rviz.urdf
python3 tools/rviz_urdf_compat.py DM/urdf/ReBot_Arm_DM.urdf > /tmp/ReBot_Arm_DM_rviz.urdf
```

在 Python ROS 2 launch 中，应将脚本的输出直接作为 `robot_description`：

```python
from launch.substitutions import Command, FindPackageShare, PathJoinSubstitution
from launch_ros.parameter_descriptions import ParameterValue

package_share = FindPackageShare("<package_name>")
urdf_file = PathJoinSubstitution(
    [package_share, "description", "urdf", "ReBot_Arm_RS.urdf"]
)
compat_script = PathJoinSubstitution(
    [package_share, "tools", "rviz_urdf_compat.py"]
)
robot_description = ParameterValue(
    Command(["python3 ", compat_script, " ", urdf_file]),
    value_type=str,
)
```

接入 MoveIt 时，在创建 `move_group` 和 RViz 节点之前处理 `MoveItConfigsBuilder` 生成的配置：

```python
from importlib.machinery import SourceFileLoader

compat = SourceFileLoader("rviz_urdf_compat", compat_script_path).load_module()
description_key = "robot_description"
source_urdf = moveit_config.robot_description[description_key]
moveit_config.robot_description[description_key] = (
    compat.make_rviz_compatible(source_urdf)
)
```

请把 `tools/rviz_urdf_compat.py` 随 ROS package 一起安装，并确保 `robot_state_publisher`、MoveIt `move_group` 和 RViz 收到同一份处理后的 `robot_description`。

### MuJoCo

两个机械臂目录都包含可直接加载的 MJCF XML 和全部依赖网格。复制完整 `RS/` 或 `DM/` 目录，并保留 `mjcf/` 与 `meshes/` 的相邻层级，即可独立加载，无需安装 ROS 或克隆数字孪生工程。

| 机械臂 | MJCF 文件 | 用途 |
| --- | --- | --- |
| RS | [rs_arm.xml](RS/mjcf/rs_arm.xml) | 机械臂、夹爪及可切换腕部相机的视觉模型 |
| RS | [rs_grasp_scene.xml](RS/mjcf/rs_grasp_scene.xml) | 引用 `rs_arm.xml`，增加抓取物体及俯视相机 |
| DM | [rebotarm_b601_colored.xml](DM/mjcf/rebotarm_b601_colored.xml) | 默认彩色模型与抓取场景 |
| DM | [rebotarm_b601_stl.xml](DM/mjcf/rebotarm_b601_stl.xml) | 原有单材质 STL 模型 |
| DM | [rebotarm_b601_kinematic.xml](DM/mjcf/rebotarm_b601_kinematic.xml) | 原有基础几何运动学模型 |
| DM | [simple_rebotarm.xml](DM/mjcf/simple_rebotarm.xml) | 原有简化模型 |

在本目录下用 Python 加载所需模型：

```python
import mujoco

model = mujoco.MjModel.from_xml_path("RS/mjcf/rs_grasp_scene.xml")
data = mujoco.MjData(model)
mujoco.mj_step(model, data)
```

RS 腕部相机的型号、几何分组和光学位姿记录在 [wrist_cameras.json](RS/mjcf/wrist_cameras.json)。切换型号属于应用层行为，单独加载 XML 时采用默认 D405。相机几何只参与显示，仿真视场角不代表实机标定。

归档 XML 只调整网格引用路径，保留关节、执行器、惯量、接触、相机及场景定义。RS 的左右夹指映射保持原样。请保留完整的分段夹指网格，避免用单一凸包替换。

在仓库根目录检查引用路径与文件哈希：

```bash
python3 Rebot_Arm_description/tools/verify_models.py
# 可选：同时加载全部六个模型并进行短时仿真，需要 mujoco 和 numpy。
python3 Rebot_Arm_description/tools/verify_models.py --mujoco
```

本次迁移已用 MuJoCo 3.10.0 验证：六个模型均能加载，编译后的模型数组与来源模型一致，运行 200 步后的状态也一致。这是加载与回归检查，不代表新增的抓取性能测试。

## 修改与同步规则

1. **只改颜色**：优先修改 URDF `<material>` 或渲染器的 roughness/metalness，不要改变碰撞 STL。
2. **改视觉几何**：检查 Web、RViz 与 MuJoCo 外观；不要默认视觉变化会自动同步到碰撞模型。
3. **改 URDF 碰撞**：重新验证 MoveIt 自碰撞、关节全行程和末端附近接触。
4. **改夹爪精细碰撞**：RS、DM 共用同一套几何，应同步更新两端并重新验证抓取、闭合和释放。
5. **改左右夹指名称或坐标**：同步检查 RS 的左右反向映射和 MJCF 中的 `pos/quat`，不能只重命名文件。
6. **发布前**：确认所有 URDF 引用存在、XML 可解析，并在 Linux 上检查文件名大小写。

## 来源与同步

当前运行时源文件位于：

```text
# RS
rebotarm_ros2_RS/src/rebotarm_bringup/description/
rebotarm_ros2_RS/src/rebotarm_mujoco_rs/models/

# DM（位于 DM 仓库）
reBotArm_ros2_DM/src/rebotarm_bringup/description/
reBotArm_ros2_DM/src/rebotarm_mujoco/models/
```

`Rebot_Arm_description/` 是面向复用者整理的自包含副本。运行时源模型发生变化后，应审核并同步更新这里的对应 URDF/MJCF/STL，并重新执行引用完整性和仿真验证。


归档 MJCF 及其引用资源的来源提交和 SHA-256 哈希见 [`source.json`](source.json)。现有数字孪生工程及其运行时模型路径保持原样，本次迁移不会让工程自动改为读取本目录。保留 [`RS/mjcf/THIRD_PARTY_MODELS.md`](RS/mjcf/THIRD_PARTY_MODELS.md)、其 `licenses/` 目录及 [`DM/mjcf/SOURCE_LICENSE.txt`](DM/mjcf/SOURCE_LICENSE.txt) 的来源声明。RS 来源 README 记载，原始模型在所列上游版本中没有许可证；本次归档保留这一记录，不为它另行指定许可证。相机来源继续见 [`Camera/source.json`](Camera/source.json)。

## 选择建议

- 需要 B601-RS 外观、ROS 模型或 RS 工程集成：使用整个 `RS/`。
- 需要 B601-DM 材质分件、ROS 模型或 DM 工程集成：使用整个 `DM/`。
- 只复用夹爪 MuJoCo 碰撞：两端几何相同，可任选一套，但必须保留全部 10 个分件及正确的左右坐标映射。
- 不确定需要哪些文件：复制整个版本目录最安全，文件分类主要用于理解和维护，不要求使用者手动挑选。
