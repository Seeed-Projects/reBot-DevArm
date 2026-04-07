# 🦾 reBot-DevArm：すべての開発者のためのオープンソースロボットアーム

<p align="center">
  <img src="./media/v1.0.png" alt="reBot-DevArm バナー">
</p>

<p align="center">
    <!-- CC BY-NC-SA 4.0 バッジに置き換え、非商用利用であることを明示 -->
    <a href="./LICENSE">
        <img src="https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg" alt="ライセンス：CC BY-NC-SA 4.0">
    </a>
    <img src="https://img.shields.io/badge/Commercial-Contact%20Us-red.svg" alt="yaohui.zhu@seeed.cc">
    <img src="https://img.shields.io/badge/ROS-Noetic%20%7C%20Humble-orange.svg" alt="ROS サポート">
    <img src="https://img.shields.io/badge/Framework-LeRobot-yellow.svg" alt="LeRobot">
    <img src="https://img.shields.io/badge/Framework-Isaac Sim-yellow.svg" alt="LeRobot">
</p>

<p align="center">
  <strong>100% 完全オープンソース · Embodied AI · ハードウェア・ソフトウェア統合 · 個人利用/教育利用は無料 · 商用利用には認可が必要</strong>
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
    <img src="https://img.shields.io/badge/Documentation-📕-blue" alt="ロボティクス wiki"></a>
</p>



## 📖 はじめに

**reBot-DevArm（reBot Arm B601 DM および reBot Arm B601 RS）** は、Embodied AI の学習ハードルを下げることに取り組むロボットアームプロジェクトです。私たちは **「真のオープンソース」** に重点を置いています。コードだけでなく、あらゆるものを惜しみなくオープンソース化します：
- 🦾 **2つのロボットアームバージョン**：同一の外観を持つ2種類のロボットアーム、**Robostride** と **Damiao** の両バージョンについて、すべてのオープンソースファイルを提供します。
- 🛠️ **ハードウェア設計図**：板金部品および3Dプリント部品のソースファイル。
- 🔩 **BOM リスト**：すべてのネジの仕様や購入リンクに至るまで詳細に記載。
- 💻 **ソフトウェア & アルゴリズム**：Python SDK、ROS1/2、Isaac Sim、LeRobot など。

## ご自身のreBot Armを入手するには

- 5種類のキットをご用意しています
  - **アーム本体モーターキット**：モーターとワイヤーハーネスのみを含むキット
  - **アーム本体構造部品キット**：構造部品のみを含むキット
  - **アームグリッパーフルキット**：グリッパー用モーター、配線、構造部品を含むキット
  - **フルキット**：アーム本体とグリッパーをセットにしたフルセット
  - **組立済みアーム**：完成品として組み立てられたロボットアーム

ご自身が既にお持ちの部品に合わせて、SeeedStudioモールにて残りのパーツをご購入いただけます（入荷予定：2026年4月15日）。

[こちらに情報をご登録いただければ、数量限定の事前予約リンクを事前にお送りいたします。](https://forms.gle/1MwdVKUqkuGu3C7L7)

## 🗺️ ロードマップ & ステータス

私たちは、主流のロボット開発エコシステムへの継続的なメンテナンスと適応に取り組んでいます。以下は、現在の対応状況と予定リリーススケジュールです。

### reBot Arm B601 DM
| 対応エコシステム | 状態 | 説明 / 予定公開日 | 関連ドキュメント |
| :--- | :---: | :--- | :--- |
| **モーター基本使用** | ✅ 完了 | 基本的なモーション制御と API ラッパー化 | [Damiao Technology](https://wiki.seeedstudio.com/cn/damiao_series/) |
| **新バージョン STEP 3D 構造部品および BOM のオープンソース化** | ✅ 完了 | 新バージョンの全パーツの STEP ファイル、部品 BOM、およびすべての加工部品の参考価格 | [reBot Arm B601-DM BOM](./hardware/reBot_B601_DM/readme_jp.md) |
| **実機性能テスト参考** | ✅ 完了  | 通常動作および限界動作におけるロボットアームの性能参考 |[Performance Testing](./hardware/reBot_B601_DM/performance_testing/Performance_Testing_JP.md) |
| **組み立て動画** | 🚧 進行中 | 超詳細な組み立て手順と動画 | [予定：2026.04.10] |
| **ROS2 (Humble)** | 🚧 進行中  | コアドライバはすでに完成しており、現在 MoveIt2 を最適化中です | [予定：2026.04.10] |
| **Python SDK** | 🚧 進行中  |  | [予定：2026.04.10] |
| **Pinocchio 対応** | 🚧 進行中  | Pinocchio フレームワークへの対応を行い、ロボットアームの順運動学/逆運動学および重力補償機能を実現 | [GitHub リポジトリ](https://github.com/vectorBH6/reBotArm_control_py/tree/main) 継続更新中 |
| **Isaac Sim シミュレーション** | 🚧 進行中  | USD モデルをインポートし、シミュレーションによる遠隔操作を実現 | [予定：2026.04.20] |
| **LeRobot 対応** | 🚧 進行中  | Hugging Face LeRobot 学習フレームワークへの対応 | [予定：2026.04.30] |
| **最新アルゴリズムの段階的更新** | ⏳ 計画中 | 主流アルゴリズムを段階的に更新予定 | 継続中 |
| **完全無料コースシリーズの提供** | ⏳ 計画中 | 主流アルゴリズムを段階的に更新予定 | 継続中 |



### reBot Arm B601 RS

| 対応エコシステム | 状態 | 説明 / 予定公開日 | 関連ドキュメント |
| :--- | :---: | :--- | :--- |
| **モーター基本使用** | ✅ 完了 | 基本的なモーション制御と API ラッパー化 | [Robstride](https://wiki.seeedstudio.com/cn/robstride_control/) |
| **新バージョン STEP 3D 構造部品および BOM のオープンソース化** | 🚧 進行中 | 新バージョンの全パーツの STEP ファイル、部品 BOM、およびすべての加工部品の参考価格 | 予定 [2026.04.31] |
| **組み立て動画** | 🚧 進行中 | 超詳細な組み立て手順と動画 | [予定 2026.05.10] |
| **ROS2 (Humble)** | ⏳ 計画中 | コアドライバはすでに完成しており、現在 MoveIt2 を最適化中です | [予定 2026.05] |
| **LeRobot 対応** | ⏳ 計画中 | Hugging Face LeRobot 学習フレームワークへの対応 | [予定 2026.05] |
| **Pinocchio 対応** | ⏳ 計画中 | Pinocchio フレームワークへの対応を行い、ロボットアームの順運動学/逆運動学および重力補償機能を実現 | [予定 2026.05] |
| **Isaac Sim シミュレーション** | ⏳ 計画中 | USD モデルをインポートし、シミュレーションによる遠隔操作を実現 | [予定 2026.05] |
| **最新アルゴリズムの段階的更新** | ⏳ 計画中 | 主流アルゴリズムを段階的に更新予定 | 継続中 |
| **完全無料コースシリーズの提供** | ⏳ 計画中 | 主流アルゴリズムを段階的に更新予定 | 継続中 |


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
*   **👂 音声インタラクション**: [ReSpeaker マイクアレイ / 音声認識](https://wiki.seeedstudio.com/ReSpeaker_Mic_Array_v2.0/)
*   **🧭 動作 & 姿勢**: [IMU（6軸/9軸） / ジャイロスコープ / 磁力計](https://wiki.seeedstudio.com/Sensor/IMU/)
*   **🤖 総合キット**: [その他のロボティクスセンサー & ドライバ例](https://wiki.seeedstudio.com/robotics_page/)


> 👉 **[クリックして Wiki ナレッジベースへ移動](https://wiki.seeedstudio.com/)** （すべてのチュートリアルは無料で閲覧できます）

---

## ⚙️ ハードウェア仕様

reBot-DevArm は、デスクトップ向け Embodied AI アプリケーションのために設計されており、可搬重量と柔軟性のバランスを取っています。

| パラメータ | reBot Arm B601-DM |
| :--- | :--- |
| **推奨連続可搬重量** | アーム到達範囲ワークスペースの 70% 以内で 1.5 kg 未満 |
| **推奨可搬重量** | **1.5 kg** |
| **最大リーチ** | **650 mm** |
| **重量** | 約 4.5 kg |
| **繰り返し精度** | < 0.2 mm |
| **自由度（DOF）** | 6 DOF + 1 グリッパー（オープンソース CAN サーボグリッパーおよび関節モーターグリッパーは近日公開予定） |
| **対応プラットフォーム/エコシステム** | ROS1、ROS2、LeRobot、Pinocchio、Isaac Sim、Python SDK |
| **供給電圧** | DC 24V |

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
*   **[Fashion Star](https://fashionrobo.com/)**

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

[![Star History Chart](https://api.star-history.com/svg?repos=Seeed-Projects/reBot-DevArm&type=date&legend=top-left)](https://www.star-history.com/#Seeed-Projects/reBot-DevArm&type=date&legend=top-left)

# reBot-DevArm プロジェクトライセンス
Copyright (c) [2025] [Seeed Studio]

本作品は **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License** のもとでライセンスされています。
このライセンスのコピーを表示するには、次をご覧ください： http://creativecommons.org/licenses/by-nc-sa/4.0/

--------------------------------------------------------------------------------

## 権利および制限に関する声明

このオープンソースプロジェクトの中核的な目的は、知識共有を促進し、開発者や愛好家が最小限のコストで最先端のロボットアーム技術にアクセスし学べるようにすることです。私たちは、完全無料かつ一般公開されたドキュメントと動画チュートリアルを提供し、ユーザーが迅速に使い始め、深い研究を行い、ロボティクスの普及と実用化を共に推進できるよう支援します。

### I. 非商用利用ポリシー

本プロジェクトのすべてのオープンソースコンテンツは、個人学習、研究、および非商用利用のために全面的に利用可能です。個人ユーザーには次のことが許可されます：

* プロジェクトのオープンソースドキュメント、コード、およびチュートリアルを閲覧し学習すること；
* 個人学習および研究目的でオープンソースコンテンツを修正およびデバッグすること；
* 個人利用のためにロボットアームを組み立てること、または非商用目的でオープンソースコンテンツに基づいて二次開発を行うこと。

### II. 商用利用ポリシー

私たちは、開発者、ロボティクス愛好家、そしてサードパーティプラットフォームが reBot ロボットアームを基に二次開発を行い、実世界での応用を推進することを積極的に奨励し支援します。以下に、許可される商業活動と禁止される商業活動を示します：

#### (1) 許可される商業活動

私たちは、すべての開発者の努力と正当な収益を尊重します。Seeed から reBot B601 シリーズロボットアームを購入し、ご自身の成果を加えた場合、以下を含むがこれらに限定されない形で、その成果を商用化することができます：

* アプリケーション指向のソフトウェアシステムを開発し、それを商業的に宣伝または販売すること；
* 体系的な教育コース（オンライン/オフライン）を作成し、有料のトレーニングまたは知識サービスを提供すること；
* 世界各地でオフライン教育、トレーニング、技術普及活動を実施すること；
* オープンソースコミュニティ、知識の普及、ロボティクス技術の実世界応用に貢献するその他の商業活動。

上記の適法な商業活動については、ぜひ私たちにご連絡ください。私たちは商用認可、実装支援、およびプロモーション支援を提供します。また、あなたのプロジェクトの成功を支援するため、認可について公開発表を行う場合もあります。

#### (2) 禁止される商業活動

本プロジェクトの製品にわずかな変更を加え、IP、ロゴ、または関連識別子を差し替えたうえで、自社ブランドとして販売することは禁止されています。このような行為は実質的な技術革新には当たらず、開発者の成長、オープンソースコミュニティ、本プロジェクト自体のいずれにも利益をもたらしません。これらの行為は違反と見なされ、私たちは対応を取る権利を留保します。

### III. 協業 & 連絡先

私たちは、適法な枠組みの中で、すべての開発者およびパートナーと協力し、reBot ロボットアームプロジェクトの成熟と展開を推進したいと考えています。実世界のロボットアプリケーションの実現に関心を持つ個人および組織に対し、私たちは以下を提供します：

* 商用ライセンスおよび知的財産コンプライアンス支援；
* プロジェクトソリューションのプロモーション支援；
* ロボットアームおよび関連ソリューションのカスタム開発サービス；
* 共同研究開発および共同開発の機会。

商業協業に関心がある場合、または関連するニーズがある場合は、どうぞお気軽にご連絡ください。ロボティクス技術の導入と産業化を共に前進させましょう。


## ☎ お問い合わせ
- **オープンソース進捗 & 技術サポート**-Yaohui: yaohui.zhu@seeed.cc
- **今後の協業 & カスタマイズ**-Elaine: elaine.wu@seeed.cc
