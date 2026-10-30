# 🤖 reBot DevArm オープンソースハードウェア仕様書

<p align="center">
  <img src="../../media/v1.1.png" alt="reBot-DevArm バナー">
</p>
<p align="center">
  <strong>
    <a href="./readme_zh.md">简体中文</a> &nbsp;|&nbsp;
    <a href="./readme.md">English</a> &nbsp;|&nbsp;
    <a href="./readme_jp.md">日本語</a>&nbsp;|&nbsp;
    <a href="./readme_fr.md">français</a>&nbsp;|&nbsp;
    <a href="./readme_es.md">Español</a>
  </strong>
</p>

| 日付 | バージョン | ファイル名 | 変更履歴 |
|----------|------|----------|------|
| 2026-03-31 | v1.0 | reBot_B601_DM_v1.0_20260331.step | 初回アップロード |
| 2026-04-15 | v1.1 | reBot_B601_DM_v1.1_20260415.step | エンドジョイント3つのモーターにケーブル拘束を追加し、緩みや外れを防止。ジョイント1のモデルを4310から4340Pに修正。ベース剛性を高めるため、底部にCNCパーツ 02_Base_Reinforcement_Part.step を追加。 |
| 2026-10-30 | v1.1 | reBot_B601_DM_v1.1_20260625.step | ワイヤーハーネスをすべて金型成形による高品質なカスタムハーネスに交換。前腕と手首の2つの3Dプリント製ブラケットの内部を微調整し、ケーブルが穴位置を通過できるようにしました。 |

このBOMは、大疆43シリーズモーターを使用する reBot Arm B601 DM ロボットアーム用です。もう一方のバージョンである reBot Arm B601 RS は RobStride モーターを使用しています。[BOMはこちら](../reBot_B601_RS/README.md)をご覧ください。

# 📦 ファイル構成
*   3D_Printed_Parts/: すべての3Dプリント部品のStepファイル。
*   Metal_Parts/: すべてのCNC加工金属部品のStepファイル。
*   Purchased_Parts/: すべての購入部品のStepファイル。
*   reBot_B601_DM_v1.1_20260625.step: ロボットアームのフルアセンブリファイル（現行版）。

# 🛒[全部品を入手](https://www.seeedstudio.com/reBot-Arm-B601-DM-Bundle.html)
- 5種類のキットオプションを提供しています：
  - **アームボディモーターキット**: ロボットアーム用のモーターと配線ハーネスのみを含む。
  - **アームボディ構造キット**: 機械的構造部品のみを含む。
  - **グリッパーコンプリートキット**: グリッパー用のモーター、配線ハーネス、構造部品を含む。
  - **フルキット**: ロボットアーム本体とグリッパーの完全なセットを含む。
  - **組立済みロボットアーム**: 完全に組み立てられた完成品のロボットアーム。

# 📊 部品表 (BOM)

> [!WARNING]
> 宣言: 公開されているBOMは、Seeedからの最終出荷バージョンを**示すものではありません**。このオープンソースv1.1は、開発者が最小コストで再現できるように最適化されており、一部の必須でない詳細は簡略化されています。
> Seeedの最終生産バージョンには、誤動作防止のための金属レーザー刻印、耐久性のために一部の3Dプリント部品を金属に置き換え、工場でのばらつきに対応するためのクリアランスと加工公差の調整（精度とコストのバランス）、および追加コストでのカスタム配線（例：組み紐スリーブ保護）が含まれます。ただし、機械的構造は同一です。

---

## 🖨️ 3Dプリント部品

| 部品説明 | 画像 | ファイル名 | 材料 | 数量 | 注記 |
|----------|------|--------|------|----------|------|
| ロボットアームベースプラットフォーム | <img src="./3D_Printed_Parts/images/02-BASE.png" width="80"> | 01_BASE_Plate.step | Bambu ABS Black | 1 | 0.4mmノズル、0.2mmレイヤー高さ、30%インフィル |
| ロボットアームベースリンク | <img src="./3D_Printed_Parts/images/02-BASE_02.png" width="80"> | 01_BASE_Link.step | Bambu ABS Black | 1 | 0.4mmノズル、0.2mmレイヤー高さ、30%インフィル |
| 上アーム左フィラー | <img src="./3D_Printed_Parts/images/02-DOWN_TRIM_1.png" width="80"> | 01_Upper_Arm_Fuller_L.step | Bambu PLA Black & Green | 1 | 0.4mmノズル、0.2mmレイヤー高さ、15%インフィル |
| 上アーム右フィラー | <img src="./3D_Printed_Parts/images/02-DOWN_TRIM_2.png" width="80"> | 01_Upper_Arm_Fuller_R.step | Bambu PLA Black & Green | 1 | 0.4mmノズル、0.2mmレイヤー高さ、15%インフィル |
| 上アーム中央フィラー | <img src="./3D_Printed_Parts/images/02-DOWN-FILLING.png" width="80"> | 01_Upper_Arm_Fuller_M.step | Bambu ABS Black | 1 | 0.4mmノズル、0.2mmレイヤー高さ、30%インフィル |
| 上アーム水平リミットブロック | <img src="./3D_Printed_Parts/images/02-SPACER-DOWN.png" width="80"> | 01_Upper_Arm_Limit.step | Bambu ABS Black | 1 | 0.4mmノズル、0.2mmレイヤー高さ、30%インフィル |
| アームハンドル | <img src="./3D_Printed_Parts/images/02-HANDLE.png" width="80"> | 01_Arm_Handle.step | Bambu ABS Black | 1 | 0.4mmノズル、0.2mmレイヤー高さ、30%インフィル |
| 下アーム左フィラー | <img src="./3D_Printed_Parts/images/02-UP-TRIM_1.png" width="80"> | 01_Lower_Arm_Filler_L.step | Bambu PLA Black & Green | 1 | 0.4mmノズル、0.2mmレイヤー高さ、15%インフィル |
| 下アーム右フィラー | <img src="./3D_Printed_Parts/images/02-UP-TRIM_2.png" width="80"> | 01_Lower_Arm_Filler_R.step | Bambu PLA Black & Green | 1 | 0.4mmノズル、0.2mmレイヤー高さ、15%インフィル |
| 下アーム中央フィラー | <img src="./3D_Printed_Parts/images/02-UP-FILLING.png" width="80"> | 01_Lower_Arm_Filler_M.step | Bambu ABS Black | 1 | 0.4mmノズル、0.2mmレイヤー高さ、30%インフィル |
| 上アームカバー | <img src="./3D_Printed_Parts/images/02-DOWN-COVER.png" width="80"> | 01_Upper_Arm_Cover.step | Bambu PLA Green | 1 | 0.4mmノズル、0.2mmレイヤー高さ、15%インフィル |
| 下アームカバー | <img src="./3D_Printed_Parts/images/02-UP-COVER.png" width="80"> | 01_Lower_Arm_Cover.step | Bambu PLA Green | 1 | 0.4mmノズル、0.2mmレイヤー高さ、15%インフィル |
| モーター5保護カバー | <img src="./3D_Printed_Parts/images/02-MOTOR-COVER.png" width="80"> | 01_Motor_Cover.step | Bambu ABS Black | 1 | 0.4mmノズル、0.2mmレイヤー高さ、30%インフィル |
| グリッパー水平リミット | <img src="./3D_Printed_Parts/images/02-SPACER.png" width="80"> | 01_Lower_Arm_Limit.step | Bambu PLA Green | 1 | 0.4mmノズル、0.2mmレイヤー高さ、15%インフィル |
| グリッパースライダーサポートブラケット | <img src="./3D_Printed_Parts/images/02-3D-RAIL-BRACKET.png" width="80"> | 01-Rail-Bracket.step | Bambu PLA Green | 1 | 0.4mmノズル、0.2mmレイヤー高さ、15%インフィル |
| グリッパーフィンガー | <img src="./3D_Printed_Parts/images/02-CLIP_1.png" width="80"> | 01_Finger.step | Bambu ABS Black | 2 | 0.4mmノズル、0.2mmレイヤー高さ、45%インフィル |
| モーター5 ケーブル拘束 | <img src="./3D_Printed_Parts/images/01_Joint5_Cable Restraint_A.png" width="80"> | 01_Joint5_Cable Restraint_A.step | Bambu PLA Green | 1 | 0.4mmノズル、0.2mmレイヤー高さ、15%インフィル |
| モーター6＆7 ケーブル拘束 A | <img src="./3D_Printed_Parts/images/01_Joint6_7_Cable Restraint_A.png" width="80"> | 01_Joint6_7_Cable Restraint_A.step | Bambu ABS Black | 2 | 0.4mmノズル、0.2mmレイヤー高さ、30%インフィル |
| モーター6＆7 ケーブル拘束 B | <img src="./3D_Printed_Parts/images/01_Joint6_7_Cable Restraint_B.png" width="80"> | 01_Joint6_7_Cable Restraint_B.step | Bambu ABS Black | 2 | 0.4mmノズル、0.2mmレイヤー高さ、30%インフィル |
| - | 参考価格 | 平均 **50$** | | | 材料費と印刷時間により価格変動 |


配線ハーネス1を長期間引き回して使用すると、モーター側コネクタが摩耗し、接触不良が発生する可能性があります。
下記の部品を3Dプリンタで造形することで、この不具合リスクを抑えられます。

| 部品詳細 | 画像 | ファイル名 | 材質 | 個数 | 備考 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 1号モーター両面用配線ハーネスクリップ | <img src="./3D_Printed_Parts/images/DM_Motor1_wiring_harness_clip.jpg" width="80"> | `DM_Motor1_wiring_harness_clip.stp` | Bambu Lab 黒ABS樹脂 | 2個 | ノズル径0.4mm、積層ピッチ0.2mm、充填率30% |


## 📷 対応カメラマウント

| 部品説明 | 画像 | ファイル名 | 材料 | 数量 | 注記 |
|----------|------|--------|------|----------|------|
| [Orbbec Gemini2](https://www.seeedstudio.com/Orbbec-Gemini-2-3D-Camera-p-6464.html) | <img src="./3D_Printed_Parts/images/Gemini2_mount.png" width="80"> | [`D435_Gemini2_Mount.step`](../camera-mounts/b601-camera-mounts/D435_Gemini2_Mount.step) | Bambu ABS Black | 1 | 0.4mmノズル、0.2mmレイヤー高さ、30%インフィル |

B601 の手首カメラマウントは **B601-RS と B601-DM で共通**です。モデル、プレビュー、ダウンロードは[共通カメラマウント一覧（英語）](../camera-mounts/README.md)をご覧ください。

### 🧩 印刷推奨事項
- レイヤー高さ: 0.2 mm
- ノズル: 0.4 mm
- サポート: 必要に応じて追加
- 材料: 高温・耐荷重部品にはABS（インフィル30～80%）、ナイロンまたはカーボン繊維強化材料も可。外装部品にはPLA（インフィル15%）。
- 耐荷重部品の推奨材料：

---

## 🔩 CNC加工金属部品

> [!WARNING]
> 注記に記載されている一部の部品は3Dプリントに置き換え可能で、コストを大幅に削減できます。

| 部品説明 | 画像 | ファイル名 | 材料 | 数量 | 加工 | 注記 |
|----------|------|--------|----------|------|------|------|
| モーター1 ベアリングマウント | <img src="./Metal_Parts/images/02_Base_Reinforcement_Part.png" width="80"> | 02_Base_Reinforcement_Part.step | アルミニウム合金 5052 | 1 | CNC | コスト削減のため、高インフィルABSで3Dプリント可能 |
| モーター1 回転軸 | <img src="./Metal_Parts/images/02_Arm_Yaw_Limit.png" width="80"> | 02_Arm_Yaw_Limit.step | アルミニウム合金 5052 | 1 | CNC | ヨー角運動制限を追加 |
| モーター2–5 フロントスペーサー | <img src="./Metal_Parts/images/02_Motor_Front_Spacer.png" width="80"> | 02_Motor_Front_Spacer.step | アルミニウム合金 5052 | 4 | CNC | ABS、インフィル30%で3Dプリント可能 |
| モーター2–4 リアスペーサー | <img src="./Metal_Parts/images/02_Motor_Back_Spacer.png" width="80"> | 02_Motor_Back_Spacer.step | アルミニウム合金 5052 | 3 | CNC | |
| モーター2–4 リアフランジ | <img src="./Metal_Parts/images/02_FLANGE.png" width="80"> | 02_FLANGE.step | アルミニウム合金 5052 | 3 | CNC | |
| 手首モーター5 ブラケット | <img src="./Metal_Parts/images/02_Wrist_Bracket.png" width="80"> | 02_Wrist_Bracket.step | アルミニウム合金 5052 | 1 | CNC | |
| グリッパーコネクタ A | <img src="./Metal_Parts/images/02_Gripper_Connector_A.png" width="80"> | 02_Gripper_Connector_A.step | アルミニウム合金 5052 | 1 | CNC | |
| グリッパーコネクタ B | <img src="./Metal_Parts/images/02_Gripper_Connector_B.png" width="80"> | 02_Gripper_Connector_B.step | アルミニウム合金 5052 | 1 | CNC | |
| グリッパースライダー金属ブラケット | <img src="./Metal_Parts/images/02_Slider_Bracket.png" width="80"> | 02_Slider_Bracket.step | アルミニウム合金 5052 | 1 | CNC | 高インフィルABSで3Dプリント可能だが、長期使用は非推奨 |
| スライダーからグリッパーへの延長部 | <img src="./Metal_Parts/images/02_Slider_Extension.png" width="80"> | 02_Slider_Extension.step | アルミニウム合金 5052 | 2 | CNC | |
| 上下アームリンク左 | <img src="./Metal_Parts/images/02_Lower_Upper_Link_L.png" width="80"> | 02_Lower_Upper_Link_L.step | アルミニウム合金 5052 | 1 | CNC | |
| 上下アームリンク右 | <img src="./Metal_Parts/images/02_Lower_Upper_Link_R.png" width="80"> | 02_Lower_Upper_Link_R.step | アルミニウム合金 5052 | 1 | CNC | |
| 下アーム-手首リンク左 | <img src="./Metal_Parts/images/02_Lower_Wrist_Link_L.png" width="80"> | 02_Lower_Wrist_Link_L.step | アルミニウム合金 5052 | 1 | CNC | |
| 下アーム-手首リンク右 | <img src="./Metal_Parts/images/02_Lower_Wrist_Link_R.png" width="80"> | 02_Lower_Wrist_Link_R.step | アルミニウム合金 5052 | 1 | CNC | |
| ギアコネクタ | <img src="./Metal_Parts/images/02_Gear_Connector.png" width="80"> | 02_Gear_Connector.step | アルミニウム合金 5052 | 1 | CNC | |
| ラック | <img src="./Metal_Parts/images/Rack.png" width="80"> | 02_Rack.step | アルミニウム合金 5052 | 2 | CNC | |
| リンク 1 | <img src="./Metal_Parts/images/Link1.png" width="80"> | 03_Link1.step | アルミニウム合金 5052 | 1 | CNC + 板金 | |
| リンク 2 | <img src="./Metal_Parts/images/Link2.png" width="80"> | 03_Link2.step | アルミニウム合金 5052 | 2 | CNC + 板金 | |
| リンク 3 左 | <img src="./Metal_Parts/images/Link3_L.png" width="80"> | 03_Link3_L.step | アルミニウム合金 5052 | 1 | CNC + 板金 | |
| リンク 3 右 | <img src="./Metal_Parts/images/Link3_R.png" width="80"> | 03_Link3_R.step | アルミニウム合金 5052 | 1 | CNC + 板金 | |
| リンク 5 | <img src="./Metal_Parts/images/Link5.png" width="80"> | 03_Link5.step | アルミニウム合金 5052 | 1 | CNC + 板金 | |
| - | 市場参考価格 | 平均 **250$** | | | アルミニウムコスト、公差要件、納期により価格変動 |

### 🧩 加工仕様
- 主要寸法公差: ±0.02 mm GB/T1840-M
- 表面仕上げ: アルマイト / サンドブラスト
- 嵌合部品推奨: H7 / インターフェリンスフィット
---

## 🛒 購入部品 (標準部品)

> [!WARNING]
> 組み立て・ネジ締めはご自身で行っていただく必要があるため、標準的な六角穴付きネジを選択しています。長時間の動作後、ネジが緩み、ロボットアームの精度に影響を与える可能性があります。そのため、各ジョイントのネジにネジロックを行うためのホットメルト接着剤を別途購入する必要があります。

電動ドリルなどの工具をお持ちの場合は、代わりにロックワッシャーやネジロック剤付きネジを購入しても構いません。ただし、電動ドライバーを使用する際は**非常に重要なこと**ですが、ネジ山をなめないように最も低いトルク設定を使用してください。ネジ山をなめると、元に戻せない損傷が発生します。

| 名前 | 仕様 / モデル | 数量 | 参考価格 | 注記 |
|------|----------|------|----------|------|
| ブラシレスモーター | DM4310(V4) | 4 | 120 $/unit | [SeeedStudio](https://www.seeedstudio.com/Damiao-4310-Actuator-Motor-p-6823.html) |
| ブラシレスモーター | DM4340P(V4) | 3 | 175 $/unit | [SeeedStudio](https://www.seeedstudio.com/DM4340P-Actuator-p-6663.html) |
| CAN-USBドライバーボード | | 1 | 15 $/unit | [SeeedStudio](https://www.seeedstudio.com/DM-CAN-USB-Driver-Borad-p-6706.html) |
| ベアリング | 6707ZZ | 1 | 13 $/unit | [Amazon](https://www.amazon.com/uxcell-35x44x5mm-Shielded-Precision-Lubricated/dp/B0D6WBMW3F/ref=sr_1_1) |
| ベアリング | 6803ZZ | 3 | 13 $/unit | [Amazon](https://www.amazon.com/uxcell-17x26x5mm-Shielded-Precision-Lubricated/dp/B0D54JSWBZ/ref=sr_1_1) |
| ベアリング | AXK5578 | 1 | 12 $/unit | [Amazon](https://www.amazon.com/PZRT-AXK5578-Thrust-Bearings-Washers/dp/B0B3M3RZGW/ref=sr_1_1) |
| リニアレール | MGN9-170mm | 1 | 23 $/unit | [Amazon](https://www.amazon.com/uxcell-Sliding-Carriage-Bearing-Printers/dp/B0D54L45WM/ref=sr_1_1) |
| スライダーブロック | MGN9 | 2 | 10 $/unit | [Amazon](https://www.amazon.com/uxcell-Bearing-Sliding-Carriage-Anti-Fall/dp/B0D9QBQDKB/ref=sr_1_8) |
| ギア | モジュール1、ボス型、16歯、ボア6mm | 1 | 44$/unit | [Amazon](https://www.amazon.com/Module-15-Teeth-Finished-Perforation/dp/B0GDSR1LKM/ref=sr_1_1) |
| シリコンパッド | 30x9x2mm | 1 | 10 $ | [Amazon](https://www.amazon.com/Self-Adhesive-Anti-Sliding-Anti-Scratch-Protectors-Appliances/dp/B0F9KVYXFZ/ref=sr_1_3) |
| ネジ | HM3-12mm ネジ | 14+ | | [Amazon](https://www.amazon.com/BNUOK-120pcs-Stainless-Threads-Spanner/dp/B0DJQGMQZM/ref=sr_1_4) |
| ネジ | HM3-25mm ネジ | 14+ | | [Amazon](https://www.amazon.com/BNUOK-120pcs-Stainless-Threads-Spanner/dp/B0DJQFGRPQ/ref=sr_1_4) |
| ネジ | HM3-6mm ネジ | 16+ | | [Amazon](https://www.amazon.com/BNUOK-120pcs-Stainless-Threads-Spanner/dp/B0DJQG5YLF/ref=sr_1_4) |
| ネジ | HM4-75mm 止めネジ | 4+ | | [Amazon](https://www.amazon.com/iexcell-Partially-Threaded-Thread-Socket/dp/B0DR1NX178/ref=sr_1_1) |
| ネジ | KM3*12mm ネジ | 30+ | | [Amazon](https://www.amazon.com/Uxcell-a16011300ux0872-M3x12mm-Carbon-Countersunk/dp/B01E6EIC2S/ref=sr_1_1) |
| ネジ | KM3*16mm ネジ | 34+ | | [Amazon](https://www.amazon.com/Uxcell-a16011300ux0872-M3x12mm-Carbon-Countersunk/dp/B01E6EIC2S/ref=sr_1_1) |
| ネジ | KM3*7mm ネジ | 76+ | | [Amazon](https://www.amazon.com/Uxcell-a16011300ux0872-M3x12mm-Carbon-Countersunk/dp/B01E6EIC2S/ref=sr_1_1) |
| ネジ | KM3*9mm ネジ | 31+ | | [Amazon](https://www.amazon.com/Uxcell-a16011300ux0872-M3x12mm-Carbon-Countersunk/dp/B01E6EIC2S/ref=sr_1_1) |
| ネジ | KM3*8mm マイクロプロファイル六角穴付きネジ | 31+ | | [Amazon](https://www.amazon.com/SMALLRIG-Screw-Screws-12pcs-Pack/dp/B01MS60KSY/ref=sr_1_1) |
| ネジ | KA3*12mm | 72+ | | [Amazon](https://www.amazon.com/uxcell-Phillips-Tapping-Screws-Silver/dp/B01MXSS95N/ref=sr_1_3) |
| 位置決めピン | M4*8mm | 数本 | | [Amazon](https://www.amazon.com/HARFINGTON-Stainless-Cylindrical-Furniture-Installation/dp/B0F6CWL4MP/ref=sr_1_6) |
| 位置決めピン | M4*12mm | 数本 | | [Amazon](https://www.amazon.com/HARFINGTON-Stainless-Cylindrical-Furniture-Installation/dp/B0F6CWL4MP/ref=sr_1_6) |
| ドライバーセット | 六角レンチセット | 1 | 16$ | [Amazon](https://www.amazon.com/Amazon-Basics-Ratcheting-Electronics-Screwdriver/dp/B07V4TFWFZ/ref=sr_1_2) |
| <img src="./Purchased_Parts/XT30_2+2.png" width="80"> | XT30 2+2 350mm | 2 | 4 $/cable | 両端アングル |
| <img src="./Purchased_Parts/XT30_2+2.png" width="80"> | XT30 2+2 350mm | 1 | 4 $/cable | 一端アングル、一端ストレート |
| <img src="./Purchased_Parts/XT30_2+2.png" width="80"> | XT30 2+2 200mm | 3 | 4 $/cable | 両端アングル |
| <img src="./Purchased_Parts/XT30_2+2.png" width="80"> | XT30 2+2 200mm | 1 | 3 $/cable | 両端ストレート |

### 固定方法について
付属の3Dプリント部品を基に、土台を自由に加工していただけます。机の天板の厚さに合わせて、Gクランプを使用することも可能です。

| 名称 | 仕様/型式 | 数量 | 参考価格 | 備考 |
|------|----------|------|----------|------|
| 木工用クランプ | 6インチ Gクランプ | 2個 | 1個あたり20ドル | [Amazon](https://www.amazon.com/gp/aw/d/B092J1YW2M/?_encoding=UTF8&pd_rd_plhdr=t&aaxitk=3557c048ce58e7dbb50b40c3af69f1d6&hsa_cr_id=0&qid=1774772748&sr=1-1-9e67e56a-6f64-441f-a281-df67fc737124&ref_=sbx_s_sparkle_sbtcd_asin_0_img&pd_rd_w=bNqtC&content-id=amzn1.sym.2fb72bc8-96ef-420d-b08f-c04b69f36507%3Aamzn1.sym.2fb72bc8-96ef-420d-b08f-c04b69f36507&pf_rd_p=2fb72bc8-96ef-420d-b08f-c04b69f36507&pf_rd_r=KDCPNZRHFWEWBWVHWSTR&pd_rd_wg=sBvfF&pd_rd_r=52b946ee-46e2-4e74-86ee-99e291552e44) |

### 電源について
本ロボットアームは標準で電源が付属しておりません。お手持ちのバッテリーを接続するか、台湾製の信頼性の高い**24V 14.6A MeanWell製電源**を別途ご購入ください。
加えて、現地基準に適合した3ピンプラグ、及びXT30メスコネクタ付き配線ハーネスもご用意いただく必要があります。

#### 消耗品BOM

| 名称 | 仕様 | 数量 | 参考価格 | 備考 | 画像 |
|:---|:---|:---:|:---:|:---|:---:|
| 電源装置 | LRS-350-24 (24V 14.6A) | 1 | 27.35ドル | [amazon](https://www.amazon.com/MEAN-WELL-LRS-350-24-350-4W-Switchable/dp/B013ETVO12/ref=sr_1_1?crid=36B2HIB8MM2IT&dib=eyJ2IjoiMSJ9.vpZwmjb4m5KMNcsg2Kb7wr8DDWa-ryUqO5fConlxqlsGoTVB5HN2uBBnRNZI0kcACiaR5DKFiYWvIHLEUN3luZqJAzogeQkeT-fol0m835-oBBWSud1ixkGayrl5nRsF5KMgfvkwAIW949dTTpU2CWdNMrf8g43_vKWaytfX9SHeMJ1hmhS6Kab6fBgER6CgB47K_eEmoJj3KhrjJMtn980osDG-bCLniBcRAHThmXsVRVdpGPsmckGLLyaXrIGRG9plhKI-F7H8hfqW7vzGbwIV_bF8cFtRjdRm5Shtb0o.ekLYD0hsc1Uzji4qKl0Q0USpDTr92JEMQobBXl9lYD0&dib_tag=se&keywords=LRS-350-24&qid=1780021690&s=industrial&sprefix=lrs-350-24%2Cindustrial%2C696&sr=1-1&th=1) | <img src="./Purchased_Parts/LRS-350-24.png" width="80"> |
| 電源コード | 米国規格ACケーブル | 1 | 4.49ドル | [amazon](https://www.amazon.com/LIFEPOE-Power-3-3ft-Black-3-Prong/dp/B0FK4KPW2G/ref=sr_1_1?crid=2W5766PT8EOKA&dib=eyJ2IjoiMSJ9.7E5s-9-Zh-jJAdni-17Iyt1Mr3GJD6hMt9pfk-0S5YxZtknZik9OiePitwUom0pYUbePRpdqa0dCZtGUjluQDEJbSDePHCGvBV6bwQU7wfwd0Loo4WJJmH_2CM1KRKSPcxHXRH0i1i5yuy4g7fDxxn3nPGYU3aF00m5jiIkMfYFgOxH4yURjjZeTMZAIO9wiVQUsPrlM51UIgpPo2YYdCQVUsxjumSsTAm0Jpt2SsBEdT-QzXSIKpLSvQ6kGijXF-4ZevaxiShJdmwU8t2LobDLcalXEOl3lriZTGhjwxow.r0oBabUkGwewhvO3IKlBMULdhUSe6yNTsjfFUaBsjyU&dib_tag=se&keywords=US%2BStandard%2BAC%2BCable%3B%2B1.5m%2B-%2B3%2B*%2B1.5mm%C2%B2&nsdOptOutParam=true&qid=1780021862&s=industrial&sprefix=lrs-350-24%2Cindustrial%2C387&sr=1-1&th=1) | <img src="./Purchased_Parts/US Standard AC Cable.png" width="80"> |
| 出力ポート | XT60E 固定メスコネクタ／XT60E メス＋圧着端子 - 10cm／端子穴 4mm | 1 | 9.99ドル | [amazon](https://www.amazon.com/LINSYRC-XT60E-F-Connector-Battery-Quadcopter/dp/B0CQK1P1DP/ref=pd_sbs_d_sccl_1_2/133-3898271-3474923?pd_rd_w=FmCVA&content-id=amzn1.sym.aa738fbd-ad05-4d11-aae2-04b598db6305&pf_rd_p=aa738fbd-ad05-4d11-aae2-04b598db6305&pf_rd_r=03QM0MRVZA968N9X6X6E&pd_rd_wg=WOZ9q&pd_rd_r=6e0577d2-de73-4427-affd-a271808e1453&pd_rd_i=B0CQK1P1DP&psc=1) | <img src="./Purchased_Parts/XT60E Female to Copper Lug Pigtail.png" width="80"> |
| AC電源配線 | 1.5mm²、赤・青・黄 各1本（端子はご自身で圧着してください。圧着済みリード線は付属しません）、10cm | 3 | 0.99ドル | [aliexpress](https://www.aliexpress.com/item/1005008648016252.html?spm=a2g0o.productlist.main.2.15c9ZpluZpluHP&algo_pvid=09efee83-d80c-4ece-b588-3b1ef73279a3&algo_exp_id=09efee83-d80c-4ece-b588-3b1ef73279a3-1&pdp_ext_f=%7B%22order%22%3A%22230%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21USD%213.58%210.99%21%21%2124.09%216.65%21%400b0b305117800339070873795e0f3d%2112000046086542230%21sea%21US%216593543849%21ABX%211%210%21n_tag%3A-29910%3Bd%3A518b3f9d%3Bm03_new_user%3A-29895%3BpisId%3A5000000207178484&curPageLogUid=74aJ9L7lm7hs&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005008648016252%7C_p_origin_prod%3A&gatewayAdapt=4itemAdapt) | <img src="./Purchased_Parts/RV Grounding Wire Coil with Y-Terminal Lugs.png" width="80"> |
| 三合一 IEC インレットソケット | 赤色スイッチ付きクイックコネクトタイプ（ダブルナット） | 1 | 1.98ドル | [aliexpress](https://www.aliexpress.com/item/1005005962021242.html?spm=a2g0o.imagesearchproductlist.main.17.7db7cZZdcZZdCY&algo_pvid=270b0987-1973-41ad-a2b9-6fe008f9edb5&algo_exp_id=270b0987-1973-41ad-a2b9-6fe008f9edb5&pdp_ext_f=%7B%22order%22%3A%22346%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21USD%213.31%211.98%21%21%2122.30%2113.35%21%400b0b305117800327806706342e118f%2112000035062406338%21sea%21US%216593543849%21ABX%211%210%21n_tag%3A-29910%3Bd%3A518b3f9d%3Bm03_new_user%3A-29895%3BpisId%3A5000000204886261&curPageLogUid=87JUDbPbch2i&utparam-url=scene%3Aimage_search%7Cquery_from%3Apc_web_image_search%7Cx_object_id%3A1005005962021242%7C_p_origin_prod%3A) | <img src="./Purchased_Parts/3-in-1 IEC Inlet Socket.png" width="80"> |
| XT30-XT60 変換ケーブル | XT30U メス - XT60 オス | 1 | 8.99ドル | [amazon](https://www.amazon.com/dp/B0BY8PSHK6?th=1) | <img src="./Purchased_Parts/XT30U_female_to_XT60_male.png" width="80"> |
| 304ステンレス 十字穴付き皿ねじ | M4x6 | 6 | 0.37ドル | / | / |
| 304ステンレス 十字穴付き皿ねじ | M3x8 | 2 | 0.36ドル | / | / |
| 304ステンレス 十字穴付きなべねじ | M3x8 | 2 | 0.32ドル | / | / |
| 六角ナット | M3x2.5 | 2 | 2.10 CNY | / | / |


#### プリント部品BOM

| 名称 | 画像 | 数量 | 備考 |
|:---|:---|:---:|:---|
| [フロントカバー](./3D_Printed_Parts/DM-power-Top%20Cover.stp) | <img src="./3D_Printed_Parts/images/DM-power-Top Cover.png" width="80"> | 1 | PLA、0.4mmノズル、0.2mmレイヤー高さ、30%インフィル |
| [リアカバー](./3D_Printed_Parts/DM-power-Bottom%20Cover.stp) | <img src="./3D_Printed_Parts/images/DM-power-Bottom Cover.png" width="80"> | 1 | PLA、0.4mmノズル、0.2mmレイヤー高さ、30%インフィル |
| [フロントカバー スライドカバー](./3D_Printed_Parts/DM-power-Top%20Cover-Sliding%20Cover.stp) | <img src="./3D_Printed_Parts/images/DM-power-Top Cover-Sliding Cover.png" width="80"> | 1 | PLA、0.4mmノズル、0.2mmレイヤー高さ、30%インフィル |

#### 電源の組み立て

電源の組み立ては、フロントカバーとリアカバーの二つの工程に分かれます。

##### 1. フロントカバーの組み立て

| Step | 操作手順 | 画像 | 備考 |
|:---:|---|---|---|
| 1-1 | フロントカバーの組み立てに必要な部品とプリント部品を準備する | <img src="./Assembly_Steps/powerstep_images/1-1.png" width="80"> | 部品がすべて揃っているか確認してください |
| 1-2 | 各部品の結線順序の説明。結線順序に従って組み立てる | <img src="./Assembly_Steps/powerstep_images/1-2(1).png" width="80" style="margin-right:4%;"><img src="./Assembly_Steps/powerstep_images/1-2(2).png" width="80"><br><img src="./Assembly_Steps/powerstep_images/1-2(3).png" width="80"> | 必ず結線順序どおりに接続してください |
| 1-3 | XT60 コネクタを取り付ける | <img src="./Assembly_Steps/powerstep_images/1-3(1).png" width="80" style="margin-right:4%;"><img src="./Assembly_Steps/powerstep_images/1-3(2).png" width="80"> | 304ステンレス十字穴付き皿ねじ M3x8 と六角ナット M3x2.5 で固定します |
| 1-4 | 三合一 IEC ソケットを取り付ける | <img src="./Assembly_Steps/powerstep_images/1-4(1).png" width="80" style="margin-right:4%;"><img src="./Assembly_Steps/powerstep_images/1-4(2).png" width="80"> | 三合一 IEC ソケットを304ステンレス十字穴付きなべねじ M3x8 で固定します |
| 1-5 | フロントカバー内部の配線 | <img src="./Assembly_Steps/powerstep_images/1-5(1).png" width="80"><br><img src="./Assembly_Steps/powerstep_images/1-5(2).png" width="80"> | 結線順序図と照らし合わせて接続を確認してください |
| 1-6 | フロントカバーと電源の両側を固定する | <img src="./Assembly_Steps/powerstep_images/1-6(1).png" width="80" style="margin-right:4%;"><img src="./Assembly_Steps/powerstep_images/1-6(2).png" width="80"> | 304ステンレス十字穴付き皿ねじ M4x6 ×2 |
| 1-7 | スライドカバーを取り付ける | <img src="./Assembly_Steps/powerstep_images/1-7(1).png" width="80" style="margin-right:4%;"><img src="./Assembly_Steps/powerstep_images/1-7(2).png" width="80"> | 電源の下側から差し込みます |
| 1-8 | スライドカバーを固定する | <img src="./Assembly_Steps/powerstep_images/1-8.png" width="80"> | 304ステンレス十字穴付き皿ねじ M4x6 ×2 |

---

##### 2. リアカバーの組み立て

| Step | 操作手順 | 画像 | 備考 |
|:---:|---|---|---|
| 2-1 | リアカバーの組み立てに必要な部品とプリント部品を準備する | <img src="./Assembly_Steps/powerstep_images/2-1.png" width="80"> | 付属品がすべて揃っているか確認してください |
| 2-2 | リアカバーと電源を組み合わせる | <img src="./Assembly_Steps/powerstep_images/2-2.png" width="80"> | 位置を合わせてください |
| 2-3 | リアカバーと電源の両側を固定する | <img src="./Assembly_Steps/powerstep_images/2-3(1).png" width="80" style="margin-right:4%;"><img src="./Assembly_Steps/powerstep_images/2-3(2).png" width="80"> | 304ステンレス十字穴付き皿ねじ M4x6 ×2 |

---

##### 3. 組み立て完了

| Step | 操作手順 | 画像 | 備考 |
|:---:|---|---|---|
| 1 | 電源ソリューションの組み立てが完了しました | <img src="./Assembly_Steps/powerstep_images/3.png" width="80"> | すべてのねじが締まっているか確認してください |

---