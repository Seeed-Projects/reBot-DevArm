
# 🦾 reBot-DevArm: Open Source Robotic Arm for All Developers

<p align="center">
  <img src="./media/v1.0.png" alt="reBot-DevArm Banner">
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
  <strong>🚀 100% Open Source · Embodied AI · Full Hardware + Software Stack</strong>
</p>

<p align="center">
  <strong>📦 Build your own robotic arm · 🧠 Learn robotics · 🏭 Deploy real applications</strong>
</p>


<p align="center">
  <strong>
    <a href="./README_zh.md">简体中文</a> &nbsp;|&nbsp;
    <a href="./README.md">English</a> &nbsp;|&nbsp;
    <a href="./README_JP.md">日本語</a>&nbsp;|&nbsp;
    <a href="./README_Fr.md">français</a>&nbsp;|&nbsp;
    <a href="./README_es.md">Español</a>
  </strong>
</p>

<p align="center">
<a href="https://discord.gg/AbGuqJhDpQ">
    <img src="https://img.shields.io/discord/1409155673572249672?color=7289DA&label=Discord&logo=discord&logoColor=white"></a>
<a href="https://wiki.seeedstudio.com/robotics_page/">  
    <img src="https://img.shields.io/badge/Documentation-📕-blue" alt="robotics wiki"></a>
</p>

## 📖 Introduction

**reBot-DevArm (reBot Arm B601 DM and reBot Arm B601 RS)** is a robotic arm project dedicated to lowering the barrier to learning Embodied AI. We focus on **"True Open Source"** — not just the code, we unreservedly open source everything:
- 🦾 **Two versions of the robotic arm**：We will provide all open-source files for two versions of the robotic arm with the same appearance: **Robostride** and **Damiao**.
- 🛠️ **Hardware Blueprints**: Source files for sheet metal parts and 3D printed parts.
- 🔩 **BOM List**: Detailed down to the specifications and purchase links for every single screw.
- 💻 **Software & Algorithms**: Python SDK, ROS1/2, Isaac Sim, LeRobot, etc.

## Build Your Own reBot Arm

- We offer five kit options:
  - **Arm Body Motor Kit**: Includes only motors and wiring harnesses for the robotic arm.
  - **Arm Body Structural Kit**: Includes only mechanical structural components.
  - **Gripper Complete Kit**: Includes motors, wiring harnesses and structural components for the gripper.
  - **Full Kit**: Includes the complete set of the robotic arm body and gripper.
  - **Pre‑assembled Robotic Arm**: Fully assembled finished robotic arm.

You may purchase the remaining parts from the SeeedStudio Store based on the components you already have (expected availability: April 15, 2026).

[You can leave your information here, and we will send you the limited pre-order link in advance.](https://forms.gle/1MwdVKUqkuGu3C7L7)


## 🗺️ Roadmap & Status

We are committed to continuously maintaining and adapting to mainstream robot development ecosystems. Below is our current adaptation progress and planned release schedule:

### reBot Arm B601 DM
| Supported Ecosystem | Status | Description / Estimated Release Date | Related Documentation |
| :--- | :---: | :--- | :--- |
| **Basic Motor Usage** | ✅ Completed | Basic motion control and API encapsulation | [Damiao Technology](https://wiki.seeedstudio.com/cn/damiao_series/) |
| **Open-Sourcing of the New STEP 3D Structural Parts and BOM** | ✅ Completed | STEP files for all parts in the new version, parts BOM, and reference prices for all machined components | [reBot Arm B601-DM BOM](./hardware/reBot_B601_DM/readme.md) |
| **Reference for Real Machine Performance Testing** | ✅ Completed   | Performance Reference of Robotic Arm under Normal and Extreme Operating Conditions |[Performance Testing](./hardware/reBot_B601_DM/performance_testing/Performance_Testing.md) |
| **Assembly Video** | 🚧 In Progress | Ultra-detailed assembly steps and video | [Expected: 2026.04.10] |
| **ROS2 (Humble)** | 🚧 In Progress  | Core drivers have been completed, and MoveIt2 is currently being optimized | [Expected: 2026.04.10] |
| **Python SDK** | 🚧 In Progress  |  | [Expected: 2026.04.10] |
| **Pinocchio Integration** | 🚧 In Progress  | Adaptation to the Pinocchio framework, enabling forward/inverse kinematics and gravity compensation for the robotic arm | [GitHub Repository](https://github.com/vectorBH6/reBotArm_control_py/tree/main) Continuously Updating |
| **Isaac Sim Simulation** | 🚧 In Progress  | Import USD models and enable simulated teleoperation | [Expected: 2026.04.20] |
| **LeRobot Integration** | 🚧 In Progress  | Adaptation to the Hugging Face LeRobot training framework | [Expected: 2026.04.30] |
| **Gradual Updates of the Latest Algorithms** | ⏳ Planned | Mainstream algorithms will be updated progressively | Ongoing |
| **Launch of a Series of Completely Free Courses** | ⏳ Planned | Mainstream algorithms will be updated progressively | Ongoing |



### reBot Arm B601 RS

| Supported Ecosystem | Status | Description / Estimated Release Date | Related Documentation |
| :--- | :---: | :--- | :--- |
| **Basic Motor Usage** | ✅ Completed | Basic motion control and API encapsulation | [Robstride](https://wiki.seeedstudio.com/cn/robstride_control/) |
| **Open-Sourcing of the New STEP 3D Structural Parts and BOM** | 🚧 In Progress | STEP files for all parts in the new version, parts BOM, and reference prices for all machined components | Expected [2026.04.31] |
| **Assembly Video** | 🚧 In Progress | Ultra-detailed assembly steps and video | [Expected 2026.05.10] |
| **ROS2 (Humble)** | ⏳ Planned | Core drivers have been completed, and MoveIt2 is currently being optimized | [Expected 2026.05] |
| **LeRobot Integration** | ⏳ Planned | Adaptation to the Hugging Face LeRobot training framework | [Expected 2026.05] |
| **Pinocchio Integration** | ⏳ Planned | Adaptation to the Pinocchio framework, enabling forward/inverse kinematics and gravity compensation for the robotic arm | [Expected 2026.05] |
| **Isaac Sim Simulation** | ⏳ Planned | Import USD models and enable simulated teleoperation | [Expected 2026.05] |
| **Gradual Updates of the Latest Algorithms** | ⏳ Planned | Mainstream algorithms will be updated progressively | Ongoing |
| **Launch of a Series of Completely Free Courses** | ⏳ Planned | Mainstream algorithms will be updated progressively | Ongoing |



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

| Parameter | reBot Arm B601-DM |
| :--- | :--- |
| **Recommended Continuous Payload** | Less than 1.5 kg within 70% of arm reach workspace |
| **Recommended Payload** | **1.5 kg** |
| **Max Reach** | **650 mm** |
| **Weight** | Approx. 4.5 kg |
| **Repeatability** | < 0.2 mm |
| **Degrees of Freedom (DOF)** | 6 DOF + 1 Gripper (Open source CAN servo gripper and joint motor gripper coming soon) |
| **Supported Platforms/Ecosystems** | ROS1, ROS2, LeRobot, Pinocchio, Isaac Sim, Python SDK |
| **Supply Voltage** | DC 24V |

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

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Seeed-Projects/reBot-DevArm&type=date&legend=top-left)](https://www.star-history.com/#Seeed-Projects/reBot-DevArm&type=date&legend=top-left)

# reBot-DevArm Project License
Copyright (c) [2025] [Seeed Studio]

This work is licensed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License**.
To view a copy of this license, visit: http://creativecommons.org/licenses/by-nc-sa/4.0/

--------------------------------------------------------------------------------

## Rights and Restrictions Statement

The core purpose of this open-source project is to promote knowledge sharing and enable developers and enthusiasts to access and learn cutting-edge robotic arm technologies at minimal cost. We provide completely free and publicly available documentation and video tutorials to help users get started quickly, conduct in-depth research, and jointly promote the popularization and practical application of robotics.

### I. Non-Commercial Use Policy

All open-source content of this project is fully available for personal learning, research, and non-commercial use. Individual users are allowed to:

* View and study the project’s open-source documentation, code, and tutorials;
* Modify and debug the open-source content for personal learning and research purposes;
* Assemble robotic arms for personal use or conduct secondary development based on the open-source content for non-commercial purposes.

### II. Commercial Use Policy

We actively encourage and support developers, robotics enthusiasts, and third-party platforms to carry out secondary development based on the reBot robotic arm and promote real-world applications. The following outlines permitted and prohibited commercial activities:

#### (1) Permitted Commercial Activities

We respect every developer’s efforts and legitimate earnings. If you purchase the reBot B601 series robotic arm from Seeed and contribute your own work, you may commercialize the results of your efforts, including but not limited to:

* Developing application-oriented software systems and promoting or selling them commercially;
* Creating structured educational courses (online/offline) and offering paid training or knowledge services;
* Conducting offline education, training, and technology outreach activities worldwide;
* Other commercial activities that contribute to the open-source community, knowledge dissemination, and real-world application of robotics technology.

For the above compliant commercial activities, you are welcome to contact us. We will provide commercial authorization, implementation support, and promotional assistance. We may also publicly announce your authorization to help your project succeed.

#### (2) Prohibited Commercial Activities

It is prohibited to make minor modifications to this project’s product, replace IP, logos, or related identifiers, and sell it under a self-owned brand. Such actions do not constitute substantial technical innovation and do not benefit developer growth, the open-source community, or the project itself. These behaviors are considered violations, and we reserve the right to take action.

### III. Collaboration & Contact

We hope to collaborate with all developers and partners within a compliant framework to promote the maturity and deployment of the reBot robotic arm project. For individuals and organizations interested in bringing real-world robotic applications to life, we offer:

* Commercial licensing and intellectual property compliance support;
* Assistance in promoting project solutions;
* Custom development services for robotic arms and related solutions;
* Joint R&D and co-development opportunities.

If you are interested in commercial collaboration or have related needs, please feel free to contact us. Let’s work together to advance the adoption and industrialization of robotics technology.


## ☎ Contact Us
- **Open‑Source Progress & Technical Support**-Yaohui: yaohui.zhu@seeed.cc
- **Future Collaboration & Customization**-Elaine: elaine.wu@seeed.cc
