# 🤖 reBot DevArm 开源硬件说明


<p align="center">
  <img src="../../media/v1.1.png" alt="reBot-DevArm Banner">
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


|  日期 | 版本号 | 文件名 | 更新日志 |
|----------|------|----------|------|
|  3.31.2026 | v1.0 |  reBot_B601_DM_v1.0_20260331.step  | 第一次上传 |
|  4.25.2026 | v1.1 |  reBot_B601_DM_v1.1_20260425.step  | 增加了末端3个关节电机的线束卡口`Cable Restraint`，防松防脱落。修复了第一个关节型号`由4310改为4340P`。底部增加了CNC件`02_Base_Reinforcement_Part.step`加强底部强度。增加了线束卡扣。 |
|  10.30.2026 | v1.1 |  reBot_B601_DM_v1.1_20260625.step  | 线束全部更换为开模定制的更高质量线束；小臂与腕部的两个 3D 打印支架内部做了微调，使线束能够穿过孔位。 |


当前BOM为reBot Arm B601 DM机械臂清单，所使用的是Damiao43系列电机，另一款reBot Arm B601 RS机械臂所使用的是RobStride电机，[清单请看这里](../reBot_B601_RS/README.md)

# 📦 文件结构
*   `3D_Printed_Parts/`: 所有3D打印文件的Step。
*   `Metal_Parts/`: 所有金属加工文件的Step。
*   `Purchased_Parts/`: 所有购买件的Step。
*   `reBot_B601_DM_v1.1_20260625.step`：机械臂整体装配文件（当前版本）；`reBot_B601_DM_v1.1_20260425.step` 保留为上一版。

# 📊 物料清单（BOM）

> [!WARNING]
>特此申明，公布的BOM并非代表Seeed出货的最终版本，此`v1.1`开源版本是方便开发者并能够尽可能减少成本自己加工复现的版本,减少了一些不必要的细节开支，Seeed 最终出货版本会有金属镭雕防呆提示，部分3D打印件为了耐久会替换为金属件，根据金属加工厂的误差做间隙和加工精度调整（精度和成本的平衡），线束的特殊定制（例如增加编制绳保护）等需要增加一定成本的细节优化，但是结构构型相同。

---

## 🖨️ 3D打印件

|  零件描述 | 图片 | 文件名 | 材料 | 数量 | 备注 |
|----------|------|--------|------|----------|------|
| 机械臂底座平台 | <img src="./3D_Printed_Parts/images/02-BASE.png" width="80"> | `01_BASE_Plate.step` | 拓竹 ABS 黑色  |  1 |  0.4喷嘴 0.2层高 30%填充 |
| 机械臂底座 | <img src="./3D_Printed_Parts/images/02-BASE_02.png" width="80"> | `01_BASE_Link.step` | 拓竹 ABS 黑色  |  1 |  0.4喷嘴 0.2层高 30%填充 |
| 大臂左侧填充 | <img src="./3D_Printed_Parts/images/02-DOWN_TRIM_1.png" width="80"> | `01_Upper_Arm_Fuller_L.step` | 拓竹 PLA 黑色和绿色  |  1 |  0.4喷嘴 0.2层高 15%填充 |
| 大臂右侧填充 | <img src="./3D_Printed_Parts/images/02-DOWN_TRIM_2.png" width="80"> | `01_Upper_Arm_Fuller_R.step` | 拓竹 PLA 黑色和绿色 |  1 |  0.4喷嘴 0.2层高 15%填充 |
| 大臂中间填充 | <img src="./3D_Printed_Parts/images/02-DOWN-FILLING.png" width="80"> | `01_Upper_Arm_Fuller_M.step` | 拓竹 ABS 黑色  |  1 |  0.4喷嘴 0.2层高 30%填充 |
| 大臂水平限位块 | <img src="./3D_Printed_Parts/images/02-SPACER-DOWN.png" width="80"> | `01_Upper_Arm_Limit.step` |拓竹 ABS 黑色  |  1 |  0.4喷嘴 0.2层高 30%填充 |
| 机械臂提手 | <img src="./3D_Printed_Parts/images/02-HANDLE.png" width="80"> | `01_Arm_Handle.step` |拓竹 ABS 黑色  |  1 |  0.4喷嘴 0.2层高 30%填充 |
| 小臂左侧填充 | <img src="./3D_Printed_Parts/images/02-UP-TRIM_1.png" width="80"> | `01_Lower_Arm_Filler_L.step` |拓竹 PLA 黑色和绿色  |  1 |  0.4喷嘴 0.2层高 15%填充 |
| 小臂右侧填充 | <img src="./3D_Printed_Parts/images/02-UP-TRIM_2.png" width="80"> | `01_Lower_Arm_Filler_R.step` |拓竹 PLA 黑色和绿色  |  1 |  0.4喷嘴 0.2层高 15%填充 |
| 小臂中间填充 | <img src="./3D_Printed_Parts/images/02-UP-FILLING.png" width="80"> | `01_Lower_Arm_Filler_M.step` |拓竹 ABS 黑色  |  1 |  0.4喷嘴 0.2层高 30%填充 |
| 大臂装饰 | <img src="./3D_Printed_Parts/images/02-DOWN-COVER.png" width="80"> | `01_Upper_Arm_Cover.step` |拓竹 PLA 绿色  |  1 |  0.4喷嘴 0.2层高 15%填充 |
| 小臂装饰 | <img src="./3D_Printed_Parts/images/02-UP-COVER.png" width="80"> | `01_Lower_Arm_Cover.step` |拓竹 PLA 绿色  |  1 |  0.4喷嘴 0.2层高 15%填充 |
| 5号电机保护盖 | <img src="./3D_Printed_Parts/images/02-MOTOR-COVER.png" width="80"> | `01_Motor_Cover.step` |拓竹 ABS 黑色  |  1 |  0.4喷嘴 0.2层高 30%填充 |
| 夹爪水平限位 | <img src="./3D_Printed_Parts/images/02-SPACER.png" width="80"> | `01_Lower_Arm_Limit.step` |  拓竹 PLA 绿色  |  1 |  0.4喷嘴 0.2层高 15%填充 |
| 夹爪滑块填充支架 | <img src="./3D_Printed_Parts/images/02-3D-RAIL-BRACKET.png" width="80"> | `01-Rail-Bracket.step` |  拓竹 PLA 绿色  |  1 |  0.4喷嘴 0.2层高 15%填充 |
| 夹爪  | <img src="./3D_Printed_Parts/images/02-CLIP_1.png" width="80"> | `01_Finger.step` |  拓竹 ABS 黑色  |  2 |  0.4喷嘴 0.2层高 45%填充 |
| 电机5线束约束加固 | <img src="./3D_Printed_Parts/images/01_Joint5_Cable Restraint_A.png" width="80"> | `01_Joint5_Cable Restraint_A.step` |  拓竹 PLA 绿色  |  1 |  0.4喷嘴 0.2层高 15%填充 |
| 电机6和7线束约束加固  | <img src="./3D_Printed_Parts/images/01_Joint6_7_Cable Restraint_A.png" width="80"> | `01_Joint6_7_Cable Restraint_A.step` |  拓竹 ABS 黑色  |  2 |  0.4喷嘴 0.2层高 30%填充 |
| 电机6和7线束约束加固  | <img src="./3D_Printed_Parts/images/01_Joint6_7_Cable Restraint_B.png" width="80"> | `01_Joint6_7_Cable Restraint_B.step` |  拓竹 ABS 黑色  |  2 |  0.4喷嘴 0.2层高 30%填充 |
|   | `参考价格` | 平均**350RMB**  | |  | 因打印材料价格、和工厂打印时长不同，价格略有浮动|  |  

长期使用过程中拖拽线束1会磨损电机接口导致接触不良，你可以打印如下文件降低这个风险。
|  零件描述 | 图片 | 文件名 | 材料 | 数量 | 备注 |
|----------|------|--------|------|----------|------|
| 电机1两个面的线束卡扣  | <img src="./3D_Printed_Parts/images/DM_Motor1_wiring_harness_clip.jpg" width="80"> | `DM_Motor1_wiring_harness_clip.stp` |  拓竹 ABS 黑色  |  2 |  0.4喷嘴 0.2层高 30%填充 |


##  📷兼容的相机支架

|  零件描述 | 图片 | 文件名 | 材料 | 数量 | 备注 |
|----------|------|--------|------|----------|------|
| Orbbec Gemini2相机 | <img src="./3D_Printed_Parts/images/Gemini2_mount.png" width="80"> | [`D435_Gemini2_Mount.step`](../camera-mounts/b601-camera-mounts/D435_Gemini2_Mount.step) | 拓竹 ABS 黑色  |  1 |  0.4喷嘴 0.2层高 30%填充 |


B601 腕部相机支架由 **B601-RS 和 B601-DM 通用**。模型、预览图和下载链接统一维护在[摄像头支架资源目录](../camera-mounts/README_zh.md)。

### 🧩 打印建议
- 层高：0.2 mm
- 喷嘴：0.4 mm
- 支撑：按需添加  
- 材料：需要受到高温和一定力的部分使用的是ABS材料并且填充在30%~80%，也可以改为尼龙 / 碳纤增强材料，外观装饰件使用的是PLA，填充15%。
- 受力件建议材料：

---

## 🔩 金属加工件

> [!WARNING]
> 这里部分可用3D打印替代的零件已在备注中表明，可极大进一步降低成本开支。

| 零件描述 | 图片 | 文件名 | 材料 | 数量 |  加工工艺 |  备注 |
|----------|------|--------|----------|------|------|------|
| 电机1轴承安装位 | <img src="./Metal_Parts/images/02_Base_Reinforcement_Part.png" width="80"> | `02_Base_Reinforcement_Part.step` |铝合金5052  | 1 | CNC| 可用3D打印ABS，增加填充来降低成本  | 
| 电机1旋转轴 | <img src="./Metal_Parts/images/02_Arm_Yaw_Limit.png" width="80"> | `02_Arm_Yaw_Limit.step` |铝合金5052  | 1 | CNC| 增加了航向角的运动限位 | 
| 电机2-5的正面垫片 | <img src="./Metal_Parts/images/02_Motor_Front_Spacer.png" width="80"> | `02_Motor_Front_Spacer.step` |铝合金5052  | 4 | CNC| 可用3D打印ABS，30%填充来降低成本 | 
| 电机2-4的背面垫片 | <img src="./Metal_Parts/images/02_Motor_Back_Spacer.png" width="80"> | `02_Motor_Back_Spacer.step` |铝合金5052  | 3 | CNC|  | 
| 电机2-4的背面法兰 | <img src="./Metal_Parts/images/02_FLANGE.png" width="80"> | `02_FLANGE.step` |铝合金5052  | 3 | CNC| | 
| 腕部电机5底座 | <img src="./Metal_Parts/images/02_Wrist_Bracket.png" width="80"> | `02_Wrist_Bracket.step` |铝合金5052  | 1 | CNC|  | 
| 爪子连接器A | <img src="./Metal_Parts/images/02_Gripper_Connector_A.png" width="80"> | `02_Gripper_Connector_A.step` |铝合金5052  | 1 | CNC|  | 
| 爪子连接器B | <img src="./Metal_Parts/images/02_Gripper_Connector_B.png" width="80"> | `02_Gripper_Connector_B.step` |铝合金5052  | 1 | CNC|  | 
| 爪子滑块金属支架 | <img src="./Metal_Parts/images/02_Slider_Bracket.png" width="80"> | `02_Slider_Bracket.step` |铝合金5052  | 1 | CNC|  可用3D打印ABS，增加填充来降低成本，但是不推荐长期使用   | 
| 滑块与爪子连接器 | <img src="./Metal_Parts/images/02_Slider_Extension.png" width="80"> | `02_Slider_Extension.step` |铝合金5052  | 2 | CNC| | 
| 大小臂关节连接件左 | <img src="./Metal_Parts/images/02_Lower_Upper_Link_L.png" width="80"> | `02_Lower_Upper_Link_L.step` |铝合金5052  | 1 | CNC|  | 
| 大小臂关节连接件右 | <img src="./Metal_Parts/images/02_Lower_Upper_Link_R.png" width="80"> | `02_Lower_Upper_Link_R.step` |铝合金5052  | 1 | CNC|  | 
| 小臂与腕关节连接件左 | <img src="./Metal_Parts/images/02_Lower_Wrist_Link_L.png" width="80"> | `02_Lower_Wrist_Link_L.step` |铝合金5052  | 1 | CNC|  | 
| 小臂与腕关节连接件右 | <img src="./Metal_Parts/images/02_Lower_Wrist_Link_R.png" width="80"> | `02_Lower_Wrist_Link_R.step` |铝合金5052  | 1 | CNC| | 
| 齿轮连接器  | <img src="./Metal_Parts/images/02_Gear_Connector.png" width="80"> | `02_Gear_Connector.step` |  铝合金5052  |  1 |  CNC |  |
| 齿条  | <img src="./Metal_Parts/images/Rack.png" width="80"> | `02_Rack.step` |  铝合金5052  |  2 |  CNC |  |
| 连杆1  | <img src="./Metal_Parts/images/Link1.png" width="80"> | `03_Link1.step` |  铝合金5052  |  1 |  CNC+钣金 | |
| 连杆2  | <img src="./Metal_Parts/images/Link2.png" width="80"> | `03_Link2.step` |  铝合金5052  |  2 |  CNC+钣金 |  |
| 连杆3左  | <img src="./Metal_Parts/images/Link3_L.png" width="80"> | `03_Link3_L.step` |  铝合金5052  |  1 |  CNC+钣金 |  |
| 连杆3右  | <img src="./Metal_Parts/images/Link3_R.png" width="80"> | `03_Link3_R.step` |  铝合金5052  |  1 |  CNC+钣金 |  |
| 连杆5  | <img src="./Metal_Parts/images/Link5.png" width="80"> | `03_Link5.step` |  铝合金5052  |  1 |  CNC+钣金 |  |
| 多家市场参考价格  |  | 平均**1500RMB**  | |  | 因铝5052成本浮动、加工精度要求、工厂交期等，价格略有浮动|  |  

### 🧩 加工说明
- 关键尺寸公差：±0.02 mm GB/T1840-M；
- 表面处理：阳极氧化 / 喷砂   
- 配合件建议采用 H7 / 过盈配合  

---

## 🛒 外购件（标准件）

> [!WARNING]
> 考虑到大家需要自己组装拧螺丝，所以选购的螺丝是普通的内六角螺丝，长时间运行后可能会出现螺丝松动从而影响机械臂精度，这里需要大家额外购买热熔胶去对每个关节处的螺丝进行防松操作，如果大家手上有电钻等，可以购买防松螺丝，但是切记使用电动螺丝刀要用最小档的力，防止螺丝滑丝造成无法逆转的损失（非常重要）。


| 名称                                                    | 规格型号           | 数量  | 参考价格    | 备注                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ----------------------------------------------------- | -------------- | --- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 无刷电机                                                  | DM4310(V4)     | 4   | 599 元/颗 | [淘宝](https://item.taobao.com/item.htm?abbucket=16&id=815333472865&mi_id=0000BBduPQSNDe7t7l-kaDZprI2E6kNsYTdnIiwH62i7n_M&ns=1&skuId=5965481553139&spm=a21n57.1.hoverItem.1&utparam=%7B%22aplus_abtest%22%3A%22d4587e8df92c3a52b25c3f2889f2cd86%22%7D&xxc=taobaoSearch)                                                                                                                                                                                                                          |
| 无刷电机                                                  | DM4340P(V4)    | 3   | 899 元/颗 | [淘宝](https://item.taobao.com/item.htm?abbucket=16&id=849494670743&mi_id=0000MPvkz-066vyLlQn2cv859QrngX-Vt0TPNvgPJBW6ax8&ns=1&priceTId=2147830517747671329473705e133c&skuId=6130885315934&spm=a21n57.1.hoverItem.1&utparam=%7B%22aplus_abtest%22%3A%2248ef8bac34ee3e270d4c45e14d20362d%22%7D&xxc=taobaoSearch)                                                                                                                                                                                  |
| CAN-USB驱动板                                            |                | 1   | 60 元/颗  | [淘宝](https://item.taobao.com/item.htm?spm=tbpc.boughtlist.suborder_itemtitle.1.34672e8dbqwe4F&id=815478282425&mi_id=0000QH7PiOe9C0g_Gr_xVT_5DsSwf1LKh7pUf8E29umKozc)                                                                                                                                                                                                                                                                                                                           |
| CAN-电源分离板                                             |                | 1   | 9 元/颗   | [淘宝](https://item.taobao.com/item.htm?spm=tbpc.boughtlist.suborder_itemtitle.1.34672e8dbqwe4F&id=815810342495&mi_id=0000wRC5oAjSpP97L1MdVvbyjhwWx0DIkM7obz-rrRxzNpk)                                                                                                                                                                                                                                                                                                                           |
| 轴承                                                    | 6707ZZ         | 1   | 14.8元/个 | [淘宝](https://item.taobao.com/item.htm?spm=tbpc.boughtlist.suborder_itemtitle.1.34672e8dbqwe4F&id=14242929760&mi_id=0000jmnysQzOgG430JIVTJKYMcTjegmveaBKHKqXECnMNqI)                                                                                                                                                                                                                                                                                                                            |
| 轴承                                                    | 6803ZZ         | 3   | 1.25元/个 | [淘宝](https://item.taobao.com/item.htm?spm=tbpc.boughtlist.suborder_itemtitle.1.34672e8dbqwe4F&id=14777231362&mi_id=0000Qrhc1yLjSnZZ49VXZZ6WRp0tCWSF9c_rwUTyvM3qrJ0)                                                                                                                                                                                                                                                                                                                            |
| 轴承                                                    | AXK5578        | 1   | 17元/个   | [淘宝](https://item.taobao.com/item.htm?spm=tbpc.boughtlist.suborder_itemtitle.1.34672e8dbqwe4F&id=775311326057&mi_id=0000Gs6JGuzFwDcfxC1n_IgT31HEMir7Nux6FQ0MWykWZxk)                                                                                                                                                                                                                                                                                                                           |
| 滑轨                                                    | MGN9-170mm     | 1   | 20元/个   | [淘宝](https://item.taobao.com/item.htm?spm=tbpc.boughtlist.suborder_itemtitle.1.34672e8dbqwe4F&id=709992228016&mi_id=0000SmlMWqGr3-_hhWvTFizH7DX2WGsiXQ5uHqWxuOfW56k)                                                                                                                                                                                                                                                                                                                           |
| 滑块                                                    | MGN9           | 2   | 20元/个   | [淘宝](https://item.taobao.com/item.htm?spm=tbpc.boughtlist.suborder_itemtitle.1.34672e8dbqwe4F&id=709992228016&mi_id=0000SmlMWqGr3-_hhWvTFizH7DX2WGsiXQ5uHqWxuOfW56k)                                                                                                                                                                                                                                                                                                                           |
| 齿轮                                                    | 1模凸台16齿内孔8     | 1个  | 10元     | [淘宝](https://item.taobao.com/item.htm?abbucket=16&id=520920342046&mi_id=0000ndZxSrO0S9kOpXVDMEflCQP9E0X0EOrYRMd0ctZ81vo&ns=1&priceTId=213e004717763169907362571e13c2&skuId=4293928238550&spm=a21n57.1.hoverItem.5&utparam=%7B%22aplus_abtest%22%3A%223c2a09ad537bf188532cdc53e5ecece5%22%7D&xxc=taobaoSearch)                                                                                                                                                                                  |
| 硅胶垫                                                   | 30x9x2mm       | 1个  | 4.6元    | [淘宝](https://item.taobao.com/item.htm?spm=tbpc.boughtlist.suborder_itemtitle.1.34672e8dbqwe4F&id=952654692170&mi_id=00000XvbaL70Ji98nZvHOun9hqfeuNj3O9SK72n39KsHeKg)                                                                                                                                                                                                                                                                                                                           |
| 螺丝                                                    | HM3-12mm螺丝     | 14+ |         | [淘宝](https://detail.tmall.com/item.htm?ali_refid=a3_430673_1006%3A1123480325%3AH%3Ap1yyEEnsxLyF2bElweRCig%3D%3D%3A0f70d2fdc511b0322d752e0a897bdd7f&ali_trackid=282_0f70d2fdc511b0322d752e0a897bdd7f&id=635755541429&loginBonus=1&mi_id=0000eYWK-l9Kna660G1cfaZJF75R_gn1sgAQjFGXQLhzfN4&mm_sceneid=1_0_116096069_0&priceTId=214784bc17719128848504972e13b0&skuId=4551620356171&spm=a21n57.sem.item.1&utparam=%7B%22aplus_abtest%22%3A%2202c560a0a4574762e6fc37b298f739f5%22%7D&xxc=ad_ztc)      |
| 螺丝                                                    | HM3-25mm螺丝     | 14+ |         | [淘宝](https://detail.tmall.com/item.htm?ali_refid=a3_430673_1006%3A1123480325%3AH%3Ap1yyEEnsxLyF2bElweRCig%3D%3D%3A0f70d2fdc511b0322d752e0a897bdd7f&ali_trackid=282_0f70d2fdc511b0322d752e0a897bdd7f&id=635755541429&loginBonus=1&mi_id=0000eYWK-l9Kna660G1cfaZJF75R_gn1sgAQjFGXQLhzfN4&mm_sceneid=1_0_116096069_0&priceTId=214784bc17719128848504972e13b0&skuId=4551620356176&spm=a21n57.sem.item.1&utparam=%7B%22aplus_abtest%22%3A%2202c560a0a4574762e6fc37b298f739f5%22%7D&xxc=ad_ztc)      |
| 螺丝                                                    | HM3-6mm螺丝      | 16+ |         | [淘宝](https://detail.tmall.com/item.htm?ali_refid=a3_430673_1006%3A1123480325%3AH%3Ap1yyEEnsxLyF2bElweRCig%3D%3D%3A0f70d2fdc511b0322d752e0a897bdd7f&ali_trackid=282_0f70d2fdc511b0322d752e0a897bdd7f&id=635755541429&loginBonus=1&mi_id=0000eYWK-l9Kna660G1cfaZJF75R_gn1sgAQjFGXQLhzfN4&mm_sceneid=1_0_116096069_0&priceTId=214784bc17719128848504972e13b0&skuId=5969643827976&spm=a21n57.sem.item.1&utparam=%7B%22aplus_abtest%22%3A%2202c560a0a4574762e6fc37b298f739f5%22%7D&xxc=ad_ztc)      |
| 螺丝                                                    | HM4-75mm螺丝     | 4+  |         | [淘宝](https://detail.tmall.com/item.htm?ali_refid=a3_430673_1006%3A1123480325%3AH%3Ap1yyEEnsxLyF2bElweRCig%3D%3D%3A0f70d2fdc511b0322d752e0a897bdd7f&ali_trackid=282_0f70d2fdc511b0322d752e0a897bdd7f&id=635755541429&loginBonus=1&mi_id=0000eYWK-l9Kna660G1cfaZJF75R_gn1sgAQjFGXQLhzfN4&mm_sceneid=1_0_116096069_0&priceTId=214784bc17719128848504972e13b0&skuId=4969298563959&spm=a21n57.sem.item.1&utparam=%7B%22aplus_abtest%22%3A%2202c560a0a4574762e6fc37b298f739f5%22%7D&xxc=ad_ztc)      |
| 螺丝                                                    | KM3*12mm螺丝     | 30+ |         | [淘宝](https://item.taobao.com/item.htm?abbucket=16&id=613190015864&mi_id=0000VdxIoOlEaJpSrLq2vLlI9zjiVrkuPuOVyvBE36EDPr4&ns=1&priceTId=2150455917750559194186583e1322&skuId=4311239436959&spm=a21n57.1.hoverItem.3&utparam=%7B%22aplus_abtest%22%3A%221f5215bc4932e358d04aa9396324733d%22%7D&xxc=taobaoSearch)                                                                                                                                                                                  |
| 螺丝                                                    | KM3*16mm螺丝     | 34+ |         | [淘宝](https://item.taobao.com/item.htm?abbucket=16&id=613190015864&mi_id=0000VdxIoOlEaJpSrLq2vLlI9zjiVrkuPuOVyvBE36EDPr4&ns=1&priceTId=2150455917750559194186583e1322&skuId=4311239436961&spm=a21n57.1.hoverItem.3&utparam=%7B%22aplus_abtest%22%3A%221f5215bc4932e358d04aa9396324733d%22%7D&xxc=taobaoSearch)                                                                                                                                                                                  |
| 螺丝                                                    | KM3*7mm螺丝      | 76+ |         | [淘宝](https://item.taobao.com/item.htm?abbucket=16&id=613190015864&mi_id=0000VdxIoOlEaJpSrLq2vLlI9zjiVrkuPuOVyvBE36EDPr4&ns=1&priceTId=2150455917750559194186583e1322&skuId=4724446993652&spm=a21n57.1.hoverItem.3&utparam=%7B%22aplus_abtest%22%3A%221f5215bc4932e358d04aa9396324733d%22%7D&xxc=taobaoSearch)                                                                                                                                                                                  |
| 螺丝                                                    | KM3*8mm小头螺丝    | 8+  |         | [淘宝](https://item.taobao.com/item.htm?id=642549715436&mi_id=0000bxmYL09ykBrw-UWZ3y5Iq9Y-166UYadwAz4L7aTNK7E&spm=tbpc.boughtlist.suborder_itemtitle.1.55df2e8dCZZV7z)                                                                                                                                                                                                                                                                                                                           |
| 螺丝                                                    | KM3*9mm螺丝      | 31+ |         | [淘宝](https://item.taobao.com/item.htm?abbucket=16&id=613190015864&mi_id=0000VdxIoOlEaJpSrLq2vLlI9zjiVrkuPuOVyvBE36EDPr4&ns=1&priceTId=2150455917750559194186583e1322&skuId=4724446993652&spm=a21n57.1.hoverItem.3&utparam=%7B%22aplus_abtest%22%3A%221f5215bc4932e358d04aa9396324733d%22%7D&xxc=taobaoSearch)                                                                                                                                                                                  |
| 螺丝                                                    | KA3*12mm螺丝     | 72+ |         | [淘宝](https://item.taobao.com/item.htm?ali_refid=a3_430673_1006%3A1102994973%3AH%3AWHGm2E7ibMKcnakRaz6MFrH3PlJ6ubQc%3A360d164336dc500f86095c6788a8306c&ali_trackid=282_360d164336dc500f86095c6788a8306c&id=37344431027&loginBonus=1&mi_id=0000sZSyKR9KRUK0K4CFACa7ljNBmPerG6CkoH6aFLFQcak&mm_sceneid=1_0_16285785_0&priceTId=2147840817725227816732933e1881&skuId=4878935333385&spm=a21n57.sem.item.46&utparam=%7B%22aplus_abtest%22%3A%22745e5c8f0bdd579c000b9a605536cca4%22%7D&xxc=ad_ztc)    |
| 定位销                                                   | M4*7mm         | 若干  |         | [淘宝](https://detail.tmall.com/item.htm?ali_refid=a3_430673_1006%3A1106093812%3AH%3AqaP01blctzUlvNCSHu2%2FFw%3D%3D%3A0beef205b4b351e345ceee856077b9c5&ali_trackid=282_0beef205b4b351e345ceee856077b9c5&id=713343372783&loginBonus=1&mi_id=0000ZYbuL98mVG_3t7yBpIllmQuZBdIQKtwQo0Em2DH9BjM&mm_sceneid=1_0_45541520_0&priceTId=215043ea17719852619937966e18b0&skuId=4997771881973&spm=a21n57.sem.item.48&utparam=%7B%22aplus_abtest%22%3A%22a638ecb7e68bc1b045a4ea185ad2b68f%22%7D&xxc=ad_ztc)    |
| 定位销                                                   | M4*12mm        | 若干  |         | [淘宝](https://detail.tmall.com/item.htm?ali_refid=a3_430673_1006%3A1106093812%3AH%3AqaP01blctzUlvNCSHu2%2FFw%3D%3D%3A0beef205b4b351e345ceee856077b9c5&ali_trackid=282_0beef205b4b351e345ceee856077b9c5&id=713343372783&loginBonus=1&mi_id=0000ZYbuL98mVG_3t7yBpIllmQuZBdIQKtwQo0Em2DH9BjM&mm_sceneid=1_0_45541520_0&priceTId=215043ea17719852619937966e18b0&skuId=4997771881973&spm=a21n57.sem.item.48&utparam=%7B%22aplus_abtest%22%3A%22a638ecb7e68bc1b045a4ea185ad2b68f%22%7D&xxc=ad_ztc)    |
| 螺丝刀套装                                                 | 内六角            | 1   |         | [淘宝](https://item.taobao.com/item.htm?ali_refid=a3_430673_1006%3A1152819095%3AH%3AtPKCTCB%2F0j2TZojn4CiB7UF5eyLJccfe%3Aa62b3fa4b0125a40dfaab5f9ccc7c823&ali_trackid=282_a62b3fa4b0125a40dfaab5f9ccc7c823&id=562945549227&loginBonus=1&mi_id=0000VXz6mJNLkLFTxQS8rMWJRcfikO8DqifVTbrFtqkIhew&mm_sceneid=1_0_132982962_0&priceTId=214782a117737986005742252e1156&skuId=4460422443682&spm=a21n57.sem.item.4&utparam=%7B%22aplus_abtest%22%3A%22b12590bfc8970b607c5a7d457c220161%22%7D&xxc=ad_ztc) |
| <img src="./Purchased_Parts/XT30_2+2.png" width="80"> | XT30 2+2 350mm | 2   | 25元/根   | [两端弯头](https://item.taobao.com/item.htm?spm=tbpc.boughtlist.suborder_itemtitle.1.11ef2e8dGXDrsZ&id=45608377884&mi_id=0000fi4TRgR5Rpbt443OEA-hXzsZjWBADLtHC7g-Hypk2_c)                                                                                                                                                                                                                                                                                                                          |
| <img src="./Purchased_Parts/XT30_2+2.png" width="80"> | XT30 2+2 350mm | 1   | 25元/根   | [一侧弯头一侧直头](https://item.taobao.com/item.htm?spm=tbpc.boughtlist.suborder_itemtitle.1.11ef2e8dGXDrsZ&id=45608377884&mi_id=0000fi4TRgR5Rpbt443OEA-hXzsZjWBADLtHC7g-Hypk2_c)                                                                                                                                                                                                                                                                                                                      |
| <img src="./Purchased_Parts/XT30_2+2.png" width="80"> | XT30 2+2 200mm | 3   | 22元/根   | [两端弯头](https://item.taobao.com/item.htm?spm=tbpc.boughtlist.suborder_itemtitle.1.11ef2e8dGXDrsZ&id=45608377884&mi_id=0000fi4TRgR5Rpbt443OEA-hXzsZjWBADLtHC7g-Hypk2_c)                                                                                                                                                                                                                                                                                                                          |
| 需定制                                                   | XT30 2+2 200mm | 1   | 15元/根   | [两端直头](https://item.taobao.com/item.htm?spm=tbpc.boughtlist.suborder_itemtitle.1.11ef2e8dGXDrsZ&id=45608377884&mi_id=0000fi4TRgR5Rpbt443OEA-hXzsZjWBADLtHC7g-Hypk2_c)                                                                                                                                                                                                                                                                                                                          |

### 关于固定
| 名称 | 规格型号 | 数量 | 参考价格 | 备注 |
|------|----------|------|----------|------|
| 木工夹 | 6寸G夹 | 2 | 23.8元/个 | [淘宝](https://detail.tmall.com/item.htm?abbucket=16&id=586725303306&mi_id=00004yT93hDa9u4UdEwb8EDkia6N9T53oyrA4Q1RxXqFPPM&ns=1&priceTId=214781ea17747691228482392e12c1&skuId=3982108632344&spm=a21n57.1.hoverItem.17&utparam=%7B%22aplus_abtest%22%3A%22ad4370173bfc94cfe771df00b37e06f9%22%7D&xxc=taobaoSearch) |

### 关于电源

 机械臂在发货时并未配备电源/默认情况下不带电源。您可自行连接电池，或选购一款24V14.6AMeanWell电源供应器。此外，您还需购买符合当地标准的三芯插头以及带有XT30母接头的接线束线带。

耗材BOM：

| 名称 | 规格型号 | 数量 | 参考价格 | 备注 | 图片 |
|------|----------|------|----------|------|-----|
| 电源 | LRS-350-24(24V 14.6A) | 1 | 118.75元 | [京东](https://item.jd.com/10161209537214.html?pcdk=PnAKnVITa6CLRCfJa1bRuUjjKE-kqYkXpDPGKHbwO4IuChTalUbxo5XvL-gKQSl9.rQ4a.tlbT&spmTag=YTAyNDAuYjAwMjQ5My5jMDAwMDQwMjcuMSUyM3NrdV9jYXJkJTQwMTc4MTYxMTAyODQwNiUyMzE3NTAwNjczMzc4MzgxNzg2NTc2MTE1JTIzMjAzMTA0NjkzMw#switch-sku) | <img src="./Purchased_Parts/LRS-350-24.png" width="80"> |
| 电源线 | 品字头中国标AC线；1.5m-国标3*1.5平方 | 1 | 10.1元 | [淘宝](https://item.taobao.com/item.htm?ali_refid=a3_430582_1006%3A1105615587%3AN%3AB%2Bm3wWI7DKWv2B1Ao1zaQw%3D%3D%3Ad813f59d10002e32a3cad4089078639a&ali_trackid=1_d813f59d10002e32a3cad4089078639a&id=563831183799&mi_id=0000yZ5nJxYKyYQFNkE-J27E2vJ7e72HEp5wPw0l0GOp3es&mm_sceneid=1_0_26399180_0&priceTId=2147848417799347060606382e13a0&skuId=4883125309759&spm=a21n57.1.hoverItem.1&utparam=%7B%22aplus_abtest%22%3A%22b14df3dfddb2b6f551794738b363317b%22%7D&xxc=ad_ztc) | <img src="./Purchased_Parts/CCC Certified China GB Plug to IEC C13 Power Cord.png" width="80"> |
| 输出口 | XT60E固定母头；XT60E固定母头+铜鼻-10厘米；4mm铜鼻孔 | 1 | 12.88元 | [淘宝](https://item.taobao.com/item.htm?id=956673114150&mi_id=0000_uyaWp89k03eiekkFeMWKpszoM6ZAOTjbIq27BJDMH0&skuId=5884092837633&spm=tbpc.boughtlist.suborder_itemtitle.1.fc742e8dyFymSC) | <img src="./Purchased_Parts/XT60E Female to Copper Lug Pigtail.png" width="80"> |
| 电源AC连接线 | 1.5平方；红色，蓝色，黄注绿色各1根；UT-4.2单头半剥；10CM | 3 | 1.92元 | [淘宝](https://item.taobao.com/item.htm?id=735823838383&mi_id=0000tDETNB5HlQlbvU4caiMyLKg29f6HC2cUnIiwhoqMpEg&ns=1&priceTId=214784da17797856786187222e1ca6&skuId=5397670862340&spm=a21n57.1.similarHoverItem.1&utparam=%7B%22aplus_abtest%22%3A%22f5929e70f42743346b130caea01d1341%22%7D&xxc=taobaoSearch) | <img src="./Purchased_Parts/RV Grounding Wire Coil with Y-Terminal Lugs.png" width="80"> |
| 三合一品字插座 | 带红开快接款(双螺帽)（红灯） | 1 | 6.6元 | [淘宝](https://detail.tmall.com/item.htm?id=970232786169&mi_id=0000Ug3fwg0hgRytmCjZn5XZfDpWRx9slULUlaY0-e5vStc&spm=tbpc.boughtlist.suborder_itemtitle.1.fc742e8dyFymSC) | <img src="./Purchased_Parts/3-in-1 Quick-Connect IEC 320-C14 Inlet.png" width="80"> |
| XT30转XT60连接线插头线航模16awg | XT30U母头转XT60公头 线长30CM | 1 | 7.5元 | [淘宝](https://item.taobao.com/item.htm?from=cart&id=933046470955&mi_id=000084EQEzOGgtB0DVpTa15GOaDbFTT5gTbDf7xph4gmYxk&skuId=5988958399582&spm=a1z0d.6639537%2F202410.item.d933046470955.350b74844tliiy&upStreamPrice=750) | <img src="./Purchased_Parts/XT30U_female_to_XT60_male.png" width="80"> |
| 304十字沉头螺丝 | M4X6 | 6 | 2.39元 | / | / |
| 304十字沉头螺丝 | M3X8 | 2 | 2.34元 | / | / |
| 304十字圆头螺丝 | M3X8 | 2 | 2.1元 | / | / |
| 六角螺母 | M3X2.5 | 2 | 2.1元 | / | / |

打印件BOM：

| 名称 | 图片 | 数量  | 备注  |
| ------ | ---- | --- | ---- |
| [前壳](./3D_Printed_Parts/DM-power-Top%20Cover.stp) | <img src="./3D_Printed_Parts/images/DM-power-Top Cover.png" width="80"> | 1 | PLA0.4喷嘴 0.2层高 30%填充 |
| [后壳](./3D_Printed_Parts/DM-power-Bottom%20Cover.stp) | <img src="./3D_Printed_Parts/images/DM-power-Bottom Cover.png" width="80"> | 1 | PLA0.4喷嘴 0.2层高 30%填充 |
| [前壳（滑盖）](./3D_Printed_Parts/DM-power-Top%20Cover-Sliding%20Cover.stp) | <img src="./3D_Printed_Parts/images/DM-power-Top Cover-Sliding Cover.png" width="80"> | 1 | PLA0.4喷嘴 0.2层高 30%填充 |

#### 电源组装

- 电源方案组装步骤分为前壳和后壳两个部分：

##### 1.前壳组装

| Step | 操作说明 | 图片 | 备注 |
|:---:|---|---|---|
| 1-1 | 准备前壳组装所需零件和打印件 | <img src="./Assembly_Steps/powerstep_images/1-1.png" width="80"> | 检查零件是否齐全 |
| 1-2 | 各零件线序说明，按线序进行组装 | <img src="./Assembly_Steps/powerstep_images/1-2(1).png" width="80" style="margin-right:4%;"><img src="./Assembly_Steps/powerstep_images/1-2(2).png" width="80"><br><img src="./Assembly_Steps/powerstep_images/1-2(3).png" width="80"> | 严格按照线序连接 |
| 1-3 | 安装 XT60 座子 | <img src="./Assembly_Steps/powerstep_images/1-3(1).png" width="80" style="margin-right:4%;"><img src="./Assembly_Steps/powerstep_images/1-3(2).png" width="80"> | 使用304十字沉头螺丝M3X8和六角螺母M3X2.5固定 |
| 1-4 | 安装三合一品字插座 | <img src="./Assembly_Steps/powerstep_images/1-4(1).png" width="80" style="margin-right:4%;"><img src="./Assembly_Steps/powerstep_images/1-4(2).png" width="80"> | 304十字圆头螺丝M3X8对三合一品字插座固定 |
| 1-5 | 前壳内部接线 | <img src="./Assembly_Steps/powerstep_images/1-5(1).png" width="80"><br><img src="./Assembly_Steps/powerstep_images/1-5(2).png" width="80"> | 对照线序图检查连接 |
| 1-6 | 固定前壳与电源两侧 | <img src="./Assembly_Steps/powerstep_images/1-6(1).png" width="80" style="margin-right:4%;"><img src="./Assembly_Steps/powerstep_images/1-6(2).png" width="80"> | M4X6_304十字沉头螺丝X2 |
| 1-7 | 安装滑盖 | <img src="./Assembly_Steps/powerstep_images/1-7(1).png" width="80" style="margin-right:4%;"><img src="./Assembly_Steps/powerstep_images/1-7(2).png" width="80"> | 从电源底部推入 |
| 1-8 | 固定滑盖 | <img src="./Assembly_Steps/powerstep_images/1-8.png" width="80"> | M4X6_304十字沉头螺丝X2 |

---

##### 2.后壳组装

| Step | 操作说明 | 图片 | 备注 |
|:---:|---|---|---|
| 2-1 | 准备后壳组装所需零件和打印件 | <img src="./Assembly_Steps/powerstep_images/2-1.png" width="80"> | 检查配件完整性 |
| 2-2 | 将后壳与电源组装 | <img src="./Assembly_Steps/powerstep_images/2-2.png" width="80"> | 对齐位置 |
| 2-3 | 固定后壳与电源两侧 | <img src="./Assembly_Steps/powerstep_images/2-3(1).png" width="80" style="margin-right:4%;"><img src="./Assembly_Steps/powerstep_images/2-3(2).png" width="80"> | M4X6_304十字沉头螺丝X2 |

---

##### 3.总体完成

| Step | 操作说明 | 图片 | 备注 |
|:---:|---|---|---|
| 1 | 电源方案总体组装完成 | <img src="./Assembly_Steps/powerstep_images/3.png" width="80"> | 检查所有螺丝紧固情况 |

---
