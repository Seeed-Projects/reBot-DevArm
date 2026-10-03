<div align="center">

# 🦾 reBot-DevArm

**The Open-Source Robotic Arm for Every Developer**

<img src="./media/RS5_56.png" alt="reBot-DevArm Banner" width="1000">

<a href="https://certification.oshwa.org/cn000024.html"><img src="./media/certification-mark-CN000024-wide.png" alt="OSHWA Certified" width="180"></a>

[![Hardware License: CERN-OHL-W-2.0](https://img.shields.io/badge/License-CERN--OHL--W--2.0--Hardware-green.svg)](./LICENSE)
[![Software License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0--Software-pink.svg)](./LICENSE)
[![ROS](https://img.shields.io/badge/ROS-Noetic%20%7C%20Humble-orange.svg)](#roadmap-and-status)
[![LeRobot](https://img.shields.io/badge/Framework-LeRobot-yellow.svg)](#roadmap-and-status)
[![Isaac Sim](https://img.shields.io/badge/Framework-Isaac%20Sim-yellow.svg)](#roadmap-and-status)
[![Commercial](https://img.shields.io/badge/Commercial-Contact%20Us-red.svg)](mailto:yaohui.zhu@seeed.cc)

**100% Open Source · Embodied AI · Full Hardware + Software Stack**

🌐 [Landing Page](https://279070161-sketch.github.io/reBot/) · 📚 [Tutorial Center](https://wiki.seeedstudio.com/robotics_page/) · ▶ [Online Demo](https://yang-ci.github.io/Rebot_Arm_AGV/)

[![Discord](https://img.shields.io/discord/1409155673572249672?color=7289DA&label=Discord&logo=discord&logoColor=white)](https://discord.gg/AbGuqJhDpQ)
[![Documentation](https://img.shields.io/badge/Documentation-%F0%9F%93%95-blue)](https://wiki.seeedstudio.com/robotics_page/)

[简体中文](README_zh.md) · [English](README.md) · [日本語](README_JP.md) · [français](README_Fr.md) · [Español](README_es.md)

</div>

---

## 📑 Contents

- [📖 Introduction](#introduction)
- [🛒 Get Your reBot Arm](#get-your-rebot-arm)
- [🚀 Try the Online Simulation](#try-the-online-simulation)
- [🗺️ Roadmap and Status](#roadmap-and-status)
- [⚙️ Hardware Specifications](#hardware-specifications)
- [🌟 Community Showcase](#community-showcase)
- [🧹 Optional Hardware](#optional-hardware)
- [🎓 Full-Stack Robotics Ecosystem](#full-stack-robotics-ecosystem)
- [🙌 Acknowledgments and Contributors](#acknowledgments-and-contributors)
- [📄 License](#license)
- [☎ Contact Us](#contact-us)

---

## 📖 Introduction

**reBot-DevArm** — the **reBot Arm B601-DM** and **reBot Arm B601-RS** — is a robotic arm project dedicated to lowering the barrier to learning Embodied AI. We believe in **true open source**: not just the code, but everything, released without reservation.

- 🦾 **Two arm models** — All design files for the **B601-DM (Damiao)** and **B601-RS (Robstride)**, two arms sharing the same appearance.
- 🛠️ **Hardware blueprints** — Source files for sheet-metal and 3D-printed parts.
- 🔩 **BOM list** — Detailed down to the spec and purchase link of every single screw.
- 💻 **Software & algorithms** — Python SDK, ROS1/2, Isaac Sim, LeRobot, and more.

## 🛒 Get Your reBot Arm

| Model | Official Store | Other Channels |
| :--- | :--- | :--- |
| **reBot Arm B601-DM** | [SeeedStudio Bazaar](https://www.seeedstudio.com/reBot-Arm-B601-DM-Assembled-Kit-with-Power-Supply-Bundle.html) | [Amazon](https://www.amazon.com/dp/B0H2TWVFSW) · [AliExpress](https://de.aliexpress.com/item/1005012108314029.html) |
| **reBot Arm B601-RS** | [SeeedStudio Bazaar](https://www.seeedstudio.com/reBot-Arm-B601-RS-Bundle-p-6898.html) | [AliExpress](https://www.aliexpress.us/item/3256812343811970.html?gatewayAdapt=deu2usa4itemAdapt) |

### B601-DM Kit Options

Five kit options are available at [SeeedStudio.com](https://www.seeedstudio.com/reBot-Arm-B601-DM-Bundle.html):

- **Arm Body Motor Kit** — Motors and wiring harnesses only.
- **Arm Body Structural Kit** — Mechanical structural components only.
- **Gripper Complete Kit** — Motors, wiring, and structure for the gripper.
- **Full Kit** — Complete arm body and gripper.
- **Pre-assembled Robotic Arm** — Fully assembled, ready to use.

> 💡 The kit does not include a power adapter or C-clamps as standard, since you may power it with batteries or mount it on a custom DIY base. Purchase a [power supply](https://www.seeedstudio.com/AC-DC-Power-Adapter-IEC-60320-C14-XT30-Female-24V-4-5A-1200mm-L190-W92-5-H36mm-p-6764.html) and [power cord](https://www.seeedstudio.com/reServer-AC-US-p-5052.html) separately, or see the Mean Well solution at the bottom of the [BOM](./hardware/reBot_B601_DM/readme.md#about-power-supply).

### B601-RS Kit Options

Two kit options are available at [SeeedStudio.com](https://www.seeedstudio.com/reBot-Arm-B601-RS-Assembled-Kit-with-Gripper-p-6865.html):

- **Full Kit** — Unassembled complete arm body and gripper.
- **Pre-assembled Robotic Arm** — Fully assembled, ready to use.

> 💡 We recommend the [Mean Well 48V 12.5A](https://www.amazon.com/sspa/click?ie=UTF8&spc=MTo0NzgzODk2NzUxNTQ0NzEyOjE3ODE2MTA2NTU6c3BfYXRmOjIwMDExNjA5NjQwMTc5ODo6MDo6&url=%2FLRS-350-48-Price-Switching-Supply-MeanWell%2Fdp%2FB0BP6S5DYR%2Fref%3Dsr_1_1_sspa%3Fcrid%3D27VPQOWNPN9UG%26dib%3DeyJ2IjoiMSJ9.qK84sGJa4-74kbCEX11MOFBju8sSQUdFsbHw6PNvmaEHnhzjX2T7dyhRNJY01mXxpWk8lccGOwnezxmqLKUjqglX_FI26mrxlvZf0KNiLdJ8QnhKsber4KDoyyLHNxWGV451uHCzZbCDXxM0iYXVnubuVourRaRURlyMorRavuLd2a32kABx-BKqyF5Dfr7dV453ecE6QULFqG-UVLBaBRijbxQGTJ2YiNyXAqn3bkM.Bt5mAPOJNAWGnXCC2mwvjdDdccZd1_0-WRXZpP4mR4M%26dib_tag%3Dse%26keywords%3DLRS-350-48%26qid%3D1781610655%26sprefix%3Dlrs-350-%252Caps%252C331%26sr%3D8-1-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9hdGY%26psc%3D1) power supply for the RS model. For full performance, opt for a 48V 25A adapter.

### Leader Arm (Optional)

Purchase the [Leader Arm](https://www.seeedstudio.com/Star-Arm-102-p-6765.html?qid=P2U7IG_yskyak5m_1776415593315) and a [12V 10A power supply](https://www.seeedstudio.com/FY1209900-12V-10A-Power-Adapter-12V-10A-p-6496.html); the 12V DC adapter of the SO-ARM101 also works.

## 🚀 Try the Online Simulation

Experience the reBot Arm B601-RS MuJoCo digital twin directly in your browser — no installation required. Switch between the standard arm and AGV configurations, control joints and TCP, view the overhead and D405 wrist cameras, and run the automated put-away and stacking demos. The initial model download may take a moment; Chrome or Edge is recommended.

<p align="center">
  <a href="https://yang-ci.github.io/Rebot_Arm_AGV/"><strong>▶ Launch the reBot Arm Interactive Demo</strong></a>
</p>

## 🗺️ Roadmap and Status

We continuously maintain and adapt to mainstream robot development ecosystems. Below is our current progress and release plan.

### reBot Arm B601-DM

| Ecosystem | Status | Description | Documentation |
| :--- | :---: | :--- | :--- |
| Basic Motor Usage | ✅ Done | Motion control and API encapsulation | [Damiao Technology](https://wiki.seeedstudio.com/cn/damiao_series/) |
| STEP 3D Parts & BOM | ✅ Done | STEP files, parts BOM, and reference prices | [reBot Arm B601-DM BOM](./hardware/reBot_B601_DM/readme.md) |
| Real-Machine Performance Testing | ✅ Done | Performance under normal and extreme conditions | [Performance Testing](./hardware/reBot_B601_DM/performance_testing/Performance_Testing.md) |
| Assembly Video | ✅ Done | Ultra-detailed assembly steps and video | [Getting Started](https://wiki.seeedstudio.com/rebot_b601_dm_getting_started/) |
| Python SDK | ✅ Done | One-stop motor read/write & control (Robstride, Damiao, Mota, Gaoqing, Hexfellow…) | [Motorbridge](https://motorbridge.seeedstudio.com) · [Web UI](https://rebot-devarm.w0x7ce.eu/) |
| ROS2 Integration | ✅ Done | Kinematics, trajectory planning, gravity compensation | [ROS2 Guide](https://wiki.seeedstudio.com/rebot_arm_b601_dm_ros2_integration/) |
| Pinocchio Integration | ✅ Done | Forward/inverse kinematics and gravity compensation | [Pinocchio Guide](https://wiki.seeedstudio.com/rebot_arm_b601_dm_pinocchio_meshcat/) · [Repo](https://github.com/Seeed-Projects/reBotArm_control_py) |
| Isaac Sim Simulation | ✅ Done | USD models and simulated teleoperation | [Wiki](https://wiki.seeedstudio.com/rebot_arm_b601_dm_isaacsim/) |
| LeRobot Integration | ✅ Done | Hugging Face LeRobot training framework | [LeRobot Guide](https://wiki.seeedstudio.com/rebot_arm_b601_dm_lerobot/) |
| Depth Camera Integration | ✅ Done | YOLO + depth camera visual grasping demo | [Grasping Demo](https://wiki.seeedstudio.com/rebot_arm_b601_dm_grasping_demo/) |
| reSpeaker Voice Integration | ✅ Done | reSpeaker Flex 4-mic array, voice-driven control with spatial awareness | [Voice Control](https://wiki.seeedstudio.com/control_rebot_arm_using_voice_with_respeaker_flex/) |
| Latest Algorithms | ⏳ Planned | Mainstream algorithms updated progressively | Ongoing |
| Free Course Series | ⏳ Planned | A series of completely free courses | Ongoing |

#### Community Contributions

| Ecosystem | Author | Description | Repository |
| :--- | :---: | :--- | :--- |
| ROS2 (Humble), third-party integration, URDF / rebotarm_bringup | [@danieldoradotalaveron-rb](https://github.com/danieldoradotalaveron-rb) | 1. **Passive diagnostics monitor** (`rebotarm_monitor_ros2`) — `/diagnostics` overlay for `rqt_robot_monitor`, serial/CAN-aware aggregator;<br>2. **Safe park & shutdown** — capture rest pose on connect, slow return on shutdown or `/rebotarm/park`;<br>3. **Gravity compensation (smooth stop)** — MIT ramp-out to eliminate clack and jerk during pos/vel handoff;<br>4. **Gamepad teleop with IK/FK & safety** — end-effector control via IK, live RViz visualization (simulation-only test);<br>5. **D405 eye-in-hand TF** — Xacro under `end_link` for RViz visualization & TF only. | [rebotarm_monitor_ros2](https://github.com/danieldoradotalaveron-rb/rebotarm_monitor_ros2) · [reBotArmController_ROS2](https://github.com/danieldoradotalaveron-rb/reBotArmController_ROS2) |

### reBot Arm B601-RS

| Ecosystem | Status | Description | Documentation |
| :--- | :---: | :--- | :--- |
| Basic Motor Usage | ✅ Done | Motion control and API encapsulation | [Robstride](https://wiki.seeedstudio.com/cn/robstride_control/) |
| STEP 3D Parts & BOM | ✅ Done | STEP files, parts BOM, and reference prices | [reBot Arm B601-RS BOM](./hardware/reBot_B601_RS/README.md) |
| Getting Started | ✅ Done | Quick start for the B601-RS | [Getting Started](https://wiki.seeedstudio.com/rebot_b601_rs_getting_started/) |
| Assembly Video | ✅ Done | Ultra-detailed assembly steps and video | [Assembly Video](https://wiki.seeedstudio.com/rebot_b601_rs_getting_started/) |
| ROS2 (Humble) | ✅ Done | Kinematics, trajectory planning, gravity compensation, MoveIt2 | [ROS2 Guide](https://wiki.seeedstudio.com/rebot_arm_b601_rs_ros2_integration/) |
| LeRobot Integration | ✅ Done | Hugging Face LeRobot training framework | [LeRobot Guide](https://wiki.seeedstudio.com/rebot_arm_b601_rs_lerobot/) |
| Pinocchio Integration | ✅ Done | Forward/inverse kinematics and gravity compensation | [Pinocchio Guide](https://wiki.seeedstudio.com/rebot_arm_b601_rs_pinocchio_meshcat/) · [Repo](https://github.com/Seeed-Projects/reBotArm_control_py) |
| Depth Camera Integration | ✅ Done | YOLO + depth camera visual grasping demo | [Grasping Demo](https://wiki.seeedstudio.com/rebot_arm_b601_rs_grasping_demo/) |
| Embodied Agent Architecture | ✅ Done | Accepts natural-language commands (e.g. "pick up the red block"), auto-plans and executes grasping | [Design](https://wiki.seeedstudio.com/wrc_demo_tutorial/) · [Source](https://github.com/TheMoonAstronaut/wrc.git) |
| Isaac Sim Simulation | ✅ Done | USD models and simulated teleoperation | [DLI Course](https://www.seeedstudio.com/sim-to-real-with-seeed-rebot-and-nvidia-isaac) · [Repo](https://github.com/Seeed-Projects/reBot-Isaacsim) |
| Latest Algorithms | ⏳ Planned | Mainstream algorithms updated progressively | Ongoing |
| Free Course Series | ⏳ Planned | A series of completely free courses | Ongoing |

#### Community Contributions

| Ecosystem | Author | Description | Repository |
| :--- | :---: | :--- | :--- |
| iPhone, HEBI Mobile I/O and Meta Quest teleoperation | [@ammarjmahmood](https://github.com/ammarjmahmood) | Move a phone or a Quest controller and the gripper follows, using the relative pose mapping from TidyBot++ (CoRL 2024): native SwiftUI and ARKit iPhone app, HEBI Mobile I/O, WebXR passthrough on Quest, a 200 Hz MIT driver with gravity feedforward, IK on the official RS URDF and safety interlocks. Tested on a B601-RS with an iPhone 16 Pro Max. | [rebot-phone-teleop](https://github.com/ammarjmahmood/rebot-phone-teleop) |

## ⚙️ Hardware Specifications

Designed for desktop Embodied AI applications, balancing payload and flexibility.

| Parameter | reBot Arm B601-DM | reBot Arm B601-RS |
| :--- | :--- | :--- |
| Payload | 1.5 kg | **2.5 kg** |
| Recommended Workspace | 70% of arm reach | 70% of arm reach |
| Max Reach | 767 mm | **754 mm** |
| Weight | **≈ 4.5 kg** | ≈ 6.7 kg |
| Repeatability | < 0.2 mm | < 0.2 mm |
| Degrees of Freedom | 6 DOF + 1 Gripper | 6 DOF + 1 Gripper |
| Supported Ecosystems | ROS1, ROS2, LeRobot, Pinocchio, Isaac Sim, Python SDK | ROS1, ROS2, LeRobot, Pinocchio, Isaac Sim, Python SDK |
| Supply Voltage | DC 24V | DC 48V |

## 🌟 Community Showcase

|  |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: |
| <a href="https://www.kaggle.com/competitions/gemma-4-good-hackathon/writeups/new-writeup-1778618527713"><img src="/community/GEM-4.png" height="80" alt="GEM-4"></a><br><sub>[GEM-4](https://www.kaggle.com/competitions/gemma-4-good-hackathon/writeups/new-writeup-1778618527713)</sub> | <a href="https://x.com/Linyan_Fu/status/2056383947341525180"><img src="/community/from_Linyan.png" height="80" alt="Linyan Fu"></a><br><sub>[Linyan Fu](https://x.com/Linyan_Fu/status/2056383947341525180) · [Apheth D Almeida](https://x.com/Apheth_DAlmeida/status/2053503164507476096)</sub> | <a href="https://x.com/DhruvDiddi/status/2046605015008383284"><img src="/community/from_Diddi.png" height="80" alt="Dhruv Diddi"></a><br><sub>[Dhruv Diddi](https://x.com/DhruvDiddi/status/2046605015008383284)</sub> | <a href="https://x.com/ed0henderson/status/2055076839002095743"><img src="/community/from_Henderson.jpg" height="80" alt="Ed Henderson"></a><br><sub>[Ed Henderson](https://x.com/ed0henderson/status/2055076839002095743)</sub> | <img src="/community/from_Sameer.png" height="80" alt="Sameer"><br><sub>Sameer</sub> |
| <a href="https://x.com/pham_blnh/status/2061994096374505710"><img src="/community/from_Binh_Pham.png" height="80" alt="Binh Pham"></a><br><sub>[Binh Pham](https://x.com/pham_blnh/status/2061994096374505710)</sub> | <a href="https://www.instagram.com/reel/DY7Ny8OPjVu/?utm_source=ig_web_copy_link&igsh=NTc4MTIwNjQ2YQ=="><img src="/community/from_fangtianchonghui.png" height="80" alt="FangTianChongHui"></a><br><sub>[FangTianChongHui](https://www.instagram.com/reel/DY7Ny8OPjVu/?utm_source=ig_web_copy_link&igsh=NTc4MTIwNjQ2YQ==)</sub> | <a href="https://x.com/dong1505lin"><img src="/community/from_xensedyl.png" height="80" alt="Xense YaoLin Dong"></a><br><sub>[Xense YaoLin Dong](https://x.com/dong1505lin)</sub> | <a href="https://x.com/ed0henderson/status/2055076839002095743"><img src="/community/from_Henderson_2.png" height="80" alt="Ed Henderson"></a><br><sub>[Ed Henderson](https://x.com/ed0henderson/status/2055076839002095743)</sub> | <a href="https://x.com/yoshikai_man/status/2079938975398244705"><img src="/community/YOR_Car.png" height="80" alt="yoshikai_man"></a><br><sub>[yoshikai_man](https://x.com/yoshikai_man/status/2079938975398244705)</sub> |
| <a href="https://github.com/lipengdong/hei-rebot-lift"><img src="/community/hei-robot-lift-play.gif" height="80" alt="hei-rebot-lift"></a><br><sub>[hei-rebot-lift](https://github.com/lipengdong/hei-rebot-lift)</sub> | <a href="https://www.linkedin.com/posts/activity-7484390995862781952-TX4m?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE6WUL4BWkFeyUj0TJ5JlGf6IG4iRHAicUo"><img src="/community/VR_with_reBot.png" height="80" alt="Martin Kemka"></a><br><sub>[Martin Kemka](https://www.linkedin.com/posts/activity-7484390995862781952-TX4m?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE6WUL4BWkFeyUj0TJ5JlGf6IG4iRHAicUo)</sub> | <a href="https://www.linkedin.com/posts/kamil-buczy%C5%84ski-102843301_seeedstudio-rebotarm-seeedprojectofthemonth-ugcPost-7485297094715461633-RV_6/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE6WUL4BWkFeyUj0TJ5JlGf6IG4iRHAicUo"><img src="/community/reBot_grasp_fruit.png" height="80" alt="Kamil Buczyński"></a><br><sub>[Kamil Buczyński](https://www.linkedin.com/posts/kamil-buczy%C5%84ski-102843301_seeedstudio-rebotarm-seeedprojectofthemonth-ugcPost-7485297094715461633-RV_6/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE6WUL4BWkFeyUj0TJ5JlGf6IG4iRHAicUo)</sub> | <a href="https://www.linkedin.com/posts/doradodaniel_computervision-spatialai-sim2real-share-7474727487374184448-NhwX/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE6WUL4BWkFeyUj0TJ5JlGf6IG4iRHAicUo"><img src="/community/Daniel_Dorado.jpg" height="80" alt="Daniel Dorado"></a><br><sub>[Daniel Dorado](https://www.linkedin.com/posts/doradodaniel_computervision-spatialai-sim2real-share-7474727487374184448-NhwX/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE6WUL4BWkFeyUj0TJ5JlGf6IG4iRHAicUo)</sub> | <a href="https://www.linkedin.com/posts/asierarranz_nvidia-physicalai-isaaclab-ugcPost-7480271721942417408-YNwu/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE6WUL4BWkFeyUj0TJ5JlGf6IG4iRHAicUo"><img src="/community/Groot_N1.7.png" height="80" alt="Asier"></a><br><sub>[Asier](https://www.linkedin.com/posts/asierarranz_nvidia-physicalai-isaaclab-ugcPost-7480271721942417408-YNwu/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE6WUL4BWkFeyUj0TJ5JlGf6IG4iRHAicUo)</sub> |
| <a href="https://x.com/thermalpastor/status/2103842737032458567"><img src="/community/thermalpastor.png" height="80" alt="H"></a><br><sub>[H](https://x.com/thermalpastor/status/2103842737032458567)</sub> | <a href="https://x.com/Alpha10six/status/2103860758559994216"><img src="/community/alpha_rover.png" height="80" alt="alpha_rover"></a><br><sub>[alpha_rover](https://x.com/Alpha10six/status/2103860758559994216)</sub> | <a href="https://x.com/DilumSanjaya/status/2102806161728885145"><img src="/community/DilumSanjaya.png" height="80" alt="Dilum Sanjaya"></a><br><sub>[Dilum Sanjaya](https://x.com/DilumSanjaya/status/2102806161728885145)</sub> | <a href="https://x.com/pham_blnh/status/2101003855731593544"><img src="/community/pham_blnh.png" height="80" alt="Binh"></a><br><sub>[Binh](https://x.com/pham_blnh/status/2101003855731593544)</sub> | <a href="https://x.com/LeRobotHF/status/2104519372333048112"><img src="/community/LeRobot.png" height="80" alt="LeRobot"></a><br><sub>[LeRobot](https://x.com/LeRobotHF/status/2104519372333048112)</sub> |
| <a href="https://x.com/raghav2956/status/2104659668375339475"><img src="/community/Raghav_Kumar.png" height="80" alt="Raghav Kumar"></a><br><sub>[Raghav Kumar](https://x.com/raghav2956/status/2104659668375339475)</sub> | <a href="https://www.linkedin.com/posts/kamil-buczy%C5%84ski-102843301_seeedstudio-ai-agent-ugcPost-7510738285707776000-1SMQ/?utm_source=social_share_send&utm_medium=android_app&rcm=ACoAAE6WUL4BWkFeyUj0TJ5JlGf6IG4iRHAicUo"><img src="/community/Kamil_Buczynski.png" height="80" alt="Kamil Buczyński"></a><br><sub>[Kamil Buczyński](https://www.linkedin.com/posts/kamil-buczy%C5%84ski-102843301_seeedstudio-ai-agent-ugcPost-7510738285707776000-1SMQ/?utm_source=social_share_send&utm_medium=android_app&rcm=ACoAAE6WUL4BWkFeyUj0TJ5JlGf6IG4iRHAicUo)</sub> | <a href="https://www.linkedin.com/feed/update/urn:li:activity:7510701008885309440/"><img src="/community/Fictionlab.png" height="80" alt="Fictionlab"></a><br><sub>[Fictionlab](https://www.linkedin.com/feed/update/urn:li:activity:7510701008885309440/)</sub> | <a href="https://x.com/seeedstudio/status/2101965998954107303"><img src="/community/box2bridge.png" height="80" alt="box2bridge"></a><br><sub>[box2bridge](https://x.com/seeedstudio/status/2101965998954107303)</sub> | <a href="https://x.com/seeedstudio/status/2095469352976003482"><img src="/community/Fangtian.png" height="80" alt="FangTianChongHui"></a><br><sub>[FangTianChongHui](https://x.com/seeedstudio/status/2095469352976003482)</sub> |

<p align="center">
  <a href="https://www.seeedstudio.com/sim-to-real-with-seeed-rebot-and-nvidia-isaac"><img src="/community/sim-to-real-vla.gif" height="90" alt="Sim-to-Real VLA Course"></a><br>
  <sub><a href="https://www.seeedstudio.com/sim-to-real-with-seeed-rebot-and-nvidia-isaac">Seeed reBot Arm × NVIDIA Isaac — Sim-to-Real VLA Course</a></sub>
</p>

## 🧹 Optional Hardware

### Wrist Camera Mount

| 32×32 UVC | Intel D435i | Intel D405 & Gemini 305 | Gemini 2 |
| :--- | :--- | :--- | :--- |
| <img src="./hardware/reBot_B601_DM/3D_Printed_Parts/images/UVC_camera_mount.png" height="100"> | <img src="./hardware/reBot_B601_DM/3D_Printed_Parts/images/D435i.jpg" height="100"> | <img src="./hardware/reBot_B601_DM/3D_Printed_Parts/images/D405.jpg" height="100"> | <img src="./hardware/reBot_B601_DM/3D_Printed_Parts/images/Gemini2.jpg" height="100"> |
| [STEP](hardware/reBot_B601_DM/3D_Printed_Parts/UVC32_mount.step) | [STEP](hardware/reBot_B601_DM/3D_Printed_Parts/D435_Gemini2_Mount.step) | [STEP](hardware/reBot_B601_DM/3D_Printed_Parts/D405_305_Mount.step) · [design notes](https://github.com/bowenszhu/rebot-b601-rs-d405-wrist-mount/tree/v1.0.0) | [STEP](hardware/reBot_B601_DM/3D_Printed_Parts/D435_Gemini2_Mount.step) |

### Leader Arm Compatibility

| Star Arm 102-LD | Open to compatibility integration |
| :--- | :--- |
| <img src="./hardware/reBot_B601_DM/3D_Printed_Parts/images/star_arm_102.jpg" height="100"> | [Series Hub](https://fashionstar.com.hk/robot-arm/star-arm-102/) · [GitHub repo](https://github.com/servodevelop/Star-Arm-102) |

### DIY Soft Finger

| Soft Finger | Open to compatibility integration |
| :--- | :--- |
| <img src="./hardware/reBot_B601_DM/3D_Printed_Parts/images/Soft_Finger.png" height="100"> | Coming soon |
| [Finger Mount (ABS/PLA)](hardware/reBot_B601_DM/3D_Printed_Parts/Soft_Gripper_Mount.step) · [Finger (TPU 95+)](hardware/reBot_B601_DM/3D_Printed_Parts/Soft_Gripper_Finger.step) | Coming soon |

### Recommended Optional Hardware

| Category | Type | Preview | Product | Link |
| :--- | :--- | :--- | :--- | :--- |
| **Camera** | Depth Camera | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/0/-/0-101090144--orbbec-gemini-2-3d-camera.jpg" alt="Orbbec Gemini 2" width="120"> | **Orbbec Gemini 2 3D Camera** | [Seeed Studio](https://www.seeedstudio.com/Orbbec-Gemini-2-3D-Camera-p-6464.html) |
| **Camera** | Depth Camera | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/1/0/1000000774.png" alt="Orbbec Gemini 336" width="120"> | **Orbbec Gemini 336 Depth Camera** | [Seeed Studio](https://www.seeedstudio.com/Orbbec-Gemini-336-3D-Camera-3D-p-6662.html) |
| **Camera** | Depth Camera | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/1/-/1-100010971-orbbec-gemini-335-lg.jpg" alt="Orbbec Gemini 335LG" width="120"> | **Orbbec Gemini 335LG 3D Camera** | [Seeed Studio](https://www.seeedstudio.com/Orbbec-Gemini-335LG-3D-Camera-p-6541.html) |
| **Camera** | Depth Camera | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/0/0/0035718.png" alt="SLAMTEC Aurora S" width="120"> | **SLAMTEC Aurora S** | [Seeed Studio](https://www.seeedstudio.com/SLAMTEC-Aurora-S-AI-Integrated-Spatial-Perception-System-p-6669.html) |
| **Camera** | Depth Camera | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/i/n/intel_realsense_d435i_34_1_1.jpg" alt="Intel RealSense D435i" width="120"> | **Intel RealSense Depth Camera D435i** | [Seeed Studio](https://www.seeedstudio.com/Intel-RealSense-Depth-Camera-D435i-p-4423.html) |
| **Camera** | Depth Camera | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/1/-/1-100000540-realsense-d405-3d-camera.jpg" alt="RealSense D405" width="120"> | **RealSense Depth Camera D405** | [Seeed Studio](https://www.seeedstudio.com/RealSense-D405-3D-Camera-p-6758.html) |
| **Camera** | Monocular Camera | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/0/-/0-101090101-3mp-gmsl2-camera-module-190-degree.jpg" alt="Sensing SG3S-ISX031C-GMSL2F" width="120"> | **Sensing SG3S-ISX031C-GMSL2F 3MP GMSL2 Camera** | [Seeed Studio](https://www.seeedstudio.com/SG3S-ISX031C-GMSL2F-p-6245.html) |
| **Camera** | Monocular Camera | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/s/2/s231.1.jpg" alt="ET-S231" width="120"> | **ET-S231 Megapixel 120° Wide-Angle 1080P USB Camera** | [Seeed Studio](https://www.seeedstudio.com/ET-S231-120-USB-Camera-p-6683.html) |
| **Microphone** | Mic Array | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/1/-/1-100070894-respeaker-flex-xvf3800-circular-4-with-xiao-esp32s3_1_.jpg" alt="reSpeaker Flex XVF3800" width="120"> | **reSpeaker Flex XVF3800 Circular-4 with XIAO ESP32S3** | [Seeed Studio](https://www.seeedstudio.com/reSpeaker-Flex-XVF3800-Circular-4-with-XIAO-ESP32S3-p-6739.html) |
| **Microphone** | Mic Array | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/1/-/1-respeaker-xvf3800-4-mic-array.jpg" alt="reSpeaker XMOS XVF3800" width="120"> | **reSpeaker XMOS XVF3800** | [Seeed Studio](https://www.seeedstudio.com/ReSpeaker-XVF3800-USB-Mic-Array-p-6488.html) |
| **Controller** | Edge Controller | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/1/1/110110147.jpg" alt="reComputer J3011" width="120"> | **reComputer J3011-Orin Nano 8GB** | [Seeed Studio](https://www.seeedstudio.com/reComputer-J3011-p-5590.html) |
| **Controller** | Edge Controller | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/i/m/image-kit-3.png" alt="Jetson AGX Thor" width="120"> | **NVIDIA Jetson AGX Thor Developer Kit** | [Seeed Studio](https://www.seeedstudio.com/NVIDIA-Jetson-AGX-Thor-Developer-Kit-p-9965.html) |

## 🎓 Full-Stack Robotics Ecosystem

reBot-DevArm is not just a robotic arm — it is a robotics learning community. The following general tutorials are shared for free:

**🖥️ Edge Computing & Master Control**

- [![Jetson](https://img.shields.io/badge/NVIDIA-reComputer%20Jetson-76B900?style=for-the-badge&logo=nvidia&logoColor=white)](https://wiki.seeedstudio.com/NVIDIA_Jetson/) — AI inference & compute core
- [![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-4B%20%2F%205-C51A4A?style=for-the-badge&logo=Raspberry%20Pi&logoColor=white)](https://wiki.seeedstudio.com/raspberry-pi-devices/) — general Linux dev environment
- [![ESP32](https://img.shields.io/badge/MCU-Seeed%20XIAO%20(ESP32)-0091BD?style=for-the-badge&logo=espressif&logoColor=white)](https://wiki.seeedstudio.com/SeeedStudio_XIAO_Series_Introduction/) — low-power wireless control node

**📡 Sensors & Peripherals**

- **Motors & Servos** — [Damiao / Gogo / Robstride / Mita / Feite / Fashion Star](https://wiki.seeedstudio.com/robotics_page/)
- **Visual Perception** — [Depth cameras / LiDAR / vision algorithms](https://wiki.seeedstudio.com/robotics_page/)
- **Voice Interaction** — [reSpeaker mic arrays / voice control / spatial awareness (DoA)](https://wiki.seeedstudio.com/control_rebot_arm_using_voice_with_respeaker_flex/)
- **Motion & Attitude** — [IMU (6/9-axis) / gyroscopes / magnetometers](https://wiki.seeedstudio.com/Sensor_accelerometer/)
- **Comprehensive Kits** — [more robotics sensors & driver examples](https://wiki.seeedstudio.com/robotics_page/)

> 👉 **[Enter the Wiki Knowledge Base](https://wiki.seeedstudio.com/)** — all tutorials are free to view.

## 🙌 Acknowledgments and Contributors

The path of open source is never lonely. The reBot-DevArm project would not exist without the support of Seeed Studio, the global open-source community, and our hardware partners.

**🌍 Ecosystem & Software Support**

- [Seeed Studio](https://www.seeedstudio.com/) — hardware supply chain and technical support
- [Hugging Face LeRobot](https://github.com/huggingface/lerobot) — end-to-end robot learning framework
- [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim) — robot simulation and synthetic data platform

**⚙️ Core Hardware Partners**

- [Damiao Technology](https://www.damiaokeji.com/)
- [Robstride](https://robstride.com/)
- [Fashion Star](https://fashionstar.com.hk/wiki/)

**💡 Inspiration**

- [SO-ARM100](https://github.com/TheRobotStudio/SO-ARM100/tree/main)
- [Mobile ALOHA](https://github.com/tonyzhaozh/aloha)
- [Dummy-Robot (Zhihui Jun)](https://github.com/peng-zhihui/Dummy-Robot)
- [OpenArm](https://openarm.dev/)
- [I2RT](https://i2rt.com/)
- [TRLC-DK1](https://github.com/robot-learning-co/trlc-dk1)

**🎃 Prototype Contributors**

- SeeedStudio AI Robotics Team — Yaohui Zhu (yaohui.zhu@seeed.cc)
- SeeedStudio STU — Wentao Dong
- SeeedStudio STU — Weiwei Xu
- SeeedStudio Purchasing Department — Fengqun Peng

**👥 Contributors**

<p align="center"><a href="https://github.com/Seeed-Projects/reBot-DevArm/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=Seeed-Projects/reBot-DevArm" />
</a></p>

*Coming soon — welcome to submit PRs and become a contributor!*

### ⭐ Star History

<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/star-history/star-history-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/star-history/star-history-light.svg">
  <img src="assets/star-history/star-history-light.svg">
</picture>
</p>

## 📄 License

- **Hardware Design** © 2026 Seeed Studio Co., Ltd. — open sourced under [CERN-OHL-W-2.0](https://ohwr.org/cern_ohl_w_v2.txt)
- **Firmware Code** © 2026 Seeed Studio Co., Ltd. — open sourced under [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)

### Rights and Restrictions

The reBot Arm project has always followed the core philosophy of **agility, openness, responsibility, and symbiosis** to serve the developer community. Our vision is to let every enthusiast master the hardware architecture and software principles of robotic arms, and experience cutting-edge embodied-intelligence algorithms through reBot.

For the first five months after launch, the project used the **CC BY-SA NC (Non-Commercial)** license, so developers could focus on iterating and improving the product during its early phase. After months of polishing, **effective May 11, 2026**, the project transitioned to the **CERN-OHL-W 2.0** open-source license, achieving **100% full-stack open source (hardware and software) with full commercial-compliance and usage rights for all scenarios**.

Hardware and software use different licenses — please confirm the terms applicable to the part you use.

| Item | Hardware (CERN-OHL-W-2.0) | Software SDK (Apache-2.0) |
| :--- | :--- | :--- |
| ✅ Commercial Use | ✅ Allowed | ✅ Allowed |
| ✅ Modification | ✅ Allowed | ✅ Allowed |
| ✅ Redistribution | ✅ Allowed | ✅ Allowed |
| ✅ Closed-source Integration | ❌ Conditional (see [CERN-OHL-W-2.0](https://ohwr.org/cern_ohl_w_v2.txt)) | ✅ Allowed (no disclosure required) |
| ⚠️ Copyright Retention | ✅ Required | ✅ Required |
| ⚠️ License Text Retention | ✅ Required | ✅ Required |
| ⚠️ Modification Notice | ✅ Required (date + description) | ✅ Required (description) |
| ⚠️ Patent Grant | ✅ Explicit | ✅ Explicit |
| ⚠️ Source Provision on Distribution | ✅ Must provide "Complete Source" | ❌ Not required |
| ⚠️ External/Closed Module Compatibility | ✅ Allowed (Weakly Reciprocal) | ✅ Fully allowed |
| 🔗 Relation to Other Components | Independent interface modules (External Material) may stay closed | No restrictions |
| 📄 Official Full Text | [CERN-OHL-W-2.0](https://ohwr.org/cern_ohl_w_v2.txt) | [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) |

## ☎ Contact Us

- **Open-Source Progress & Technical Support** — Yaohui: yaohui.zhu@seeed.cc
- **Future Collaboration & Customization** — Elaine: elaine.wu@seeed.cc
