# ReBot Arm B601 Mechanical Description Package

<p align="center">
  <strong>
    <a href="./README_zh.md">简体中文</a> &nbsp;|&nbsp;
    <a href="./README.md">English</a>
  </strong>
</p>

`Rebot_Arm_description/` collects the URDF and STL resources currently used by the B601-RS and B601-DM for reuse in Web applications, RViz, ROS 2, MuJoCo, and other robotics projects.

This directory uses relative paths and includes the meshes required for model rendering, URDF collision geometry, and detailed MuJoCo gripper collisions. When copying it, keep each complete model directory intact instead of flattening all STL files into a single directory.

> This is a model package organized for distribution and reuse. It is not the only runtime directory read automatically by the current applications. See [Sources and synchronization](#sources-and-synchronization) for the ROS 2 and MuJoCo runtime resource locations in the RS and DM projects.

## Directory structure

```text
Rebot_Arm_description/
├── README.md
├── README_zh.md
├── tools/
│   └── rviz_urdf_compat.py  # ROS 2 Jazzy RViz multi-material compatibility helper
├── RS/
│   ├── README.md
│   ├── README_zh.md
│   ├── urdf/
│   │   └── ReBot_Arm_RS.urdf
│   └── meshes/
│       ├── visual/             # 22 meshes: RS rendering and colors only
│       ├── shared/             # 10 meshes: shared by RS URDF rendering and collision
│       └── mujoco_collision/   # 10 meshes: detailed RS MuJoCo gripper collisions
└── DM/
    ├── README.md
    ├── README_zh.md
    ├── urdf/
    │   └── ReBot_Arm_DM.urdf
    └── meshes/
        ├── visual/             # 30 meshes: DM rendering and colors only
        ├── collision/          # 10 meshes: DM URDF collisions only
        ├── shared/             # 4 meshes: shared by DM rendering and MuJoCo collision
        └── mujoco_collision/   # 6 meshes: DM MuJoCo finger collisions only
```

## Mesh categories

| Directory | Purpose | Effect of changes |
| --- | --- | --- |
| `visual/` | Appearance, colors, and structural details only | Affects Web/RViz/MuJoCo appearance and should not change physical contact |
| `collision/` | URDF collision detection only | Affects MoveIt, collision detection, and simulations that use URDF collision geometry |
| `shared/` | Serves both purposes for that model | Both rendering and collision behavior must be checked before making changes |
| `mujoco_collision/` | Detailed MuJoCo gripper contact meshes | Affects gripping, penetration, friction, and grasp stability |

Files are categorized by how they are actually used in each model, not by whether the parts are geometrically identical. The same STL may therefore be in `mujoco_collision/` for RS and in `shared/` for DM.

## RS and DM comparison

| Item | B601-RS | B601-DM |
| --- | --- | --- |
| Main URDF | `RS/urdf/ReBot_Arm_RS.urdf` | `DM/urdf/ReBot_Arm_DM.urdf` |
| Arm body | RS-specific links, CNC parts, motors, and PLA meshes | DM-specific links and material-separated meshes |
| Physical gripper structure | Identical to DM | Identical to RS |
| URDF gripper appearance | Two larger `PLA + CNC` visual parts per side | Four material parts per side: black finger, gray carriage, yellow travel stop, and metal rack |
| Detailed MuJoCo gripper collisions | All 10 STL files are used only by MuJoCo | The same 10 STL files: 6 are MuJoCo-only and 4 are also used for URDF rendering |
| URDF collision strategy | 10 complete meshes used for both rendering and collision in `shared/` | 10 independent complete collision meshes in `collision/` |
| Left/right naming | Due to the RS MJCF local-coordinate convention, RS left maps to the DM right file and vice versa | Uses the original DM left/right names |

### Why RS has 10 `mujoco_collision` meshes while DM has 6 + 4

Both models use the same set of 10 detailed gripper-collision STL files. Their contents have been verified individually:

- Six finger segments: `front`, `mid`, and `rear` for each side.
- Four carriage and travel-stop parts: `carriage_grey` and `travel_stop_yellow` for each side.

For RS, none of these 10 files participate in the URDF appearance, so they all live in `RS/meshes/mujoco_collision/`.

For DM, the four carriage and travel-stop parts are also visible URDF models and therefore live in `DM/meshes/shared/`. The remaining six finger segments are used only by MuJoCo and live in `DM/meshes/mujoco_collision/`. This is a usage-category difference, not a geometry difference.

## URDF path conventions

Both main URDF files use relative paths, for example:

```xml
<mesh filename="../meshes/visual/example.stl" />
```

Therefore:

- Keep the relative hierarchy between `urdf/` and `meshes/`.
- Update the URDF whenever moving or renaming a mesh directory.
- Linux filenames are case-sensitive; do not interchange `.STL` and `.stl` casually.
- Model dimensions are in meters and joint angles are in radians. Do not apply the scale again in the loader.

## Reusing the package

### Web / Three.js

Place the complete `RS/` or `DM/` directory somewhere accessible to the static server, then load the corresponding `urdf/ReBot_Arm_*.urdf`. The server must also serve the adjacent `meshes/` directory.

For rendering, the URDF automatically loads meshes referenced from `visual/` and `shared/`. Do not overlay the DM material-separated parts directly onto the RS `PLA + CNC` visual parts, as this can cause z-fighting, excessive brightness, and duplicate surfaces.

### ROS 2 / RViz / MoveIt

Copy the selected model into the ROS package's `description/` directory and consider changing its relative paths to:

```text
package://<package_name>/description/meshes/...
```

Also make sure `setup.py` or `CMakeLists.txt` installs every URDF and STL file. RViz handles visualization only; whether MoveIt uses the collision meshes depends on the loaded robot description.

> [!IMPORTANT]
> ROS 2 Jazzy's RViz may render every mesh in a link with multiple differently colored visuals using only that link's first material. Before starting RViz or MoveIt, process the URDF passed to `robot_description` with [`tools/rviz_urdf_compat.py`](tools/rviz_urdf_compat.py). The script writes the converted result to stdout and never modifies the source URDF.

The script moves extra visuals into zero-offset fixed child links, preserving the original mesh poses, materials, and collision definitions. It also lightens the RS black materials for RViz/Ogre display without changing the source URDF or the colors used by Web/MuJoCo. DM does not match those `rs_*` material names, so it only applies the multi-visual split.

Preview the converted output from the command line:

```bash
python3 tools/rviz_urdf_compat.py RS/urdf/ReBot_Arm_RS.urdf > /tmp/ReBot_Arm_RS_rviz.urdf
python3 tools/rviz_urdf_compat.py DM/urdf/ReBot_Arm_DM.urdf > /tmp/ReBot_Arm_DM_rviz.urdf
```

In a Python ROS 2 launch file, feed the script output directly as the `robot_description`:

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

For MoveIt integration, process the `MoveItConfigsBuilder` output before creating the `move_group` and RViz nodes:

```python
from importlib.machinery import SourceFileLoader

compat = SourceFileLoader("rviz_urdf_compat", compat_script_path).load_module()
description_key = "robot_description"
source_urdf = moveit_config.robot_description[description_key]
moveit_config.robot_description[description_key] = (
    compat.make_rviz_compatible(source_urdf)
)
```

Install `tools/rviz_urdf_compat.py` together with the ROS package, and make sure `robot_state_publisher`, the MoveIt `move_group`, and RViz all receive the same processed `robot_description`.

### MuJoCo

This directory provides the STL files required by MuJoCo, but does not contain a complete MJCF scene. In the MJCF, use `<compiler meshdir="...">` or `<mesh file="...">` to reference:

- RS: all 10 detailed collision parts in `RS/meshes/mujoco_collision/`.
- DM: the six segmented parts in `DM/meshes/mujoco_collision/` plus the four carriage and travel-stop parts in `DM/meshes/shared/`.

Do not replace these segmented meshes with a single convex hull of the complete finger. Doing so may reintroduce interpenetration during closing, overly large contact surfaces, or unstable grasping.

## Modification and synchronization rules

1. **Changing colors only:** Prefer changing the URDF `<material>` or the renderer's roughness/metalness. Do not alter collision STL files.
2. **Changing visual geometry:** Check appearance in Web, RViz, and MuJoCo. Do not assume visual changes are automatically reflected in the collision model.
3. **Changing URDF collisions:** Revalidate MoveIt self-collision, the full joint range, and contact near the end effector.
4. **Changing detailed gripper collisions:** RS and DM share the same geometry. Update both versions and revalidate grasping, closing, and release.
5. **Changing finger names or coordinates:** Check the reversed RS left/right mapping and the MJCF `pos/quat` values. Renaming a file alone is not sufficient.
6. **Before release:** Confirm that every URDF reference exists, the XML parses successfully, and filename casing is correct on Linux.

## Sources and synchronization

The current runtime source files are located at:

```text
# RS
rebotarm_ros2_RS/src/rebotarm_bringup/description/
rebotarm_ros2_RS/src/rebotarm_mujoco_rs/models/

# DM (in the DM repository)
reBotArm_ros2_DM/src/rebotarm_bringup/description/
reBotArm_ros2_DM/src/rebotarm_mujoco/models/
```

`Rebot_Arm_description/` is a self-contained copy organized for reuse. When the runtime source models change, synchronize the corresponding URDF and STL files here, then rerun reference-integrity and simulation checks.

## Choosing a model

- For the B601-RS appearance, ROS model, or RS project integration, use the complete `RS/` directory.
- For the B601-DM material-separated parts, ROS model, or DM project integration, use the complete `DM/` directory.
- To reuse only the MuJoCo gripper collisions, either model's geometry can be used, but all 10 parts and the correct left/right coordinate mapping must be retained.
- If you are unsure which files you need, copy the complete model directory. The categories primarily support understanding and maintenance; users do not need to select the files manually.
