<div align="center">

# 🦾 reBot-DevArm

**すべての開発者のためのオープンソースロボットアーム**

<img src="./media/RS5_56.png" alt="reBot-DevArm Banner" width="1000">

<a href="https://certification.oshwa.org/cn000024.html"><img src="./media/certification-mark-CN000024-wide.png" alt="OSHWA 認証" width="180"></a>

[![ハードウェアライセンス: CERN-OHL-W-2.0](https://img.shields.io/badge/License-CERN--OHL--W--2.0--Hardware-green.svg)](./LICENSE)
[![ソフトウェアライセンス: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0--Software-pink.svg)](./LICENSE)
[![ROS](https://img.shields.io/badge/ROS-Noetic%20%7C%20Humble-orange.svg)](#ロードマップ)
[![LeRobot](https://img.shields.io/badge/Framework-LeRobot-yellow.svg)](#ロードマップ)
[![Isaac Sim](https://img.shields.io/badge/Framework-Isaac%20Sim-yellow.svg)](#ロードマップ)
[![商用](https://img.shields.io/badge/Commercial-Contact%20Us-red.svg)](mailto:yaohui.zhu@seeed.cc)

**100% オープンソース · Embodied AI · ハードウェア + ソフトウェアのフルスタック**

🌐 [ランディングページ](https://279070161-sketch.github.io/reBot/) · 📚 [チュートリアルセンター](https://wiki.seeedstudio.com/robotics_page/) · ▶ [オンラインデモ](https://yang-ci.github.io/Rebot_Arm_AGV/)

[![Discord](https://img.shields.io/discord/1409155673572249672?color=7289DA&label=Discord&logo=discord&logoColor=white)](https://discord.gg/AbGuqJhDpQ)
[![ドキュメント](https://img.shields.io/badge/Documentation-%F0%9F%93%95-blue)](https://wiki.seeedstudio.com/robotics_page/)

[简体中文](README_zh.md) · [English](README.md) · [日本語](README_JP.md) · [français](README_Fr.md) · [Español](README_es.md)

</div>

---

## 📑 目次

- [📖 はじめに](#はじめに)
- [🛒 入手方法](#入手方法)
- [🚀 オンライン体験](#オンライン体験)
- [🗺️ ロードマップ](#ロードマップ)
- [⚙️ ハードウェア仕様](#ハードウェア仕様)
- [🌟 コミュニティ作品](#コミュニティ作品)
- [🧹 オプションパーツ](#オプションパーツ)
- [🎓 フルスタックエコシステム](#フルスタックエコシステム)
- [🙌 謝辞と貢献者](#謝辞と貢献者)
- [📄 ライセンス](#ライセンス)
- [☎ お問い合わせ](#お問い合わせ)

---

## 📖 はじめに

**reBot-DevArm** —— **reBot Arm B601-DM** および **reBot Arm B601-RS** —— は、Embodied AI の学習ハードルを下げることに取り組むロボットアームプロジェクトです。私たちは「真のオープンソース」を重視し、コードだけでなく、あらゆるものを惜しみなく公開しています。

- 🦾 **2つのロボットアームモデル** —— 同一外観の **B601-DM（Damiao）** と **B601-RS（Robstride）** の全オープンソースファイルを提供
- 🛠️ **ハードウェア設計図** —— 板金部品および 3D プリント部品のソースファイル
- 🔩 **BOM リスト** —— すべてのネジの仕様や購入リンクに至るまで詳細に記載
- 💻 **ソフトウェア & アルゴリズム** —— Python SDK、ROS1/2、Isaac Sim、LeRobot など

## 🛒 入手方法

| モデル | 公式ストア | その他のチャネル |
| :--- | :--- | :--- |
| **reBot Arm B601-DM** | [SeeedStudio Bazaar](https://www.seeedstudio.com/reBot-Arm-B601-DM-Assembled-Kit-with-Power-Supply-Bundle.html) | [Amazon](https://www.amazon.com/dp/B0H2TWVFSW) · [AliExpress](https://de.aliexpress.com/item/1005012108314029.html) |
| **reBot Arm B601-RS** | [SeeedStudio Bazaar](https://www.seeedstudio.com/reBot-Arm-B601-RS-Bundle-p-6898.html) | [AliExpress](https://www.aliexpress.us/item/3256812343811970.html?gatewayAdapt=deu2usa4itemAdapt) |

### B601-DM キットオプション

[Seeedstudio.com](https://www.seeedstudio.com/reBot-Arm-B601-DM-Bundle.html) にて 5 種類のキットをご用意しています：

- **アーム本体モーターキット** —— ロボットアーム用のモーターとワイヤーハーネスのみ
- **アーム本体構造キット** —— 機械構造部品のみ
- **グリッパー完全キット** —— グリッパー用のモーター、ワイヤーハーネス、構造部品
- **フルキット** —— ロボットアーム本体とグリッパーの完全セット
- **組立済みロボットアーム** —— 完全に組み立てられた完成品

> 💡 SeeedStudio キットには標準付属品として電源アダプターと C 型クランプは含まれません（バッテリー給電や DIY ベースへの取り付けを考慮）。別途 [電源](https://www.seeedstudio.com/AC-DC-Power-Adapter-IEC-60320-C14-XT30-Female-24V-4-5A-1200mm-L190-W92-5-H36mm-p-6764.html) と [電源コード](https://www.seeedstudio.com/reServer-AC-US-p-5052.html) を購入するか、[BOM](./hardware/reBot_B601_DM/readme.md#about-power-supply) 末尾の Mean Well 電源ソリューションをご参照ください。

### B601-RS キットオプション

[Seeedstudio.com](https://www.seeedstudio.com/reBot-Arm-B601-RS-Assembled-Kit-with-Gripper-p-6865.html) にて 2 種類のキットをご用意しています：

- **フルキット** —— ロボットアーム本体とグリッパーの未組立完全セット
- **組立済みロボットアーム** —— 完全に組み立てられた完成品

> 💡 RS モデルには [Mean Well 48V 12.5A](https://www.amazon.com/sspa/click?ie=UTF8&spc=MTo0NzgzODk2NzUxNTQ0NzEyOjE3ODE2MTA2NTU6c3BfYXRmOjIwMDExNjA5NjQwMTc5ODo6MDo6&url=%2FLRS-350-48-Price-Switching-Supply-MeanWell%2Fdp%2FB0BP6S5DYR%2Fref%3Dsr_1_1_sspa%3Fcrid%3D27VPQOWNPN9UG%26dib%3DeyJ2IjoiMSJ9.qK84sGJa4-74kbCEX11MOFBju8sSQUdFsbHw6PNvmaEHnhzjX2T7dyhRNJY01mXxpWk8lccGOwnezxmqLKUjqglX_FI26mrxlvZf0KNiLdJ8QnhKsber4KDoyyLHNxWGV451uHCzZbCDXxM0iYXVnubuVourRaRURlyMorRavuLd2a32kABx-BKqyF5Dfr7dV453ecE6QULFqG-UVLBaBRijbxQGTJ2YiNyXAqn3bkM.Bt5mAPOJNAWGnXCC2mwvjdDdccZd1_0-WRXZpP4mR4M%26dib_tag%3Dse%26keywords%3DLRS-350-48%26qid%3D1781610655%26sprefix%3Dlrs-350-%252Caps%252C331%26sr%3D8-1-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9hdGY%26psc%3D1) 電源の使用を強く推奨します。より強い出力で性能を最大限に引き出す場合は、48V 25A 電源アダプターを選択できます。

### マスターアーム（Leader Arm、オプション）

[Leader Arm](https://www.seeedstudio.com/Star-Arm-102-p-6765.html?qid=P2U7IG_yskyak5m_1776415593315) と [12V 10A 電源](https://www.seeedstudio.com/FY1209900-12V-10A-Power-Adapter-12V-10A-p-6496.html) を購入できます。SO-ARM101 の 12V DC 電源アダプターで Leader に給電することも可能です。

## 🚀 オンライン体験

インストール不要で、reBot Arm B601-RS の MuJoCo デジタルツインをブラウザから直接体験できます。標準アームと AGV 構成の切り替え、関節と TCP の操作、俯瞰カメラと D405 手首カメラの表示、自動収納・積み上げデモを利用できます。初回のモデル読み込みには少し時間がかかる場合があります。Chrome または Edge を推奨します。

<p align="center">
  <a href="https://yang-ci.github.io/Rebot_Arm_AGV/"><strong>▶ reBot Arm インタラクティブデモを起動</strong></a>
</p>

## 🗺️ ロードマップ

主流のロボット開発エコシステムへの継続的なメンテナンスと適応に取り組んでいます。以下は現在の対応状況とリリース計画です。

### reBot Arm B601-DM

| 対応エコシステム | 状態 | 説明 | 関連ドキュメント |
| :--- | :---: | :--- | :--- |
| モーター基本使用 | ✅ 完了 | 基本的なモーション制御と API ラッパー化 | [Damiao Technology](https://wiki.seeedstudio.com/cn/damiao_series/) |
| STEP 3D 構造部品 & BOM のオープンソース化 | ✅ 完了 | 新バージョン全パーツの STEP ファイル、BOM、加工部品の参考価格 | [reBot Arm B601-DM BOM](./hardware/reBot_B601_DM/readme.md) |
| 実機性能テスト参考 | ✅ 完了 | 通常動作・限界動作における性能参考 | [Performance Testing](./hardware/reBot_B601_DM/performance_testing/Performance_Testing.md) |
| 組み立て動画 | ✅ 完了 | 超詳細な組み立て手順と動画 | [Getting Started](https://wiki.seeedstudio.com/rebot_b601_dm_getting_started/) |
| Python SDK | ✅ 完了 | Robstride、Damiao、Mota、Gaoqing、Hexfellow など各種モーターの読み書き・制御をワンストップ統合 | [Motorbridge](https://motorbridge.seeedstudio.com) · [Web UI](https://rebot-devarm.w0x7ce.eu/) |
| ROS2 統合 | ✅ 完了 | 運動学、軌道計画、重力補償に対応した ROS2 コントローラー | [ROS2 ガイド](https://wiki.seeedstudio.com/rebot_arm_b601_dm_ros2_integration/) |
| Pinocchio 統合 | ✅ 完了 | 順運動学/逆運動学と重力補償を実現 | [Pinocchio ガイド](https://wiki.seeedstudio.com/rebot_arm_b601_dm_pinocchio_meshcat/) · [リポジトリ](https://github.com/Seeed-Projects/reBotArm_control_py) |
| Isaac Sim シミュレーション | ✅ 完了 | USD モデルのインポートとシミュレーション遠隔操作 | [Wiki](https://wiki.seeedstudio.com/rebot_arm_b601_dm_isaacsim/) |
| VR テレオペレーション | ✅ 完了 | PICO 4 VR ベースのバイラテラル遠隔操作 | [リポジトリ](https://github.com/Eaglewzw/lerobot-teleoperator-rebot-vr) |
| LeRobot 統合 | ✅ 完了 | Hugging Face LeRobot トレーニングフレームワークに対応 | [LeRobot ガイド](https://wiki.seeedstudio.com/rebot_arm_b601_dm_lerobot/) |
| 深度カメラ統合 | ✅ 完了 | YOLO と深度カメラによるビジュアル把持デモ | [把持デモ](https://wiki.seeedstudio.com/rebot_arm_b601_dm_grasping_demo/) |
| reSpeaker 音声統合 | ✅ 完了 | reSpeaker Flex 4 マイクアレイによる空間認識対応の音声駆動制御 | [音声制御](https://wiki.seeedstudio.com/control_rebot_arm_using_voice_with_respeaker_flex/) |
| 最新アルゴリズムの段階的更新 | ⏳ 計画中 | 主流アルゴリズムを段階的に更新予定 | 継続中 |
| 完全無料コースシリーズの提供 | ⏳ 計画中 | 完全無料のコースシリーズを順次提供予定 | 継続中 |

#### 開発者からの貢献

| 対応エコシステム | 作者 | 説明 | リポジトリ |
| :--- | :---: | :--- | :--- |
| ROS2 (Humble)、third-party 統合、URDF / rebotarm_bringup | [@danieldoradotalaveron-rb](https://github.com/danieldoradotalaveron-rb) | 1. **パッシブ診断モニター**（`rebotarm_monitor_ros2`）—— `rqt_robot_monitor` 向け `/diagnostics` オーバーレイ、serial/CAN 対応アグリゲーター；<br>2. **安全な退避とシャットダウン** —— 接続時に休止姿勢を取得し、シャットダウン時や `/rebotarm/park` でゆっくり復帰；<br>3. **重力補償（スムーズ停止）** —— MIT ランプアウトで pos/vel 引き継ぎ時の衝撃・急動作を低減；<br>4. **IK/FK と安全対策を備えたゲームパッドテレオペ** —— IK によるエンドエフェクタ制御、RViz ライブ可視化（シミュレーションのみでテスト）；<br>5. **D405 eye-in-hand TF** —— `end_link` 下の Xacro 設定で RViz 可視化と TF のみに対応。 | [rebotarm_monitor_ros2](https://github.com/danieldoradotalaveron-rb/rebotarm_monitor_ros2) · [reBotArmController_ROS2](https://github.com/danieldoradotalaveron-rb/reBotArmController_ROS2) |

### reBot Arm B601-RS

| 対応エコシステム | 状態 | 説明 | 関連ドキュメント |
| :--- | :---: | :--- | :--- |
| モーター基本使用 | ✅ 完了 | 基本的なモーション制御と API ラッパー化 | [Robstride](https://wiki.seeedstudio.com/cn/robstride_control/) |
| STEP 3D 構造部品 & BOM のオープンソース化 | ✅ 完了 | 新バージョン全パーツの STEP ファイル、BOM、加工部品の参考価格 | [reBot Arm B601-RS BOM](./hardware/reBot_B601_RS/README.md) |
| クイックスタート | ✅ 完了 | B601-RS のクイックスタート | [Getting Started](https://wiki.seeedstudio.com/rebot_b601_rs_getting_started/) |
| 組み立て動画 | ✅ 完了 | 超詳細な組み立て手順と動画 | [組み立て動画](https://wiki.seeedstudio.com/rebot_b601_rs_getting_started/) |
| ROS2 (Humble) | ✅ 完了 | 運動学、軌道計画、重力補償、MoveIt2 に対応 | [ROS2 ガイド](https://wiki.seeedstudio.com/rebot_arm_b601_rs_ros2_integration/) |
| LeRobot 統合 | ✅ 完了 | Hugging Face LeRobot トレーニングフレームワークに対応 | [LeRobot ガイド](https://wiki.seeedstudio.com/rebot_arm_b601_rs_lerobot/) |
| Pinocchio 統合 | ✅ 完了 | 順運動学/逆運動学と重力補償を実現 | [Pinocchio ガイド](https://wiki.seeedstudio.com/rebot_arm_b601_rs_pinocchio_meshcat/) · [リポジトリ](https://github.com/Seeed-Projects/reBotArm_control_py) |
| 深度カメラ統合 | ✅ 完了 | YOLO と深度カメラによるビジュアル把持デモ | [把持デモ](https://wiki.seeedstudio.com/rebot_arm_b601_rs_grasping_demo/) |
| エンボディド・エージェント・アーキテクチャ | ✅ 完了 | 自然言語コマンド（例：「pick up the red block」）を受信し、把持計画を自動生成・実行 | [設計](https://wiki.seeedstudio.com/ja/wrc_demo_tutorial/) · [ソースコード](https://github.com/TheMoonAstronaut/wrc.git) |
| Isaac Sim シミュレーション | ✅ 完了 | USD モデルのインポートとシミュレーション遠隔操作 | [Github リポジトリ](https://github.com/Seeed-Projects/reBot-Isaacsim) |
| 最新アルゴリズムの段階的更新 | ⏳ 計画中 | 主流アルゴリズムを段階的に更新予定 | 継続中 |
| 完全無料コースシリーズの提供 | ⏳ 計画中 | 完全無料のコースシリーズを順次提供予定 | 継続中 |

#### 開発者からの貢献

| 対応エコシステム | 作者 | 説明 | リポジトリ |
| :--- | :---: | :--- | :--- |
| iPhone、HEBI Mobile I/O、Meta Quest によるテレオペレーション | [@ammarjmahmood](https://github.com/ammarjmahmood) | スマートフォンや Quest コントローラーを動かすとグリッパーが追従します。TidyBot++（CoRL 2024）の相対姿勢マッピングを採用：ネイティブ SwiftUI と ARKit の iPhone アプリ、HEBI Mobile I/O、Quest の WebXR パススルー、200 Hz MIT ドライバー、重力フィードフォワード、公式 RS URDF による逆運動学と安全インターロック。B601-RS と iPhone 16 Pro Max で検証済み。 | [rebot-phone-teleop](https://github.com/ammarjmahmood/rebot-phone-teleop) |

## ⚙️ ハードウェア仕様

デスクトップ向け Embodied AI アプリケーション向けに設計され、可搬重量と柔軟性のバランスを取っています。

| パラメータ | reBot Arm B601-DM | reBot Arm B601-RS |
| :--- | :--- | :--- |
| 作業負荷 | 1.5 kg | **2.5 kg** |
| 推奨作業空間 | アーム到達範囲の 70% | アーム到達範囲の 70% |
| 最大リーチ | 767 mm | **754 mm** |
| 自重 | **約 4.5 kg** | 約 6.7 kg |
| 繰り返し精度 | < 0.2 mm | < 0.2 mm |
| 自由度 | 6 DOF + 1 グリッパー | 6 DOF + 1 グリッパー |
| 対応プラットフォーム | ROS1、ROS2、LeRobot、Pinocchio、Isaac Sim、Python SDK | ROS1、ROS2、LeRobot、Pinocchio、Isaac Sim、Python SDK |
| 供給電圧 | DC 24V | DC 48V |

## 🌟 コミュニティ作品

|  |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: |
| <a href="https://www.kaggle.com/competitions/gemma-4-good-hackathon/writeups/new-writeup-1778618527713"><img src="/community/GEM-4.png" height="80" alt="GEM-4"></a><br><sub>[GEM-4 より](https://www.kaggle.com/competitions/gemma-4-good-hackathon/writeups/new-writeup-1778618527713)</sub> | <a href="https://x.com/Linyan_Fu/status/2056383947341525180"><img src="/community/from_Linyan.png" height="80" alt="Linyan Fu"></a><br><sub>[Linyan Fu より](https://x.com/Linyan_Fu/status/2056383947341525180) · [Apheth D Almeida](https://x.com/Apheth_DAlmeida/status/2053503164507476096)</sub> | <a href="https://x.com/DhruvDiddi/status/2046605015008383284"><img src="/community/from_Diddi.png" height="80" alt="Dhruv Diddi"></a><br><sub>[Dhruv Diddi より](https://x.com/DhruvDiddi/status/2046605015008383284)</sub> | <a href="https://x.com/ed0henderson/status/2055076839002095743"><img src="/community/from_Henderson.jpg" height="80" alt="Ed Henderson"></a><br><sub>[Ed Henderson より](https://x.com/ed0henderson/status/2055076839002095743)</sub> | <img src="/community/from_Sameer.png" height="80" alt="Sameer"><br><sub>Sameer</sub> |
| <a href="https://x.com/pham_blnh/status/2061994096374505710"><img src="/community/from_Binh_Pham.png" height="80" alt="Binh Pham"></a><br><sub>[Binh Pham より](https://x.com/pham_blnh/status/2061994096374505710)</sub> | <a href="https://www.instagram.com/reel/DY7Ny8OPjVu/?utm_source=ig_web_copy_link&igsh=NTc4MTIwNjQ2YQ=="><img src="/community/from_fangtianchonghui.png" height="80" alt="FangTianChongHui"></a><br><sub>[FangTianChongHui より](https://www.instagram.com/reel/DY7Ny8OPjVu/?utm_source=ig_web_copy_link&igsh=NTc4MTIwNjQ2YQ==)</sub> | <a href="https://x.com/dong1505lin"><img src="/community/from_xensedyl.png" height="80" alt="Xense YaoLin Dong"></a><br><sub>[Xense YaoLin Dong](https://x.com/dong1505lin)</sub> | <a href="https://x.com/ed0henderson/status/2055076839002095743"><img src="/community/from_Henderson_2.png" height="80" alt="Ed Henderson"></a><br><sub>[Ed Henderson より](https://x.com/ed0henderson/status/2055076839002095743)</sub> | <a href="https://x.com/yoshikai_man/status/2079938975398244705"><img src="/community/YOR_Car.png" height="80" alt="yoshikai_man"></a><br><sub>[yoshikai_man より](https://x.com/yoshikai_man/status/2079938975398244705)</sub> |
| <a href="https://github.com/lipengdong/hei-rebot-lift"><img src="/community/hei-robot-lift-play.gif" height="80" alt="hei-rebot-lift"></a><br><sub>[hei-rebot-lift より](https://github.com/lipengdong/hei-rebot-lift)</sub> | <a href="https://www.linkedin.com/posts/activity-7484390995862781952-TX4m?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE6WUL4BWkFeyUj0TJ5JlGf6IG4iRHAicUo"><img src="/community/VR_with_reBot.png" height="80" alt="Martin Kemka"></a><br><sub>[Martin Kemka より](https://www.linkedin.com/posts/activity-7484390995862781952-TX4m?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE6WUL4BWkFeyUj0TJ5JlGf6IG4iRHAicUo)</sub> | <a href="https://www.linkedin.com/posts/kamil-buczy%C5%84ski-102843301_seeedstudio-rebotarm-seeedprojectofthemonth-ugcPost-7485297094715461633-RV_6/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE6WUL4BWkFeyUj0TJ5JlGf6IG4iRHAicUo"><img src="/community/reBot_grasp_fruit.png" height="80" alt="Kamil Buczyński"></a><br><sub>[Kamil Buczyński より](https://www.linkedin.com/posts/kamil-buczy%C5%84ski-102843301_seeedstudio-rebotarm-seeedprojectofthemonth-ugcPost-7485297094715461633-RV_6/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE6WUL4BWkFeyUj0TJ5JlGf6IG4iRHAicUo)</sub> | <a href="https://www.linkedin.com/posts/doradodaniel_computervision-spatialai-sim2real-share-7474727487374184448-NhwX/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE6WUL4BWkFeyUj0TJ5JlGf6IG4iRHAicUo"><img src="/community/Daniel_Dorado.jpg" height="80" alt="Daniel Dorado"></a><br><sub>[Daniel Dorado より](https://www.linkedin.com/posts/doradodaniel_computervision-spatialai-sim2real-share-7474727487374184448-NhwX/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE6WUL4BWkFeyUj0TJ5JlGf6IG4iRHAicUo)</sub> | <a href="https://www.linkedin.com/posts/asierarranz_nvidia-physicalai-isaaclab-ugcPost-7480271721942417408-YNwu/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE6WUL4BWkFeyUj0TJ5JlGf6IG4iRHAicUo"><img src="/community/Groot_N1.7.png" height="80" alt="Asier"></a><br><sub>[Asier より](https://www.linkedin.com/posts/asierarranz_nvidia-physicalai-isaaclab-ugcPost-7480271721942417408-YNwu/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE6WUL4BWkFeyUj0TJ5JlGf6IG4iRHAicUo)</sub> |
| <a href="https://x.com/thermalpastor/status/2103842737032458567"><img src="/community/thermalpastor.png" height="80" alt="H"></a><br><sub>[H より](https://x.com/thermalpastor/status/2103842737032458567)</sub> | <a href="https://x.com/Alpha10six/status/2103860758559994216"><img src="/community/alpha_rover.png" height="80" alt="alpha_rover"></a><br><sub>[alpha_rover より](https://x.com/Alpha10six/status/2103860758559994216)</sub> | <a href="https://x.com/DilumSanjaya/status/2102806161728885145"><img src="/community/DilumSanjaya.png" height="80" alt="Dilum Sanjaya"></a><br><sub>[Dilum Sanjaya より](https://x.com/DilumSanjaya/status/2102806161728885145)</sub> | <a href="https://x.com/pham_blnh/status/2101003855731593544"><img src="/community/pham_blnh.png" height="80" alt="Binh"></a><br><sub>[Binh より](https://x.com/pham_blnh/status/2101003855731593544)</sub> | <a href="https://x.com/LeRobotHF/status/2104519372333048112"><img src="/community/LeRobot.png" height="80" alt="LeRobot"></a><br><sub>[LeRobot より](https://x.com/LeRobotHF/status/2104519372333048112)</sub> |
| <a href="https://x.com/raghav2956/status/2104659668375339475"><img src="/community/Raghav_Kumar.png" height="80" alt="Raghav Kumar"></a><br><sub>[Raghav Kumar より](https://x.com/raghav2956/status/2104659668375339475)</sub> | <a href="https://www.linkedin.com/posts/kamil-buczy%C5%84ski-102843301_seeedstudio-ai-agent-ugcPost-7510738285707776000-1SMQ/?utm_source=social_share_send&utm_medium=android_app&rcm=ACoAAE6WUL4BWkFeyUj0TJ5JlGf6IG4iRHAicUo"><img src="/community/Kamil_Buczynski.png" height="80" alt="Kamil Buczyński"></a><br><sub>[Kamil Buczyński より](https://www.linkedin.com/posts/kamil-buczy%C5%84ski-102843301_seeedstudio-ai-agent-ugcPost-7510738285707776000-1SMQ/?utm_source=social_share_send&utm_medium=android_app&rcm=ACoAAE6WUL4BWkFeyUj0TJ5JlGf6IG4iRHAicUo)</sub> | <a href="https://www.linkedin.com/feed/update/urn:li:activity:7510701008885309440/"><img src="/community/Fictionlab.png" height="80" alt="Fictionlab"></a><br><sub>[Fictionlab より](https://www.linkedin.com/feed/update/urn:li:activity:7510701008885309440/)</sub> | <a href="https://x.com/seeedstudio/status/2101965998954107303"><img src="/community/box2bridge.png" height="80" alt="box2bridge"></a><br><sub>[box2bridge より](https://x.com/seeedstudio/status/2101965998954107303)</sub> | <a href="https://x.com/seeedstudio/status/2095469352976003482"><img src="/community/Fangtian.png" height="80" alt="FangTianChongHui"></a><br><sub>[FangTianChongHui より](https://x.com/seeedstudio/status/2095469352976003482)</sub> |

<p align="center">
  <a href="https://www.seeedstudio.com/sim-to-real-with-seeed-rebot-and-nvidia-isaac"><img src="/community/sim-to-real-vla.gif" height="90" alt="Sim-to-Real VLA コース"></a><br>
  <sub><a href="https://www.seeedstudio.com/sim-to-real-with-seeed-rebot-and-nvidia-isaac">Seeed reBot Arm × NVIDIA Isaac —— Sim-to-Real VLA コース</a></sub>
</p>

## 🧹 オプションパーツ

### 手首カメラマウント

これらの手首カメラマウントは **B601-RS と B601-DM で共通**です。全モデル、プレビュー、ダウンロードは[カメラマウントとデータ収集用リソース一覧（英語）](hardware/camera-mounts/README.md)をご覧ください。

| 32×32 UVC カメラ | Intel D435i | Intel D405 & Gemini 305 | Gemini 2 |
| :--- | :--- | :--- | :--- |
| <img src="./hardware/reBot_B601_DM/3D_Printed_Parts/images/UVC_camera_mount.png" height="100"> | <img src="./hardware/reBot_B601_DM/3D_Printed_Parts/images/D435i.jpg" height="100"> | <img src="./hardware/reBot_B601_DM/3D_Printed_Parts/images/D405.jpg" height="100"> | <img src="./hardware/reBot_B601_DM/3D_Printed_Parts/images/Gemini2.jpg" height="100"> |
| [STEP](hardware/camera-mounts/b601-camera-mounts/UVC32_mount.step) | [STEP](hardware/camera-mounts/b601-camera-mounts/D435_Gemini2_Mount.step) | [STEP](hardware/camera-mounts/b601-camera-mounts/D405_305_Mount.step) · [設計説明](https://github.com/bowenszhu/rebot-b601-rs-d405-wrist-mount/tree/v1.0.0) | [STEP](hardware/camera-mounts/b601-camera-mounts/D435_Gemini2_Mount.step) |

### マスターアーム（Leader Arm）対応

| Star Arm 102-LD | 各種アームの接続・互換に対応予定 |
| :--- | :--- |
| <img src="./hardware/reBot_B601_DM/3D_Printed_Parts/images/star_arm_102.jpg" height="100"> | [シリーズハブ](https://fashionstar.com.hk/robot-arm/star-arm-102/) · [GitHub リポジトリ](https://github.com/servodevelop/Star-Arm-102) |

### DIY ソフトフィンガー

| ソフトフィンガー | 互換性統合に対応可能 |
| :--- | :--- |
| <img src="./hardware/reBot_B601_DM/3D_Printed_Parts/images/Soft_Finger.png" height="100"> | 近日公開 |
| [フィンガー取付台（ABS/PLA）](hardware/reBot_B601_DM/3D_Printed_Parts/Soft_Gripper_Mount.step) · [フィンガー本体（TPU 95+）](hardware/reBot_B601_DM/3D_Printed_Parts/Soft_Gripper_Finger.step) | 近日公開 |

### おすすめオプションパーツ

| カテゴリ | 種類 | 画像 | 製品 | リンク |
| :--- | :--- | :--- | :--- | :--- |
| **カメラ** | デプスカメラ | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/0/-/0-101090144--orbbec-gemini-2-3d-camera.jpg" alt="Orbbec Gemini 2" width="120"> | **Orbbec Gemini 2 3D Camera** | [Seeed Studio](https://www.seeedstudio.com/Orbbec-Gemini-2-3D-Camera-p-6464.html) |
| **カメラ** | デプスカメラ | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/1/0/1000000774.png" alt="Orbbec Gemini 336" width="120"> | **Orbbec Gemini 336 Depth Camera** | [Seeed Studio](https://www.seeedstudio.com/Orbbec-Gemini-336-3D-Camera-3D-p-6662.html) |
| **カメラ** | デプスカメラ | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/1/-/1-100010971-orbbec-gemini-335-lg.jpg" alt="Orbbec Gemini 335LG" width="120"> | **Orbbec Gemini 335LG 3D Camera** | [Seeed Studio](https://www.seeedstudio.com/Orbbec-Gemini-335LG-3D-Camera-p-6541.html) |
| **カメラ** | デプスカメラ | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/0/0/0035718.png" alt="SLAMTEC Aurora S" width="120"> | **SLAMTEC Aurora S** | [Seeed Studio](https://www.seeedstudio.com/SLAMTEC-Aurora-S-AI-Integrated-Spatial-Perception-System-p-6669.html) |
| **カメラ** | デプスカメラ | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/i/n/intel_realsense_d435i_34_1_1.jpg" alt="Intel RealSense D435i" width="120"> | **Intel RealSense Depth Camera D435i** | [Seeed Studio](https://www.seeedstudio.com/Intel-RealSense-Depth-Camera-D435i-p-4423.html) |
| **カメラ** | デプスカメラ | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/1/-/1-100000540-realsense-d405-3d-camera.jpg" alt="RealSense D405" width="120"> | **RealSense Depth Camera D405** | [Seeed Studio](https://www.seeedstudio.com/RealSense-D405-3D-Camera-p-6758.html) |
| **カメラ** | 単眼カメラ | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/0/-/0-101090101-3mp-gmsl2-camera-module-190-degree.jpg" alt="Sensing SG3S-ISX031C-GMSL2F" width="120"> | **Sensing SG3S-ISX031C-GMSL2F 3MP GMSL2 Camera** | [Seeed Studio](https://www.seeedstudio.com/SG3S-ISX031C-GMSL2F-p-6245.html) |
| **カメラ** | 単眼カメラ | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/s/2/s231.1.jpg" alt="ET-S231" width="120"> | **ET-S231 Megapixel 120° 広角 1080P USB カメラ** | [Seeed Studio](https://www.seeedstudio.com/ET-S231-120-USB-Camera-p-6683.html) |
| **マイク** | マイクアレイ | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/1/-/1-100070894-respeaker-flex-xvf3800-circular-4-with-xiao-esp32s3_1_.jpg" alt="reSpeaker Flex XVF3800" width="120"> | **reSpeaker Flex XVF3800 Circular-4 with XIAO ESP32S3** | [Seeed Studio](https://www.seeedstudio.com/reSpeaker-Flex-XVF3800-Circular-4-with-XIAO-ESP32S3-p-6739.html) |
| **マイク** | マイクアレイ | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/1/-/1-respeaker-xvf3800-4-mic-array.jpg" alt="reSpeaker XMOS XVF3800" width="120"> | **reSpeaker XMOS XVF3800** | [Seeed Studio](https://www.seeedstudio.com/ReSpeaker-XVF3800-USB-Mic-Array-p-6488.html) |
| **コントローラー** | エッジコントローラー | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/1/1/110110147.jpg" alt="reComputer J3011" width="120"> | **reComputer J3011-Orin Nano 8GB** | [Seeed Studio](https://www.seeedstudio.com/reComputer-J3011-p-5590.html) |
| **コントローラー** | エッジコントローラー | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/i/m/image-kit-3.png" alt="Jetson AGX Thor" width="120"> | **NVIDIA Jetson AGX Thor Developer Kit** | [Seeed Studio](https://www.seeedstudio.com/NVIDIA-Jetson-AGX-Thor-Developer-Kit-p-9965.html) |

## 🎓 フルスタックエコシステム

reBot-DevArm は単なるロボットアームではなく、ロボティクス学習コミュニティでもあります。以下の一般向けチュートリアルを無料で共有しています：

**🖥️ エッジコンピューティング & メインコントロール**

- [![Jetson](https://img.shields.io/badge/NVIDIA-reComputer%20Jetson-76B900?style=for-the-badge&logo=nvidia&logoColor=white)](https://wiki.seeedstudio.com/NVIDIA_Jetson/) —— AI 推論 & 計算コア
- [![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-4B%20%2F%205-C51A4A?style=for-the-badge&logo=Raspberry%20Pi&logoColor=white)](https://wiki.seeedstudio.com/raspberry-pi-devices/) —— 汎用 Linux 開発環境
- [![ESP32](https://img.shields.io/badge/MCU-Seeed%20XIAO%20(ESP32)-0091BD?style=for-the-badge&logo=espressif&logoColor=white)](https://wiki.seeedstudio.com/SeeedStudio_XIAO_Series_Introduction/) —— 低消費電力ワイヤレス制御ノード

**📡 センサー & 周辺機器**

- **モーター & サーボ** —— [Damiao / Gogo / Robstride / Mita / Feite / Fashion Star](https://wiki.seeedstudio.com/robotics_page/)
- **ビジュアル知覚** —— [深度カメラ / LiDAR / ビジョンアルゴリズム](https://wiki.seeedstudio.com/robotics_page/)
- **音声インタラクション** —— [reSpeaker マイクアレイ / 音声制御 / 空間認識（DoA）](https://wiki.seeedstudio.com/control_rebot_arm_using_voice_with_respeaker_flex/)
- **動作 & 姿勢** —— [IMU（6 軸/9 軸）/ ジャイロスコープ / 磁力計](https://wiki.seeedstudio.com/Sensor_accelerometer/)
- **総合キット** —— [その他のロボティクスセンサー & ドライバ例](https://wiki.seeedstudio.com/robotics_page/)

> 👉 **[クリックして Wiki ナレッジベースへ](https://wiki.seeedstudio.com/)** —— すべてのチュートリアルは無料で閲覧できます。

## 🙌 謝辞と貢献者

オープンソースの道は決して孤独ではありません。reBot-DevArm の誕生は、Seeed Studio、世界中のオープンソースコミュニティ、そして優れたハードウェアパートナーの支援なしには実現できませんでした。以下のプロジェクトとチームに最大限の敬意を表します：

**🌍 エコシステム & ソフトウェアサポート**

- [Seeed Studio](https://www.seeedstudio.com/) —— 包括的なハードウェアサプライチェーンと技術サポート
- [Hugging Face LeRobot](https://github.com/huggingface/lerobot) —— 優れたエンドツーエンドのロボット学習フレームワーク
- [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim) —— 強力なロボットシミュレーションおよび合成データプラットフォーム

**⚙️ コアハードウェアパートナー**

- [Damiao Technology](https://www.damiaokeji.com/)
- [Robstride](https://robstride.com/)
- [Fashion Star](https://fashionstar.com.hk/wiki/)

**💡 インスピレーション**

- [SO-ARM100](https://github.com/TheRobotStudio/SO-ARM100/tree/main)
- [Mobile ALOHA](https://github.com/tonyzhaozh/aloha)
- [Dummy-Robot (Zhihui Jun)](https://github.com/peng-zhihui/Dummy-Robot)
- [OpenArm](https://openarm.dev/)
- [I2RT](https://i2rt.com/)
- [TRLC-DK1](https://github.com/robot-learning-co/trlc-dk1)

**🎃 プロトタイプ貢献者**

- SeeedStudio AI Robotics Team —— Yaohui Zhu（yaohui.zhu@seeed.cc）
- SeeedStudio STU —— Wentao Dong
- SeeedStudio STU —— Weiwei Xu
- SeeedStudio Purchasing Department —— Fengqun Peng

**👥 貢献者**

<p align="center"><a href="https://github.com/Seeed-Projects/reBot-DevArm/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=Seeed-Projects/reBot-DevArm" />
</a></p>

*近日公開予定…… ぜひ PR を送ってコントリビューターになってください！*

### ⭐ Star 履歴

<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/star-history/star-history-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/star-history/star-history-light.svg">
  <img src="assets/star-history/star-history-light.svg">
</picture>
</p>

## 📄 ライセンス

- **ハードウェア設計** © 2026 Seeed Studio Co., Ltd. —— [CERN-OHL-W-2.0](https://ohwr.org/cern_ohl_w_v2.txt) に基づきオープンソース化
- **ファームウェアコード** © 2026 Seeed Studio Co., Ltd. —— [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) に基づきオープンソース化

### 権利と制限事項

reBot Arm ロボットアームプロジェクトは、常に「機敏性・開放性・責任感・共創」という中核理念を掲げて開発者コミュニティに貢献してきました。ビジョンは、すべての愛好家が reBot を通じてロボットアームのハードウェアアーキテクチャとソフトウェアの基本原理を体系的に習得し、先端の身体性人工知能アルゴリズムを体験できるようにすることです。

プロジェクト開始当初は **CC BY-SA NC（非営利）オープンソースライセンス**を採用し、未成熟な段階で開発者と貢献者が商業的な要求に煩わされることなく製品の反復改善に集中できるようにしました。SeeedStudio による数ヶ月の徹底的な磨き上げを経て、**2026 年 5 月 11 日より** CC BY-SA NC から **CERN-OHL-W 2.0 オープンソースライセンス**へ正式に移行し、ハードウェアとソフトウェアの全チェーンで 100% オープンソース化、全シナリオでの商業的遵守使用を許可しました。

本プロジェクトではハードウェアとソフトウェアで異なるライセンスを適用します。使用前に該当部分のライセンス条項をご確認ください。

| 項目 | ハードウェア（CERN-OHL-W-2.0） | ソフトウェア SDK（Apache-2.0） |
| :--- | :--- | :--- |
| ✅ 商用利用 | ✅ 許可 | ✅ 許可 |
| ✅ 改変 | ✅ 許可 | ✅ 許可 |
| ✅ 再配布 | ✅ 許可 | ✅ 許可 |
| ✅ クローズドソースでの統合/再公開 | ❌ 条件付きで許可（[CERN-OHL-W-2.0](https://ohwr.org/cern_ohl_w_v2.txt) 参照） | ✅ 許可（修正コードの公開は不要） |
| ⚠️ 著作権表示の保持 | ✅ 必須 | ✅ 必須 |
| ⚠️ ライセンス原文の保持 | ✅ 必須 | ✅ 必須 |
| ⚠️ 変更箇所の明示 | ✅ 必須（変更内容と日付を明記） | ✅ 必須（変更内容を明記） |
| ⚠️ 特許許諾 | ✅ 明確な特許許諾 | ✅ 明確な特許許諾 |
| ⚠️ 配布時のソース提供 | ✅ **必須**（ハードウェアの「完全なソース」を提供） | ❌ ソース提供の義務なし |
| ⚠️ 外部/クローズドモジュールとの互換性 | ✅ 許可（Weakly Reciprocal 特性） | ✅ 完全に許可 |
| 🔗 他のコンポーネントとの関係 | 独立したインターフェースモジュール（External Material）は元のライセンス（クローズドも可）を維持可能 | 無制限。あらゆるライセンスのコードライブラリとリンク可能 |
| 📄 公式ライセンス全文 | [CERN-OHL-W-2.0](https://ohwr.org/cern_ohl_w_v2.txt) | [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) |

## ☎ お問い合わせ

- **オープンソース進捗 & 技術サポート** —— Yaohui：yaohui.zhu@seeed.cc
- **今後の協業 & カスタマイズ** —— Elaine：elaine.wu@seeed.cc
