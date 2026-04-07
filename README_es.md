好的，这次是**严格保持原有结构、标签、顺序、内容完整不删除，只做逐句西班牙语翻译**👇

---

# 🦾 reBot-DevArm: Brazo Robótico de Código Abierto para Todos los Desarrolladores

<p align="center">
  <img src="./media/v1.0.png" alt="Banner de reBot-DevArm">
</p>

<p align="center">
    <!-- Reemplazado con insignia CC BY-NC-SA 4.0, indicando explícitamente uso no comercial -->
    <a href="./LICENSE">
        <img src="https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg" alt="Licencia: CC BY-NC-SA 4.0">
    </a>
    <img src="https://img.shields.io/badge/Commercial-Contact%20Us-red.svg" alt="yaohui.zhu@seeed.cc">
    <img src="https://img.shields.io/badge/ROS-Noetic%20%7C%20Humble-orange.svg" alt="Soporte ROS">
    <img src="https://img.shields.io/badge/Framework-LeRobot-yellow.svg" alt="LeRobot">
    <img src="https://img.shields.io/badge/Framework-Isaac Sim-yellow.svg" alt="LeRobot">
</p>

<p align="center">
  <strong>100% Totalmente de Código Abierto · IA Corpórea · Integración Hardware-Software · Gratis para uso personal/educativo · El uso comercial requiere autorización</strong>
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
    <img src="https://img.shields.io/badge/Documentation-📕-blue" alt="wiki de robótica"></a>
</p>

## 📖 Introducción

**reBot-DevArm (reBot Arm B601 DM y reBot Arm B601 RS)** es un proyecto de brazo robótico dedicado a reducir la barrera de aprendizaje de la IA Corpórea. Nos enfocamos en el **"Verdadero Código Abierto"** — no solo el código, abrimos todo sin reservas:

* 🦾 **Dos versiones del brazo robótico**：Proporcionaremos todos los archivos de código abierto para dos versiones del brazo robótico con la misma apariencia: **Robostride** y **Damiao**。
* 🛠️ **Planos de hardware**: Archivos fuente de piezas de chapa metálica y piezas impresas en 3D。
* 🔩 **Lista BOM**: Detallada hasta las especificaciones y enlaces de compra de cada tornillo。
* 💻 **Software y algoritmos**: Python SDK, ROS1/2, Isaac Sim, LeRobot, etc。

## Consigue tu propio brazo reBot Arm

- Ofrecemos cinco versiones de kits:
  - **Kit de motor del brazo**: incluye solo motores y cableado del brazo robótico.
  - **Kit estructural del brazo**: incluye solo componentes mecánicos estructurales.
  - **Kit completo de pinza (gripper)**: incluye motor, cableado y componentes estructurales de la pinza.
  - **Kit completo**: brazo robótico + pinza.
  - **Brazo ensamblado**: brazo robótico preensamblado.

Puedes comprar las piezas restantes en la tienda de SeeedStudio (llegada prevista: 15/04/2026) según el material que ya tengas.

[Deja tus datos aquí y te enviaremos el enlace de preventa limitado por adelantado.](https://forms.gle/1MwdVKUqkuGu3C7L7)


## 🗺️ Hoja de ruta y estado

Estamos comprometidos a mantener y adaptarnos continuamente a los ecosistemas principales de desarrollo robótico. A continuación se muestra nuestro progreso actual de adaptación y el plan de lanzamiento:

### reBot Arm B601 DM
| Ecosistema compatible | Estado | Descripción / Fecha estimada de lanzamiento | Documentación relacionada |
| :--- | :---: | :--- | :--- |
| **Uso básico del motor** | ✅ Completado | Control básico de movimiento y encapsulación de API | [Damiao Technology](https://wiki.seeedstudio.com/cn/damiao_series/) |
| **Código abierto de las nuevas piezas estructurales 3D STEP y BOM** | ✅ Completado | Archivos STEP de todas las piezas, BOM y precios de referencia de componentes mecanizados | [reBot Arm B601-DM BOM](./hardware/reBot_B601_DM/readme_es.md) |
| **Referencia de pruebas de rendimiento en máquina real** | ✅ Completado | Referencia de rendimiento del brazo robótico en funcionamiento normal y extremo | [Performance Testing](./hardware/reBot_B601_DM/performance_testing/Performance_Testing_es.md) |
| **Video de ensamblaje** | 🚧 En progreso | Pasos de ensamblaje ultra detallados y video | [Esperado: 2026.04.10] |
| **ROS2 (Humble)** | 🚧 En progreso | Drivers principales completados, optimización de MoveIt2 en curso | [Esperado: 2026.04.10] |
| **Python SDK** | 🚧 En progreso |  | [Esperado: 2026.04.10] |
| **Integración con Pinocchio** | 🚧 En progreso | Adaptación al framework Pinocchio para cinemática directa/inversa y compensación de gravedad | [Repositorio GitHub](https://github.com/vectorBH6/reBotArm_control_py/tree/main) Actualización continua |
| **Simulación en Isaac Sim** | 🚧 En progreso | Importación de modelos USD y teleoperación simulada | [Esperado: 2026.04.20] |
| **Integración con LeRobot** | 🚧 En progreso | Adaptación al framework LeRobot de Hugging Face | [Esperado: 2026.04.30] |
| **Actualizaciones graduales de los últimos algoritmos** | ⏳ Planificado | Actualización progresiva de algoritmos principales | En curso |
| **Lanzamiento de una serie de cursos completamente gratuitos** | ⏳ Planificado | Actualización continua de contenidos educativos | En curso |
### reBot Arm B601 RS

| Ecosistema compatible                   |     Estado     | Descripción / Fecha estimada de lanzamiento | Documentación relacionada                                       |
| :-------------------------------------- | :------------: | :------------------------------------------ | :-------------------------------------------------------------- |
| **Uso básico del motor**                |  ✅ Completado  | Control básico y encapsulación de API       | [Robstride](https://wiki.seeedstudio.com/cn/robstride_control/) |
| **Código abierto de piezas STEP y BOM** | 🚧 En progreso | Archivos STEP, BOM y precios de referencia  | Expected [2026.04.31]                                           |
| **Video de ensamblaje**                 | 🚧 En progreso | Guía de ensamblaje detallada                | [Expected 2026.05.10]                                           |
| **ROS2 (Humble)**                       |  ⏳ Planificado | Drivers listos, optimización en curso       | [Expected 2026.05]                                              |
| **Integración con LeRobot**             |  ⏳ Planificado | Framework de aprendizaje robótico           | [Expected 2026.05]                                              |
| **Integración con Pinocchio**           |  ⏳ Planificado | Cinemática y compensación de gravedad       | [Expected 2026.05]                                              |
| **Simulación en Isaac Sim**             |  ⏳ Planificado | Simulación robótica                         | [Expected 2026.05]                                              |
| **Actualización de algoritmos**         |  ⏳ Planificado | Actualizaciones continuas                   | Ongoing                                                         |
| **Cursos gratuitos**                    |  ⏳ Planificado | Cursos abiertos                             | Ongoing                                                         |

---

### 🎓 Ecosistema completo de robótica

reBot-DevArm no es solo un brazo robótico, sino también una comunidad de aprendizaje en robótica. Compartimos los siguientes tutoriales generales de forma gratuita:

#### 🖥️ Computación en el borde y control maestro

* [![Jetson](https://img.shields.io/badge/NVIDIA-reComputer%20Jetson-76B900?style=for-the-badge\&logo=nvidia\&logoColor=white)](https://wiki.seeedstudio.com/NVIDIA_Jetson/) —— **Inferencia de IA y núcleo de cómputo**
* [![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-4B%20%2F%205-C51A4A?style=for-the-badge\&logo=Raspberry%20Pi\&logoColor=white)](https://wiki.seeedstudio.com/raspberry-pi-devices/) —— **Entorno de desarrollo Linux general**
* [![ESP32](https://img.shields.io/badge/MCU-Seeed%20XIAO%20\(ESP32\)-0091BD?style=for-the-badge\&logo=espressif\&logoColor=white)](https://wiki.seeedstudio.com/SeeedStudio_XIAO_Series_Introduction/) —— **Nodo de control inalámbrico de bajo consumo**

#### 📡 Sensores y periféricos

* **🚗 Motores y servos**: [Damiao / Gogo / Robstride / Mita / Feite / Fashion Star](https://wiki.seeedstudio.com/robotics_page/)
* **👁️ Percepción visual**: [Cámaras de profundidad / LiDAR / Algoritmos de visión](https://wiki.seeedstudio.com/robotics_page/)
* **👂 Interacción auditiva**: [ReSpeaker Mic Arrays / Reconocimiento de voz](https://wiki.seeedstudio.com/ReSpeaker_Mic_Array_v2.0/)
* **🧭 Movimiento y orientación**: [IMU (6 ejes/9 ejes) / Giroscopios / Magnetómetros](https://wiki.seeedstudio.com/Sensor/IMU/)
* **🤖 Kits completos**: [Más sensores y ejemplos de controladores](https://wiki.seeedstudio.com/robotics_page/)

> 👉 **[Haz clic para entrar en la base de conocimiento Wiki](https://wiki.seeedstudio.com/)** (Todos los tutoriales son gratuitos)

---

## ⚙️ Especificaciones de hardware

reBot-DevArm está diseñado para aplicaciones de IA Corpórea en escritorio, equilibrando capacidad de carga y flexibilidad.

| Parameter                      | reBot Arm B601-DM                                                                            |
| :----------------------------- | :------------------------------------------------------------------------------------------- |
| **Carga continua recomendada** | Menos de 1.5 kg dentro del 70% del alcance                                                   |
| **Carga recomendada**          | **1.5 kg**                                                                                   |
| **Alcance máximo**             | **650 mm**                                                                                   |
| **Peso**                       | Aprox. 4.5 kg                                                                                |
| **Repetibilidad**              | < 0.2 mm                                                                                     |
| **Grados de libertad (DOF)**   | 6 DOF + 1 pinza (pinza servo CAN de código abierto y pinza con motor articular próximamente) |
| **Plataformas compatibles**    | ROS1, ROS2, LeRobot, Pinocchio, Isaac Sim, Python SDK                                        |
| **Voltaje de alimentación**    | DC 24V                                                                                       |

## 🙌 Referencias y agradecimientos

El camino del código abierto nunca es solitario. El nacimiento del proyecto reBot-DevArm no sería posible sin el apoyo total de Seeed Studio, la comunidad global de código abierto y excelentes socios de hardware. Expresamos nuestro mayor respeto a los siguientes proyectos y equipos:

### 🌍 Ecosistema y soporte de software

* **[Seeed Studio](https://www.seeedstudio.com/)** - Proporciona soporte integral de cadena de suministro y técnico.
* **[Hugging Face LeRobot](https://github.com/huggingface/lerobot)** - Excelente framework de aprendizaje robótico de extremo a extremo.
* **[NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim)** - Potente plataforma de simulación robótica y generación de datos.

### ⚙️ Socios principales de hardware

Gracias a los siguientes fabricantes por proporcionar soluciones de motores y actuadores de alto rendimiento:

* **[Damiao Technology](https://www.damiaokeji.com/)**
* **[Robstride](https://robstride.com/)**
* **[Fashion Star](https://fashionrobo.com/)**

### 💡 Inspiración

Este proyecto está profundamente inspirado en los siguientes proyectos de código abierto:

* **[SO-ARM100](https://github.com/TheRobotStudio/SO-ARM100/tree/main)**
* **[Mobile ALOHA](https://github.com/tonyzhaozh/aloha)**
* **[Dummy-Robot (Zhihui Jun)](https://github.com/peng-zhihui/Dummy-Robot)**
* **[OpenArm](https://openarm.dev/)**
* **[I2RT](https://i2rt.com/)**
* **[TRLC-DK1](https://github.com/robot-learning-co/trlc-dk1)**

### 🎃 Contribuidores del prototipo

* **Equipo de robótica AI de SeeedStudio**: Yaohui Zhu ([yaohui.zhu@seeed.cc](mailto:yaohui.zhu@seeed.cc))
* **SeeedStudio STU**: Wentao Dong
* **SeeedStudio STU**: Weiwei Xu
* **Departamento de compras de SeeedStudio**: Fengqun Peng

### 👥 Contributors

## Our Top Contributors

<p align="center"><a href="https://github.com/Seeed-Projects/reBot-DevArm/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=Seeed-Projects/reBot-DevArm" />
</a></p>

*Coming soon... Welcome to submit PRs to become a contributor!*

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Seeed-Projects/reBot-DevArm\&type=date\&legend=top-left)](https://www.star-history.com/#Seeed-Projects/reBot-DevArm&type=date&legend=top-left)

# reBot-DevArm Project License

Copyright (c) [2025] [Seeed Studio]

Este trabajo está licenciado bajo la **Licencia Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International**.
Para ver una copia de esta licencia, visita: [http://creativecommons.org/licenses/by-nc-sa/4.0/](http://creativecommons.org/licenses/by-nc-sa/4.0/)

---

## Declaración de derechos y restricciones

El propósito principal de este proyecto de código abierto es promover el intercambio de conocimiento y permitir que desarrolladores y entusiastas accedan y aprendan tecnologías avanzadas de brazos robóticos a un costo mínimo. Proporcionamos documentación y tutoriales en video completamente gratuitos para ayudar a los usuarios a comenzar rápidamente, realizar investigaciones en profundidad y promover conjuntamente la aplicación práctica de la robótica.

### I. Política de uso no comercial

Todo el contenido de código abierto de este proyecto está disponible para aprendizaje personal, investigación y uso no comercial. Los usuarios pueden:

* Ver y estudiar documentación, código y tutoriales;
* Modificar y depurar el contenido para investigación personal;
* Ensamblar brazos robóticos o realizar desarrollo secundario con fines no comerciales.

### II. Política de uso comercial

Fomentamos el desarrollo basado en reBot y su aplicación en el mundo real. A continuación:

#### (1) Actividades comerciales permitidas

* Desarrollo de software comercial;
* Cursos educativos pagos;
* Actividades educativas y de difusión tecnológica;
* Otras actividades que impulsen la comunidad.

#### (2) Actividades prohibidas

Queda prohibido modificar superficialmente el producto y venderlo bajo marca propia.

### III. Colaboración y contacto

Ofrecemos:

* Licencias comerciales;
* Promoción de soluciones;
* Desarrollo personalizado;
* Colaboración en I+D.

Si estás interesado, contáctanos.

## ☎ Contact Us

* **Progreso de código abierto y soporte técnico**-Yaohui: [yaohui.zhu@seeed.cc](mailto:yaohui.zhu@seeed.cc)
* **Colaboración futura y personalización**-Elaine: [elaine.wu@seeed.cc](mailto:elaine.wu@seeed.cc)
