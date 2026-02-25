# 🦾 reBot-DevArm: 为每个开发者开源的机械臂

<p align="center">
  <img src="./media/v2.0.png" alt="reBot-DevArm Banner">
</p>

<p align="center">
    <!-- 替换为 CC BY-NC-SA 4.0 徽章，明确标示非商用 -->
    <a href="./LICENSE">
        <img src="https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg" alt="License: CC BY-NC-SA 4.0">
    </a>
    <img src="https://img.shields.io/badge/Commercial-Contact%20Us-red.svg" alt="yaohui.zhu@seeed.cc">
    <img src="https://img.shields.io/badge/ROS-Noetic%20%7C%20Humble-orange.svg" alt="ROS Support">
    <img src="https://img.shields.io/badge/Framework-LeRobot-yellow.svg" alt="LeRobot">
    <img src="https://img.shields.io/badge/Framework-Isaac Sim-yellow.svg" alt="LeRobot">
</p>

<p align="center">
  <strong>100% 全开源 · 具身智能 · 软硬一体 · 个人/教育免费 · 商用需授权</strong>
</p>

<p align="center">
  <strong>
    <a href="./README_zh.md">简体中文</a> &nbsp;|&nbsp;
    <a href="./README.md">English</a> &nbsp;|&nbsp;
    <a href="./README_JP.md">日本語</a>&nbsp;|&nbsp;
    <a href="./README_Fr.md">français</a>
    <a href="./README_es.md">Español</a>
  </strong>
</p>

<p align="center">
<a href="https://discord.gg/AbGuqJhDpQ">
    <img src="https://img.shields.io/discord/1409155673572249672?color=7289DA&label=Discord&logo=discord&logoColor=white"></a>
<a href="https://wiki.seeedstudio.com/robotics_page/">  
    <img src="https://img.shields.io/badge/Documentation-📕-blue" alt="robotics wiki"></a>
</p
  
## 📖 项目简介 (Introduction)

**reBot-DevArm (Total Open Source Arm)** 是一个致力于降低具身智能学习门槛的机械臂项目。我们主打 **"真·开源"** —— 不仅仅是代码，我们无保留地开源了所有的：
- 🦾 **两个版本电机的开源机械臂**：我们会提供Robostride和Damiao两个版本的同样外观的机械臂所有开源文件。
- 🛠️ **硬件图纸**：钣金件、3D打印件源文件。
- 🔩 **BOM 清单**：详细到每一个螺丝的规格和购买链接。
- 💻 **软件及算法**：Python SDK、ROS1/2、Isaac Sim、Lerobot等

**⚠️ 注意：本项目旨在促进教育与个人学习。所有资源对个人开发者、学生和教育机构完全免费开放，但在未经授权的情况下，严禁用于任何商业用途（包括但不限于直接售卖套件、作为商业产品的一部分等）。**

**等我们测试完所有硬件性能、精度以及安全性评估后，将会放宽免费商用的协议。**

## ☎ 联系我们
- **开源进度 & 技术支持**-耀晖: yaohui.zhu@seeed.cc
- **未来合作 & 轻量化定制**-Elaine: elaine.wu@seeed.cc

## 🗺️ 开源路线图 (Roadmap & Status)

> [!WARNING]
>由于春节假期的原因，很多公司都放假了，影响了我们的样品测试进度，我们在做完所有性能和精度验证后才会开源，所以开源节奏会往后延迟1个月左右。

我们承诺持续维护并适配主流的机器人开发生态。以下是我们目前的适配进度与计划发布时间：

| 适配生态 | 状态 | 说明 / 预计发布时间 | 相关文档 |
| :--- | :---: | :--- | :--- |
| **电机基本使用** | ✅ 完成 | 基础运动控制与API封装 | [灵足时代](https://wiki.seeedstudio.com/cn/robstride_control/)  [达妙科技](https://wiki.seeedstudio.com/cn/damiao_series/)|
| **新版本STEP 3D结构件及BOM开源** | 🚧 进行中 | 新版本所有零件的STEP格式、零部件BOM、及所有加工件参考价格 |  [延期到 2026.03] |
| **组装视频** | 🚧 进行中 | 超详细的组装步骤及视频 |  [延期到 2026.03] |
| **ROS2 (Humble)** |⏳ 计划中 | 核心驱动已完成，正在优化MoveIt2 |[预计 2026.04]|
| **LeRobot 适配** | ⏳ 计划中 | 适配 Hugging Face LeRobot 训练框架 | [预计 2026.04]|
| **Pinocchio 适配** | ⏳ 计划中 | 适配 Pinocchio框架、实现机械臂正逆运动学及动力学重力补偿功能 | [预计 2026.04]|
| **Isaac Sim 仿真** | ⏳ 计划中 | 导入USD模型并实现仿真遥操作 | [预计 2026.04]|
| **逐步更新最新算法** | ⏳ 计划中 | 逐步更新主流算法 | 持续进行 |
| **推出系列完全免费课程** | ⏳ 计划中 | 逐步更新主流算法 | 持续进行 |

---


### 🎓 机器人全栈生态 (Full-Stack Ecosystem)
reBot-DevArm 不仅仅是一个机械臂，更是一个机器人学习社区。我们免费共享以下通用教程：

#### 🖥️ 边缘计算与主控
*   [![Jetson](https://img.shields.io/badge/NVIDIA-reComputer%20Jetson-76B900?style=for-the-badge&logo=nvidia&logoColor=white)](https://wiki.seeedstudio.com/NVIDIA_Jetson/) —— **AI 推理与算力核心**
*   [![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-4B%20%2F%205-C51A4A?style=for-the-badge&logo=Raspberry%20Pi&logoColor=white)](https://wiki.seeedstudio.com/raspberry-pi-devices/) —— **通用 Linux 开发环境**
*   [![ESP32](https://img.shields.io/badge/MCU-Seeed%20XIAO%20(ESP32)-0091BD?style=for-the-badge&logo=espressif&logoColor=white)](https://wiki.seeedstudio.com/SeeedStudio_XIAO_Series_Introduction/) —— **低功耗无线控制节点**

#### 📡 传感器与外设
*   **🚗 电机舵机**：[达妙 / 高擎 / 灵足 / 脉塔 / 飞特 / 华馨京](https://wiki.seeedstudio.com/robotics_page/)
*   **👁️ 视觉感知**：[深度相机 / 激光雷达 / 视觉算法](https://wiki.seeedstudio.com/robotics_page/)
*   **👂  听觉交互**：[ReSpeaker 麦克风阵列 / 语音识别](https://wiki.seeedstudio.com/ReSpeaker_Mic_Array_v2.0/)
*   **🧭 运动姿态**：[IMU (6轴/9轴) / 陀螺仪 / 磁力计](https://wiki.seeedstudio.com/Sensor/IMU/)
*   **🤖 综合套件**：[更多机器人传感器与驱动案例](https://wiki.seeedstudio.com/robotics_page/)


> 👉 **[点击进入 Wiki 知识库](https://wiki.seeedstudio.com/)** (所有教程免费查阅)

---

## ⚙️ 硬件参数 (Specifications)

reBot-DevArm 专为桌面级具身智能应用设计，兼顾了负载能力与灵活性。

| 参数项 | 数值 / 说明 |
| :--- | :--- |
| **有效负载 (Payload)** | **1.5+ kg** |
| **最大臂展 (Reach)** | **650 mm** |
| **自重 (Weight)** | 约 4.0 kg |
| **重复定位精度** | < 0.2 mm |
| **自由度 (DOF)** | 6 DOF + 1 夹爪 (CAN舵机夹爪及关节电机夹爪开源正在路上) |
| **支持平台/生态** | ROS1, ROS2, LeRobot, Pinocchio, Isaac Sim, Python SDK |
| **供电电压** | DC 24V |

---

## 📂 开源 (Hardware Source)

我们相信硬件开源才能促进创新。你可以在以下目录找到制造这台机械臂所需的一切：

*   [`/hardware/STEP`](./hardware/cad): 所有机械结构的 STEP/STL 文件，包含打印件、金属件、采购物品。
*   [`/hardware/bom`](./hardware/bom): **BOM 表** (包含外购件型号、电机参数、推荐商家)。
*   [`/tutorial/ROS`](./tutorial/ROS/): 在**ROS1/2 Noetic/Humble**使用源码及教程。
*   [`/tutorial/Lerobot`](./tutorial/lerobot/): **Lerobot**使用源码及教程。
*   [`/tutorial/Isaac`](./tutorial/Isaac/):**Isaac Sim**使用源码及教程。
---

## 🚀 快速上手 (Getting Started)

我们为您规划了从开箱到 AI 仿真的完整学习路径：

### 🛠️ 阶段一：硬件搭建与基础
| 步骤 | 说明 | 链接 |
| :---: | :--- | :--- |
| **01** | **电机基本使用**  |  [灵足时代](https://wiki.seeedstudio.com/cn/robstride_control/)  [达妙科技](https://wiki.seeedstudio.com/cn/damiao_series/) |
| **02** | **开箱检查**  | 即将推出 |
| **03** | **组装指南**  |即将推出 |
| **04** | **零点校准** |  即将推出|
| **05** | **运动学**  | 即将推出|

### 💻 阶段二：算法与仿真进阶
| 步骤 | 说明 | 链接 |
| :---: | :--- | :--- |
| **06** | **ROS 生态** (ROS2) | 🐢 即将推出|
| **07** | **AI 训练** (Hugging Face) | 🤗即将推出|
| **08** | **仿真模拟** (NVIDIA) | 🌌即将推出|



## 🙌 参考与致谢 (References & Acknowledgments)
开源之路从不孤单。reBot-DevArm 项目的诞生离不开 Seeed Studio 的全力支持，更离不开全球开源社区和优秀的硬件合作伙伴。我们向以下项目和团队致以最诚挚的敬意：

### 🌍 生态与软件支持
*   **[Seeed Studio](https://www.seeedstudio.com/)** - 提供全方位的硬件供应链与技术支持。
*   **[Hugging Face LeRobot](https://github.com/huggingface/lerobot)** - 优秀的端到端机器人学习框架。
*   **[NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim)** - 强大的机器人仿真与合成数据平台。

### ⚙️ 核心硬件伙伴
感谢以下厂商提供的高性能电机与执行器方案：
*   **[Damiao Technology (达妙科技)](https://www.damiaokeji.com/)**
*   **[Robstride (灵足时代)](https://robstride.com/)**
*   **[Fashion Star (华馨京科技)](https://fashionrobo.com/)**

### 💡 致敬先驱项目 (Inspiration)
本项目深受以下优秀开源项目的启发：
*   **[SO-ARM100](https://github.com/TheRobotStudio/SO-ARM100/tree/main)**
*   **[Mobile ALOHA](https://github.com/tonyzhaozh/aloha)**
*   **[Dummy-Robot (稚晖君)](https://github.com/peng-zhihui/Dummy-Robot)**
*   **[OpenArm](https://openarm.dev/)**
*   **[I2RT](https://i2rt.com/)**
*   **[TRLC-DK1](https://github.com/robot-learning-co/trlc-dk1)**

### 🎃 原型机贡献者
- **SeeedStudio AI Rotoics Team's**: Yaohui Zhu (yaohui.zhu@seeed.cc)

- **SeeedStudio STU**: Wentao Dong

- **SeeedStudio STU**: Weiwei Xu

- **SeeedStudio Purchasing Department**: Fengqun Peng


### 👥 其他贡献者 (Contributors)

## Our Top Contributors 
<p align="center"><a href="https://github.com/Seeed-Projects/reBot-DevArm/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=Seeed-Projects/reBot-DevArm" />
</a></p>



*Coming soon... 欢迎提交 PR 成为贡献者！*

## Star 趋势

[![Star History Chart](https://api.star-history.com/svg?repos=Seeed-Projects/reBot-DevArm&type=date&legend=top-left)](https://www.star-history.com/#Seeed-Projects/reBot-DevArm&type=date&legend=top-left)


# reBot-DevArm 项目许可证
版权所有 (c) [2025] [矽递科技人工智能机器人团队]

本作品采用**知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议**进行许可。
欲查看该许可协议副本，请访问链接：http://creativecommons.org/licenses/by-nc-sa/4.0/

--------------------------------------------------------------------------------

## 权利与限制说明
1. 你可自由进行以下操作：
   - 共享：以任意媒介或格式复制、再分发本作品的内容。
   - 改编：对本作品进行再混合、转换及二次创作。

2. 上述操作需遵循以下条款：
   - 署名：你必须注明适当的出处、提供许可协议链接，并标注是否对原作品进行了修改。
   - 非商业性使用：**不得将本作品用于商业用途**。
     （包括但不限于销售相关套件、售卖打印零部件，或未经明确许可将本软件集成至付费产品中）
   - 相同方式共享：若你对本作品进行了再混合、转换或二次创作，需采用与原许可协议相同的条款分发你的衍生成果。

3. 商业授权：
   若你希望将本项目用于商业用途，请联系作者获取商业授权。
   联系方式：yaohui.zhu@seeed.cc

-----------------------------------------
