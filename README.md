
# 🦾 reBot-DevArm: Open Source Robotic Arm for All Developers

<p align="center">
  <img src="./media/v1.5.jpg" alt="reBot-DevArm Banner">
</p>

<p align="center">
    <!-- Replaced with CC BY-NC-SA 4.0 badge, explicitly indicating non-commercial use -->
    <a href="./LICENSE">
        <img src="https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg" alt="License: CC BY-NC-SA 4.0">
    </a>
    <img src="https://img.shields.io/badge/Commercial-Contact%20Us-red.svg" alt="yaohui.zhu@seeed.cc">
    <img src="https://img.shields.io/badge/ROS-Noetic%20%7C%20Humble-orange.svg" alt="ROS Support">
    <img src="https://img.shields.io/badge/Framework-LeRobot-yellow.svg" alt="LeRobot">
    <img src="https://img.shields.io/badge/Framework-Isaac Sim-yellow.svg" alt="LeRobot">
</p>

<p align="center">
  <strong>100% Fully Open Source · Embodied AI · Hardware-Software Integration · Free for Personal/Education · Commercial Use Requires Authorization</strong>
</p>

<p align="center">
  <strong>
    <a href="./README_zh.md">简体中文</a> &nbsp;|&nbsp;
    <a href="./README.md">English</a> &nbsp;|&nbsp;
    <a href="./README_JP.md">日本語</a>&nbsp;|&nbsp;
    <a href="./README_Fr.md">français</a>
  </strong>
</p>

<p align="center">
<a href="https://discord.gg/AbGuqJhDpQ">
    <img src="https://img.shields.io/discord/1409155673572249672?color=7289DA&label=Discord&logo=discord&logoColor=white"></a>
<a href="https://wiki.seeedstudio.com/robotics_page/">  
    <img src="https://img.shields.io/badge/Documentation-📕-blue" alt="robotics wiki"></a>
</p>

## 📖 Introduction

**reBot-DevArm** is a robotic arm project dedicated to lowering the barrier to learning Embodied AI. We focus on **"True Open Source"** — not just the code, we unreservedly open source everything:

- 🛠️ **Hardware Blueprints**: Source files for sheet metal parts and 3D printed parts.
- 🔩 **BOM List**: Detailed down to the specifications and purchase links for every single screw.
- 💻 **Software & Algorithms**: Python SDK, ROS1/2, Isaac Sim, LeRobot, etc.

**⚠️ Note: This project is intended to promote education and personal learning. All resources are completely free for individual developers, students, and educational institutions. However, any unauthorized commercial use (including but not limited to selling kits directly or using it as part of a commercial product) is strictly prohibited.**

## 🗺️ Roadmap & Status

We are committed to continuously maintaining and adapting to mainstream robot development ecosystems. Below is our current adaptation progress and planned release schedule:

| Ecosystem | Status | Description / ETA | Documentation |
| :--- | :---: | :--- | :--- |
| **Basic Motor Usage** | ✅ Done | Basic motion control and API encapsulation | [View Docs](https://wiki.seeedstudio.com/cn/damiao_series/) |
| **New Version STEP 3D Structure & BOM** | 🚧 In Progress | STEP files for all new parts, component BOM, and reference prices for all machined parts | [ETA 2026.02] |
| **Assembly Video** | 🚧 In Progress | Ultra-detailed assembly steps and video | [ETA 2026.02] |
| **ROS2 (Humble)** |⏳ Planned | Core driver completed, optimizing MoveIt2 |[ETA 2026.03]|
| **LeRobot Adaptation** | ⏳ Planned | Adapting to the Hugging Face LeRobot training framework | [ETA 2026.03]|
| **Pinocchio Adaptation** | ⏳ Planned | Adapting to the Pinocchio framework, implementing forward/inverse kinematics and dynamic gravity compensation | [ETA 2026.03]|
| **Isaac Sim Simulation** | ⏳ Planned | Importing USD models and implementing simulation teleoperation | [ETA 2026.03]|
| **Gradual Algorithm Updates** | ⏳ Planned | Gradually updating mainstream algorithms | Continuous |
| **Launch of Fully Free Courses** | ⏳ Planned | Step-by-step tutorials | Continuous |

---


### 🎓 Full-Stack Robotics Ecosystem
reBot-DevArm is not just a robotic arm, but a robotics learning community. We share the following general tutorials for free:

#### 🖥️ Edge Computing & Master Control
*   [![Jetson](https://img.shields.io/badge/NVIDIA-reComputer%20Jetson-76B900?style=for-the-badge&logo=nvidia&logoColor=white)](https://wiki.seeedstudio.com/NVIDIA_Jetson/) —— **AI Inference & Compute Core**
*   [![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-4B%20%2F%205-C51A4A?style=for-the-badge&logo=Raspberry%20Pi&logoColor=white)](https://wiki.seeedstudio.com/raspberry-pi-devices/) —— **General Linux Development Environment**
*   [![ESP32](https://img.shields.io/badge/MCU-Seeed%20XIAO%20(ESP32)-0091BD?style=for-the-badge&logo=espressif&logoColor=white)](https://wiki.seeedstudio.com/SeeedStudio_XIAO_Series_Introduction/) —— **Low-power Wireless Control Node**

#### 📡 Sensors & Peripherals
*   **🚗 Motors & Servos**: [Damiao / Gogo / Robstride / Mita / Feite / Fashion Star](https://wiki.seeedstudio.com/robotics_page/)
*   **👁️ Visual Perception**: [Depth Cameras / LiDAR / Vision Algorithms](https://wiki.seeedstudio.com/robotics_page/)
*   **👂 Auditory Interaction**: [ReSpeaker Mic Arrays / Speech Recognition](https://wiki.seeedstudio.com/ReSpeaker_Mic_Array_v2.0/)
*   **🧭 Motion & Attitude**: [IMU (6-axis/9-axis) / Gyroscopes / Magnetometers](https://wiki.seeedstudio.com/Sensor/IMU/)
*   **🤖 Comprehensive Kits**: [More Robotics Sensors & Driver Examples](https://wiki.seeedstudio.com/robotics_page/)


> 👉 **[Click to Enter Wiki Knowledge Base](https://wiki.seeedstudio.com/)** (All tutorials are free to view)

---

## ⚙️ Hardware Specifications

reBot-DevArm is designed for desktop Embodied AI applications, balancing payload capacity with flexibility.

| Parameter | Value / Description |
| :--- | :--- |
| **Payload** | **1.5+ kg** |
| **Max Reach** | **650 mm** |
| **Weight** | Approx. 4.0 kg |
| **Repeatability** | < 0.2 mm |
| **Degrees of Freedom (DOF)** | 6 DOF + 1 Gripper (Open source CAN servo gripper and joint motor gripper coming soon) |
| **Supported Platforms/Ecosystems** | ROS1, ROS2, LeRobot, Pinocchio, Isaac Sim, Python SDK |
| **Supply Voltage** | DC 24V |

---

## 📂 Open Source (Hardware Source)

We believe hardware open source fosters innovation. You can find everything needed to build this arm in the following directories:

*   [`/hardware/STEP`](./hardware/cad): STEP/STL files for all mechanical structures, including printed parts, metal parts, and purchased items.
*   [`/hardware/bom`](./hardware/bom): **BOM List** (Includes purchased component models, motor parameters, recommended vendors).
*   [`/tutorial/ROS`](./tutorial/ROS/): Source code and tutorials for **ROS1/2 Noetic/Humble**.
*   [`/tutorial/Lerobot`](./tutorial/lerobot/): Source code and tutorials for **LeRobot**.
*   [`/tutorial/Isaac`](./tutorial/Isaac/): Source code and tutorials for **Isaac Sim**.
---

## 🚀 Getting Started

We have planned a complete learning path for you, from unboxing to AI simulation:

### 🛠️ Phase 1: Hardware Build & Basics
| Step | Description | Link |
| :---: | :--- | :--- |
| **01** | **Basic Learning of Motors** | [📄 Click to View](https://wiki.seeedstudio.com/cn/damiao_series/) |
| **02** | **Unboxing** | Coming Soon |
| **03** | **Assembly Guide** | Coming Soon |
| **04** | **Zero Calibration** | Coming Soon |
| **05** | **Kinematics Testing** | Coming Soon |

### 💻 Phase 2: Advanced Algorithms & Simulation
| Step | Description | Link |
| :---: | :--- | :--- |
| **06** | **ROS Ecosystem** (ROS2) | 🐢 Coming Soon |
| **07** | **AI Training** (Hugging Face) | 🤗 Coming Soon |
| **08** | **Simulation** (NVIDIA) | 🌌 Coming Soon |

---

## 🙌 References & Acknowledgments
The path of open source is never lonely. The birth of the reBot-DevArm project would not be possible without the full support of Seeed Studio, the global open source community, and excellent hardware partners. We pay our highest respects to the following projects and teams:

### 🌍 Ecosystem & Software Support
*   **[Seeed Studio](https://www.seeedstudio.com/)** - Providing comprehensive hardware supply chain and technical support.
*   **[Hugging Face LeRobot](https://github.com/huggingface/lerobot)** - An excellent end-to-end robot learning framework.
*   **[NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim)** - A powerful robot simulation and synthetic data platform.

### ⚙️ Core Hardware Partners
Thanks to the following manufacturers for providing high-performance motor and actuator solutions:
*   **[Damiao Technology](https://www.damiaokeji.com/)**
*   **[Robstride](https://robstride.com/)**
*   **[Fashion Star](https://fashionrobo.com/)**

### 💡 Inspiration
This project is deeply inspired by the following excellent open source projects:
*   **[SO-ARM100](https://github.com/TheRobotStudio/SO-ARM100/tree/main)**
*   **[Mobile ALOHA](https://github.com/tonyzhaozh/aloha)**
*   **[Dummy-Robot (Zhihui Jun)](https://github.com/peng-zhihui/Dummy-Robot)**
*   **[OpenArm](https://openarm.dev/)**
*   **[I2RT](https://i2rt.com/)**
*   **[TRLC-DK1](https://github.com/robot-learning-co/trlc-dk1)**

### 🎃 Prototype Contributors
- **SeeedStudio AI Robotics Team's**: Yaohui Zhu (yaohui.zhu@seeed.cc)
- **SeeedStudio STU**: Wentao Dong
- **SeeedStudio STU**: Weiwei Xu
- **SeeedStudio Purchasing Department**: Fengqun Peng


### 👥 Contributors

## Our Top Contributors 
<p align="center"><a href="https://github.com/Seeed-Projects/reBot-DevArm/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=Seeed-Projects/reBot-DevArm" />
</a></p>



*Coming soon... Welcome to submit PRs to become a contributor!*



# reBot-DevArm Project License
Copyright (c) [2025] [Seeed Studio AI Robotics Team]

This work is licensed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License**.
To view a copy of this license, visit: http://creativecommons.org/licenses/by-nc-sa/4.0/

--------------------------------------------------------------------------------

## Rights and Restrictions
1. You are free to:
   - Share: Copy and redistribute the material in any medium or format.
   - Adapt: Remix, transform, and build upon the material.

2. Under the following terms:
   - Attribution: You must give appropriate credit, provide a link to the license, and indicate if changes were made.
   - NonCommercial: **You may not use the material for commercial purposes**.
     (Including but not limited to selling related kits, selling printed parts, or integrating this software into paid products without explicit permission).
   - ShareAlike: If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.

3. Commercial Authorization:
   If you wish to use this project for commercial purposes, please contact the author to obtain commercial authorization.
   Contact: yaohui.zhu@seeed.cc

