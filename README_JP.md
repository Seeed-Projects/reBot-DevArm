# 🦾 reBot-DevArm: 全ての開発者のためのオープンソース・ロボットアーム

<p align="center">
  <img src="./media/v2.0.png" alt="reBot-DevArm Banner">
</p>

<p align="center">
    <!-- CC BY-NC-SA 4.0バッジに置き換え、非営利目的であることを明示 -->
    <a href="./LICENSE">
        <img src="https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg" alt="ライセンス: CC BY-NC-SA 4.0">
    </a>
    <img src="https://img.shields.io/badge/Commercial-Contact%20Us-red.svg" alt="yaohui.zhu@seeed.cc">
    <img src="https://img.shields.io/badge/ROS-Noetic%20%7C%20Humble-orange.svg" alt="ROSサポート">
    <img src="https://img.shields.io/badge/Framework-LeRobot-yellow.svg" alt="LeRobot">
    <img src="https://img.shields.io/badge/Framework-Isaac Sim-yellow.svg" alt="LeRobot">
</p>

<p align="center">
  <strong>100%完全オープンソース · 具身智能 (Embodied AI) · ハードウェアとソフトウェアの統合 · 個人/教育利用は無料 · 商用利用は要認可</strong>
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

## 📖 はじめに

**reBot-DevArm** は、具身智能（Embodied AI）の学習障壁を下げるためのロボットアームプロジェクトです。私たちは「真のオープンソース」を重視しており、コードだけでなく、以下を含むすべてを無条件で公開します：
- 🦾 **2つのバージョンのロボットアーム**：同じ外観を持つ **Robostride** 版と **Damiao** 版の2つのオープンソースファイルを提供します。
- 🛠️ **ハードウェア設計図**：板金部品および3Dプリント部品のソースファイル。
- 🔩 **BOMリスト**：ネジ1本に至るまでの詳細な仕様と購入リンク。
- 💻 **ソフトウェアとアルゴリズム**：Python SDK、ROS1/2、Isaac Sim、LeRobotなど。

**⚠️ 注意：本プロジェクトは教育および個人学習の促進を目的としています。すべてのリソースは個人開発者、学生、教育機関に対して完全に無料です。ただし、許可なく商用利用すること（キットの直接販売や商用製品の一部としての利用を含むがこれらに限定されない）は厳禁されています。**

**ハードウェアの性能、精度、安全性の評価がすべて完了した後、無料の商用利用ライセンスを緩和する予定です。**

## ☎ お問い合わせ
- **オープンソースの進捗とテクニカルサポート** - Yaohui: yaohui.zhu@seeed.cc
- **将来の提携とカスタマイズ** - Elaine: elaine.wu@seeed.cc

## 🗺️ ロードマップと進捗状況

> [!WARNING]
> 旧正月休暇のため、多くのサプライヤーや提携企業が業務を停止しており、ロボットアームのサンプルテストの進捗に影響が出ています。オープンソースファイルの公開は、**すべての性能および精度検証が完了した後**に行うため、公開スケジュールは約1ヶ月遅れる見込みです。

私たちは、主流のロボット開発エコシステムへの継続的なメンテナンスと適応に努めています。以下は現在の適応状況とリリースの計画です：

| エコシステム | 状態 | 説明 / 予定時期 | ドキュメント |
| :--- | :---: | :--- | :--- |
| **基本的なモーターの使用** | ✅ 完了 | 基本的なモーションコントロールとAPIのカプセル化 | [Robostride](https://wiki.seeedstudio.com/robstride_control/) [Damiao](https://wiki.seeedstudio.com/damiao_series/)|
| **新バージョン STEP 3D構造 & BOM** | 🚧 進行中 | 新部品のSTEPファイル、コンポーネントBOM、加工部品の参考価格 | [遅延 2026.03] |
| **組み立て動画** | 🚧 進行中 | 詳細な組み立て手順とビデオ | [遅延 2026.03] |
| **ROS2 (Humble)** |⏳ 計画中 | コアドライバー完了、MoveIt2の最適化中 |[予定 2026.04]|
| **LeRobotへの適応** | ⏳ 計画中 | Hugging Face LeRobotトレーニングフレームワークへの適応 | [予定 2026.04]|
| **Pinocchioへの適応** | ⏳ 計画中 | Pinocchioフレームワークへの適応、順/逆運動学および動的重力補償の実装 | [予定 2026.04]|
| **Isaac Sim シミュレーション** | ⏳ 計画中 | USDモデルのインポートとシミュレーションテレオペレーションの実装 | [予定 2026.04]|
| **アルゴリズムの段階的な更新** | ⏳ 計画中 | 主流アルゴリズムの順次更新 | 継続的 |
| **完全無料コースの開始** | ⏳ 計画中 | ステップバイステップのチュートリアル | 継続的 |

---

### 🎓 フルスタック・ロボティクス・エコシステム
reBot-DevArmは単なるロボットアームではなく、ロボット工学の学習コミュニティです。以下の一般的なチュートリアルを無料で共有しています：

#### 🖥️ エッジコンピューティングとマスターコントロール
*   [![Jetson](https://img.shields.io/badge/NVIDIA-reComputer%20Jetson-76B900?style=for-the-badge&logo=nvidia&logoColor=white)](https://wiki.seeedstudio.com/NVIDIA_Jetson/) —— **AI推論と計算コア**
*   [![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-4B%20%2F%205-C51A4A?style=for-the-badge&logo=Raspberry%20Pi&logoColor=white)](https://wiki.seeedstudio.com/raspberry-pi-devices/) —— **一般的なLinux開発環境**
*   [![ESP32](https://img.shields.io/badge/MCU-Seeed%20XIAO%20(ESP32)-0091BD?style=for-the-badge&logo=espressif&logoColor=white)](https://wiki.seeedstudio.com/SeeedStudio_XIAO_Series_Introduction/) —— **低電力ワイヤレス制御ノード**

#### 📡 センサーと周辺機器
*   **🚗 モーターとサーボ**: [Damiao / Gogo / Robstride / Mita / Feite / Fashion Star](https://wiki.seeedstudio.com/robotics_page/)
*   **👁️ 視覚認識**: [深度カメラ / LiDAR / 画像処理アルゴリズム](https://wiki.seeedstudio.com/robotics_page/)
*   **👂 聴覚インタラクション**: [ReSpeaker マイクアレイ / 音声認識](https://wiki.seeedstudio.com/ReSpeaker_Mic_Array_v2.0/)
*   **🧭 動きと姿勢**: [IMU (6軸/9軸) / ジャイロスコープ / 磁気計](https://wiki.seeedstudio.com/Sensor/IMU/)
*   **🤖 総合キット**: [その他のロボティクスセンサーとドライバーの例](https://wiki.seeedstudio.com/robotics_page/)

> 👉 **[Wikiナレッジベースはこちらをクリック](https://wiki.seeedstudio.com/)** (すべてのチュートリアルを無料で閲覧可能)

---

## ⚙️ ハードウェア仕様

reBot-DevArmは、ペイロード能力と柔軟性のバランスを考慮した、デスクトップ向けの具身智能（Embodied AI）アプリケーション用に設計されています。

| パラメーター | 値 / 説明 |
| :--- | :--- |
| **ペイロード** | **1.5+ kg** |
| **最大リーチ** | **650 mm** |
| **重量** | 約 4.0 kg |
| **繰り返し精度** | < 0.2 mm |
| **自由度 (DOF)** | 6 DOF + 1 グリッパー (オープンソースのCANサーボグリッパーとジョイントモーターグリッパーを近日公開予定) |
| **サポートされるプラットフォーム/エコシステム** | ROS1, ROS2, LeRobot, Pinocchio, Isaac Sim, Python SDK |
| **供給電圧** | DC 24V |

---

## 📂 オープンソース（ハードウェアソース）

私たちは、ハードウェアのオープンソース化が革新を促進すると信じています。アームの構築に必要なものはすべて以下のディレクトリにあります：

*   [`/hardware/STEP`](./hardware/cad): プリント部品、金属部品、購入品を含むすべての機械構造のSTEP/STLファイル。
*   [`/hardware/bom`](./hardware/bom): **BOMリスト**（購入コンポーネントのモデル、モーターパラメーター、推奨ベンダーを含む）。
*   [`/tutorial/ROS`](./tutorial/ROS/): **ROS1/2 Noetic/Humble** のソースコードとチュートリアル。
*   [`/tutorial/Lerobot`](./tutorial/lerobot/): **LeRobot** のソースコードとチュートリアル。
*   [`/tutorial/Isaac`](./tutorial/Isaac/): **Isaac Sim** のソースコードとチュートリアル。

---

## 🚀 はじめに

開封からAIシミュレーションまで、完全な学習パスを計画しています：

### 🛠️ フェーズ 1: ハードウェア構築と基本
| ステップ | 説明 | リンク |
| :---: | :--- | :--- |
| **01** | **モーターの基本学習** | [Robostride](https://wiki.seeedstudio.com/robstride_control/) [Damiao](https://wiki.seeedstudio.com/damiao_series/)|
| **02** | **開封** | 近日公開 |
| **03** | **組み立てガイド** | 近日公開 |
| **04** | **ゼロ校正** | 近日公開 |
| **05** | **運動学テスト** | 近日公開 |

### 💻 フェーズ 2: 高度なアルゴリズムとシミュレーション
| ステップ | 説明 | リンク |
| :---: | :--- | :--- |
| **06** | **ROSエコシステム** (ROS2) | 🐢 近日公開 |
| **07** | **AIトレーニング** (Hugging Face) | 🤗 近日公開 |
| **08** | **シミュレーション** (NVIDIA) | 🌌 近日公開 |

---

## 🙌 参考文献と謝辞
オープンソースの道は決して孤独ではありません。reBot-DevArmプロジェクトの誕生は、Seeed Studio、世界のオープンソースコミュニティ、および優れたハードウェアパートナーの全面的なサポートなしには不可能でした。私たちは以下のプロジェクトとチームに最高の敬意を表します：

### 🌍 エコシステムとソフトウェアサポート
*   **[Seeed Studio](https://www.seeedstudio.com/)** - 包括的なハードウェアサプライチェーンとテクニカルサポートを提供。
*   **[Hugging Face LeRobot](https://github.com/huggingface/lerobot)** - 優れたエンドツーエンドのロボット学習フレームワーク。
*   **[NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim)** - 強力なロボットシミュレーションおよび合成データプラットフォーム。

### ⚙️ コアハードウェアパートナー
高性能なモーターとアクチュエーターソリューションを提供していただいた以下のメーカーに感謝いたします：
*   **[大喵科技 (Damiao Technology)](https://www.damiaokeji.com/)**
*   **[Robstride](https://robstride.com/)**
*   **[Fashion Star](https://fashionrobo.com/)**

### 💡 インスピレーション
本プロジェクトは、以下の優れたオープンソースプロジェクトから深いインスピレーションを受けています：
*   **[SO-ARM100](https://github.com/TheRobotStudio/SO-ARM100/tree/main)**
*   **[Mobile ALOHA](https://github.com/tonyzhaozh/aloha)**
*   **[Dummy-Robot (Zhihui Jun)](https://github.com/peng-zhihui/Dummy-Robot)**
*   **[OpenArm](https://openarm.dev/)**
*   **[I2RT](https://i2rt.com/)**
*   **[TRLC-DK1](https://github.com/robot-learning-co/trlc-dk1)**

### 🎃 プロトタイプ貢献者
- **SeeedStudio AI Robotics Team**: Yaohui Zhu (yaohui.zhu@seeed.cc)
- **SeeedStudio STU**: Wentao Dong
- **SeeedStudio STU**: Weiwei Xu
- **SeeedStudio 購買部門**: Fengqun Peng

### 👥 貢献者

## 主要な貢献者

<p align="center"><a href="https://github.com/Seeed-Projects/reBot-DevArm/graphs/contributors">
   <img src="https://contributors-img.web.app/image?repo=Seeed-Projects/reBot-DevArm" />
</a></p>

*近日公開... PRの提出を歓迎します！*

## スター履歴

[![Star History Chart](https://api.star-history.com/svg?repos=Seeed-Projects/reBot-DevArm&type=date&legend=top-left)](https://www.star-history.com/#Seeed-Projects/reBot-DevArm&type=date&legend=top-left)

# reBot-DevArm プロジェクトライセンス
Copyright (c) [2025] [Seeed Studio AI Robotics Team]

本作品は **クリエイティブ・コモンズ 表示 - 非営利 - 継承 4.0 国際 ライセンス** の下で提供されています。ライセンスのコピーを確認するには、以下にアクセスしてください：http://creativecommons.org/licenses/by-nc-sa/4.0/

--------------------------------------------------------------------------------

## 権利と制限
1. あなたは自由に：
    - 共有：いかなる媒体や形式でも資料を複製し、再配布できます。
    - 翻案：資料をリミックスし、改変し、その上に構築できます。

2. 以下の条件に従う必要があります：
    - 表示：適切なクレジットを表示し、ライセンスへのリンクを提供し、変更があった場合はその旨を示す必要があります。
    - 非営利：**営利目的で資料を利用することはできません**。
      （明示的な許可なく関連キットを販売すること、プリント部品を販売すること、または本ソフトウェアを有料製品に統合することを含みますが、これらに限定されません）。
    - 継承：資料をリミックスし、改変し、またはその上に構築した場合、あなたの貢献を元の資料と同じライセンスの下で配布する必要があります。

3. 商用認可：
    営利目的で本プロジェクトを利用したい場合は、著者に連絡して商用認可を取得してください。
    連絡先：yaohui.zhu@seeed.cc

