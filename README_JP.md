# 🦾 reBot-DevArm：すべての開発者のためのオープンソースロボットアーム

<p align="center">
  <img src="./media/RS5_56.png" alt="reBot-DevArm バナー">
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
    <img src="https://img.shields.io/badge/Framework-Isaac%20Sim-yellow.svg" alt="LeRobot">
</p>

<p align="center">
  <strong>🚀 100% オープンソース · Embodied AI · ハードウェア + ソフトウェアのフルスタック</strong>
</p>

<p align="center">
  <strong>📦 自分だけのロボットアームを構築 · 🧠 ロボティクスを学ぶ · 🏭 実アプリケーションへ展開</strong>
</p>

<table align="center">
  <tr>
    <td>
      <a href="https://www.youtube.com/watch?v=ONbpv3seiG8">
        <img src="https://img.icons8.com/ios-filled/100/ff0000/youtube-play.png" width="40">
      </a>
    </td>
    <td>
      <a href="https://www.youtube.com/watch?v=ONbpv3seiG8">
        About The reBot Arm
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
    <img src="https://img.shields.io/badge/Documentation-%F0%9F%93%95-blue" alt="ロボティクス wiki"></a>
</p>

<p align="center">
  <strong>🛒 公式ストアで購入</strong>
</p>


<table align="center" border="1" cellpadding="12" cellspacing="12">
  <tr>
    <td align="center" width="260" bgcolor="#FFF8F0">
      <b>&#x1F9FE; reBot Arm B601-DM</b><br><br>
      <a href="https://www.seeedstudio.com/reBot-Arm-B601-DM-Assembled-Kit-with-Power-Supply-Bundle.html" target="_blank">
        <big><b>&#x1F6D2; SeeedStudio Bazaar</b></big>
      </a>
        <a href="https://www.amazon.com/dp/B0H2TWVFSW" target="_blank">
        <big><b>&#x1F6D2; Amazon</b></big>
      </a>
      </a>
        <a href="https://de.aliexpress.com/item/1005012108314029.html" target="_blank">
        <big><b>&#x1F6D2; Aliexpress</b></big>
      </a>
    </td>
    <td align="center" width="260" bgcolor="#F0F4FF">
      <b>&#x1F9FE; reBot Arm B601-RS</b><br><br>
      <a href="https://www.seeedstudio.com/reBot-Arm-B601-RS-Bundle-p-6898.html" target="_blank">
        <big><b>&#x1F6D2;  SeeedStudio Bazaar</b></big>
      </a>
      <a href="https://www.aliexpress.us/item/3256812343811970.html?gatewayAdapt=deu2usa4itemAdapt" target="_blank">
        <big><b>&#x1F6D2; Aliexpress</b></big>
      </a>
    </td>
  </tr>
</table>



## 📖 はじめに

**reBot-DevArm（reBot Arm B601 DM および reBot Arm B601 RS）** は、Embodied AI の学習ハードルを下げることに取り組むロボットアームプロジェクトです。私たちは **「真のオープンソース」** に重点を置いています。コードだけでなく、あらゆるものを惜しみなくオープンソース化します：
- 🦾 **2つのロボットアームバージョン**：同一の外観を持つ2種類のロボットアーム、**Robostride** と **Damiao** の両バージョンについて、すべてのオープンソースファイルを提供します。
- 🛠️ **ハードウェア設計図**：板金部品および3Dプリント部品のソースファイル。
- 🔩 **BOM リスト**：すべてのネジの仕様や購入リンクに至るまで詳細に記載。
- 💻 **ソフトウェア & アルゴリズム**：Python SDK、ROS1/2、Isaac Sim、LeRobot など。

## ご自身のreBot Armを入手するには

- [Seeedstudio.com](https://www.seeedstudio.com/reBot-Arm-B601-DM-Bundle.html) で5種類のキットをご用意しています：
  - **アーム本体モーターキット**：ロボットアーム用のモーターとワイヤーハーネスのみを含みます。
  - **アーム本体構造キット**：機械構造部品のみを含みます。
  - **グリッパー完全キット**：グリッパー用のモーター、ワイヤーハーネス、構造部品を含みます。
  - **フルキット**：ロボットアーム本体とグリッパーの完全なセットを含みます。
  - **組立済みロボットアーム**：完全に組み立てられた完成品のロボットアームです。

- Seeedstudioキットには、標準付属品として電源アダプターおよびC型クランプは含まれていません。これは、ユーザーがバッテリーで給電したり、カスタムDIYベースに取り付けたりする可能性を考慮したものです。別途 [電源](https://www.seeedstudio.com/AC-DC-Power-Adapter-IEC-60320-C14-XT30-Female-24V-4-5A-1200mm-L190-W92-5-H36mm-p-6764.html) と [電源コード](https://www.seeedstudio.com/reServer-AC-US-p-5052.html) を購入するか、[BOM](./hardware/reBot_B601_DM/readme.md#about-power-supply) の末尾に記載されている Mean Well 電源ソリューションを参照してください。

- [Leader Arm](https://www.seeedstudio.com/Star-Arm-102-p-6765.html?qid=P2U7IG_yskyak5m_1776415593315) と [12V 10A 電源](https://www.seeedstudio.com/FY1209900-12V-10A-Power-Adapter-12V-10A-p-6496.html) も購入できます。SO-ARM101 の12VDC電源アダプターを使用して Leader に給電することもできます。

-------------------
- reBot Arm RS バージョンについては、[Seeedstudio.com](https://www.seeedstudio.com/reBot-Arm-B601-RS-Assembled-Kit-with-Gripper-p-6865.html) で2種類のキットをご用意しています：
  - **フルキット**：ロボットアーム本体とグリッパーの未組立完全セットを含みます。
  - **組立済みロボットアーム**：完全に組み立てられた完成品のロボットアームです。

- RSモデルには [Meanwell 48V 12.5A](https://www.amazon.com/sspa/click?ie=UTF8&spc=MTo0NzgzODk2NzUxNTQ0NzEyOjE3ODE2MTA2NTU6c3BfYXRmOjIwMDExNjA5NjQwMTc5ODo6MDo6&url=%2FLRS-350-48-Price-Switching-Supply-MeanWell%2Fdp%2FB0BP6S5DYR%2Fref%3Dsr_1_1_sspa%3Fcrid%3D27VPQOWNPN9UG%26dib%3DeyJ2IjoiMSJ9.qK84sGJa4-74kbCEX11MOFBju8sSQUdFsbHw6PNvmaEHnhzjX2T7dyhRNJY01mXxpWk8lccGOwnezxmqLKUjqglX_FI26mrxlvZf0KNiLdJ8QnhKsber4KDoyyLHNxWGV451uHCzZbCDXxM0iYXVnubuVourRaRURlyMorRavuLd2a32kABx-BKqyF5Dfr7dV453ecE6QULFqG-UVLBaBRijbxQGTJ2YiNyXAqn3bkM.Bt5mAPOJNAWGnXCC2mwvjdDdccZd1_0-WRXZpP4mR4M%26dib_tag%3Dse%26keywords%3DLRS-350-48%26qid%3D1781610655%26sprefix%3Dlrs-350-%252Caps%252C331%26sr%3D8-1-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9hdGY%26psc%3D1) 電源の使用を強く推奨します。より強力な出力で性能を最大限に引き出したい場合は、48V 25A 電源アダプターを選択できます。
------------------


## 🗺️ ロードマップ & ステータス

私たちは、主流のロボット開発エコシステムへの継続的なメンテナンスと適応に取り組んでいます。以下は、現在の対応状況と予定リリーススケジュールです。

### reBot Arm B601 DM
| 対応エコシステム | 状態 | 説明 / 予定公開日 | 関連ドキュメント |
| :--- | :---: | :--- | :--- |
| **モーター基本使用** | ✅ 完了 | 基本的なモーション制御と API ラッパー化 | [Damiao Technology](https://wiki.seeedstudio.com/cn/damiao_series/) |
| **新バージョン STEP 3D 構造部品および BOM のオープンソース化** | ✅ 完了 | 新バージョンの全パーツの STEP ファイル、部品 BOM、およびすべての加工部品の参考価格 | [reBot Arm B601-DM BOM](./hardware/reBot_B601_DM/readme.md) |
| **実機性能テスト参考** | ✅ 完了 | 通常動作および限界動作におけるロボットアームの性能参考 | [Performance Testing](./hardware/reBot_B601_DM/performance_testing/Performance_Testing.md) |
| **組み立て動画** | ✅ 完了 | 超詳細な組み立て手順と動画 | [Getting Started with reBot Arm B601-DM](https://wiki.seeedstudio.com/rebot_b601_dm_getting_started/) |
| **Python SDK** | ✅ 継続的に最適化中、PR歓迎 | Robstride、Damiao、Mota、Gaoqing、Hexfellow など各種モーターの読み書きと制御をワンストップで統合します。 | [Getting Started with Motorbridge](https://motorbridge.seeedstudio.com) and [Web UI](https://rebot-devarm.w0x7ce.eu/) |
| **ROS2 統合** | ✅ 完了 | 運動学、軌道計画、重力補償に対応した ROS2 統合 reBot Arm コントローラー | [reBot Arm B601-DM ROS2 Integration Guide](https://wiki.seeedstudio.com/rebot_arm_b601_dm_ros2_integration/) |
| **Pinocchio 統合** | ✅ 完了 | Pinocchio フレームワークへの対応により、ロボットアームの順運動学/逆運動学および重力補償を実現 | [Getting Started with Pinocchio for reBot Arm B601-DM](https://wiki.seeedstudio.com/rebot_arm_b601_dm_pinocchio_meshcat/) and [Github repo](https://github.com/Seeed-Projects/reBotArm_control_py) |
| **Isaac Sim シミュレーション** | 🚧 進行中 | USD モデルをインポートし、シミュレーションによる遠隔操作を実現 |[Wiki](https://wiki.seeedstudio.com/rebot_arm_b601_dm_isaacsim/)|
| **LeRobot 統合** | ✅ 完了 | Hugging Face LeRobot トレーニングフレームワークへの対応 | [Getting Started with LeRobot-based reBot Arm](https://wiki.seeedstudio.com/rebot_arm_b601_dm_lerobot/) |
| **深度カメラ統合** | ✅ 完了 | YOLO と深度カメラに基づくビジュアル把持デモ | [Getting Started with Visual Grasping Demo](https://wiki.seeedstudio.com/rebot_arm_b601_dm_grasping_demo/) |
| **reSpeaker 音声統合** | ✅ 完了 | reSpeaker Flex 4マイクアレイを追加し、空間認識を備えた音声駆動のインテリジェントロボットアーム制御システムを構築 | [reBot Arm B601-DM Voice Control](https://wiki.seeedstudio.com/control_rebot_arm_using_voice_with_respeaker_flex/) |
| **最新アルゴリズムの段階的更新** | ⏳ 計画中 | 主流アルゴリズムを段階的に更新予定 | Ongoing |
| **完全無料コースシリーズの提供** | ⏳ 計画中 | 主流アルゴリズムを段階的に更新予定 | Ongoing |

#### 開発者からの貢献
| 対応エコシステム | 作者 | 説明 / 予定公開日 | 関連ドキュメントまたはリポジトリ |
| :--- | :---: | :--- | :--- |
| **ROS2 (Humble), third_party 統合, URDF / rebotarm_bringup** | [@danieldoradotalaveron-rb](https://github.com/danieldoradotalaveron-rb) | 1. **パッシブ診断モニター** (`rebotarm_monitor_ros2`): `rqt_robot_monitor` 向け `/diagnostics` オーバーレイ、serial/CAN 対応アグリゲーター;<br>2. **安全な退避とシャットダウン**: 接続時に休止姿勢を取得し、シャットダウンまたは `/rebotarm/park` 時にゆっくり戻して急落を防止;<br>3. **重力補償 (スムーズ停止)**: 重力補償終了時に MIT ランプアウトを行い、pos/vel 引き継ぎ時の衝撃、急動作、不安定性を低減;<br>4. **IK/FK と安全対策を備えたゲームパッドテレオペ**: IK によるエンドエフェクタ制御、RViz でのロボット状態のライブ可視化 (シミュレーションのみでテスト);<br>5. **D405 eye-in-hand TF**: `rebotarm_bringup` の `end_link` 下に Xacro 設定を追加し、RViz 可視化と TF のみに使用 (driver/depth/intrinsics なし)。取付姿勢は launch ファイルで調整可能、ブラケットキャリブレーションは未完了。Teleop FK/IK はアームのみの `fixend_core` URDF を使用し、RSP/RViz には完全な xacro を使用。 | [rebotarm_monitor_ros2](https://github.com/danieldoradotalaveron-rb/rebotarm_monitor_ros2)、[reBotArmController_ROS2](https://github.com/danieldoradotalaveron-rb/reBotArmController_ROS2) |

### reBot Arm B601 RS

| 対応エコシステム | 状態 | 説明 / 予定公開日 | 関連ドキュメント |
| :--- | :---: | :--- | :--- |
| **モーター基本使用** | ✅ 完了 | 基本的なモーション制御と API ラッパー化 | [Robstride](https://wiki.seeedstudio.com/cn/robstride_control/) |
| **新バージョン STEP 3D 構造部品および BOM のオープンソース化** | ✅ 完了 | 新バージョンの全パーツの STEP ファイル、部品 BOM、およびすべての機械加工部品の参考価格 | [reBot Arm B601-RS BOM](./hardware/reBot_B601_RS/README.md) |
| **クイックスタート** | ✅ 完了 | B601-RS のクイックスタート | [Getting Started with reBot Arm B601-RS](https://wiki.seeedstudio.com/rebot_b601_rs_getting_started/) |
| **組み立て動画** | ✅ 完了 | 超詳細な組み立て手順と動画 | [reBot Arm B601-RS Assembly Video](https://wiki.seeedstudio.com/rebot_b601_rs_getting_started/) |
| **ROS2 (Humble)** | ✅ 完了 | 運動学、軌道計画、重力補償および MoveIt2 に対応した ROS2 統合 reBot Arm コントローラー | [reBot Arm B601-RS ROS2 Integration Guide](https://wiki.seeedstudio.com/rebot_arm_b601_rs_ros2_integration/) |
| **LeRobot 統合** | ✅ 完了 | Hugging Face LeRobot トレーニングフレームワークへの対応 | [Getting Started with LeRobot-based reBot Arm](https://wiki.seeedstudio.com/rebot_arm_b601_rs_lerobot/) |
| **Pinocchio 統合** | ✅ 完了 | Pinocchio フレームワークへの対応により、ロボットアームの順運動学/逆運動学および重力補償を実現 | [Getting Started with Pinocchio for reBot Arm B601-RS](https://wiki.seeedstudio.com/rebot_arm_b601_rs_pinocchio_meshcat/) と [Github repo](https://github.com/vectorBH6/reBotArm_control_py) |
| **深度カメラ統合** | ✅ 完了 | YOLO と深度カメラに基づくビジュアル把持デモ | [Getting Started with Visual Grasping Demo](https://wiki.seeedstudio.com/rebot_arm_b601_dm_grasping_demo/) |
| **Isaac Sim シミュレーション** | ✅ 完了 | USD モデルをインポートし、シミュレーションによる遠隔操作を実現 | [Github Repo](https://github.com/Seeed-Projects/reBot-Isaacsim) |
| **最新アルゴリズムの段階的更新** | ⏳ 計画中 | 主流アルゴリズムを段階的に更新予定 | Ongoing |
| **完全無料コースシリーズの提供** | ⏳ 計画中 | 主流アルゴリズムを段階的に更新予定 | Ongoing |


---

## ⚙️ ハードウェア仕様

reBot-DevArm は、デスクトップ向け Embodied AI アプリケーションのために設計されており、可搬重量と柔軟性のバランスを取っています。

| パラメータ | reBot Arm B601-DM | reBot Arm B601-RS |
| :--- | :--- | :--- |
| **作業負荷 (Payload)** | 1.5 kg | **2.5 kg** |
| **推奨作業空間** | アーム到達範囲ワークスペースの 70% | アーム到達範囲ワークスペースの 70% |
| **最大リーチ (Reach)** | 767 mm | **754 mm** |
| **自重 (Weight)** | **約 4.5 kg** | 約 6.7 kg |
| **繰り返し精度** | < 0.2 mm | < 0.2 mm |
| **自由度 (DOF)** | 6 DOF + 1 グリッパー | 6 DOF + 1 グリッパー |
| **対応プラットフォーム/エコシステム** | ROS1、ROS2、LeRobot、Pinocchio、Isaac Sim、Python SDK | ROS1、ROS2、LeRobot、Pinocchio、Isaac Sim、Python SDK |
| **供給電圧** | DC 24V | DC 48V |

## コミュニティからのフィードバック
| <img src="/community/GEM-4.png" height="100"> | <img src="/community/from_Linyan.png" height="100">   |<img src="/community/from_Diddi.png" height="100">  |<img src="/community/from_Henderson.jpg" height="100">  | <img src="/community/from_Sameer.png" height="100">|
| --- | --- | --- | --- |  --- | 
| [From GEM-4: Gemma Embodied 4 Physical Assistance](https://www.kaggle.com/competitions/gemma-4-good-hackathon/writeups/new-writeup-1778618527713) | [From Linyan Fu](https://x.com/Linyan_Fu/status/2056383947341525180)  and [Apheth D Almeida](https://x.com/Apheth_DAlmeida/status/2053503164507476096)| [From Dhruv Diddi](https://x.com/DhruvDiddi/status/2046605015008383284)  | [From Ed Henderson](https://x.com/ed0henderson/status/2055076839002095743)  | From Sameer | 
| <img src="/community/from_Binh_Pham.png" height="100"> | <img src="/community/from_fangtianchonghui.png" height="100">   |<img src="/community/from_xensedyl.png" height="100">  |<img src="/community/from_Henderson_2.png" height="100">  | <img src="/community/YOR_Car.png" height="100"> |
| [From Binh_Pham](https://x.com/pham_blnh/status/2061994096374505710) | [From FangTianChongHui](https://www.instagram.com/reel/DY7Ny8OPjVu/?utm_source=ig_web_copy_link&igsh=NTc4MTIwNjQ2YQ==)| [Xense YaoLin Dong](https://x.com/dong1505lin)  | [From Ed Henderson](https://x.com/ed0henderson/status/2055076839002095743)  |  [From yoshikai_man](https://x.com/yoshikai_man/status/2079938975398244705)  | 

| <img src="/community/hei-robot-lift-play.gif" height="100"> | <img src="/community/VR_with_reBot.png" height="100">   |<img src="/community/reBot_grasp_fruit.png" height="100">  |<img src="/community/Daniel_Dorado.jpg" height="100">  | <img src="/community/Groot_N1.7.png" height="100"> |
| --- | --- | --- | --- |  --- | 
| [From hei-rebot-lift](https://github.com/lipengdong/hei-rebot-lift) | [From Martin Kemka](https://www.linkedin.com/posts/activity-7484390995862781952-TX4m?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE6WUL4BWkFeyUj0TJ5JlGf6IG4iRHAicUo)| [From Kamil Buczyński](https://www.linkedin.com/posts/kamil-buczy%C5%84ski-102843301_seeedstudio-rebotarm-seeedprojectofthemonth-ugcPost-7485297094715461633-RV_6/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE6WUL4BWkFeyUj0TJ5JlGf6IG4iRHAicUo)  | [From Daniel Dorado](https://www.linkedin.com/posts/doradodaniel_computervision-spatialai-sim2real-share-7474727487374184448-NhwX/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE6WUL4BWkFeyUj0TJ5JlGf6IG4iRHAicUo)  |  [From Asier](https://www.linkedin.com/posts/asierarranz_nvidia-physicalai-isaaclab-ugcPost-7480271721942417408-YNwu/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE6WUL4BWkFeyUj0TJ5JlGf6IG4iRHAicUo)  | 

| <img src="/community/sim-to-real-vla.gif" height="100"> |
| --- |
| [Seeed reBot Arm と NVIDIA Isaac の Sim-to-Real VLA コース](https://www.seeedstudio.com/sim-to-real-with-seeed-rebot-and-nvidia-isaac) |

## 🧹オプションパーツ
### 手首カメラマウント
| 32×32 UVCカメラ | Intel D435i | Intel D405 & Gemini 305 | Gemini 2 |
| --- | --- | --- | --- |
| <img src="/hardware/reBot_B601_DM/3D_Printed_Parts/images/UVC_camera_mount.png" height="100"> | <img src="/hardware/reBot_B601_DM/3D_Printed_Parts/images/D435i.jpg" height="100"> |  <img src="/hardware/reBot_B601_DM/3D_Printed_Parts/images/D405.jpg" height="100"> | <img src="/hardware/reBot_B601_DM/3D_Printed_Parts/images/Gemini2.jpg" height="100"> |
| [STEP](/hardware/reBot_B601_DM/3D_Printed_Parts/UVC32_mount.step) | [STEP](/hardware/reBot_B601_DM/3D_Printed_Parts/D435_Gemini2_Mount.step) | [STEP](/hardware/reBot_B601_DM/3D_Printed_Parts/D405_305_Mount.step) |[STEP](/hardware/reBot_B601_DM/3D_Printed_Parts/D435_Gemini2_Mount.step) |

### マスターアーム（Leader Arm）対応
| Star Arm 102-LD | 各種アームの接続・互換に対応予定 |
| --- | --- |
|  <img src="./hardware/reBot_B601_DM/3D_Printed_Parts/images/star_arm_102.jpg" height="100">  | [View Series Hub](https://fashionstar.com.hk/robot-arm/star-arm-102/) &[Github repo](https://github.com/servodevelop/Star-Arm-102) |

### DIY ソフトフィンガー
| ソフトフィンガー | 互換性統合に対応可能 |
| --- | --- |
|  <img src="/hardware/reBot_B601_DM/3D_Printed_Parts/images/Soft_Finger.png" height="100">  |近日公開|
| [フィンガー取付台(ABS/PLA)](/hardware/reBot_B601_DM/3D_Printed_Parts/Soft_Gripper_Mount.step) 及び [フィンガー本体(TPU 95+)](/hardware/reBot_B601_DM/3D_Printed_Parts/Soft_Gripper_Finger.step)  |近日公開 |

### おすすめオプションパーツ
<table>
  <thead>
    <tr>
      <th>カテゴリ</th>
      <th>種類</th>
      <th>画像</th>
      <th>製品</th>
      <th>リンク</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="8" align="center"><strong>カメラ</strong></td>
      <td rowspan="6" align="center">デプスカメラ</td>
      <td align="center"><img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/0/-/0-101090144--orbbec-gemini-2-3d-camera.jpg" alt="Orbbec Gemini 2 3D Camera" width="120"></td>
      <td><strong>Orbbec Gemini 2 3D Camera</strong></td>
      <td><a href="https://www.seeedstudio.com/Orbbec-Gemini-2-3D-Camera-p-6464.html">Seeed Studio</a></td>
    </tr>
    <tr>
      <td align="center"><img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/1/0/1000000774.png" alt="Orbbec Gemini 336 Depth Camera" width="120"></td>
      <td><strong>Orbbec Gemini 336 Depth Camera</strong></td>
      <td><a href="https://www.seeedstudio.com/Orbbec-Gemini-336-3D-Camera-3D-p-6662.html">Seeed Studio</a></td>
    </tr>
    <tr>
      <td align="center"><img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/1/-/1-100010971-orbbec-gemini-335-lg.jpg" alt="Orbbec Gemini 335LG 3D Camera" width="120"></td>
      <td><strong>Orbbec Gemini 335LG 3D Camera</strong></td>
      <td><a href="https://www.seeedstudio.com/Orbbec-Gemini-335LG-3D-Camera-p-6541.html">Seeed Studio</a></td>
    </tr>
    <tr>
      <td align="center"><img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/0/0/0035718.png" alt="SLAMTEC Aurora S, Integrated Spatial Perception Module" width="120"></td>
      <td><strong>SLAMTEC Aurora S</strong><br><sub>Integrated Spatial Perception Module</sub></td>
      <td><a href="https://www.seeedstudio.com/SLAMTEC-Aurora-S-AI-Integrated-Spatial-Perception-System-p-6669.html">Seeed Studio</a></td>
    </tr>
    <tr>
      <td align="center"><img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/i/n/intel_realsense_d435i_34_1_1.jpg" alt="Intel RealSense Depth Camera D435i" width="120"></td>
      <td><strong>Intel RealSense Depth Camera D435i</strong></td>
      <td><a href="https://www.seeedstudio.com/Intel-RealSense-Depth-Camera-D435i-p-4423.html">Seeed Studio</a></td>
    </tr>
    <tr>
      <td align="center"><img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/1/-/1-100000540-realsense-d405-3d-camera.jpg" alt="RealSense Depth Camera D405" width="120"></td>
      <td><strong>RealSense Depth Camera D405</strong></td>
      <td><a href="https://www.seeedstudio.com/RealSense-D405-3D-Camera-p-6758.html">Seeed Studio</a></td>
    </tr>
    <tr>
      <td rowspan="2" align="center">単眼カメラ</td>
      <td align="center"><img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/0/-/0-101090101-3mp-gmsl2-camera-module-190-degree.jpg" alt="Sensing SG3S-ISX031C-GMSL2F 3MP GMSL2 Camera" width="120"></td>
      <td><strong>Sensing SG3S-ISX031C-GMSL2F 3MP GMSL2 Camera</strong></td>
      <td><a href="https://www.seeedstudio.com/SG3S-ISX031C-GMSL2F-p-6245.html">Seeed Studio</a></td>
    </tr>
    <tr>
      <td align="center"><img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/s/2/s231.1.jpg" alt="ET-S231 Megapixel 120 Degree Wide-Angle 1080P USB Camera Module" width="120"></td>
      <td><strong>ET-S231 Megapixel 120 Degree Wide-Angle 1080P USB Camera Module</strong></td>
      <td><a href="https://www.seeedstudio.com/ET-S231-120-USB-Camera-p-6683.html">Seeed Studio</a></td>
    </tr>
    <tr>
      <td rowspan="2" align="center"><strong>マイク</strong></td>
      <td rowspan="2" align="center">マイクアレイ</td>
      <td align="center"><img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/1/-/1-100070894-respeaker-flex-xvf3800-circular-4-with-xiao-esp32s3_1_.jpg" alt="reSpeaker Flex XVF3800 Circular-4 with XIAO ESP32S3" width="120"></td>
      <td><strong>reSpeaker Flex XVF3800 Circular-4 with XIAO ESP32S3</strong><br><sub>AI Mic Array for Robotics and Embodied AI</sub></td>
      <td><a href="https://www.seeedstudio.com/reSpeaker-Flex-XVF3800-Circular-4-with-XIAO-ESP32S3-p-6739.html">Seeed Studio</a></td>
    </tr>
    <tr>
      <td align="center"><img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/1/-/1-respeaker-xvf3800-4-mic-array.jpg" alt="reSpeaker XMOS XVF3800" width="120"></td>
      <td><strong>reSpeaker XMOS XVF3800</strong><br><sub>AI-powered 4-Mic Array for Clear Voice Even in Noise</sub></td>
      <td><a href="https://www.seeedstudio.com/ReSpeaker-XVF3800-USB-Mic-Array-p-6488.html">Seeed Studio</a></td>
    </tr>
    <tr>
      <td rowspan="2" align="center"><strong>コントローラー</strong></td>
      <td rowspan="2" align="center">エッジコントローラー</td>
      <td align="center"><img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/1/1/110110147.jpg" alt="reComputer J3011-Orin Nano 8GB" width="120"></td>
      <td><strong>reComputer J3011-Orin Nano 8GB</strong></td>
      <td><a href="https://www.seeedstudio.com/reComputer-J3011-p-5590.html">Seeed Studio</a></td>
    </tr>
    <tr>
      <td align="center"><img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/i/m/image-kit-3.png" alt="NVIDIA Jetson AGX Thor Developer Kit" width="120"></td>
      <td><strong>NVIDIA Jetson AGX Thor Developer Kit</strong></td>
      <td><a href="https://www.seeedstudio.com/NVIDIA-Jetson-AGX-Thor-Developer-Kit-p-9965.html">Seeed Studio</a></td>
    </tr>
  </tbody>
</table>

---


### 🎓 フルスタック・ロボティクスエコシステム
reBot-DevArm は単なるロボットアームではなく、ロボティクス学習コミュニティでもあります。以下の一般向けチュートリアルを無料で共有しています：

#### 🖥️ エッジコンピューティング & メインコントロール
*   [![Jetson](https://img.shields.io/badge/NVIDIA-reComputer%20Jetson-76B900?style=for-the-badge&logo=nvidia&logoColor=white)](https://wiki.seeedstudio.com/NVIDIA_Jetson/) —— **AI 推論 & 計算コア**
*   [![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-4B%20%2F%205-C51A4A?style=for-the-badge&logo=Raspberry%20Pi&logoColor=white)](https://wiki.seeedstudio.com/raspberry-pi-devices/) —— **汎用 Linux 開発環境**
*   [![ESP32](https://img.shields.io/badge/MCU-Seeed%20XIAO%20(ESP32)-0091BD?style=for-the-badge&logo=espressif&logoColor=white)](https://wiki.seeedstudio.com/SeeedStudio_XIAO_Series_Introduction/) —— **低消費電力ワイヤレス制御ノード**

#### 📡 センサー & 周辺機器
*   **🚗 モーター & サーボ**: [Damiao / Gogo / Robstride / Mita / Feite / Fashion Star](https://wiki.seeedstudio.com/robotics_page/)
*   **👁️ ビジュアル知覚**: [深度カメラ / LiDAR / ビジョンアルゴリズム](https://wiki.seeedstudio.com/robotics_page/)
*   **👂 音声インタラクション**: [reSpeaker Mic Arrays/Voice Control/Spatial Awareness(DoA)](https://wiki.seeedstudio.com/control_rebot_arm_using_voice_with_respeaker_flex/)
*   **🧭 動作 & 姿勢**: [IMU（6軸/9軸） / ジャイロスコープ / 磁力計](https://wiki.seeedstudio.com/Sensor_accelerometer/)
*   **🤖 総合キット**: [その他のロボティクスセンサー & ドライバ例](https://wiki.seeedstudio.com/robotics_page/)


> 👉 **[クリックして Wiki ナレッジベースへ移動](https://wiki.seeedstudio.com/)** （すべてのチュートリアルは無料で閲覧できます）

---

## 🙌 参考資料 & 謝辞
オープンソースの道は決して孤独ではありません。reBot-DevArm プロジェクトの誕生は、Seeed Studio、世界中のオープンソースコミュニティ、そして優れたハードウェアパートナーの全面的な支援なしには実現できませんでした。以下のプロジェクトとチームに最大限の敬意を表します：

### 🌍 エコシステム & ソフトウェアサポート
*   **[Seeed Studio](https://www.seeedstudio.com/)** - 包括的なハードウェアサプライチェーンと技術サポートを提供。
*   **[Hugging Face LeRobot](https://github.com/huggingface/lerobot)** - 優れたエンドツーエンドのロボット学習フレームワーク。
*   **[NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim)** - 強力なロボットシミュレーションおよび合成データプラットフォーム。

### ⚙️ コアハードウェアパートナー
高性能なモーターおよびアクチュエータソリューションを提供してくださった以下のメーカーに感謝します：
*   **[Damiao Technology](https://www.damiaokeji.com/)**
*   **[Robstride](https://robstride.com/)**
*   **[Fashion Star](https://fashionstar.com.hk/wiki/)**

### 💡 インスピレーション
本プロジェクトは、以下の優れたオープンソースプロジェクトから大きなインスピレーションを受けています：
*   **[SO-ARM100](https://github.com/TheRobotStudio/SO-ARM100/tree/main)**
*   **[Mobile ALOHA](https://github.com/tonyzhaozh/aloha)**
*   **[Dummy-Robot (Zhihui Jun)](https://github.com/peng-zhihui/Dummy-Robot)**
*   **[OpenArm](https://openarm.dev/)**
*   **[I2RT](https://i2rt.com/)**
*   **[TRLC-DK1](https://github.com/robot-learning-co/trlc-dk1)**

### 🎃 プロトタイプ貢献者
- **SeeedStudio AI Robotics Team's**: Yaohui Zhu (yaohui.zhu@seeed.cc)
- **SeeedStudio STU**: Wentao Dong
- **SeeedStudio STU**: Weiwei Xu
- **SeeedStudio Purchasing Department**: Fengqun Peng


### 👥 貢献者

## 私たちのトップ貢献者 
<p align="center"><a href="https://github.com/Seeed-Projects/reBot-DevArm/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=Seeed-Projects/reBot-DevArm" />
</a></p>



*近日公開予定... ぜひ PR を送ってコントリビューターになってください！*

## Star 履歴

## Star History

<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" 
          srcset="assets/star-history/star-history-dark.svg">

  <source media="(prefers-color-scheme: light)" 
          srcset="assets/star-history/star-history-light.svg">

  <img src="assets/star-history/star-history-light.svg">
</picture>
</p>

# reBot-DevArm プロジェクトライセンス

- **ハードウェア設計** © 2026 深圳矽递科技股份有限公司(SeeedStudio)、 [CERN-OHL-W-2.0](https://ohwr.org/cern_ohl_w_v2.txt) に基づきオープンソース化
- **ファームウェアコード** © 2026 深圳矽递科技股份有限公司(SeeedStudio)、 [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) に基づきオープンソース化

## 権利と制限事項の説明

尊敬する開発者ならびに業界の専門家の皆様、reBot Armロボットアームプロジェクトは、常に**機敏性、開放性、責任感、共創**という中核的理念を掲げ、開発者の皆様にサービスを提供してまいりました。私たちのビジョンは、reBotプロジェクトを通じて、すべての愛好家の皆様がロボットアームのハードウェアアーキテクチャやソフトウェアの基本原理を体系的に習得し、先端の身体性人工知能アルゴリズムを体験できるようにすることです。

プロジェクト開始から5か月間は、**CC BY-SA NC（非営利）オープンソースライセンス**を採用してきました。これは、プロジェクトが未だ完全に成熟していない段階において、すべての開発者と貢献者が商業的な要求に煩わされることなく、製品の反復改善に集中し、プロジェクトの共同構築と最適化に全力を注げるようにするためです。

SeeedStudioによる数ヶ月にわたる徹底的な製品磨きと技術的蓄積を経て、**2026年5月11日より**、reBot ArmプロジェクトはCC BY-SA NCライセンスから **CERN-OHL-W 2.0 オープンソースライセンス**へ正式に移行します。

これにより、プロジェクトは**ハードウェアとソフトウェアの全チェーンで100%オープンソース化**を実現し、**全シナリオにおける商業的な遵守使用**を許可します。

引き続き、包摂と協働の初心を持って、reBot Armオープンソースコミュニティの維持、発展、深耕にご参加いただき、オープンソースの成果を共有し、身体性人工知能のエコシステムを共に築いていけることを期待しております。

本プロジェクトでは、ハードウェアとソフトウェアで異なるオープンソースライセンスを適用します。ご使用前に該当する部分のライセンス条項をご確認ください。

| 項目 / ライセンス                       | reBotプロジェクト ハードウェア (CERN-OHL-W-2.0)                              | reBotプロジェクト ソフトウェアSDK (Apache-2.0)                              |
| --------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **✅ 商用利用**                  | ✅ 許可                                               | ✅ 許可                                                 |
| **✅ 改変**                  | ✅ 許可                                               | ✅ 許可                                                 |
| **✅ 再配布**                  | ✅ 許可                                               | ✅ 許可                                                 |
| **✅ クローズドソースでの統合/再公開**       | ❌ 条件付きで許可（詳細は [CERN-OHL-W-2.0](https://ohwr.org/cern_ohl_w_v2.txt) を参照）                             | ✅ 許可（修正コードの公開は不要）                             |
| **⚠️ 著作権表示の保持**           | ✅ 必須                                           | ✅ 必須                                             |
| **⚠️ ライセンス原文の保持**         | ✅ 必須                                           | ✅ 必須                                             |
| **⚠️ 変更箇所の明示**                 | ✅ 必須（変更内容と日付を明記）                                 | ✅ 必須（変更内容を明記）                               |
| **⚠️ 特許許諾**                   | ✅ 明確な特許許諾（詳細は [CERN-OHL-W-2.0](https://ohwr.org/cern_ohl_w_v2.txt) を参照）                           | ✅ 明確な特許許諾                                         |
| **⚠️ 配布時のソース提供要件**     | ✅ **必須**（ハードウェアの「完全なソース」を提供）        | ❌ ソース提供の義務はなし                                   |
| **⚠️ 外部/クローズドモジュールとの互換性**      | ✅ 許可（Weakly Reciprocal 特性）                     | ✅ 完全に許可                                             |
| **🔗 他のコンポーネント/モジュールとの関係**        | 独立したインターフェースモジュール（External Material）は元のライセンス（クローズドも可）を維持可能     | 無制限。あらゆるライセンスのコードライブラリとリンク可能                        |
| **📄 公式ライセンス全文**              | [CERN-OHL-W-2.0](https://ohwr.org/cern_ohl_w_v2.txt)  | [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) |

## ☎ お問い合わせ
- **オープンソース進捗 & 技術サポート**-Yaohui: yaohui.zhu@seeed.cc
- **今後の協業 & カスタマイズ**-Elaine: elaine.wu@seeed.cc
