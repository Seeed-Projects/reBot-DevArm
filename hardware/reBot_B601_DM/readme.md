# 🤖 reBot DevArm Open Source Hardware Specification


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


| Date | Version | File Name | Changelog |
|----------|------|----------|------|
|  2026-03-31 | v1.0 |  reBot_B601_DM_v1.0_20260331.step  | Initial upload |
|  2026-04-25 | v1.1 |  reBot_B601_DM_v1.1_20260425.step  | Added Cable Restraint for the 3 end joint motors to prevent loosening and disconnection. Fixed Joint 1 model from 4310 to 4340P. Added CNC part 02_Base_Reinforcement_Part.step at the bottom to enhance base rigidity. |
|  2026-10-30 | v1.1 |  reBot_B601_DM_v1.1_20260625.step  | All wire harnesses upgraded to injection-molded (tooled) custom harnesses for better quality; the two 3D-printed brackets on the forearm and wrist have been fine-tuned internally so the cables can pass through the routing holes. |


This BOM is for the reBot Arm B601 DM robotic arm, which uses Damiao 43 series motors. The other version, reBot Arm B601 RS, uses RobStride motors; [see the BOM here](../reBot_B601_RS/README.md).

# 📦 File Structure
*   3D_Printed_Parts/: Step files for all 3D printed parts.
*   Metal_Parts/: Step files for all CNC machined metal parts.
*   Purchased_Parts/: Step files for all purchased components.
*   reBot_B601_DM_v1.1_20260625.step: Full robotic arm assembly file (current); reBot_B601_DM_v1.1_20260425.step is kept as the previous revision.

# 🛒[Gets All Parts](https://www.seeedstudio.com/reBot-Arm-B601-DM-Bundle.html)
- We offer five kit options:
  - **Arm Body Motor Kit**: Includes only motors and wiring harnesses for the robotic arm.
  - **Arm Body Structural Kit**: Includes only mechanical structural components.
  - **Gripper Complete Kit**: Includes motors, wiring harnesses and structural components for the gripper.
  - **Full Kit**: Includes the complete set of the robotic arm body and gripper.
  - **Pre‑assembled Robotic Arm**: Fully assembled finished robotic arm.


# 📊 Bill of Materials (BOM)

> [!WARNING]
> Declaration: The published BOM does **not** represent the final shipping version from Seeed. This open-source v1.1 is optimized for developers to reproduce at minimal cost, with some non-essential details simplified.
> The final Seeed production version will include metal laser engraving for foolproofing, some 3D printed parts will be replaced with metal for durability, clearances and machining tolerances will be adjusted for factory variation (balancing precision and cost), and custom wiring (e.g., braided sleeve protection) will be added at extra cost. However, the mechanical structure remains identical.

---

## 🖨️ 3D Printed Parts

| Part Description | Image | File Name | Material | Qty | Notes |
|----------|------|--------|------|----------|------|
| Robotic Arm Base Platform | <img src="./3D_Printed_Parts/images/02-BASE.png" width="80"> | 01_BASE_Plate.step | Bambu ABS Black | 1 | 0.4 nozzle, 0.2 layer height, 30% infill |
| Robotic Arm Base Link | <img src="./3D_Printed_Parts/images/02-BASE_02.png" width="80"> | 01_BASE_Link.step | Bambu ABS Black | 1 | 0.4 nozzle, 0.2 layer height, 30% infill |
| Upper Arm Left Filler | <img src="./3D_Printed_Parts/images/02-DOWN_TRIM_1.png" width="80"> | 01_Upper_Arm_Fuller_L.step | Bambu PLA Black & Green | 1 | 0.4 nozzle, 0.2 layer height, 15% infill |
| Upper Arm Right Filler | <img src="./3D_Printed_Parts/images/02-DOWN_TRIM_2.png" width="80"> | 01_Upper_Arm_Fuller_R.step | Bambu PLA Black & Green | 1 | 0.4 nozzle, 0.2 layer height, 15% infill |
| Upper Arm Center Filler | <img src="./3D_Printed_Parts/images/02-DOWN-FILLING.png" width="80"> | 01_Upper_Arm_Fuller_M.step | Bambu ABS Black | 1 | 0.4 nozzle, 0.2 layer height, 30% infill |
| Upper Arm Horizontal Limit Block | <img src="./3D_Printed_Parts/images/02-SPACER-DOWN.png" width="80"> | 01_Upper_Arm_Limit.step | Bambu ABS Black | 1 | 0.4 nozzle, 0.2 layer height, 30% infill |
| Arm Handle | <img src="./3D_Printed_Parts/images/02-HANDLE.png" width="80"> | 01_Arm_Handle.step | Bambu ABS Black | 1 | 0.4 nozzle, 0.2 layer height, 30% infill |
| Lower Arm Left Filler | <img src="./3D_Printed_Parts/images/02-UP-TRIM_1.png" width="80"> | 01_Lower_Arm_Filler_L.step | Bambu PLA Black & Green | 1 | 0.4 nozzle, 0.2 layer height, 15% infill |
| Lower Arm Right Filler | <img src="./3D_Printed_Parts/images/02-UP-TRIM_2.png" width="80"> | 01_Lower_Arm_Filler_R.step | Bambu PLA Black & Green | 1 | 0.4 nozzle, 0.2 layer height, 15% infill |
| Lower Arm Center Filler | <img src="./3D_Printed_Parts/images/02-UP-FILLING.png" width="80"> | 01_Lower_Arm_Filler_M.step | Bambu ABS Black | 1 | 0.4 nozzle, 0.2 layer height, 30% infill |
| Upper Arm Cover | <img src="./3D_Printed_Parts/images/02-DOWN-COVER.png" width="80"> | 01_Upper_Arm_Cover.step | Bambu PLA Green | 1 | 0.4 nozzle, 0.2 layer height, 15% infill |
| Lower Arm Cover | <img src="./3D_Printed_Parts/images/02-UP-COVER.png" width="80"> | 01_Lower_Arm_Cover.step | Bambu PLA Green | 1 | 0.4 nozzle, 0.2 layer height, 15% infill |
| Motor 5 Protection Cover | <img src="./3D_Printed_Parts/images/02-MOTOR-COVER.png" width="80"> | 01_Motor_Cover.step | Bambu ABS Black | 1 | 0.4 nozzle, 0.2 layer height, 30% infill |
| Gripper Horizontal Limit | <img src="./3D_Printed_Parts/images/02-SPACER.png" width="80"> | 01_Lower_Arm_Limit.step | Bambu PLA Green | 1 | 0.4 nozzle, 0.2 layer height, 15% infill |
| Gripper Slider Support Bracket | <img src="./3D_Printed_Parts/images/02-3D-RAIL-BRACKET.png" width="80"> | 01-Rail-Bracket.step | Bambu PLA Green | 1 | 0.4 nozzle, 0.2 layer height, 15% infill |
| Gripper Finger | <img src="./3D_Printed_Parts/images/02-CLIP_1.png" width="80"> | 01_Finger.step | Bambu ABS Black | 2 | 0.4 nozzle, 0.2 layer height, 45% infill |
| Motor 5 Cable Restraint | <img src="./3D_Printed_Parts/images/01_Joint5_Cable Restraint_A.png" width="80"> | 01_Joint5_Cable Restraint_A.step | Bambu PLA Green | 1 | 0.4 nozzle, 0.2 layer height, 15% infill |
| Motor 6 & 7 Cable Restraint A | <img src="./3D_Printed_Parts/images/01_Joint6_7_Cable Restraint_A.png" width="80"> | 01_Joint6_7_Cable Restraint_A.step | Bambu ABS Black | 2 | 0.4 nozzle, 0.2 layer height, 30% infill |
| Motor 6 & 7 Cable Restraint B | <img src="./3D_Printed_Parts/images/01_Joint6_7_Cable Restraint_B.png" width="80"> | 01_Joint6_7_Cable Restraint_B.step | Bambu ABS Black | 2 | 0.4 nozzle, 0.2 layer height, 30% infill |
| - | Reference Price | Average **50$** | | | Price varies by material cost and printing time |

Long-term dragging of Wiring Harness 1 may abrade the motor connector and result in poor electrical contact. Printing the parts listed below can mitigate this risk.

| Part Description | Image | File Name | Material | Qty | Remarks |
| ---- | ---- | ---- | ---- | ---- | ---- |
| Wiring Harness Clips for Two Sides of Motor 1 | <img src="./3D_Printed_Parts/images/DM_Motor1_wiring_harness_clip.jpg" width="80"> | `DM_Motor1_wiring_harness_clip.stp` | Bambu Lab Black ABS | 2 | 0.4 mm nozzle, 0.2 mm layer height, 30% infill |

## 📷 Compatible Camera Mount

| Part Description | Image | File Name | Material | Qty | Notes |
|----------|------|--------|------|----------|------|
| [Orbbec Gemini2](https://www.seeedstudio.com/Orbbec-Gemini-2-3D-Camera-p-6464.html) | <img src="./3D_Printed_Parts/images/Gemini2_mount.png" width="80"> | [`D435_Gemini2_Mount.step`](../camera-mounts/b601-camera-mounts/D435_Gemini2_Mount.step) | Bambu ABS Black | 1 | 0.4mm Nozzle, 0.2mm Layer Height, 30% Infill |

The B601 wrist camera mounts are shared by **B601-RS and B601-DM**. Models, previews, and downloads are maintained in the [shared camera mount catalog](../camera-mounts/README.md).

### 🧩 Printing Recommendations
- Layer height: 0.2 mm
- Nozzle: 0.4 mm
- Supports: Add as needed
- Materials: High-temperature and load-bearing parts use ABS with 30–80% infill; may also use nylon or carbon-fiber reinforced materials. Cosmetic parts use PLA with 15% infill.
- Recommended materials for load-bearing parts:

---

## 🔩 CNC Machined Metal Parts

> [!WARNING]
> Some parts that can be replaced with 3D printing are noted in the remarks, which can significantly reduce costs.

| Part Description | Image | File Name | Material | Qty | Machining | Notes |
|----------|------|--------|----------|------|------|------|
| Motor 1 Bearing Mount | <img src="./Metal_Parts/images/02_Base_Reinforcement_Part.png" width="80"> | 02_Base_Reinforcement_Part.step | Aluminum Alloy 5052 | 1 | CNC | Can be 3D printed in ABS with high infill to reduce cost |
| Motor 1 Rotation Axis | <img src="./Metal_Parts/images/02_Arm_Yaw_Limit.png" width="80"> | 02_Arm_Yaw_Limit.step | Aluminum Alloy 5052 | 1 | CNC | Added yaw angle motion limit |
| Motor 2–5 Front Spacer | <img src="./Metal_Parts/images/02_Motor_Front_Spacer.png" width="80"> | 02_Motor_Front_Spacer.step | Aluminum Alloy 5052 | 4 | CNC | Can be 3D printed in ABS with 30% infill |
| Motor 2–4 Rear Spacer | <img src="./Metal_Parts/images/02_Motor_Back_Spacer.png" width="80"> | 02_Motor_Back_Spacer.step | Aluminum Alloy 5052 | 3 | CNC | |
| Motor 2–4 Rear Flange | <img src="./Metal_Parts/images/02_FLANGE.png" width="80"> | 02_FLANGE.step | Aluminum Alloy 5052 | 3 | CNC | |
| Wrist Motor 5 Bracket | <img src="./Metal_Parts/images/02_Wrist_Bracket.png" width="80"> | 02_Wrist_Bracket.step | Aluminum Alloy 5052 | 1 | CNC | |
| Gripper Connector A | <img src="./Metal_Parts/images/02_Gripper_Connector_A.png" width="80"> | 02_Gripper_Connector_A.step | Aluminum Alloy 5052 | 1 | CNC | |
| Gripper Connector B | <img src="./Metal_Parts/images/02_Gripper_Connector_B.png" width="80"> | 02_Gripper_Connector_B.step | Aluminum Alloy 5052 | 1 | CNC | |
| Gripper Slider Metal Bracket | <img src="./Metal_Parts/images/02_Slider_Bracket.png" width="80"> | 02_Slider_Bracket.step | Aluminum Alloy 5052 | 1 | CNC | Can be 3D printed in ABS with high infill, not recommended for long-term use |
| Slider to Gripper Extension | <img src="./Metal_Parts/images/02_Slider_Extension.png" width="80"> | 02_Slider_Extension.step | Aluminum Alloy 5052 | 2 | CNC | |
| Upper-Lower Arm Link Left | <img src="./Metal_Parts/images/02_Lower_Upper_Link_L.png" width="80"> | 02_Lower_Upper_Link_L.step | Aluminum Alloy 5052 | 1 | CNC | |
| Upper-Lower Arm Link Right | <img src="./Metal_Parts/images/02_Lower_Upper_Link_R.png" width="80"> | 02_Lower_Upper_Link_R.step | Aluminum Alloy 5052 | 1 | CNC | |
| Lower Arm-Wrist Link Left | <img src="./Metal_Parts/images/02_Lower_Wrist_Link_L.png" width="80"> | 02_Lower_Wrist_Link_L.step | Aluminum Alloy 5052 | 1 | CNC | |
| Lower Arm-Wrist Link Right | <img src="./Metal_Parts/images/02_Lower_Wrist_Link_R.png" width="80"> | 02_Lower_Wrist_Link_R.step | Aluminum Alloy 5052 | 1 | CNC | |
| Gear Connector | <img src="./Metal_Parts/images/02_Gear_Connector.png" width="80"> | 02_Gear_Connector.step | Aluminum Alloy 5052 | 1 | CNC | |
| Rack | <img src="./Metal_Parts/images/Rack.png" width="80"> | 02_Rack.step | Aluminum Alloy 5052 | 2 | CNC | |
| Link 1 | <img src="./Metal_Parts/images/Link1.png" width="80"> | 03_Link1.step | Aluminum Alloy 5052 | 1 | CNC + Sheet Metal | |
| Link 2 | <img src="./Metal_Parts/images/Link2.png" width="80"> | 03_Link2.step | Aluminum Alloy 5052 | 2 | CNC + Sheet Metal | |
| Link 3 Left | <img src="./Metal_Parts/images/Link3_L.png" width="80"> | 03_Link3_L.step | Aluminum Alloy 5052 | 1 | CNC + Sheet Metal | |
| Link 3 Right | <img src="./Metal_Parts/images/Link3_R.png" width="80"> | 03_Link3_R.step | Aluminum Alloy 5052 | 1 | CNC + Sheet Metal | |
| Link 5 | <img src="./Metal_Parts/images/Link5.png" width="80"> | 03_Link5.step | Aluminum Alloy 5052 | 1 | CNC + Sheet Metal | |
| - | Market Reference Price | Average **250$** | | | Price varies by aluminum cost, tolerance requirements, lead time |

### 🧩 Machining Specifications
- Key dimension tolerance: ±0.02 mm GB/T1840-M
- Surface finish: Anodizing / Sandblasting
- Mating parts recommended: H7 / interference fit
---

## 🛒 Purchased Parts (Standard Parts)

> [!WARNING]
> Since everyone will need to assemble and tighten the screws themselves, standard hex socket screws have been selected. After prolonged operation, the screws may loosen, which will affect the precision of the robotic arm. For this reason, you are required to purchase additional hot melt glue to perform thread locking on the screws at each joint.

If you have a power drill or similar tools, you may choose to buy lock washers or thread-locking screws instead. However, **it is extremely important** that you use the lowest torque setting when using an electric screwdriver to avoid thread stripping, which will result in irreversible damage.


  | Name | Specification / Model | Quantity | Reference Price | Notes |
  |------|----------|------|----------|------|
  | Brushless motor | DM4310(V4) | 4 | 120 $/unit | [SeeedStudio](https://www.seeedstudio.com/Damiao-4310-Actuator-Motor-p-6823.html) |
  | Brushless motor | DM4340P(V4) | 3 | 175 $/unit |  [SeeedStudio](https://www.seeedstudio.com/DM4340P-Actuator-p-6663.html)  |
  | CAN-USB driver board |  | 1 | 15 $/unit |   [SeeedStudio](https://www.seeedstudio.com/DM-CAN-USB-Driver-Borad-p-6706.html)   |
  | Bearing | 6707ZZ | 1 | 13 $/unit | [Amazong](https://www.amazon.com/uxcell-35x44x5mm-Shielded-Precision-Lubricated/dp/B0D6WBMW3F/ref=sr_1_1?crid=3J03FBU7MI31J&dib=eyJ2IjoiMSJ9.sfX192-ZSyqh-VJEgq6jR02DrJcdVTxBbKWn5TLypwoK7NyklXkZSQT-3V42_zTm98_Y8dLCtnTzJ9JVnPuBG7bfvUYv0ctrasWhZgU5DFtl2y0CtKLOUOoukmlHqCfonkjZLapmfzSVAaV-3CJYhqizbjedl6zGoDUNo2ryKd4RbtRhJXndBmf96HwTPrPH8g8KB2NPyhnPaP36r6C0Ehdb0xrqjNzKt7YcM7xkZ_8.QvCzMQ0EPe3-5SBYNcuoO5L-Yx0CSr9Vmjc-Ma7FzbY&dib_tag=se&keywords=6707ZZ&qid=1774771772&sprefix=6707zz%2Caps%2C376&sr=8-1) |
  | Bearing | 6803ZZ | 3 | 13 $/unit | [Amazong](https://www.amazon.com/uxcell-17x26x5mm-Shielded-Precision-Lubricated/dp/B0D54JSWBZ/ref=sr_1_1?crid=17L94NDI1JCC0&dib=eyJ2IjoiMSJ9.xH_s9Ui7VlS40EZvr-HektqY3VOJsM-VjyE6JaJEScIWuFZ2UYSM7G8j1fC0HSmbb7YlA0YfUxxCkUzBptwrEEdEHsP94TGplNpPAWwhnH8b76HapXR_uHbr1vu3xe0AYSYP30Quk9LMQrGjUh84bXL82z2mORuiri0VHqo5DmSguK0cHubmVaXtbR_eJ43Z7L2nNqWfgltqzmHsYm7DQvrnIBg9UMlD1o9559nCSKA.E_N7CDPQhShckT-1vHDhYvNgiqRKusa12d43hqATQ5A&dib_tag=se&keywords=6803ZZ&qid=1774771801&sprefix=6803zz%2Caps%2C397&sr=8-1) |
  | Bearing | AXK5578 | 1 | 12 $/unit | [Amazong](https://www.amazon.com/PZRT-AXK5578-Thrust-Bearings-Washers/dp/B0B3M3RZGW/ref=sr_1_1?dib=eyJ2IjoiMSJ9.TatYkzOvpYAJ5K23C7Qr9JKJsPhpJE8p1L3k5_1YqQ7ozSLNgOBEeG9pTYz-WXOWiHkbJq_zZR4FxNHAJZ4euyfOGXkOKycOyN0pUD0_WkJia0PekbRy0sYvyQbE7KZByR-40WiPSPuUcysFewSngPoDGQZzESFOUz__V9ViGCIQAPfdUe2OxVpvtbKZYCQsrSDm8b8okR25bavCvpDbBfPh0He2PEBEpl55L8RtYKmlv62XJyfYT1o29A7wO5n8-g3hpJOrKmmWCybdEEWSmquAT1cjvsPTJDaT_TICsso.6xR5pEGJgTR-u_NOyXxi8VTphoLytGd8zugy1-xu-fE&dib_tag=se&keywords=AXK5578&qid=1774771826&sr=8-1&th=1) |
  | Linear rail | MGN9-170mm | 1 | 23 $/unit | [Amazong](https://www.amazon.com/uxcell-Sliding-Carriage-Bearing-Printers/dp/B0D54L45WM/ref=sr_1_1?dib=eyJ2IjoiMSJ9.qNphfY5r4UgLDHslIliMBhC45qBKTl37lJseObJSBp79RJ4VJnAH-lYAMo-rwPiu_uqWmkN7ms4kfAokYvod1seWb5-z2_kVgVuzrCXdiRycNXjrdv3qi5Awuno0_vEqjT4WJ569tAmqm_Rujrdxss7VfpLizFxq6-R8DucuvqZ0M0Y4go9PzRFEFPu4csskz7-UkM1CUidHoKmrT-I7R1Ta0dijj2SYlR_zW0si75k.nRJTebbqw-bFyzkdU8MztHnGdt9qwnHr_gIqa-MDxEQ&dib_tag=se&keywords=MGN9&qid=1774771864&sr=8-1) |
  | Slider block | MGN9 | 2 | 10 $/unit | [Amazong](https://www.amazon.com/uxcell-Bearing-Sliding-Carriage-Anti-Fall/dp/B0D9QBQDKB/ref=sr_1_8?dib=eyJ2IjoiMSJ9.qNphfY5r4UgLDHslIliMBhC45qBKTl37lJseObJSBp79RJ4VJnAH-lYAMo-rwPiu_uqWmkN7ms4kfAokYvod1seWb5-z2_kVgVuzrCXdiRycNXjrdv3qi5Awuno0_vEqjT4WJ569tAmqm_Rujrdxss7VfpLizFxq6-R8DucuvqZ0M0Y4go9PzRFEFPu4csskz7-UkM1CUidHoKmrT-I7R1Ta0dijj2SYlR_zW0si75k.nRJTebbqw-bFyzkdU8MztHnGdt9qwnHr_gIqa-MDxEQ&dib_tag=se&keywords=MGN9&qid=1774771864&sr=8-8) |
  | Gear | Module 1, boss type, 16 teeth, 6 mm bore | 1 | 44$/unit | [Amazong](https://www.amazon.com/Module-15-Teeth-Finished-Perforation/dp/B0GDSR1LKM/ref=sr_1_1?crid=2EN1YHE8TEC58&dib=eyJ2IjoiMSJ9.54N73iSlush8K1a_teRazjBGZaQnbFM4MLysEbIq430CEYcVs0slm8KhpC_JlmjyVMocPA3vLANjERYZWweRag36NhX2GGldVTpd31kAWW4.ws8l0qBABmSVrUGX4g2o3sBbUgOnNhl3Nx_Nt-d1HT8&dib_tag=se&keywords=1%2Bmodule16%2Bteeth&qid=1774772022&sprefix=1%2BModule16%2Bteeth%2Caps%2C403&sr=8-1&th=1)  |
  | Silicone pad | 30x9x2mm | 1 | 10 $ | [Amazong](https://www.amazon.com/Self-Adhesive-Anti-Sliding-Anti-Scratch-Protectors-Appliances/dp/B0F9KVYXFZ/ref=sr_1_3?crid=LVY2LLBFQT6J&dib=eyJ2IjoiMSJ9.4qjOEtjEph1QxS_kJF2vIYqvD_8Lzt4GZ2rrywWbrAhniBvp_8YrEsVNcCPQofO4jVqBxFE8Yplyg2XXgAXlUZwzqE-Gp8MYcaPmphL8Mc1n-ARSCNaTq5gc7ZIWsS6u-kR0G2BzIlBo6NF88KvASjKYJfTHpPXHfNCPVw13P-PseVbUZwlVAO9zMHa3a84gHRd-I-mGB8SCmek9mXjN-c-bFxKvJXlz4C5YBBdt9cH3QkSmLgiLZ_iD4K1mh-MwI5WuVOXr5ZOwJ0bVpmHpc_vpbKLr7CkVack3nsC-TM0.40ujhwS5ConOfA8io_c5hcdos70HOKjMFqqKLKgNwI8&dib_tag=se&keywords=silicone%2Bsticker&qid=1774772199&sprefix=silicone%2Bsticker%2Caps%2C380&sr=8-3&th=1) |
  | Screw | HM3-12mm screw | 14+ |  | [Amazong](https://www.amazon.com/BNUOK-120pcs-Stainless-Threads-Spanner/dp/B0DJQGMQZM/ref=sr_1_4?crid=3J1D711FNBYR9&dib=eyJ2IjoiMSJ9.wo20uXEJsuYS5OBVpnH9TILDd6HtQrJUlEvvYFPE5VV6bozIiRlWwmDaoYnp345KjXwRyxbEgEaRD8gVD2vVhPXg3M266n3H8t9cWN518aR4c5WkFUkqLIqLwdGYBllKcQQ8agsrZYgSVFp9G8LJR4l9oAj8Yx4QN8MReo2k23RVk-lkWeJk1azXD88GFTmd17aiXz6fwOE45Krj4VRiy1oskx8QvMprmJXtH8KowAJo-pWdBtePCCIUUa8oLR78hi17yW_OGJattIwdAziX9RizLI-EMh3hku42WJWnb3g.lZYqsYfJunSoEUPNT04E1sFhPiudREmrI0919PaPBYI&dib_tag=se&keywords=screw+HM3-12mm&qid=1776330531&s=industrial&sprefix=screw+hm3-12mm%2Cindustrial%2C475&sr=1-4) |
  | Screw | HM3-25mm screw | 14+ |  | [Amazong](https://www.amazon.com/BNUOK-120pcs-Stainless-Threads-Spanner/dp/B0DJQFGRPQ/ref=sr_1_4?crid=3J1D711FNBYR9&dib=eyJ2IjoiMSJ9.wo20uXEJsuYS5OBVpnH9TILDd6HtQrJUlEvvYFPE5VV6bozIiRlWwmDaoYnp345KjXwRyxbEgEaRD8gVD2vVhPXg3M266n3H8t9cWN518aR4c5WkFUkqLIqLwdGYBllKcQQ8agsrZYgSVFp9G8LJR4l9oAj8Yx4QN8MReo2k23RVk-lkWeJk1azXD88GFTmd17aiXz6fwOE45Krj4VRiy1oskx8QvMprmJXtH8KowAJo-pWdBtePCCIUUa8oLR78hi17yW_OGJattIwdAziX9RizLI-EMh3hku42WJWnb3g.lZYqsYfJunSoEUPNT04E1sFhPiudREmrI0919PaPBYI&dib_tag=se&keywords=screw%2BHM3-12mm&qid=1776330531&s=industrial&sprefix=screw%2Bhm3-12mm%2Cindustrial%2C475&sr=1-4&th=1)  |
  | Screw | HM3-6mm screw | 16+ |  | [Amazong](https://www.amazon.com/BNUOK-120pcs-Stainless-Threads-Spanner/dp/B0DJQG5YLF/ref=sr_1_4?crid=3J1D711FNBYR9&dib=eyJ2IjoiMSJ9.wo20uXEJsuYS5OBVpnH9TILDd6HtQrJUlEvvYFPE5VV6bozIiRlWwmDaoYnp345KjXwRyxbEgEaRD8gVD2vVhPXg3M266n3H8t9cWN518aR4c5WkFUkqLIqLwdGYBllKcQQ8agsrZYgSVFp9G8LJR4l9oAj8Yx4QN8MReo2k23RVk-lkWeJk1azXD88GFTmd17aiXz6fwOE45Krj4VRiy1oskx8QvMprmJXtH8KowAJo-pWdBtePCCIUUa8oLR78hi17yW_OGJattIwdAziX9RizLI-EMh3hku42WJWnb3g.lZYqsYfJunSoEUPNT04E1sFhPiudREmrI0919PaPBYI&dib_tag=se&keywords=screw%2BHM3-12mm&qid=1776330531&s=industrial&sprefix=screw%2Bhm3-12mm%2Cindustrial%2C475&sr=1-4&th=1)  |
  | Screw | HM4-75mm set screw | 4+ |  | [Amazong](https://www.amazon.com/iexcell-Partially-Threaded-Thread-Socket/dp/B0DR1NX178/ref=sr_1_1?crid=35DT1MLQCOR9C&dib=eyJ2IjoiMSJ9.RlFuoSyG6Yoi2cmVkd0sQ47UpPY4y8uvofyrje4Ha76Dj6dcpknwvFT7DGc5jFqxw5Zd5g4SV-yre7xcMb3WB7MbBowQO3ZzvCgpYWcJ2xzphgz9gx0SNIr_ggqvFcAmxkNuMMVf0p9vPY-jJ2j9cbIk8IwMHlTo6kkuBINPotouNNyElpiy9qHhllwajmKY5v5uDIzJKNJvmhpUtJsd5IS7TB9VaRPkzsDbMDfR4pvs4JgNbU1Zmcu4Ex9fYcRHrOGjAZbbvNxo1r_N5MBKWbxbtZEDDKP_8Oyhgakhhnc.MTLa-_9PBksy6Qge1YqQmlejVfLKkuxB9gT-ZnB9ek0&dib_tag=se&keywords=screw+HM4-75&qid=1776330730&s=industrial&sprefix=screw+m4-75%2Cindustrial%2C401&sr=1-1)  |
  | Screw | KM3*12mm screw | 30+ |  |  [Amazong](https://www.amazon.com/Uxcell-a16011300ux0872-M3x12mm-Carbon-Countersunk/dp/B01E6EIC2S/ref=sr_1_1?crid=2VJKS347LBDWD&dib=eyJ2IjoiMSJ9.eXF2FHahloRY0Kq8sM_EkJUm7ipUgMoVSuTAPjt3ZnAINqLrPQz9A55XDHfe00KPGG3Sr1IJJQloiw7IFwewoPsbdnKBZH5JjT4Ijy_bUXju1IvrHWP4nWeYW1o29jlbHBKEa3fPl8-JzEHr9RPKe5h_Dr1vN6VFMUfszTDEzufQrIi22AsKCMTep5n0-IR7AIc7Fai93nmr4ax8USKGOD_3yu4ri0p8ClPTZzfwmDJvnTpE9J9PNN8uA-wDz72RADQu2VLry_mvb5CA1JV0vHP49Qsy-96MKXo-j3vT8m0.DWiT1Loy7A-MeTveRzxU47S6WCKwnW6MVnmpF256j-s&dib_tag=se&keywords=screw+KM3*12&qid=1776330785&s=industrial&sprefix=screw+km3+%2Cindustrial%2C984&sr=1-1) |
  | Screw | KM3*16mm screw | 34+ |  | [Amazong](https://www.amazon.com/Uxcell-a16011300ux0872-M3x12mm-Carbon-Countersunk/dp/B01E6EIC2S/ref=sr_1_1?crid=2VJKS347LBDWD&dib=eyJ2IjoiMSJ9.eXF2FHahloRY0Kq8sM_EkJUm7ipUgMoVSuTAPjt3ZnAINqLrPQz9A55XDHfe00KPGG3Sr1IJJQloiw7IFwewoPsbdnKBZH5JjT4Ijy_bUXju1IvrHWP4nWeYW1o29jlbHBKEa3fPl8-JzEHr9RPKe5h_Dr1vN6VFMUfszTDEzufQrIi22AsKCMTep5n0-IR7AIc7Fai93nmr4ax8USKGOD_3yu4ri0p8ClPTZzfwmDJvnTpE9J9PNN8uA-wDz72RADQu2VLry_mvb5CA1JV0vHP49Qsy-96MKXo-j3vT8m0.DWiT1Loy7A-MeTveRzxU47S6WCKwnW6MVnmpF256j-s&dib_tag=se&keywords=screw+KM3*12&qid=1776330785&s=industrial&sprefix=screw+km3+%2Cindustrial%2C984&sr=1-1)  |
  | Screw | KM3*7mm screw | 76+ |  |[Amazong](https://www.amazon.com/Uxcell-a16011300ux0872-M3x12mm-Carbon-Countersunk/dp/B01E6EIC2S/ref=sr_1_1?crid=2VJKS347LBDWD&dib=eyJ2IjoiMSJ9.eXF2FHahloRY0Kq8sM_EkJUm7ipUgMoVSuTAPjt3ZnAINqLrPQz9A55XDHfe00KPGG3Sr1IJJQloiw7IFwewoPsbdnKBZH5JjT4Ijy_bUXju1IvrHWP4nWeYW1o29jlbHBKEa3fPl8-JzEHr9RPKe5h_Dr1vN6VFMUfszTDEzufQrIi22AsKCMTep5n0-IR7AIc7Fai93nmr4ax8USKGOD_3yu4ri0p8ClPTZzfwmDJvnTpE9J9PNN8uA-wDz72RADQu2VLry_mvb5CA1JV0vHP49Qsy-96MKXo-j3vT8m0.DWiT1Loy7A-MeTveRzxU47S6WCKwnW6MVnmpF256j-s&dib_tag=se&keywords=screw+KM3*12&qid=1776330785&s=industrial&sprefix=screw+km3+%2Cindustrial%2C984&sr=1-1)   |
  | Screw | KM3*9mm screw | 31+ |  |[Amazong](https://www.amazon.com/Uxcell-a16011300ux0872-M3x12mm-Carbon-Countersunk/dp/B01E6EIC2S/ref=sr_1_1?crid=2VJKS347LBDWD&dib=eyJ2IjoiMSJ9.eXF2FHahloRY0Kq8sM_EkJUm7ipUgMoVSuTAPjt3ZnAINqLrPQz9A55XDHfe00KPGG3Sr1IJJQloiw7IFwewoPsbdnKBZH5JjT4Ijy_bUXju1IvrHWP4nWeYW1o29jlbHBKEa3fPl8-JzEHr9RPKe5h_Dr1vN6VFMUfszTDEzufQrIi22AsKCMTep5n0-IR7AIc7Fai93nmr4ax8USKGOD_3yu4ri0p8ClPTZzfwmDJvnTpE9J9PNN8uA-wDz72RADQu2VLry_mvb5CA1JV0vHP49Qsy-96MKXo-j3vT8m0.DWiT1Loy7A-MeTveRzxU47S6WCKwnW6MVnmpF256j-s&dib_tag=se&keywords=screw+KM3*12&qid=1776330785&s=industrial&sprefix=screw+km3+%2Cindustrial%2C984&sr=1-1)   |
  | Screw | KM3*8mm Socket Micro Profile Head Screw | 31+ |  |[Amazong](https://www.amazon.com/SMALLRIG-Screw-Screws-12pcs-Pack/dp/B01MS60KSY/ref=sr_1_1?dib=eyJ2IjoiMSJ9.YfdPTE5UVJAg4SZcWMUPtQ.OCxr-8hnCbGnQsQiwM8fg8xJifzrC4-EMmKpeYyr0Zg&dib_tag=se&keywords=Socket%2BMicro%2BProfile%2BHead%2BScrew&qid=1776336031&refinements=p_n_feature_two_browse-bin%3A2292870011&rnid=2292859011&sr=8-1&xpid=BZ-yllUUAy02h&th=1)   |
  | Screw | KA3*12mm | 72+ |  | [Amazong](https://www.amazon.com/uxcell-Phillips-Tapping-Screws-Silver/dp/B01MXSS95N/ref=sr_1_3?crid=2RJ5ZBG0M4EX5&dib=eyJ2IjoiMSJ9.v9AtN0DrK0YdOT84Puh29n1VDClJz4OwvslbH610w0_xJIkuVFk81UxgSw_lSRbHugpqkja4rz-elY-DHbh0KN4GCFH2MlZhRFjXVE1vlaChALTqgr9jxatNPvPTf8SzdxFoEMEPm3jwCnC8vqLq5xL-Wr414hMsTbVYxv_ZVmEbMV-8YYXhLWiOz9EivU2C8jWw0RFSwVtUxqhj7qgBBYV5QbJRNr1XdWmQsICMHTHy35DeIcLjyKtXOb0gEwDNyqqmdvS5LfJJaLQchjLpW1jondo5xapQVw8gWJ4yYjk.oXwiRL9W52Tlu7tMi7tT9i7g-CBYfw_AAT1LURe2Q7k&dib_tag=se&keywords=screw+ka3*12&qid=1776331569&s=industrial&sprefix=screw+ka3+%2Cindustrial%2C466&sr=1-3)  |
  | Dowel pin | M4*8mm | Several |  | [Amazong](https://www.amazon.com/HARFINGTON-Stainless-Cylindrical-Furniture-Installation/dp/B0F6CWL4MP/ref=sr_1_6?crid=2BZ4J412S4QSB&dib=eyJ2IjoiMSJ9.a3kVMi6W355gYKjK1Sl_QFVcJD8x7DTXqxgk66DoY4TnPOEV9TG7AbW7jkNk2USTJrqrb3e5Ve0EeVwHVE-_s-UUP6jFahdiVAqkZGGnuBpVxwA-MCHYQEwThEfygwAc1HVyN1n7Cvr8GAFMvs5AfciRrbUZ8AsSNGc1Obgf8qouOe8NQhyW_Zo7YINX1m3YCuTRiLZCvB6o7XlZtZ4PRh085Bva6AjjnlNOuaiPCtzjvNUtTpyLpGmqoHM165V6onFghMcuOX9RaacnxQNsRoUtKpWPEB8h48nUnUOJ1lg.Hfy_mUj7QFR_kILC4I5RNy6h7HmdswULHg3NmKmK8bU&dib_tag=se&keywords=Dowel%2Bpin%2BM4*7&qid=1776331648&s=industrial&sprefix=dowel%2Bpin%2Bm4%2B%2Cindustrial%2C399&sr=1-6&th=1)  |
  | Dowel pin | M4*12mm | Several |  | [Amazong](https://www.amazon.com/HARFINGTON-Stainless-Cylindrical-Furniture-Installation/dp/B0F6CWL4MP/ref=sr_1_6?crid=2BZ4J412S4QSB&dib=eyJ2IjoiMSJ9.a3kVMi6W355gYKjK1Sl_QFVcJD8x7DTXqxgk66DoY4TnPOEV9TG7AbW7jkNk2USTJrqrb3e5Ve0EeVwHVE-_s-UUP6jFahdiVAqkZGGnuBpVxwA-MCHYQEwThEfygwAc1HVyN1n7Cvr8GAFMvs5AfciRrbUZ8AsSNGc1Obgf8qouOe8NQhyW_Zo7YINX1m3YCuTRiLZCvB6o7XlZtZ4PRh085Bva6AjjnlNOuaiPCtzjvNUtTpyLpGmqoHM165V6onFghMcuOX9RaacnxQNsRoUtKpWPEB8h48nUnUOJ1lg.Hfy_mUj7QFR_kILC4I5RNy6h7HmdswULHg3NmKmK8bU&dib_tag=se&keywords=Dowel%2Bpin%2BM4*7&qid=1776331648&s=industrial&sprefix=dowel%2Bpin%2Bm4%2B%2Cindustrial%2C399&sr=1-6&th=1)  |
  | Screwdriver set | Hex key set | 1 | 16$  | [Amazong](https://www.amazon.com/Amazon-Basics-Ratcheting-Electronics-Screwdriver/dp/B07V4TFWFZ/ref=sr_1_2?crid=ADAY70RZDSLN&dib=eyJ2IjoiMSJ9.jcLL4o6IXTnPlPfTTzbCZCBuZx2sLkvdUQCwlL58aq__GOyLxVPnwLI0mvGptba_HeVz6ctLQ_ziQw56BMDH9IOaw-4PVJGMktQM74mWficwggm3ckDGyAH-agN_zkB3K0_W-wrS56jfcMYFbZSWhWxr-iSOC4sdXwMGlt4rYGtenyn9yAFYBIHqjU2El5_OAKuspsrF0yQvfyfQPQHs46SClWN8zlSemGVZRuVSU26f0f9yApF6BfWHANKNNhT0Mfb6bQ8oM2XUMvwaazrrKoHeTARuoflVaVZvMU776bs.r8gy_gMINEy0qy4JyK--z-IbPZEv-SWeMGohOOE7M60&dib_tag=se&keywords=Screwdriver+set&qid=1774772499&s=industrial&sprefix=screwdriver+set+%2Cindustrial%2C374&sr=1-2)  |
  | <img src="./Purchased_Parts/XT30_2+2.png" width="80"> | XT30 2+2 350mm | 2 | 4 $/cable | Both ends angled |
  | <img src="./Purchased_Parts/XT30_2+2.png" width="80"> | XT30 2+2 350mm | 1 | 4 $/cable | One angled end and one straight end |
  | <img src="./Purchased_Parts/XT30_2+2.png" width="80"> | XT30 2+2 200mm | 3 | 4 $/cable | Both ends angled |
  | <img src="./Purchased_Parts/XT30_2+2.png" width="80"> | XT30 2+2 200mm | 1 | 3 $/cable | Both ends straight |


### About Fixing
You may modify your base freely based on the 3D printed parts we provide. You can also use G-clamps according to the thickness of your desktop.

  | Name | Specification / Model | Quantity | Reference Price | Notes |
  |------|----------|------|----------|------|
  | Woodworking clamp | 6-inch G clamp | 2 | 20 $/unit | [Amazong](https://www.amazon.com/gp/aw/d/B092J1YW2M/?_encoding=UTF8&pd_rd_plhdr=t&aaxitk=3557c048ce58e7dbb50b40c3af69f1d6&hsa_cr_id=0&qid=1774772748&sr=1-1-9e67e56a-6f64-441f-a281-df67fc737124&ref_=sbx_s_sparkle_sbtcd_asin_0_img&pd_rd_w=bNqtC&content-id=amzn1.sym.2fb72bc8-96ef-420d-b08f-c04b69f36507%3Aamzn1.sym.2fb72bc8-96ef-420d-b08f-c04b69f36507&pf_rd_p=2fb72bc8-96ef-420d-b08f-c04b69f36507&pf_rd_r=KDCPNZRHFWEWBWVHWSTR&pd_rd_wg=sBvfF&pd_rd_r=52b946ee-46e2-4e74-86ee-99e291552e44) |



### About Power Supply
The robotic arm is shipped without a power supply by default. You may connect your own battery, or purchase a reliable 24V 14.6A MeanWell power supply made in Taiwan. Additionally, you will need to buy a three-pin plug compliant with local standards and a wiring harness with XT30 female connector.

#### Consumables BOM

| Name | Specification | Qty | Reference Price | Notes | Image |
|:---|:---|:---:|:---:|:---|:---:|
| Power Supply | LRS-350-24 (24V 14.6A) | 1 | $27.35 | [amazon](https://www.amazon.com/MEAN-WELL-LRS-350-24-350-4W-Switchable/dp/B013ETVO12/ref=sr_1_1?crid=36B2HIB8MM2IT&dib=eyJ2IjoiMSJ9.vpZwmjb4m5KMNcsg2Kb7wr8DDWa-ryUqO5fConlxqlsGoTVB5HN2uBBnRNZI0kcACiaR5DKFiYWvIHLEUN3luZqJAzogeQkeT-fol0m835-oBBWSud1ixkGayrl5nRsF5KMgfvkwAIW949dTTpU2CWdNMrf8g43_vKWaytfX9SHeMJ1hmhS6Kab6fBgER6CgB47K_eEmoJj3KhrjJMtn980osDG-bCLniBcRAHThmXsVRVdpGPsmckGLLyaXrIGRG9plhKI-F7H8hfqW7vzGbwIV_bF8cFtRjdRm5Shtb0o.ekLYD0hsc1Uzji4qKl0Q0USpDTr92JEMQobBXl9lYD0&dib_tag=se&keywords=LRS-350-24&qid=1780021690&s=industrial&sprefix=lrs-350-24%2Cindustrial%2C696&sr=1-1&th=1) | <img src="./Purchased_Parts/LRS-350-24.png" width="80"> |
| Power Cord | US Standard AC Cable | 1 | $4.49 | [amazon](https://www.amazon.com/LIFEPOE-Power-3-3ft-Black-3-Prong/dp/B0FK4KPW2G/ref=sr_1_1?crid=2W5766PT8EOKA&dib=eyJ2IjoiMSJ9.7E5s-9-Zh-jJAdni-17Iyt1Mr3GJD6hMt9pfk-0S5YxZtknZik9OiePitwUom0pYUbePRpdqa0dCZtGUjluQDEJbSDePHCGvBV6bwQU7wfwd0Loo4WJJmH_2CM1KRKSPcxHXRH0i1i5yuy4g7fDxxn3nPGYU3aF00m5jiIkMfYFgOxH4yURjjZeTMZAIO9wiVQUsPrlM51UIgpPo2YYdCQVUsxjumSsTAm0Jpt2SsBEdT-QzXSIKpLSvQ6kGijXF-4ZevaxiShJdmwU8t2LobDLcalXEOl3lriZTGhjwxow.r0oBabUkGwewhvO3IKlBMULdhUSe6yNTsjfFUaBsjyU&dib_tag=se&keywords=US%2BStandard%2BAC%2BCable%3B%2B1.5m%2B-%2B3%2B*%2B1.5mm%C2%B2&nsdOptOutParam=true&qid=1780021862&s=industrial&sprefix=lrs-350-24%2Cindustrial%2C387&sr=1-1&th=1) | <img src="./Purchased_Parts/US Standard AC Cable.png" width="80"> |
| Output Port | XT60E Fixed Female Connector; XT60E Female + Lug - 10cm; 4mm Lug Hole | 1 | $9.99 | [amazon](https://www.amazon.com/LINSYRC-XT60E-F-Connector-Battery-Quadcopter/dp/B0CQK1P1DP/ref=pd_sbs_d_sccl_1_2/133-3898271-3474923?pd_rd_w=FmCVA&content-id=amzn1.sym.aa738fbd-ad05-4d11-aae2-04b598db6305&pf_rd_p=aa738fbd-ad05-4d11-aae2-04b598db6305&pf_rd_r=03QM0MRVZA968N9X6X6E&pd_rd_wg=WOZ9q&pd_rd_r=6e0577d2-de73-4427-affd-a271808e1453&pd_rd_i=B0CQK1P1DP&psc=1) | <img src="./Purchased_Parts/XT60E Female to Copper Lug Pigtail.png" width="80"> |
| Power AC Wiring | 1.5mm²; Red, Blue, Yellow x1 each(User must crimp terminals to the wire — pre-crimped leads not included.); 10CM | 3 | $0.99 | [aliexpress](https://www.aliexpress.com/item/1005008648016252.html?spm=a2g0o.productlist.main.2.15c9ZpluZpluHP&algo_pvid=09efee83-d80c-4ece-b588-3b1ef73279a3&algo_exp_id=09efee83-d80c-4ece-b588-3b1ef73279a3-1&pdp_ext_f=%7B%22order%22%3A%22230%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21USD%213.58%210.99%21%21%2124.09%216.65%21%400b0b305117800339070873795e0f3d%2112000046086542230%21sea%21US%216593543849%21ABX%211%210%21n_tag%3A-29910%3Bd%3A518b3f9d%3Bm03_new_user%3A-29895%3BpisId%3A5000000207178484&curPageLogUid=74aJ9L7lm7hs&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005008648016252%7C_p_origin_prod%3A&gatewayAdapt=4itemAdapt) | <img src="./Purchased_Parts/RV Grounding Wire Coil with Y-Terminal Lugs.png" width="80"> |
| 3-in-1 IEC Inlet Socket | Quick-connect type with red switch (Dual Nuts) | 1 | $1.98 | [aliexpress](https://www.aliexpress.com/item/1005005962021242.html?spm=a2g0o.imagesearchproductlist.main.17.7db7cZZdcZZdCY&algo_pvid=270b0987-1973-41ad-a2b9-6fe008f9edb5&algo_exp_id=270b0987-1973-41ad-a2b9-6fe008f9edb5&pdp_ext_f=%7B%22order%22%3A%22346%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21USD%213.31%211.98%21%21%2122.30%2113.35%21%400b0b305117800327806706342e118f%2112000035062406338%21sea%21US%216593543849%21ABX%211%210%21n_tag%3A-29910%3Bd%3A518b3f9d%3Bm03_new_user%3A-29895%3BpisId%3A5000000204886261&curPageLogUid=87JUDbPbch2i&utparam-url=scene%3Aimage_search%7Cquery_from%3Apc_web_image_search%7Cx_object_id%3A1005005962021242%7C_p_origin_prod%3A) | <img src="./Purchased_Parts/3-in-1 IEC Inlet Socket.png" width="80"> |
| XT30 to XT60 adapter cable plug | XT30U female to XT60 male | 1 | 8.99$ | [amazon](https://www.amazon.com/dp/B0BY8PSHK6?th=1) | <img src="./Purchased_Parts/XT30U_female_to_XT60_male.png" width="80"> |
| 304 Stainless Steel Phillips Countersunk Head Screw | M4x6 | 6 | $0.37 | / | / |
| 304 Stainless Steel Phillips Countersunk Head Screw | M3x8 | 2 | $0.36 | / | / |
| 304 Stainless Steel Phillips Pan Head Screw | M3x8 | 2 | $0.32 | / | / |
| Hex Nut | M3x2.5 | 2 | 2.10 CNY | / | / |


#### Printed Parts BOM

| Name | Image | Qty | Notes |
|:---|:---|:---:|:---|
| [Front Cover](./3D_Printed_Parts/DM-power-Top%20Cover.stp) | <img src="./3D_Printed_Parts/images/DM-power-Top Cover.png" width="80"> | 1 | PLA, 0.4mm Nozzle, 0.2mm Layer Height, 30% Infill |
| [Rear Cover](./3D_Printed_Parts/DM-power-Bottom%20Cover.stp) | <img src="./3D_Printed_Parts/images/DM-power-Bottom Cover.png" width="80"> | 1 | PLA, 0.4mm Nozzle, 0.2mm Layer Height, 30% Infill |
| [Front Cover Slider](./3D_Printed_Parts/DM-power-Top%20Cover-Sliding%20Cover.stp) | <img src="./3D_Printed_Parts/images/DM-power-Top Cover-Sliding Cover.png" width="80"> | 1 | PLA, 0.4mm Nozzle, 0.2mm Layer Height, 30% Infill |

#### Power Supply Assembly

The power supply assembly is divided into two main sections: the Front Cover and the Rear Cover.

##### 1. Front Cover Assembly

| Step | Operation Instructions | Image | Remarks |
|:---:|---|---|---|
| 1-1 | Prepare the parts and printed components required for front shell assembly | <img src="./Assembly_Steps/powerstep_images/1-1.png" width="80"> | Check that all parts are complete |
| 1-2 | Wiring sequence instructions for each part; assemble according to the wiring sequence | <img src="./Assembly_Steps/powerstep_images/1-2(1).png" width="80" style="margin-right:4%;"><img src="./Assembly_Steps/powerstep_images/1-2(2).png" width="80"><br><img src="./Assembly_Steps/powerstep_images/1-2(3).png" width="80"> | Connect strictly according to the wiring sequence |
| 1-3 | Install the XT60 connector | <img src="./Assembly_Steps/powerstep_images/1-3(1).png" width="80" style="margin-right:4%;"><img src="./Assembly_Steps/powerstep_images/1-3(2).png" width="80"> | Secure with 304 stainless steel Phillips countersunk head screws M3x8 and hex nuts M3x2.5 |
| 1-4 | Install the 3-in-1 IEC socket | <img src="./Assembly_Steps/powerstep_images/1-4(1).png" width="80" style="margin-right:4%;"><img src="./Assembly_Steps/powerstep_images/1-4(2).png" width="80"> | Secure the 3-in-1 IEC socket with 304 stainless steel Phillips pan head screws M3x8 |
| 1-5 | Internal wiring of the front shell | <img src="./Assembly_Steps/powerstep_images/1-5(1).png" width="80"><br><img src="./Assembly_Steps/powerstep_images/1-5(2).png" width="80"> | Check connections against the wiring sequence diagram |
| 1-6 | Secure both sides of the front shell and the power supply | <img src="./Assembly_Steps/powerstep_images/1-6(1).png" width="80" style="margin-right:4%;"><img src="./Assembly_Steps/powerstep_images/1-6(2).png" width="80"> | M4x6 304 stainless steel Phillips countersunk head screws x2 |
| 1-7 | Install the sliding cover | <img src="./Assembly_Steps/powerstep_images/1-7(1).png" width="80" style="margin-right:4%;"><img src="./Assembly_Steps/powerstep_images/1-7(2).png" width="80"> | Push in from the bottom of the power supply |
| 1-8 | Secure the sliding cover | <img src="./Assembly_Steps/powerstep_images/1-8.png" width="80"> | M4x6 304 stainless steel Phillips countersunk head screws x2 |

---

##### 2. Rear Shell Assembly

| Step | Operation Instructions | Image | Remarks |
|:---:|---|---|---|
| 2-1 | Prepare the parts and printed components required for rear shell assembly | <img src="./Assembly_Steps/powerstep_images/2-1.png" width="80"> | Check accessories for completeness |
| 2-2 | Assemble the rear shell with the power supply | <img src="./Assembly_Steps/powerstep_images/2-2.png" width="80"> | Align the position |
| 2-3 | Secure both sides of the rear shell and the power supply | <img src="./Assembly_Steps/powerstep_images/2-3(1).png" width="80" style="margin-right:4%;"><img src="./Assembly_Steps/powerstep_images/2-3(2).png" width="80"> | M4x6 304 stainless steel Phillips countersunk head screws x2 |

---

##### 3. Overall Completion

| Step | Operation Instructions | Image | Remarks |
|:---:|---|---|---|
| 1 | Power supply solution assembly completed | <img src="./Assembly_Steps/powerstep_images/3.png" width="80"> | Check that all screws are tightened |

---
