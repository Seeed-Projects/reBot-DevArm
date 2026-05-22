# 🦾 reBot-DevArm: 为每个开发者开源的机械臂

<p align="center">
  <img src="./media/v1.0.png" alt="reBot-DevArm Banner">
</p>

<p align="center">
    <a href="https://certification.oshwa.org/cn000024.html">
  <img src="./media/certification-mark-CN000024-wide.png" width="180">
</a>
</p>

<p align="center">
    <a href="./LICENSE">
    <img src="https://img.shields.io/badge/License-CERN--OHL--W--2.0--for--hardware-green.svg" alt="License: CERN-OHL-W-2.0">
    </a>
    <img src="https://img.shields.io/badge/License-Apache--2.0--for--software-pink.svg" alt="License: Apache-2.0">
    </a>
    <img src="https://img.shields.io/badge/Commercial-Contact%20Us-red.svg" alt="yaohui.zhu@seeed.cc">
    <img src="https://img.shields.io/badge/ROS-Noetic%20%7C%20Humble-orange.svg" alt="ROS Support">
    <img src="https://img.shields.io/badge/Framework-LeRobot-yellow.svg" alt="LeRobot">
    <img src="https://img.shields.io/badge/Framework-Isaac Sim-yellow.svg" alt="LeRobot">
</p>

<p align="center">
  <strong>100% 全开源 · 具身智能 · 软硬一体 · 个人学习科研免费 · [商用宽松条件请看这里](#权利与限制说明)</strong>
</p>


<table align="center">
  <tr>
    <td>
      <a href="https://www.bilibili.com/video/BV1K9dbBNEdC/?spm_id_from=333.337.search-card.all.click">
        <img src="https://img.icons8.com/ios-filled/100/ff0000/youtube-play.png" width="40">
      </a>
    </td>
    <td>
      <a href="https://www.bilibili.com/video/BV1K9dbBNEdC/?spm_id_from=333.337.search-card.all.click">
        关于reBot Arm
      </a>
    </td>
  </tr>
</table>

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


## 📖 项目简介 (Introduction)

**reBot-DevArm (reBot Arm B601 DM 和reBot Arm B601 RS)** 是一个致力于降低自身智能学习门槛的机械臂项目。我们主打 **"真·开源"** —— 不仅仅是代码，我们无保留地开源了所有的：
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

  你可以在如下地方购买到完整零件：

  中国：[淘宝矽递科技旗舰店](https://detail.tmall.com/item.htm?app=chrome&bxsign=scdlw5VjXYQhfgOyva6IEit8asOyaYSFE5I3VXYy3VPlmlREIPF350GWGqrQeFq6zMR0LYTFVDN1CYDrBsUaYz-4JxcTqiZF-HQ6NUldhIWqF4BZVDgneY0XNmbgokb1mXQ&cpp=1&id=1042412233386&price=8295&shareUniqueId=35714007536&share_crt_v=1&shareurl=true&short_name=h.iLxfDpYMNSysFIa&sourceType=item%2Citem&sp_tk=UGU1SzU2ZmJVdE8%3D&spm=a2159r.13376460.0.0&suid=f2c61ac8-e0ca-45d0-b100-75210b69b5b9&tbSocialPopKey=shareItem&tk=Pe5K56fbUtO&un=1a387738ed21d73a0f8768acc41474bb&un_site=0&ut_sk=1.aduVZSGbgvEDAPW0%2BMUyPBgR_21646297_1776313782940.Copy.1&wxsign=tbwGGBQEcYglkjQ8Bb9ce0nY3n0Lt2A0LqWv5fIH-2gpBWlQr1YAclOKyIimOONlUMdMNexbYhHL1BfCn7tnsbQlmgAwPGYNzFYFGNmitXbVMMtxoW1WB68Oux3DSBGem9OWTXZB4ARF_FuruhSrejI1g)
  

## 🗺️ 开源路线图 (Roadmap & Status)

我们承诺持续维护并适配主流的机器人开发生态。以下是我们目前的适配进度与计划发布时间：

### reBot Arm B601 DM

| 适配生态 | 状态 | 说明 / 预计发布时间 | 相关文档 |
| :--- | :---: | :--- | :--- |
| **电机基本使用** | ✅ 完成 | 基础运动控制与API封装 |[达妙科技](https://wiki.seeedstudio.com/cn/damiao_series/)|
| **新版本STEP 3D结构件及BOM开源** | ✅ 完成 | 新版本所有零件的STEP格式、零部件BOM、及所有加工件参考价格 | [BOM](./hardware/reBot_B601_DM/readme_zh.md) |
| **真机性能测试参考** |  ✅ 完成 | 常规工作以及极限工作下的机械臂性能参考 |  [Performance Testing](./hardware/reBot_B601_DM/performance_testing/Performance_Testing_zh.md) |
| **组装视频** | ✅ 完成 | 超详细的组装步骤及视频 |  [reBot Arm B601-DM 快速入门](https://wiki.seeedstudio.com/cn/rebot_b601_dm_getting_started/) |
| **Python SDK** | ✅ 完成  |一站式集成 Robstride、Damiao、脉塔、高擎、Hexfellow 等电机读写及控制。 | [上手使用 Motorbridge教程](https://motorbridge.seeedstudio.com) 以及  [Web UI](https://rebot-devarm.w0x7ce.eu/) |
| **ROS2 集成** | ✅ 完成 | ROS2集成机械臂控制器、支持机械臂运动学、轨迹规划及重力补偿功能 |[reBot Arm B601-DM ROS2使用教程](https://wiki.seeedstudio.com/cn/rebot_arm_b601_dm_ros2_integration/)|
| **Pinocchio 适配** | ✅ 完成 | 适配 Pinocchio框架、实现机械臂正逆运动学及动力学重力补偿功能 |[reBot Arm B601-DM 的 Pinocchio 与 MeshCat 入门指南](https://wiki.seeedstudio.com/cn/rebot_arm_b601_dm_pinocchio_meshcat/) 以及 [Github 控制代码](https://github.com/vectorBH6/reBotArm_control_py)|
| **Isaac Sim 仿真** | 🚧 进行中 | 导入USD模型并实现仿真遥操作 | [由于添加额外课程延迟： 2026.06.20]|
| **LeRobot 适配** | 🚧 进行中 | 适配 Hugging Face LeRobot 训练框架 | [reBot Arm B601-DM Lerobot使用教程](https://wiki.seeedstudio.com/cn/rebot_arm_b601_dm_lerobot/)|
| **深度相机集成** | ✅ 完成 | 基于 YOLO 与深度相机的视觉夹取演示 | [reBot Arm B601-DM 视觉夹取 Demo](https://wiki.seeedstudio.com/cn/rebot_arm_b601_dm_grasping_demo/) |
| **逐步更新最新算法** | ⏳ 计划中 | 逐步更新主流算法 | 持续进行 |
| **推出系列完全免费课程** | ⏳ 计划中 | 逐步更新主流算法 | 持续进行 |


### reBot Arm B601 RS

| 适配生态 | 状态 | 说明 / 预计发布时间 | 相关文档 |
| :--- | :---: | :--- | :--- |
| **电机基本使用** | ✅ 完成 | 基础运动控制与API封装 | [灵足时代](https://wiki.seeedstudio.com/cn/robstride_control/)|
| **新版本STEP 3D结构件及BOM开源** | 🚧 进行中 | 新版本所有零件的STEP格式、零部件BOM、及所有加工件参考价格 | 预计[2026.05] |
| **组装视频** | 🚧 进行中 | 超详细的组装步骤及视频 |  [预计 2026.05.20] |
| **ROS2 (Humble)** |⏳ 计划中 | 核心驱动已完成，正在优化MoveIt2 |[预计 2026.05]|
| **LeRobot 适配** | ⏳ 计划中 | 适配 Hugging Face LeRobot 训练框架 | [预计 2026.05]|
| **Pinocchio 适配** | ⏳ 计划中 | 适配 Pinocchio框架、实现机械臂正逆运动学及动力学重力补偿功能 | [预计 2026.05]|
| **Isaac Sim 仿真** | ⏳ 计划中 | 导入USD模型并实现仿真遥操作 | [预计 2026.05]|
| **逐步更新最新算法** | ⏳ 计划中 | 逐步更新主流算法 | 持续进行 |
| **推出系列完全免费课程** | ⏳ 计划中 | 逐步更新主流算法 | 持续进行 |


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

## 有意思的社区项目
| <img src="/community/from_Linyan.png" height="100">   |<img src="/community/from_Diddi.png" height="100">  |<img src="/community/from_Henderson.jpg" height="100">  | <img src="/community/from_Sameer.png" height="100">|
| --- | --- | --- | --- | 
| [From Linyan Fu](https://x.com/Linyan_Fu/status/2056383947341525180)  and [Apheth D Almeida](https://x.com/Apheth_DAlmeida/status/2053503164507476096)| [From Dhruv Diddi](https://x.com/DhruvDiddi/status/2046605015008383284)  | [From Ed Henderson](https://x.com/ed0henderson/status/2055076839002095743)  | [From Sameer Shah Teams](https://www.youtube.com/watch?v=fM01HolVl1U&t=15s) | 

## 🧹可选硬件
### 腕部相机支架
| 32×32 UVC 相机 | Intel D435i | Intel D405 & Gemini 305 | Gemini 2 |
| --- | --- | --- | --- |
| 即将上线 | <img src="/hardware/reBot_B601_DM/3D_Printed_Parts/images/D435i.jpg" height="100"> |  <img src="/hardware/reBot_B601_DM/3D_Printed_Parts/images/D405.jpg" height="100"> | <img src="/hardware/reBot_B601_DM/3D_Printed_Parts/images/Gemini2.jpg" height="100"> |
| 即将上线 | [STEP模型文件](/hardware/reBot_B601_DM/3D_Printed_Parts/D435_Gemini2_Mount.step) | [STEP模型文件](/hardware/reBot_B601_DM/3D_Printed_Parts/D405_305_Mount.step) |[STEP模型文件](/hardware/reBot_B601_DM/3D_Printed_Parts/D435_Gemini2_Mount.step) |

### 兼容主臂（Leader Arm）
| Star Arm 102-LD | 欢迎各类机械臂兼容接入 |
| --- | --- |
|  <img src="/hardware/reBot_B601_DM/3D_Printed_Parts/images/star_arm_102.jpg" height="100">  | 即将上线 |
|  [Github 仓库](https://github.com/servodevelop/Star-Arm-102) | 即将上线 |

### 爪子DIY
| 柔性手指 | 开放兼容集成拓展 |
| --- | --- |
|  <img src="/hardware/reBot_B601_DM/3D_Printed_Parts/images/Soft_Finger.png" height="100">  |敬请期待|
| [手指安装座(ABS/PLA)](/hardware/reBot_B601_DM/3D_Printed_Parts/Soft_Gripper_Mount.step) 与 [柔性手指本体(TPU 95+)](/hardware/reBot_B601_DM/3D_Printed_Parts/Soft_Gripper_Finger.step)  |敬请期待 |




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

- **硬件设计** © 2026 深圳矽递科技股份有限公司(SeeedStudio)，基于 [CERN-OHL-W-2.0](https://ohwr.org/cern_ohl_w_v2.txt) 开源
- **固件代码** © 2026 深圳矽递科技股份有限公司(SeeedStudio)，基于 [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) 开源

## 权利与限制说明
尊敬的各位开发者及行业前辈，reBot Arm机械臂项目，始终秉持**敏捷、开放、担当、共生**的核心理念服务广大开发者，我们的愿景是让每一位爱好者都能借助reBot项目，系统掌握机械臂硬件架构、软件底层原理，沉浸式体验具身智能前沿算法。

项目上线至今五个月，一直采用 **CC BY-SA NC 非商用开源协议**。初衷是在项目尚未完全成熟的阶段，让所有开发者与贡献者能够专注于迭代完善产品，不受商业诉求干扰，全身心投入项目共建优化。

历经Seeedstudio数月深度产品打磨与技术沉淀，**自2026年5月11日起**，reBot Arm项目正式由 CC BY-SA NC 协议，升级切换为 **CERN-OHL-W 2.0 开源协议**。
自此项目实现**软硬件全链路100%开源，开放全场景商业合规使用权限**。

也期待各位继续以包容共建的初心，持续参与、维护、深耕reBot Arm开源社区，一同共享开源成果、共筑具身智能生态。

本项目硬件 (Hardware) 与软件 (Software) 使用不同开源许可协议，使用前请确认您所使用的部分对应的许可条款。

| 项目 / 许可                       | reBot项目硬件部分遵循 CERN-OHL-W-2.0                              | reBot项目软件SDK部分遵循 Apache-2.0                              |
| --------------------------------- | ------------------------------------------------------ | -------------------------------------------------------- |
| **✅ 允许 商用**                  | ✅ 允许                                               | ✅ 允许                                                 |
| **✅ 允许 修改**                  | ✅ 允许                                               | ✅ 允许                                                 |
| **✅ 允许 分发**                  | ✅ 允许                                               | ✅ 允许                                                 |
| **✅ 允许 闭源集成/再发布**       | ❌ 有条件闭源（详见说明 [CERN-OHL-W-2.0](https://ohwr.org/cern_ohl_w_v2.txt) ）                             | ✅ 允许（无需公开修改代码）                             |
| **⚠️ 必须保留版权声明**           | ✅ 必须保留                                           | ✅ 必须保留                                             |
| **⚠️ 必须保留许可证原文**         | ✅ 必须保留                                           | ✅ 必须保留                                             |
| **⚠️ 修改需注明**                 | ✅ 必须注明修改及日期                                 | ✅ 修改文件需注明修改内容                               |
| **⚠️ 专利授权**                   | ✅ 明确专利授权（详见说明 [CERN-OHL-W-2.0](https://ohwr.org/cern_ohl_w_v2.txt) ）                           | ✅ 明确专利授权                                         |
| **⚠️ 分发产品时提供源码要求**     | ✅ **必须**提供硬件“完整源”（Complete Source）        | ❌ 无强制提供源码要求                                   |
| **⚠️ 对外部/闭源模块兼容性**      | ✅ 允许（Weakly Reciprocal 特性）                     | ✅ 完全允许                                             |
| **🔗 与其他组件/模块关系**        | 独立接口模块（External Material）可保持原许可闭源     | 无限制，可链接任意许可证的代码库                        |
| **📄 官方许可证全文**              | [CERN-OHL-W-2.0](https://ohwr.org/cern_ohl_w_v2.txt)  | [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) |

## ☎ 联系我们
- **开源进度 & 技术支持**-耀晖: yaohui.zhu@seeed.cc
- **未来合作 & 轻量化定制**-Elaine: elaine.wu@seeed.cc
