# 🤖 Especificación de hardware de código abierto de reBot DevArm


<p align="center">
  <img src="../../media/v1.1.png" alt="Banner de reBot-DevArm">
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


| Fecha | Versión | Nombre del archivo | Registro de cambios |
|----------|------|----------|------|
|  2026-03-31 | v1.0 |  reBot_B601_DM_v1.0_20260331.step  | Subida inicial |
|  2026-04-25 | v1.1 |  reBot_B601_DM_v1.1_20260425.step  | Se añaden sujeciones de cables para los 3 motores de las articulaciones del extremo, para evitar que se aflojen y se desconecten. Se corrige el modelo de la articulación 1 de 4310 a 4340P. Se añade la pieza CNC 02_Base_Reinforcement_Part.step en la parte inferior para reforzar la rigidez de la base. |
|  2026-10-30 | v1.1 |  reBot_B601_DM_v1.1_20260625.step  | Todos los arneses de cables se han sustituido por arneses personalizados moldeados de mejor calidad; los dos soportes impresos en 3D del antebrazo y la muñeca se han ajustado internamente para que los cables puedan pasar por las posiciones de los orificios. |


Esta BOM corresponde al brazo robótico reBot Arm B601 DM, que utiliza motores de la serie 43 de Damiao. La otra versión, el reBot Arm B601 RS, utiliza motores RobStride; [consulta su BOM aquí](../reBot_B601_RS/README.md).

# 📦 Estructura de archivos
*   3D_Printed_Parts/: archivos STEP de todas las piezas impresas en 3D.
*   Metal_Parts/: archivos STEP de todas las piezas metálicas mecanizadas por CNC.
*   Purchased_Parts/: archivos STEP de todos los componentes comprados.
*   reBot_B601_DM_v1.1_20260625.step: archivo del ensamblaje completo del brazo robótico (versión actual).

# 🛒[Consigue todas las piezas](https://www.seeedstudio.com/reBot-Arm-B601-DM-Bundle.html)
- Ofrecemos cinco opciones de kit:
  - **Kit de motores del cuerpo del brazo**: incluye solo los motores y los arneses de cableado del brazo robótico.
  - **Kit estructural del cuerpo del brazo**: incluye solo los componentes estructurales mecánicos.
  - **Kit completo de la pinza (gripper)**: incluye los motores, los arneses de cableado y los componentes estructurales de la pinza.
  - **Kit completo**: incluye el conjunto completo del cuerpo del brazo robótico y la pinza.
  - **Brazo robótico premontado**: brazo robótico acabado y totalmente montado.


# 📊 Lista de materiales (BOM)

> [!WARNING]
> Aviso: la BOM publicada **no** representa la versión final que envía Seeed. Esta v1.1 de código abierto está optimizada para que los desarrolladores puedan reproducirla con el mínimo coste, con algunos detalles no esenciales simplificados.
> La versión final de producción de Seeed incluirá grabado láser en el metal para evitar errores de montaje (poka-yoke), algunas piezas impresas en 3D se sustituirán por metal para mayor durabilidad, las holguras y tolerancias de mecanizado se ajustarán a la variabilidad de fábrica (equilibrando precisión y coste) y se añadirá cableado personalizado (p. ej., protección con malla trenzada) con coste adicional. No obstante, la estructura mecánica es idéntica.

---

## 🖨️ Piezas impresas en 3D

| Descripción de la pieza | Imagen | Nombre del archivo | Material | Cant. | Notas |
|----------|------|--------|------|----------|------|
| Plataforma base del brazo robótico | <img src="./3D_Printed_Parts/images/02-BASE.png" width="80"> | 01_BASE_Plate.step | ABS Bambu Lab negro | 1 | boquilla de 0.4 mm, altura de capa de 0.2 mm, relleno del 30% |
| Eslabón de la base del brazo robótico | <img src="./3D_Printed_Parts/images/02-BASE_02.png" width="80"> | 01_BASE_Link.step | ABS Bambu Lab negro | 1 | boquilla de 0.4 mm, altura de capa de 0.2 mm, relleno del 30% |
| Relleno izquierdo del brazo superior | <img src="./3D_Printed_Parts/images/02-DOWN_TRIM_1.png" width="80"> | 01_Upper_Arm_Fuller_L.step | PLA Bambu Lab negro y verde | 1 | boquilla de 0.4 mm, altura de capa de 0.2 mm, relleno del 15% |
| Relleno derecho del brazo superior | <img src="./3D_Printed_Parts/images/02-DOWN_TRIM_2.png" width="80"> | 01_Upper_Arm_Fuller_R.step | PLA Bambu Lab negro y verde | 1 | boquilla de 0.4 mm, altura de capa de 0.2 mm, relleno del 15% |
| Relleno central del brazo superior | <img src="./3D_Printed_Parts/images/02-DOWN-FILLING.png" width="80"> | 01_Upper_Arm_Fuller_M.step | ABS Bambu Lab negro | 1 | boquilla de 0.4 mm, altura de capa de 0.2 mm, relleno del 30% |
| Tope horizontal del brazo superior | <img src="./3D_Printed_Parts/images/02-SPACER-DOWN.png" width="80"> | 01_Upper_Arm_Limit.step | ABS Bambu Lab negro | 1 | boquilla de 0.4 mm, altura de capa de 0.2 mm, relleno del 30% |
| Asa del brazo | <img src="./3D_Printed_Parts/images/02-HANDLE.png" width="80"> | 01_Arm_Handle.step | ABS Bambu Lab negro | 1 | boquilla de 0.4 mm, altura de capa de 0.2 mm, relleno del 30% |
| Relleno izquierdo del brazo inferior | <img src="./3D_Printed_Parts/images/02-UP-TRIM_1.png" width="80"> | 01_Lower_Arm_Filler_L.step | PLA Bambu Lab negro y verde | 1 | boquilla de 0.4 mm, altura de capa de 0.2 mm, relleno del 15% |
| Relleno derecho del brazo inferior | <img src="./3D_Printed_Parts/images/02-UP-TRIM_2.png" width="80"> | 01_Lower_Arm_Filler_R.step | PLA Bambu Lab negro y verde | 1 | boquilla de 0.4 mm, altura de capa de 0.2 mm, relleno del 15% |
| Relleno central del brazo inferior | <img src="./3D_Printed_Parts/images/02-UP-FILLING.png" width="80"> | 01_Lower_Arm_Filler_M.step | ABS Bambu Lab negro | 1 | boquilla de 0.4 mm, altura de capa de 0.2 mm, relleno del 30% |
| Cubierta del brazo superior | <img src="./3D_Printed_Parts/images/02-DOWN-COVER.png" width="80"> | 01_Upper_Arm_Cover.step | PLA Bambu Lab verde | 1 | boquilla de 0.4 mm, altura de capa de 0.2 mm, relleno del 15% |
| Cubierta del brazo inferior | <img src="./3D_Printed_Parts/images/02-UP-COVER.png" width="80"> | 01_Lower_Arm_Cover.step | PLA Bambu Lab verde | 1 | boquilla de 0.4 mm, altura de capa de 0.2 mm, relleno del 15% |
| Cubierta de protección del motor 5 | <img src="./3D_Printed_Parts/images/02-MOTOR-COVER.png" width="80"> | 01_Motor_Cover.step | ABS Bambu Lab negro | 1 | boquilla de 0.4 mm, altura de capa de 0.2 mm, relleno del 30% |
| Tope horizontal de la pinza | <img src="./3D_Printed_Parts/images/02-SPACER.png" width="80"> | 01_Lower_Arm_Limit.step | PLA Bambu Lab verde | 1 | boquilla de 0.4 mm, altura de capa de 0.2 mm, relleno del 15% |
| Soporte del carro de la pinza | <img src="./3D_Printed_Parts/images/02-3D-RAIL-BRACKET.png" width="80"> | 01-Rail-Bracket.step | PLA Bambu Lab verde | 1 | boquilla de 0.4 mm, altura de capa de 0.2 mm, relleno del 15% |
| Dedo de la pinza | <img src="./3D_Printed_Parts/images/02-CLIP_1.png" width="80"> | 01_Finger.step | ABS Bambu Lab negro | 2 | boquilla de 0.4 mm, altura de capa de 0.2 mm, relleno del 45% |
| Sujeción de cables del motor 5 | <img src="./3D_Printed_Parts/images/01_Joint5_Cable Restraint_A.png" width="80"> | 01_Joint5_Cable Restraint_A.step | PLA Bambu Lab verde | 1 | boquilla de 0.4 mm, altura de capa de 0.2 mm, relleno del 15% |
| Sujeción de cables A de los motores 6 y 7 | <img src="./3D_Printed_Parts/images/01_Joint6_7_Cable Restraint_A.png" width="80"> | 01_Joint6_7_Cable Restraint_A.step | ABS Bambu Lab negro | 2 | boquilla de 0.4 mm, altura de capa de 0.2 mm, relleno del 30% |
| Sujeción de cables B de los motores 6 y 7 | <img src="./3D_Printed_Parts/images/01_Joint6_7_Cable Restraint_B.png" width="80"> | 01_Joint6_7_Cable Restraint_B.step | ABS Bambu Lab negro | 2 | boquilla de 0.4 mm, altura de capa de 0.2 mm, relleno del 30% |
| - | Precio de referencia | Promedio **50 $** | | | El precio varía según el coste del material y el tiempo de impresión |

El roce continuado del arnés de cableado del motor 1 puede desgastar el conector del motor y provocar un mal contacto eléctrico. Imprimir las piezas que se indican a continuación puede mitigar este riesgo.

| Descripción de la pieza | Imagen | Nombre del archivo | Material | Cant. | Notas |
| ---- | ---- | ---- | ---- | ---- | ---- |
| Clips de arnés de cableado para ambos lados del motor 1 | <img src="./3D_Printed_Parts/images/DM_Motor1_wiring_harness_clip.jpg" width="80"> | `DM_Motor1_wiring_harness_clip.stp` | ABS Bambu Lab negro | 2 | boquilla de 0.4 mm, altura de capa de 0.2 mm, relleno del 30% |

## 📷 Soporte de cámara compatible

| Descripción de la pieza | Imagen | Nombre de archivo | Material | Cant. | Notas |
|----------|------|--------|------|----------|------|
| [Orbbec Gemini2](https://www.seeedstudio.com/Orbbec-Gemini-2-3D-Camera-p-6464.html) | <img src="./3D_Printed_Parts/images/Gemini2_mount.png" width="80"> | [`D435_Gemini2_Mount.step`](../camera-mounts/b601-camera-mounts/D435_Gemini2_Mount.step) | Bambu ABS Negro | 1 | Boquilla 0.4 mm, altura de capa 0.2 mm, relleno 30 % |

Los soportes de cámara de muñeca B601 son comunes a **B601-RS y B601-DM**. Los modelos, las vistas previas y las descargas están en el [catálogo compartido de soportes (en inglés)](../camera-mounts/README.md).

### 🧩 Recomendaciones de impresión
- Altura de capa: 0.2 mm
- Boquilla: 0.4 mm
- Soportes: añadir según sea necesario
- Materiales: las piezas sometidas a altas temperaturas y a carga se imprimen en ABS con un relleno del 30–80%; también pueden usarse nailon o materiales reforzados con fibra de carbono. Las piezas estéticas se imprimen en PLA con un relleno del 15%.
- Materiales recomendados para las piezas portantes: ABS con relleno del 30–80%, nailon o materiales reforzados con fibra de carbono

---

## 🔩 Piezas metálicas mecanizadas por CNC

> [!WARNING]
> Algunas piezas que pueden sustituirse por impresión 3D se indican en las notas, lo que puede reducir los costes considerablemente.

| Descripción de la pieza | Imagen | Nombre del archivo | Material | Cant. | Mecanizado | Notas |
|----------|------|--------|----------|------|------|------|
| Soporte del rodamiento del motor 1 | <img src="./Metal_Parts/images/02_Base_Reinforcement_Part.png" width="80"> | 02_Base_Reinforcement_Part.step | Aleación de aluminio 5052 | 1 | CNC | Puede imprimirse en 3D en ABS con relleno alto para reducir el coste |
| Eje de rotación del motor 1 | <img src="./Metal_Parts/images/02_Arm_Yaw_Limit.png" width="80"> | 02_Arm_Yaw_Limit.step | Aleación de aluminio 5052 | 1 | CNC | Añade un límite de movimiento del ángulo de guiñada |
| Espaciador delantero de los motores 2–5 | <img src="./Metal_Parts/images/02_Motor_Front_Spacer.png" width="80"> | 02_Motor_Front_Spacer.step | Aleación de aluminio 5052 | 4 | CNC | Puede imprimirse en 3D en ABS con relleno del 30% |
| Espaciador trasero de los motores 2–4 | <img src="./Metal_Parts/images/02_Motor_Back_Spacer.png" width="80"> | 02_Motor_Back_Spacer.step | Aleación de aluminio 5052 | 3 | CNC | |
| Brida trasera de los motores 2–4 | <img src="./Metal_Parts/images/02_FLANGE.png" width="80"> | 02_FLANGE.step | Aleación de aluminio 5052 | 3 | CNC | |
| Soporte del motor 5 de la muñeca | <img src="./Metal_Parts/images/02_Wrist_Bracket.png" width="80"> | 02_Wrist_Bracket.step | Aleación de aluminio 5052 | 1 | CNC | |
| Conector A de la pinza | <img src="./Metal_Parts/images/02_Gripper_Connector_A.png" width="80"> | 02_Gripper_Connector_A.step | Aleación de aluminio 5052 | 1 | CNC | |
| Conector B de la pinza | <img src="./Metal_Parts/images/02_Gripper_Connector_B.png" width="80"> | 02_Gripper_Connector_B.step | Aleación de aluminio 5052 | 1 | CNC | |
| Soporte metálico del carro de la pinza | <img src="./Metal_Parts/images/02_Slider_Bracket.png" width="80"> | 02_Slider_Bracket.step | Aleación de aluminio 5052 | 1 | CNC | Puede imprimirse en 3D en ABS con relleno alto; no recomendado para uso prolongado |
| Extensión del carro a la pinza | <img src="./Metal_Parts/images/02_Slider_Extension.png" width="80"> | 02_Slider_Extension.step | Aleación de aluminio 5052 | 2 | CNC | |
| Eslabón izquierdo entre brazo superior e inferior | <img src="./Metal_Parts/images/02_Lower_Upper_Link_L.png" width="80"> | 02_Lower_Upper_Link_L.step | Aleación de aluminio 5052 | 1 | CNC | |
| Eslabón derecho entre brazo superior e inferior | <img src="./Metal_Parts/images/02_Lower_Upper_Link_R.png" width="80"> | 02_Lower_Upper_Link_R.step | Aleación de aluminio 5052 | 1 | CNC | |
| Eslabón izquierdo entre brazo inferior y muñeca | <img src="./Metal_Parts/images/02_Lower_Wrist_Link_L.png" width="80"> | 02_Lower_Wrist_Link_L.step | Aleación de aluminio 5052 | 1 | CNC | |
| Eslabón derecho entre brazo inferior y muñeca | <img src="./Metal_Parts/images/02_Lower_Wrist_Link_R.png" width="80"> | 02_Lower_Wrist_Link_R.step | Aleación de aluminio 5052 | 1 | CNC | |
| Conector del engranaje | <img src="./Metal_Parts/images/02_Gear_Connector.png" width="80"> | 02_Gear_Connector.step | Aleación de aluminio 5052 | 1 | CNC | |
| Cremallera | <img src="./Metal_Parts/images/Rack.png" width="80"> | 02_Rack.step | Aleación de aluminio 5052 | 2 | CNC | |
| Eslabón 1 | <img src="./Metal_Parts/images/Link1.png" width="80"> | 03_Link1.step | Aleación de aluminio 5052 | 1 | CNC + chapa metálica | |
| Eslabón 2 | <img src="./Metal_Parts/images/Link2.png" width="80"> | 03_Link2.step | Aleación de aluminio 5052 | 2 | CNC + chapa metálica | |
| Eslabón 3 izquierdo | <img src="./Metal_Parts/images/Link3_L.png" width="80"> | 03_Link3_L.step | Aleación de aluminio 5052 | 1 | CNC + chapa metálica | |
| Eslabón 3 derecho | <img src="./Metal_Parts/images/Link3_R.png" width="80"> | 03_Link3_R.step | Aleación de aluminio 5052 | 1 | CNC + chapa metálica | |
| Eslabón 5 | <img src="./Metal_Parts/images/Link5.png" width="80"> | 03_Link5.step | Aleación de aluminio 5052 | 1 | CNC + chapa metálica | |
| - | Precio de referencia de mercado | Promedio **250 $** | | | El precio varía según el coste del aluminio, los requisitos de tolerancia y el plazo de entrega |

### 🧩 Especificaciones de mecanizado
- Tolerancia de las cotas clave: ±0.02 mm GB/T1840-M
- Acabado superficial: anodizado / arenado
- Se recomienda usar H7 / ajuste por interferencia en las piezas de acoplamiento
---

## 🛒 Piezas compradas (piezas estándar)

> [!WARNING]
> Dado que cada uno tendrá que montar y apretar los tornillos por su cuenta, se han elegido tornillos Allen estándar. Tras un funcionamiento prolongado, los tornillos pueden aflojarse, lo que afectará a la precisión del brazo robótico. Por este motivo, debes comprar adicionalmente pegamento termofusible para fijar las roscas de los tornillos de cada articulación.

Si tienes un taladro eléctrico o herramientas similares, puedes optar por comprar arandelas de bloqueo o tornillos con freno de rosca. No obstante, **es sumamente importante** que uses el ajuste de par más bajo al utilizar un atornillador eléctrico para evitar que los tornillos se pasen de rosca, lo que provocaría daños irreversibles.


  | Nombre | Especificación / Modelo | Cantidad | Precio de referencia | Notas |
  |------|----------|------|----------|------|
  | Motor sin escobillas | DM4310(V4) | 4 | 120 $/unidad | [SeeedStudio](https://www.seeedstudio.com/Damiao-4310-Actuator-Motor-p-6823.html) |
  | Motor sin escobillas | DM4340P(V4) | 3 | 175 $/unidad |  [SeeedStudio](https://www.seeedstudio.com/DM4340P-Actuator-p-6663.html)  |
  | Placa driver CAN-USB |  | 1 | 15 $/unidad |   [SeeedStudio](https://www.seeedstudio.com/DM-CAN-USB-Driver-Borad-p-6706.html)   |
  | Rodamiento | 6707ZZ | 1 | 13 $/unidad | [Amazon](https://www.amazon.com/uxcell-35x44x5mm-Shielded-Precision-Lubricated/dp/B0D6WBMW3F/ref=sr_1_1?crid=3J03FBU7MI31J&dib=eyJ2IjoiMSJ9.sfX192-ZSyqh-VJEgq6jR02DrJcdVTxBbKWn5TLypwoK7NyklXkZSQT-3V42_zTm98_Y8dLCtnTzJ9JVnPuBG7bfvUYv0ctrasWhZgU5DFtl2y0CtKLOUOoukmlHqCfonkjZLapmfzSVAaV-3CJYhqizbjedl6zGoDUNo2ryKd4RbtRhJXndBmf96HwTPrPH8g8KB2NPyhnPaP36r6C0Ehdb0xrqjNzKt7YcM7xkZ_8.QvCzMQ0EPe3-5SBYNcuoO5L-Yx0CSr9Vmjc-Ma7FzbY&dib_tag=se&keywords=6707ZZ&qid=1774771772&sprefix=6707zz%2Caps%2C376&sr=8-1) |
  | Rodamiento | 6803ZZ | 3 | 13 $/unidad | [Amazon](https://www.amazon.com/uxcell-17x26x5mm-Shielded-Precision-Lubricated/dp/B0D54JSWBZ/ref=sr_1_1?crid=17L94NDI1JCC0&dib=eyJ2IjoiMSJ9.xH_s9Ui7VlS40EZvr-HektqY3VOJsM-VjyE6JaJEScIWuFZ2UYSM7G8j1fC0HSmbb7YlA0YfUxxCkUzBptwrEEdEHsP94TGplNpPAWwhnH8b76HapXR_uHbr1vu3xe0AYSYP30Quk9LMQrGjUh84bXL82z2mORuiri0VHqo5DmSguK0cHubmVaXtbR_eJ43Z7L2nNqWfgltqzmHsYm7DQvrnIBg9UMlD1o9559nCSKA.E_N7CDPQhShckT-1vHDhYvNgiqRKusa12d43hqATQ5A&dib_tag=se&keywords=6803ZZ&qid=1774771801&sprefix=6803zz%2Caps%2C397&sr=8-1) |
  | Rodamiento | AXK5578 | 1 | 12 $/unidad | [Amazon](https://www.amazon.com/PZRT-AXK5578-Thrust-Bearings-Washers/dp/B0B3M3RZGW/ref=sr_1_1?dib=eyJ2IjoiMSJ9.TatYkzOvpYAJ5K23C7Qr9JKJsPhpJE8p1L3k5_1YqQ7ozSLNgOBEeG9pTYz-WXOWiHkbJq_zZR4FxNHAJZ4euyfOGXkOKycOyN0pUD0_WkJia0PekbRy0sYvyQbE7KZByR-40WiPSPuUcysFewSngPoDGQZzESFOUz__V9ViGCIQAPfdUe2OxVpvtbKZYCQsrSDm8b8okR25bavCvpDbBfPh0He2PEBEpl55L8RtYKmlv62XJyfYT1o29A7wO5n8-g3hpJOrKmmWCybdEEWSmquAT1cjvsPTJDaT_TICsso.6xR5pEGJgTR-u_NOyXxi8VTphoLytGd8zugy1-xu-fE&dib_tag=se&keywords=AXK5578&qid=1774771826&sr=8-1&th=1) |
  | Guía lineal | MGN9-170mm | 1 | 23 $/unidad | [Amazon](https://www.amazon.com/uxcell-Sliding-Carriage-Bearing-Printers/dp/B0D54L45WM/ref=sr_1_1?dib=eyJ2IjoiMSJ9.qNphfY5r4UgLDHslIliMBhC45qBKTl37lJseObJSBp79RJ4VJnAH-lYAMo-rwPiu_uqWmkN7ms4kfAokYvod1seWb5-z2_kVgVuzrCXdiRycNXjrdv3qi5Awuno0_vEqjT4WJ569tAmqm_Rujrdxss7VfpLizFxq6-R8DucuvqZ0M0Y4go9PzRFEFPu4csskz7-UkM1CUidHoKmrT-I7R1Ta0dijj2SYlR_zW0si75k.nRJTebbqw-bFyzkdU8MztHnGdt9qwnHr_gIqa-MDxEQ&dib_tag=se&keywords=MGN9&qid=1774771864&sr=8-1) |
  | Carro | MGN9 | 2 | 10 $/unidad | [Amazon](https://www.amazon.com/uxcell-Bearing-Sliding-Carriage-Anti-Fall/dp/B0D9QBQDKB/ref=sr_1_8?dib=eyJ2IjoiMSJ9.qNphfY5r4UgLDHslIliMBhC45qBKTl37lJseObJSBp79RJ4VJnAH-lYAMo-rwPiu_uqWmkN7ms4kfAokYvod1seWb5-z2_kVgVuzrCXdiRycNXjrdv3qi5Awuno0_vEqjT4WJ569tAmqm_Rujrdxss7VfpLizFxq6-R8DucuvqZ0M0Y4go9PzRFEFPu4csskz7-UkM1CUidHoKmrT-I7R1Ta0dijj2SYlR_zW0si75k.nRJTebbqw-bFyzkdU8MztHnGdt9qwnHr_gIqa-MDxEQ&dib_tag=se&keywords=MGN9&qid=1774771864&sr=8-8) |
  | Engranaje | Módulo 1, tipo cubo, 16 dientes, agujero de 6 mm | 1 | 44 $/unidad | [Amazon](https://www.amazon.com/Module-15-Teeth-Finished-Perforation/dp/B0GDSR1LKM/ref=sr_1_1?crid=2EN1YHE8TEC58&dib=eyJ2IjoiMSJ9.54N73iSlush8K1a_teRazjBGZaQnbFM4MLysEbIq430CEYcVs0slm8KhpC_JlmjyVMocPA3vLANjERYZWweRag36NhX2GGldVTpd31kAWW4.ws8l0qBABmSVrUGX4g2o3sBbUgOnNhl3Nx_Nt-d1HT8&dib_tag=se&keywords=1%2Bmodule16%2Bteeth&qid=1774772022&sprefix=1%2BModule16%2Bteeth%2Caps%2C403&sr=8-1&th=1)  |
  | Almohadilla de silicona | 30x9x2mm | 1 | 10 $ | [Amazon](https://www.amazon.com/Self-Adhesive-Anti-Sliding-Anti-Scratch-Protectors-Appliances/dp/B0F9KVYXFZ/ref=sr_1_3?crid=LVY2LLBFQT6J&dib=eyJ2IjoiMSJ9.4qjOEtjEph1QxS_kJF2vIYqvD_8Lzt4GZ2rrywWbrAhniBvp_8YrEsVNcCPQofO4jVqBxFE8Yplyg2XXgAXlUZwzqE-Gp8MYcaPmphL8Mc1n-ARSCNaTq5gc7ZIWsS6u-kR0G2BzIlBo6NF88KvASjKYJfTHpPXHfNCPVw13P-PseVbUZwlVAO9zMHa3a84gHRd-I-mGB8SCmek9mXjN-c-bFxKvJXlz4C5YBBdt9cH3QkSmLgiLZ_iD4K1mh-MwI5WuVOXr5ZOwJ0bVpmHpc_vpbKLr7CkVack3nsC-TM0.40ujhwS5ConOfA8io_c5hcdos70HOKjMFqqKLKgNwI8&dib_tag=se&keywords=silicone%2Bsticker&qid=1774772199&sprefix=silicone%2Bsticker%2Caps%2C380&sr=8-3&th=1) |
  | Tornillo | Tornillo HM3-12mm | 14+ |  | [Amazon](https://www.amazon.com/BNUOK-120pcs-Stainless-Threads-Spanner/dp/B0DJQGMQZM/ref=sr_1_4?crid=3J1D711FNBYR9&dib=eyJ2IjoiMSJ9.wo20uXEJsuYS5OBVpnH9TILDd6HtQrJUlEvvYFPE5VV6bozIiRlWwmDaoYnp345KjXwRyxbEgEaRD8gVD2vVhPXg3M266n3H8t9cWN518aR4c5WkFUkqLIqLwdGYBllKcQQ8agsrZYgSVFp9G8LJR4l9oAj8Yx4QN8MReo2k23RVk-lkWeJk1azXD88GFTmd17aiXz6fwOE45Krj4VRiy1oskx8QvMprmJXtH8KowAJo-pWdBtePCCIUUa8oLR78hi17yW_OGJattIwdAziX9RizLI-EMh3hku42WJWnb3g.lZYqsYfJunSoEUPNT04E1sFhPiudREmrI0919PaPBYI&dib_tag=se&keywords=screw+HM3-12mm&qid=1776330531&s=industrial&sprefix=screw+hm3-12mm%2Cindustrial%2C475&sr=1-4) |
  | Tornillo | Tornillo HM3-25mm | 14+ |  | [Amazon](https://www.amazon.com/BNUOK-120pcs-Stainless-Threads-Spanner/dp/B0DJQFGRPQ/ref=sr_1_4?crid=3J1D711FNBYR9&dib=eyJ2IjoiMSJ9.wo20uXEJsuYS5OBVpnH9TILDd6HtQrJUlEvvYFPE5VV6bozIiRlWwmDaoYnp345KjXwRyxbEgEaRD8gVD2vVhPXg3M266n3H8t9cWN518aR4c5WkFUkqLIqLwdGYBllKcQQ8agsrZYgSVFp9G8LJR4l9oAj8Yx4QN8MReo2k23RVk-lkWeJk1azXD88GFTmd17aiXz6fwOE45Krj4VRiy1oskx8QvMprmJXtH8KowAJo-pWdBtePCCIUUa8oLR78hi17yW_OGJattIwdAziX9RizLI-EMh3hku42WJWnb3g.lZYqsYfJunSoEUPNT04E1sFhPiudREmrI0919PaPBYI&dib_tag=se&keywords=screw%2BHM3-12mm&qid=1776330531&s=industrial&sprefix=screw%2Bhm3-12mm%2Cindustrial%2C475&sr=1-4&th=1)  |
  | Tornillo | Tornillo HM3-6mm | 16+ |  | [Amazon](https://www.amazon.com/BNUOK-120pcs-Stainless-Threads-Spanner/dp/B0DJQG5YLF/ref=sr_1_4?crid=3J1D711FNBYR9&dib=eyJ2IjoiMSJ9.wo20uXEJsuYS5OBVpnH9TILDd6HtQrJUlEvvYFPE5VV6bozIiRlWwmDaoYnp345KjXwRyxbEgEaRD8gVD2vVhPXg3M266n3H8t9cWN518aR4c5WkFUkqLIqLwdGYBllKcQQ8agsrZYgSVFp9G8LJR4l9oAj8Yx4QN8MReo2k23RVk-lkWeJk1azXD88GFTmd17aiXz6fwOE45Krj4VRiy1oskx8QvMprmJXtH8KowAJo-pWdBtePCCIUUa8oLR78hi17yW_OGJattIwdAziX9RizLI-EMh3hku42WJWnb3g.lZYqsYfJunSoEUPNT04E1sFhPiudREmrI0919PaPBYI&dib_tag=se&keywords=screw%2BHM3-12mm&qid=1776330531&s=industrial&sprefix=screw%2Bhm3-12mm%2Cindustrial%2C475&sr=1-4&th=1)  |
  | Tornillo | Tornillo prisionero HM4-75mm | 4+ |  | [Amazon](https://www.amazon.com/iexcell-Partially-Threaded-Thread-Socket/dp/B0DR1NX178/ref=sr_1_1?crid=35DT1MLQCOR9C&dib=eyJ2IjoiMSJ9.RlFuoSyG6Yoi2cmVkd0sQ47UpPY4y8uvofyrje4Ha76Dj6dcpknwvFT7DGc5jFqxw5Zd5g4SV-yre7xcMb3WB7MbBowQO3ZzvCgpYWcJ2xzphgz9gx0SNIr_ggqvFcAmxkNuMMVf0p9vPY-jJ2j9cbIk8IwMHlTo6kkuBINPotouNNyElpiy9qHhllwajmKY5v5uDIzJKNJvmhpUtJsd5IS7TB9VaRPkzsDbMDfR4pvs4JgNbU1Zmcu4Ex9fYcRHrOGjAZbbvNxo1r_N5MBKWbxbtZEDDKP_8Oyhgakhhnc.MTLa-_9PBksy6Qge1YqQmlejVfLKkuxB9gT-ZnB9ek0&dib_tag=se&keywords=screw+HM4-75&qid=1776330730&s=industrial&sprefix=screw+m4-75%2Cindustrial%2C401&sr=1-1)  |
  | Tornillo | Tornillo KM3*12mm | 30+ |  |  [Amazon](https://www.amazon.com/Uxcell-a16011300ux0872-M3x12mm-Carbon-Countersunk/dp/B01E6EIC2S/ref=sr_1_1?crid=2VJKS347LBDWD&dib=eyJ2IjoiMSJ9.eXF2FHahloRY0Kq8sM_EkJUm7ipUgMoVSuTAPjt3ZnAINqLrPQz9A55XDHfe00KPGG3Sr1IJJQloiw7IFwewoPsbdnKBZH5JjT4Ijy_bUXju1IvrHWP4nWeYW1o29jlbHBKEa3fPl8-JzEHr9RPKe5h_Dr1vN6VFMUfszTDEzufQrIi22AsKCMTep5n0-IR7AIc7Fai93nmr4ax8USKGOD_3yu4ri0p8ClPTZzfwmDJvnTpE9J9PNN8uA-wDz72RADQu2VLry_mvb5CA1JV0vHP49Qsy-96MKXo-j3vT8m0.DWiT1Loy7A-MeTveRzxU47S6WCKwnW6MVnmpF256j-s&dib_tag=se&keywords=screw+KM3*12&qid=1776330785&s=industrial&sprefix=screw+km3+%2Cindustrial%2C984&sr=1-1) |
  | Tornillo | Tornillo KM3*16mm | 34+ |  | [Amazon](https://www.amazon.com/Uxcell-a16011300ux0872-M3x12mm-Carbon-Countersunk/dp/B01E6EIC2S/ref=sr_1_1?crid=2VJKS347LBDWD&dib=eyJ2IjoiMSJ9.eXF2FHahloRY0Kq8sM_EkJUm7ipUgMoVSuTAPjt3ZnAINqLrPQz9A55XDHfe00KPGG3Sr1IJJQloiw7IFwewoPsbdnKBZH5JjT4Ijy_bUXju1IvrHWP4nWeYW1o29jlbHBKEa3fPl8-JzEHr9RPKe5h_Dr1vN6VFMUfszTDEzufQrIi22AsKCMTep5n0-IR7AIc7Fai93nmr4ax8USKGOD_3yu4ri0p8ClPTZzfwmDJvnTpE9J9PNN8uA-wDz72RADQu2VLry_mvb5CA1JV0vHP49Qsy-96MKXo-j3vT8m0.DWiT1Loy7A-MeTveRzxU47S6WCKwnW6MVnmpF256j-s&dib_tag=se&keywords=screw+KM3*12&qid=1776330785&s=industrial&sprefix=screw+km3+%2Cindustrial%2C984&sr=1-1)  |
  | Tornillo | Tornillo KM3*7mm | 76+ |  |[Amazon](https://www.amazon.com/Uxcell-a16011300ux0872-M3x12mm-Carbon-Countersunk/dp/B01E6EIC2S/ref=sr_1_1?crid=2VJKS347LBDWD&dib=eyJ2IjoiMSJ9.eXF2FHahloRY0Kq8sM_EkJUm7ipUgMoVSuTAPjt3ZnAINqLrPQz9A55XDHfe00KPGG3Sr1IJJQloiw7IFwewoPsbdnKBZH5JjT4Ijy_bUXju1IvrHWP4nWeYW1o29jlbHBKEa3fPl8-JzEHr9RPKe5h_Dr1vN6VFMUfszTDEzufQrIi22AsKCMTep5n0-IR7AIc7Fai93nmr4ax8USKGOD_3yu4ri0p8ClPTZzfwmDJvnTpE9J9PNN8uA-wDz72RADQu2VLry_mvb5CA1JV0vHP49Qsy-96MKXo-j3vT8m0.DWiT1Loy7A-MeTveRzxU47S6WCKwnW6MVnmpF256j-s&dib_tag=se&keywords=screw+KM3*12&qid=1776330785&s=industrial&sprefix=screw+km3+%2Cindustrial%2C984&sr=1-1)   |
  | Tornillo | Tornillo KM3*9mm | 31+ |  |[Amazon](https://www.amazon.com/Uxcell-a16011300ux0872-M3x12mm-Carbon-Countersunk/dp/B01E6EIC2S/ref=sr_1_1?crid=2VJKS347LBDWD&dib=eyJ2IjoiMSJ9.eXF2FHahloRY0Kq8sM_EkJUm7ipUgMoVSuTAPjt3ZnAINqLrPQz9A55XDHfe00KPGG3Sr1IJJQloiw7IFwewoPsbdnKBZH5JjT4Ijy_bUXju1IvrHWP4nWeYW1o29jlbHBKEa3fPl8-JzEHr9RPKe5h_Dr1vN6VFMUfszTDEzufQrIi22AsKCMTep5n0-IR7AIc7Fai93nmr4ax8USKGOD_3yu4ri0p8ClPTZzfwmDJvnTpE9J9PNN8uA-wDz72RADQu2VLry_mvb5CA1JV0vHP49Qsy-96MKXo-j3vT8m0.DWiT1Loy7A-MeTveRzxU47S6WCKwnW6MVnmpF256j-s&dib_tag=se&keywords=screw+KM3*12&qid=1776330785&s=industrial&sprefix=screw+km3+%2Cindustrial%2C984&sr=1-1)   |
  | Tornillo | Tornillo KM3*8mm de cabeza baja con hueco hexagonal (Socket Micro Profile Head) | 31+ |  |[Amazon](https://www.amazon.com/SMALLRIG-Screw-Screws-12pcs-Pack/dp/B01MS60KSY/ref=sr_1_1?dib=eyJ2IjoiMSJ9.YfdPTE5UVJAg4SZcWMUPtQ.OCxr-8hnCbGnQsQiwM8fg8xJifzrC4-EMmKpeYyr0Zg&dib_tag=se&keywords=Socket%2BMicro%2BProfile%2BHead%2BScrew&qid=1776336031&refinements=p_n_feature_two_browse-bin%3A2292870011&rnid=2292859011&sr=8-1&xpid=BZ-yllUUAy02h&th=1)   |
  | Tornillo | KA3*12mm | 72+ |  | [Amazon](https://www.amazon.com/uxcell-Phillips-Tapping-Screws-Silver/dp/B01MXSS95N/ref=sr_1_3?crid=2RJ5ZBG0M4EX5&dib=eyJ2IjoiMSJ9.v9AtN0DrK0YdOT84Puh29n1VDClJz4OwvslbH610w0_xJIkuVFk81UxgSw_lSRbHugpqkja4rz-elY-DHbh0KN4GCFH2MlZhRFjXVE1vlaChALTqgr9jxatNPvPTf8SzdxFoEMEPm3jwCnC8vqLq5xL-Wr414hMsTbVYxv_ZVmEbMV-8YYXhLWiOz9EivU2C8jWw0RFSwVtUxqhj7qgBBYV5QbJRNr1XdWmQsICMHTHy35DeIcLjyKtXOb0gEwDNyqqmdvS5LfJJaLQchjLpW1jondo5xapQVw8gWJ4yYjk.oXwiRL9W52Tlu7tMi7tT9i7g-CBYfw_AAT1LURe2Q7k&dib_tag=se&keywords=screw+ka3*12&qid=1776331569&s=industrial&sprefix=screw+ka3+%2Cindustrial%2C466&sr=1-3)  |
  | Pasador cilíndrico | M4*8mm | Varios |  | [Amazon](https://www.amazon.com/HARFINGTON-Stainless-Cylindrical-Furniture-Installation/dp/B0F6CWL4MP/ref=sr_1_6?crid=2BZ4J412S4QSB&dib=eyJ2IjoiMSJ9.a3kVMi6W355gYKjK1Sl_QFVcJD8x7DTXqxgk66DoY4TnPOEV9TG7AbW7jkNk2USTJrqrb3e5Ve0EeVwHVE-_s-UUP6jFahdiVAqkZGGnuBpVxwA-MCHYQEwThEfygwAc1HVyN1n7Cvr8GAFMvs5AfciRrbUZ8AsSNGc1Obgf8qouOe8NQhyW_Zo7YINX1m3YCuTRiLZCvB6o7XlZtZ4PRh085Bva6AjjnlNOuaiPCtzjvNUtTpyLpGmqoHM165V6onFghMcuOX9RaacnxQNsRoUtKpWPEB8h48nUnUOJ1lg.Hfy_mUj7QFR_kILC4I5RNy6h7HmdswULHg3NmKmK8bU&dib_tag=se&keywords=Dowel%2Bpin%2BM4*7&qid=1776331648&s=industrial&sprefix=dowel%2Bpin%2Bm4%2B%2Cindustrial%2C399&sr=1-6&th=1)  |
  | Pasador cilíndrico | M4*12mm | Varios |  | [Amazon](https://www.amazon.com/HARFINGTON-Stainless-Cylindrical-Furniture-Installation/dp/B0F6CWL4MP/ref=sr_1_6?crid=2BZ4J412S4QSB&dib=eyJ2IjoiMSJ9.a3kVMi6W355gYKjK1Sl_QFVcJD8x7DTXqxgk66DoY4TnPOEV9TG7AbW7jkNk2USTJrqrb3e5Ve0EeVwHVE-_s-UUP6jFahdiVAqkZGGnuBpVxwA-MCHYQEwThEfygwAc1HVyN1n7Cvr8GAFMvs5AfciRrbUZ8AsSNGc1Obgf8qouOe8NQhyW_Zo7YINX1m3YCuTRiLZCvB6o7XlZtZ4PRh085Bva6AjjnlNOuaiPCtzjvNUtTpyLpGmqoHM165V6onFghMcuOX9RaacnxQNsRoUtKpWPEB8h48nUnUOJ1lg.Hfy_mUj7QFR_kILC4I5RNy6h7HmdswULHg3NmKmK8bU&dib_tag=se&keywords=Dowel%2Bpin%2BM4*7&qid=1776331648&s=industrial&sprefix=dowel%2Bpin%2Bm4%2B%2Cindustrial%2C399&sr=1-6&th=1)  |
  | Juego de destornilladores | Juego de llaves hexagonales | 1 | 16 $  | [Amazon](https://www.amazon.com/Amazon-Basics-Ratcheting-Electronics-Screwdriver/dp/B07V4TFWFZ/ref=sr_1_2?crid=ADAY70RZDSLN&dib=eyJ2IjoiMSJ9.jcLL4o6IXTnPlPfTTzbCZCBuZx2sLkvdUQCwlL58aq__GOyLxVPnwLI0mvGptba_HeVz6ctLQ_ziQw56BMDH9IOaw-4PVJGMktQM74mWficwggm3ckDGyAH-agN_zkB3K0_W-wrS56jfcMYFbZSWhWxr-iSOC4sdXwMGlt4rYGtenyn9yAFYBIHqjU2El5_OAKuspsrF0yQvfyfQPQHs46SClWN8zlSemGVZRuVSU26f0f9yApF6BfWHANKNNhT0Mfb6bQ8oM2XUMvwaazrrKoHeTARuoflVaVZvMU776bs.r8gy_gMINEy0qy4JyK--z-IbPZEv-SWeMGohOOE7M60&dib_tag=se&keywords=Screwdriver+set&qid=1774772499&s=industrial&sprefix=screwdriver+set+%2Cindustrial%2C374&sr=1-2)  |
  | <img src="./Purchased_Parts/XT30_2+2.png" width="80"> | XT30 2+2 350mm | 2 | 4 $/cable | Ambos extremos en ángulo |
  | <img src="./Purchased_Parts/XT30_2+2.png" width="80"> | XT30 2+2 350mm | 1 | 4 $/cable | Un extremo en ángulo y otro recto |
  | <img src="./Purchased_Parts/XT30_2+2.png" width="80"> | XT30 2+2 200mm | 3 | 4 $/cable | Ambos extremos en ángulo |
  | <img src="./Purchased_Parts/XT30_2+2.png" width="80"> | XT30 2+2 200mm | 1 | 3 $/cable | Ambos extremos rectos |


### Sobre la fijación
Puedes modificar libremente la base a partir de las piezas impresas en 3D que proporcionamos. También puedes usar sargentos en G según el grosor de tu mesa.

  | Nombre | Especificación / Modelo | Cantidad | Precio de referencia | Notas |
  |------|----------|------|----------|------|
  | Sargento de carpintería | Sargento en G de 6 pulgadas | 2 | 20 $/unidad | [Amazon](https://www.amazon.com/gp/aw/d/B092J1YW2M/?_encoding=UTF8&pd_rd_plhdr=t&aaxitk=3557c048ce58e7dbb50b40c3af69f1d6&hsa_cr_id=0&qid=1774772748&sr=1-1-9e67e56a-6f64-441f-a281-df67fc737124&ref_=sbx_s_sparkle_sbtcd_asin_0_img&pd_rd_w=bNqtC&content-id=amzn1.sym.2fb72bc8-96ef-420d-b08f-c04b69f36507%3Aamzn1.sym.2fb72bc8-96ef-420d-b08f-c04b69f36507&pf_rd_p=2fb72bc8-96ef-420d-b08f-c04b69f36507&pf_rd_r=KDCPNZRHFWEWBWVHWSTR&pd_rd_wg=sBvfF&pd_rd_r=52b946ee-46e2-4e74-86ee-99e291552e44) |



### Sobre la alimentación
El brazo robótico se envía por defecto sin fuente de alimentación. Puedes conectar tu propia batería o comprar una fuente de alimentación MeanWell fiable de 24V 14.6A fabricada en Taiwán. Además, necesitarás comprar un enchufe de tres clavijas conforme a la normativa local y un arnés de cableado con conector XT30 hembra.

#### BOM de consumibles

| Nombre | Especificación | Cant. | Precio de referencia | Notas | Imagen |
|:---|:---|:---:|:---:|:---|:---:|
| Fuente de alimentación | LRS-350-24 (24V 14.6A) | 1 | 27.35 $ | [amazon](https://www.amazon.com/MEAN-WELL-LRS-350-24-350-4W-Switchable/dp/B013ETVO12/ref=sr_1_1?crid=36B2HIB8MM2IT&dib=eyJ2IjoiMSJ9.vpZwmjb4m5KMNcsg2Kb7wr8DDWa-ryUqO5fConlxqlsGoTVB5HN2uBBnRNZI0kcACiaR5DKFiYWvIHLEUN3luZqJAzogeQkeT-fol0m835-oBBWSud1ixkGayrl5nRsF5KMgfvkwAIW949dTTpU2CWdNMrf8g43_vKWaytfX9SHeMJ1hmhS6Kab6fBgER6CgB47K_eEmoJj3KhrjJMtn980osDG-bCLniBcRAHThmXsVRVdpGPsmckGLLyaXrIGRG9plhKI-F7H8hfqW7vzGbwIV_bF8cFtRjdRm5Shtb0o.ekLYD0hsc1Uzji4qKl0Q0USpDTr92JEMQobBXl9lYD0&dib_tag=se&keywords=LRS-350-24&qid=1780021690&s=industrial&sprefix=lrs-350-24%2Cindustrial%2C696&sr=1-1&th=1) | <img src="./Purchased_Parts/LRS-350-24.png" width="80"> |
| Cable de alimentación | Cable de CA estándar de EE. UU. | 1 | 4.49 $ | [amazon](https://www.amazon.com/LIFEPOE-Power-3-3ft-Black-3-Prong/dp/B0FK4KPW2G/ref=sr_1_1?crid=2W5766PT8EOKA&dib=eyJ2IjoiMSJ9.7E5s-9-Zh-jJAdni-17Iyt1Mr3GJD6hMt9pfk-0S5YxZtknZik9OiePitwUom0pYUbePRpdqa0dCZtGUjluQDEJbSDePHCGvBV6bwQU7wfwd0Loo4WJJmH_2CM1KRKSPcxHXRH0i1i5yuy4g7fDxxn3nPGYU3aF00m5jiIkMfYFgOxH4yURjjZeTMZAIO9wiVQUsPrlM51UIgpPo2YYdCQVUsxjumSsTAm0Jpt2SsBEdT-QzXSIKpLSvQ6kGijXF-4ZevaxiShJdmwU8t2LobDLcalXEOl3lriZTGhjwxow.r0oBabUkGwewhvO3IKlBMULdhUSe6yNTsjfFUaBsjyU&dib_tag=se&keywords=US%2BStandard%2BAC%2BCable%3B%2B1.5m%2B-%2B3%2B*%2B1.5mm%C2%B2&nsdOptOutParam=true&qid=1780021862&s=industrial&sprefix=lrs-350-24%2Cindustrial%2C387&sr=1-1&th=1) | <img src="./Purchased_Parts/US Standard AC Cable.png" width="80"> |
| Puerto de salida | Conector hembra fijo XT60E; XT60E hembra + terminal de ojal - 10cm; orificio del terminal de 4mm | 1 | 9.99 $ | [amazon](https://www.amazon.com/LINSYRC-XT60E-F-Connector-Battery-Quadcopter/dp/B0CQK1P1DP/ref=pd_sbs_d_sccl_1_2/133-3898271-3474923?pd_rd_w=FmCVA&content-id=amzn1.sym.aa738fbd-ad05-4d11-aae2-04b598db6305&pf_rd_p=aa738fbd-ad05-4d11-aae2-04b598db6305&pf_rd_r=03QM0MRVZA968N9X6X6E&pd_rd_wg=WOZ9q&pd_rd_r=6e0577d2-de73-4427-affd-a271808e1453&pd_rd_i=B0CQK1P1DP&psc=1) | <img src="./Purchased_Parts/XT60E Female to Copper Lug Pigtail.png" width="80"> |
| Cableado de CA | 1.5mm²; rojo, azul y amarillo, 1 de cada (debes crimpar tú mismo los terminales al cable; no se incluyen cables precrimpados); 10CM | 3 | 0.99 $ | [aliexpress](https://www.aliexpress.com/item/1005008648016252.html?spm=a2g0o.productlist.main.2.15c9ZpluZpluHP&algo_pvid=09efee83-d80c-4ece-b588-3b1ef73279a3&algo_exp_id=09efee83-d80c-4ece-b588-3b1ef73279a3-1&pdp_ext_f=%7B%22order%22%3A%22230%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21USD%213.58%210.99%21%21%2124.09%216.65%21%400b0b305117800339070873795e0f3d%2112000046086542230%21sea%21US%216593543849%21ABX%211%210%21n_tag%3A-29910%3Bd%3A518b3f9d%3Bm03_new_user%3A-29895%3BpisId%3A5000000207178484&curPageLogUid=74aJ9L7lm7hs&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005008648016252%7C_p_origin_prod%3A&gatewayAdapt=4itemAdapt) | <img src="./Purchased_Parts/RV Grounding Wire Coil with Y-Terminal Lugs.png" width="80"> |
| Base IEC 3 en 1 | Tipo de conexión rápida con interruptor rojo (doble tuerca) | 1 | 1.98 $ | [aliexpress](https://www.aliexpress.com/item/1005005962021242.html?spm=a2g0o.imagesearchproductlist.main.17.7db7cZZdcZZdCY&algo_pvid=270b0987-1973-41ad-a2b9-6fe008f9edb5&algo_exp_id=270b0987-1973-41ad-a2b9-6fe008f9edb5&pdp_ext_f=%7B%22order%22%3A%22346%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21USD%213.31%211.98%21%21%2122.30%2113.35%21%400b0b305117800327806706342e118f%2112000035062406338%21sea%21US%216593543849%21ABX%211%210%21n_tag%3A-29910%3Bd%3A518b3f9d%3Bm03_new_user%3A-29895%3BpisId%3A5000000204886261&curPageLogUid=87JUDbPbch2i&utparam-url=scene%3Aimage_search%7Cquery_from%3Apc_web_image_search%7Cx_object_id%3A1005005962021242%7C_p_origin_prod%3A) | <img src="./Purchased_Parts/3-in-1 IEC Inlet Socket.png" width="80"> |
| Cable adaptador XT30 a XT60 | XT30U hembra a XT60 macho | 1 | 8.99 $ | [amazon](https://www.amazon.com/dp/B0BY8PSHK6?th=1) | <img src="./Purchased_Parts/XT30U_female_to_XT60_male.png" width="80"> |
| Tornillo avellanado Phillips de acero inoxidable 304 | M4x6 | 6 | 0.37 $ | / | / |
| Tornillo avellanado Phillips de acero inoxidable 304 | M3x8 | 2 | 0.36 $ | / | / |
| Tornillo Phillips de cabeza alomada de acero inoxidable 304 | M3x8 | 2 | 0.32 $ | / | / |
| Tuerca hexagonal | M3x2.5 | 2 | ≈0.30 $ | / | / |


#### BOM de piezas impresas

| Nombre | Imagen | Cant. | Notas |
|:---|:---|:---:|:---|
| [Carcasa frontal](./3D_Printed_Parts/DM-power-Top%20Cover.stp) | <img src="./3D_Printed_Parts/images/DM-power-Top Cover.png" width="80"> | 1 | PLA, boquilla de 0.4 mm, altura de capa de 0.2 mm, relleno del 30% |
| [Carcasa trasera](./3D_Printed_Parts/DM-power-Bottom%20Cover.stp) | <img src="./3D_Printed_Parts/images/DM-power-Bottom Cover.png" width="80"> | 1 | PLA, boquilla de 0.4 mm, altura de capa de 0.2 mm, relleno del 30% |
| [Tapa deslizante de la carcasa frontal](./3D_Printed_Parts/DM-power-Top%20Cover-Sliding%20Cover.stp) | <img src="./3D_Printed_Parts/images/DM-power-Top Cover-Sliding Cover.png" width="80"> | 1 | PLA, boquilla de 0.4 mm, altura de capa de 0.2 mm, relleno del 30% |

#### Montaje de la fuente de alimentación

El montaje de la fuente de alimentación se divide en dos secciones principales: la carcasa frontal y la carcasa trasera.

##### 1. Montaje de la carcasa frontal

| Paso | Instrucciones | Imagen | Notas |
|:---:|---|---|---|
| 1-1 | Prepara las piezas y los componentes impresos necesarios para el montaje de la carcasa frontal | <img src="./Assembly_Steps/powerstep_images/1-1.png" width="80"> | Comprueba que todas las piezas estén completas |
| 1-2 | Consulta las indicaciones de la secuencia de cableado de cada pieza y monta siguiéndola | <img src="./Assembly_Steps/powerstep_images/1-2(1).png" width="80" style="margin-right:4%;"><img src="./Assembly_Steps/powerstep_images/1-2(2).png" width="80"><br><img src="./Assembly_Steps/powerstep_images/1-2(3).png" width="80"> | Sigue estrictamente la secuencia de cableado al conectar |
| 1-3 | Instala el conector XT60 | <img src="./Assembly_Steps/powerstep_images/1-3(1).png" width="80" style="margin-right:4%;"><img src="./Assembly_Steps/powerstep_images/1-3(2).png" width="80"> | Fíjalo con tornillos avellanados Phillips de acero inoxidable 304 M3x8 y tuercas hexagonales M3x2.5 |
| 1-4 | Instala la base IEC 3 en 1 | <img src="./Assembly_Steps/powerstep_images/1-4(1).png" width="80" style="margin-right:4%;"><img src="./Assembly_Steps/powerstep_images/1-4(2).png" width="80"> | Fija la base IEC 3 en 1 con tornillos Phillips de cabeza alomada de acero inoxidable 304 M3x8 |
| 1-5 | Cableado interno de la carcasa frontal | <img src="./Assembly_Steps/powerstep_images/1-5(1).png" width="80"><br><img src="./Assembly_Steps/powerstep_images/1-5(2).png" width="80"> | Comprueba las conexiones con el diagrama de la secuencia de cableado |
| 1-6 | Fija ambos lados de la carcasa frontal y la fuente de alimentación | <img src="./Assembly_Steps/powerstep_images/1-6(1).png" width="80" style="margin-right:4%;"><img src="./Assembly_Steps/powerstep_images/1-6(2).png" width="80"> | Tornillos avellanados Phillips de acero inoxidable 304 M4x6 x2 |
| 1-7 | Instala la tapa deslizante | <img src="./Assembly_Steps/powerstep_images/1-7(1).png" width="80" style="margin-right:4%;"><img src="./Assembly_Steps/powerstep_images/1-7(2).png" width="80"> | Introdúcela desde la parte inferior de la fuente de alimentación |
| 1-8 | Fija la tapa deslizante | <img src="./Assembly_Steps/powerstep_images/1-8.png" width="80"> | Tornillos avellanados Phillips de acero inoxidable 304 M4x6 x2 |

---

##### 2. Montaje de la carcasa trasera

| Paso | Instrucciones | Imagen | Notas |
|:---:|---|---|---|
| 2-1 | Prepara las piezas y los componentes impresos necesarios para el montaje de la carcasa trasera | <img src="./Assembly_Steps/powerstep_images/2-1.png" width="80"> | Comprueba que los accesorios estén completos |
| 2-2 | Monta la carcasa trasera con la fuente de alimentación | <img src="./Assembly_Steps/powerstep_images/2-2.png" width="80"> | Alinea la posición |
| 2-3 | Fija ambos lados de la carcasa trasera y la fuente de alimentación | <img src="./Assembly_Steps/powerstep_images/2-3(1).png" width="80" style="margin-right:4%;"><img src="./Assembly_Steps/powerstep_images/2-3(2).png" width="80"> | Tornillos avellanados Phillips de acero inoxidable 304 M4x6 x2 |

---

##### 3. Finalización del conjunto

| Paso | Instrucciones | Imagen | Notas |
|:---:|---|---|---|
| 1 | Montaje del sistema de alimentación completado | <img src="./Assembly_Steps/powerstep_images/3.png" width="80"> | Comprueba que todos los tornillos estén apretados |

---
