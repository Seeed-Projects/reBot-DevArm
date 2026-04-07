# 🦾 reBot-DevArm: 为每个开发者开源的机械臂

<p align="center">
  <img src="./media/v1.0.png" alt="reBot-DevArm Banner">
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
  <strong>100% 全开源 · 具身智能 · 软硬一体 · 个人学习科研免费 · [商用宽松条件请看这里](#权利与限制说明)</strong>
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
</p
  
## 📖 项目简介 (Introduction)

**reBot-DevArm (reBot Arm B601 DM 和reBot Arm B601 RS)** 是一个致力于降低具身智能学习门槛的机械臂项目。我们主打 **"真·开源"** —— 不仅仅是代码，我们无保留地开源了所有的：
- 🦾 **两个版本电机的开源机械臂**：我们会提供Robostride和Damiao两个版本的同样外观的机械臂所有开源文件。
- 🛠️ **硬件图纸**：钣金件、3D打印件源文件。
- 🔩 **BOM 清单**：详细到每一个螺丝的规格和购买链接。
- 💻 **软件及算法**：Python SDK、ROS1/2、Isaac Sim、Lerobot等

## 搭建属于你的 reBot 机械臂

- 我们提供五种套件方案：
  - **机械臂本体电机套件**：仅包含机械臂所需的电机与线束。
  - **机械臂本体结构件套件**：仅包含机械结构零部件。
  - **夹持器完整套件**：包含夹持器的电机、线束及结构件。
  - **整机完整套件**：包含机械臂本体与夹持器全套组件。
  - **成品组装机械臂**：已完成组装的成品机械臂。

你可根据手头已有的配件，在 SeeedStudio 商城选购剩余部分（预计上架时间：2026年4月15日）。

[你可以在此留下你的信息，我们将提前为你发送限量预售链接](https://jsj.top/f/PQ42WF)。

## 🗺️ 开源路线图 (Roadmap & Status)

我们承诺持续维护并适配主流的机器人开发生态。以下是我们目前的适配进度与计划发布时间：

### reBot Arm B601 DM

| 适配生态 | 状态 | 说明 / 预计发布时间 | 相关文档 |
| :--- | :---: | :--- | :--- |
| **电机基本使用** | ✅ 完成 | 基础运动控制与API封装 |[达妙科技](https://wiki.seeedstudio.com/cn/damiao_series/)|
| **新版本STEP 3D结构件及BOM开源** | ✅ 完成 | 新版本所有零件的STEP格式、零部件BOM、及所有加工件参考价格 | [BOM](./hardware/reBot_B601_DM/readme_zh.md) |
| **真机性能测试参考** |  ✅ 完成 | 常规工作以及极限工作下的机械臂性能参考 |  [Performance Testing](./hardware/reBot_B601_DM/performance_testing/Performance_Testing_zh.md) |
| **组装视频** | 🚧 进行中 | 超详细的组装步骤及视频 |  [预计 2026.04.10] |
| **Python SDK** | 🚧 进行中  |  | [预计: 2026.04.10] |
| **ROS2 (Humble)** |🚧 进行中 | 核心驱动已完成，正在优化MoveIt2 |[预计 2026.04.10]|
| **Pinocchio 适配** | 🚧 进行中 | 适配 Pinocchio框架、实现机械臂正逆运动学及动力学重力补偿功能 | [GitHub 仓库](https://github.com/vectorBH6/reBotArm_control_py/tree/main) 持续更新中 |
| **Isaac Sim 仿真** | 🚧 进行中 | 导入USD模型并实现仿真遥操作 | [预计 2026.04.20]|
| **LeRobot 适配** | 🚧 进行中 | 适配 Hugging Face LeRobot 训练框架 | [预计 2026.04.30]|
| **逐步更新最新算法** | ⏳ 计划中 | 逐步更新主流算法 | 持续进行 |
| **推出系列完全免费课程** | ⏳ 计划中 | 逐步更新主流算法 | 持续进行 |


### reBot Arm B601 RS

| 适配生态 | 状态 | 说明 / 预计发布时间 | 相关文档 |
| :--- | :---: | :--- | :--- |
| **电机基本使用** | ✅ 完成 | 基础运动控制与API封装 | [灵足时代](https://wiki.seeedstudio.com/cn/robstride_control/)|
| **新版本STEP 3D结构件及BOM开源** | 🚧 进行中 | 新版本所有零件的STEP格式、零部件BOM、及所有加工件参考价格 | 预计[2026.04.31] |
| **组装视频** | 🚧 进行中 | 超详细的组装步骤及视频 |  [预计 2026.05.10] |
| **ROS2 (Humble)** |⏳ 计划中 | 核心驱动已完成，正在优化MoveIt2 |[预计 2026.05]|
| **LeRobot 适配** | ⏳ 计划中 | 适配 Hugging Face LeRobot 训练框架 | [预计 2026.05]|
| **Pinocchio 适配** | ⏳ 计划中 | 适配 Pinocchio框架、实现机械臂正逆运动学及动力学重力补偿功能 | [预计 2026.05]|
| **Isaac Sim 仿真** | ⏳ 计划中 | 导入USD模型并实现仿真遥操作 | [预计 2026.05]|
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

| 参数项 | reBot Arm B601-DM |
| :--- | :--- |
| **推荐长期工作负载 (Payload)** | **小于1.5 kg 及 70%臂展工作空间** |
| **最大臂展 (Reach)** | **650 mm** |
| **自重 (Weight)** | 约 4.5 kg |
| **重复定位精度** | < 0.2 mm |
| **自由度 (DOF)** | 6 DOF + 1 夹爪|
| **支持平台/生态** | ROS1, ROS2, LeRobot, Pinocchio, Isaac Sim, Python SDK |
| **供电电压** | DC 24V |

---

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
版权所有 (c) [2025] [深圳矽递科技股份有限公司(SeeedStudio)]

本作品采用**知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议**进行许可。
欲查看该许可协议副本，请访问链接：http://creativecommons.org/licenses/by-nc-sa/4.0/

--------------------------------------------------------------------------------

## 权利与限制说明
本项目开源的核心宗旨是促进知识共享，以最低成本让所有开发者、爱好者接触并学习前沿机械臂技术。我们将提供完全免费、公开的文档及视频教程，助力大家快速上手、深入研究，共同推动机器人技术的普及与落地。

一、非商用使用规范

本项目所有开源内容，面向个人学习、研究及非直接商业用途完全开放，允许个人用户进行以下操作，无需额外申请授权：

- 查看、学习本项目的开源文档、代码及教程内容；
- 对开源内容进行修改、调试，用于个人学习和研究；
- 组装机械臂用于个人自用，或基于开源内容进行非商用性质的二次开发。

二、商用使用规范

我们积极鼓励并支持开发者、机器人爱好者及第三方平台，基于reBot机械臂进行二次开发，推动技术向实际应用场景落地，同时明确以下商用放宽条件及禁止行为：

（一）允许的商用行为
我们充分尊重每一位开发者的劳动成果与合理收益，若您从Seeed采购reBot B601系列机械臂，在付出自主劳动后，可对自身劳动成果部分开展商业行为，包括但不限于：

- 开发可落地的应用场景软件系统，并进行商业推广与销售；
- 制作体系化的教学课程（线上/线下），开展知识付费或培训服务；
- 在全球范围内开展线下教育培训、技术普及等活动；
- 其他有助于开源社区进步、知识传播及机器人技术落地的商业行为。
针对上述合规商用行为，欢迎您积极与我们联系，我们将提供商业授权、落地协助及推广支持，并可公开发布对您的商业授权，助力您的项目顺利落地。

（二）禁止的商用行为

禁止对本项目产品进行局部简单修改后，替换IP、logo及相关标识，生成自有品牌并进行销售。此类行为未产生实质性技术创新，对开发者成长、开源社区发展及项目本身无任何积极意义，均视为违规商用行为，我们将保留相关权利。

三、合作支持与联系方式

我们希望与所有开发者、合作伙伴在合规框架下协同发展，共同推动reBot机械臂项目成熟落地。对于学习本项目后，有意向推进机械臂真实应用场景落地的个人开发者及各机器人领域用户，我们可提供以下合作支持：
- 商业授权与知识产权合规支持；
- 项目方案的协助推广；
- 机械臂整机及相关方案的定制开发服务；
- 联合研发与项目共建。
若您有意开展商用合作或有相关合作需求，欢迎直接与我们联系，携手推动机器人技术的普及与产业落地。

## ☎ 联系我们
- **开源进度 & 技术支持**-耀晖: yaohui.zhu@seeed.cc
- **未来合作 & 轻量化定制**-Elaine: elaine.wu@seeed.cc
