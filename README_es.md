# 🦾 reBot-DevArm: Brazo Robótico de Código Abierto para Todos los Desarrolladores

<p align="center">
  <img src="./media/v2.0.png" alt="reBot-DevArm Banner">
</p>

<p align="center">
    <!-- Reemplazado por el distintivo CC BY-NC-SA 4.0, indicando explícitamente el uso no comercial -->
    <a href="./LICENSE">
        <img src="https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg" alt="Licencia: CC BY-NC-SA 4.0">
    </a>
    <img src="https://img.shields.io/badge/Comercial-Contáctanos-red.svg" alt="yaohui.zhu@seeed.cc">
    <img src="https://img.shields.io/badge/ROS-Noetic%20%7C%20Humble-orange.svg" alt="Soporte ROS">
    <img src="https://img.shields.io/badge/Framework-LeRobot-yellow.svg" alt="LeRobot">
    <img src="https://img.shields.io/badge/Framework-Isaac Sim-yellow.svg" alt="LeRobot">
</p>

<p align="center">
  <strong>100% Código Abierto · IA Encarnada · Integración Hardware-Software · Gratis para Personal/Educación · El Uso Comercial Requiere Autorización</strong>
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
      <img src="https://img.shields.io/badge/Documentación-📕-blue" alt="robotics wiki"></a>
</p>

## 📖 Introducción

**reBot-DevArm** es un proyecto de brazo robótico dedicado a reducir la barrera para aprender IA Encarnada (Embodied AI). Nos enfocamos en el **"Verdadero Código Abierto"** — no solo el código, abrimos todo sin reservas:
- 🦾 **Dos versiones del brazo robótico**: Proporcionaremos todos los archivos de código abierto para dos versiones del brazo con la misma apariencia: **Robostride** y **Damiao**.
- 🛠️ **Planos de Hardware**: Archivos fuente para piezas de chapa metálica y piezas impresas en 3D.
- 🔩 **Lista de Materiales (BOM)**: Detallada hasta las especificaciones y enlaces de compra para cada tornillo.
- 💻 **Software y Algoritmos**: SDK de Python, ROS1/2, Isaac Sim, LeRobot, etc.

**⚠️ Nota: Este proyecto tiene como objetivo promover la educación y el aprendizaje personal. Todos los recursos son completamente gratuitos para desarrolladores individuales, estudiantes e instituciones educativas. Sin embargo, cualquier uso comercial no autorizado (incluyendo pero no limitado a la venta directa de kits o su uso como parte de un producto comercial) está estrictamente prohibido.**

**Relajaremos la licencia de uso comercial gratuito una vez que completemos todas las evaluaciones de rendimiento, precisión y seguridad del hardware.**

## ☎ Contáctanos
- **Progreso de Código Abierto y Soporte Técnico** - Yaohui: yaohui.zhu@seeed.cc
- **Colaboración Futura y Personalización** - Elaine: elaine.wu@seeed.cc

## 🗺️ Hoja de Ruta y Estado

> [!WARNING]
> Debido a las festividades del Año Nuevo Chino, la mayoría de los proveedores y empresas asociadas han suspendido sus operaciones, lo que ha afectado el progreso de las pruebas de las muestras del brazo robótico. Publicaremos los archivos de código abierto **solo después de completar todas las validaciones de rendimiento y precisión**, por lo que el cronograma de apertura se retrasará aproximadamente un mes.

Estamos comprometidos con el mantenimiento continuo y la adaptación a los ecosistemas de desarrollo de robots convencionales. A continuación se muestra nuestro progreso de adaptación actual y el calendario de lanzamiento planificado:

| Ecosistema | Estado | Descripción / ETA | Documentación |
| :--- | :---: | :--- | :--- |
| **Uso Básico de Motores** | ✅ Hecho | Control de movimiento básico y encapsulación de API | [Robostride](https://wiki.seeedstudio.com/robstride_control/) [Damiao](https://wiki.seeedstudio.com/damiao_series/)|
| **Nueva Versión Estructura 3D STEP y BOM** | 🚧 En progreso | Archivos STEP para piezas nuevas, BOM de componentes y precios de referencia | [Retraso 2026.03] |
| **Video de Ensamblaje** | 🚧 En progreso | Pasos de ensamblaje ultra-detallados y video | [Retraso 2026.03] |
| **ROS2 (Humble)** |⏳ Planificado | Controlador principal completado, optimizando MoveIt2 |[ETA 2026.04]|
| **Adaptación a LeRobot** | ⏳ Planificado | Adaptación al framework de entrenamiento Hugging Face LeRobot | [ETA 2026.04]|
| **Adaptación a Pinocchio** | ⏳ Planificado | Adaptación al framework Pinocchio, implementando cinemática directa/inversa y compensación de gravedad dinámica | [ETA 2026.04]|
| **Simulación Isaac Sim** | ⏳ Planificado | Importación de modelos USD e implementación de teleoperación de simulación | [ETA 2026.04]|
| **Actualizaciones Graduales de Algoritmos** | ⏳ Planificado | Actualización gradual de algoritmos convencionales | Continuo |
| **Lanzamiento de Cursos Gratuitos** | ⏳ Planificado | Tutoriales paso a paso | Continuo |

---

### 🎓 Ecosistema de Robótica Full-Stack
reBot-DevArm no es solo un brazo robótico, sino una comunidad de aprendizaje de robótica. Compartimos los siguientes tutoriales generales de forma gratuita:

#### 🖥️ Computación en el Borde y Control Maestro
*   [![Jetson](https://img.shields.io/badge/NVIDIA-reComputer%20Jetson-76B900?style=for-the-badge&logo=nvidia&logoColor=white)](https://wiki.seeedstudio.com/NVIDIA_Jetson/) —— **Inferencia de IA y Núcleo de Cómputo**
*   [![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-4B%20%2F%205-C51A4A?style=for-the-badge&logo=Raspberry%20Pi&logoColor=white)](https://wiki.seeedstudio.com/raspberry-pi-devices/) —— **Entorno de Desarrollo Linux General**
*   [![ESP32](https://img.shields.io/badge/MCU-Seeed%20XIAO%20(ESP32)-0091BD?style=for-the-badge&logo=espressif&logoColor=white)](https://wiki.seeedstudio.com/SeeedStudio_XIAO_Series_Introduction/) —— **Nodo de Control Inalámbrico de Bajo Consumo**

#### 📡 Sensores y Periféricos
*   **🚗 Motores y Servos**: [Damiao / Gogo / Robstride / Mita / Feite / Fashion Star](https://wiki.seeedstudio.com/robotics_page/)
*   **👁️ Percepción Visual**: [Cámaras de Profundidad / LiDAR / Algoritmos de Visión](https://wiki.seeedstudio.com/robotics_page/)
*   **👂 Interacción Auditiva**: [Matrices de Micrófonos ReSpeaker / Reconocimiento de Voz](https://wiki.seeedstudio.com/ReSpeaker_Mic_Array_v2.0/)
*   **🧭 Movimiento y Actitud**: [IMU (6 ejes/9 ejes) / Giroscopios / Magnetómetros](https://wiki.seeedstudio.com/Sensor/IMU/)
*   **🤖 Kits Integrales**: [Más Sensores Robóticos y Ejemplos de Controladores](https://wiki.seeedstudio.com/robotics_page/)

> 👉 **[Haz clic para entrar en la Base de Conocimientos Wiki](https://wiki.seeedstudio.com/)** (Todos los tutoriales son de libre acceso)

---

## ⚙️ Especificaciones de Hardware

reBot-DevArm está diseñado para aplicaciones de IA Encarnada de escritorio, equilibrando la capacidad de carga con la flexibilidad.

| Parámetro | Valor / Descripción |
| :--- | :--- |
| **Carga Útil** | **1.5+ kg** |
| **Alcance Máximo** | **650 mm** |
| **Peso** | Aprox. 4.0 kg |
| **Repetibilidad** | < 0.2 mm |
| **Grados de Libertad (DOF)** | 6 DOF + 1 Pinza (Pinza servo CAN de código abierto y pinza de motor de articulación próximamente) |
| **Plataformas/Ecosistemas Soportados** | ROS1, ROS2, LeRobot, Pinocchio, Isaac Sim, SDK de Python |
| **Voltaje de Alimentación** | DC 24V |

---

## 📂 Código Abierto (Fuentes de Hardware)

Creemos que el hardware de código abierto fomenta la innovación. Puedes encontrar todo lo necesario para construir este brazo en los siguientes directorios:

*   [`/hardware/STEP`](./hardware/cad): Archivos STEP/STL para todas las estructuras mecánicas, incluyendo piezas impresas, piezas metálicas y artículos comprados.
*   [`/hardware/bom`](./hardware/bom): **Lista BOM** (Incluye modelos de componentes comprados, parámetros del motor, proveedores recomendados).
*   [`/tutorial/ROS`](./tutorial/ROS/): Código fuente y tutoriales para **ROS1/2 Noetic/Humble**.
*   [`/tutorial/Lerobot`](./tutorial/lerobot/): Código fuente y tutoriales para **LeRobot**.
*   [`/tutorial/Isaac`](./tutorial/Isaac/): Código fuente y tutoriales para **Isaac Sim**.

---

## 🚀 Guía de Inicio

Hemos planeado una ruta de aprendizaje completa para ti, desde el desembalaje hasta la simulación con IA:

### 🛠️ Fase 1: Construcción de Hardware y Conceptos Básicos
| Paso | Descripción | Enlace |
| :---: | :--- | :--- |
| **01** | **Aprendizaje Básico de Motores** | [Robostride](https://wiki.seeedstudio.com/robstride_control/) [Damiao](https://wiki.seeedstudio.com/damiao_series/)|
| **02** | **Desembalaje** | Próximamente |
| **03** | **Guía de Montaje** | Próximamente |
| **04** | **Calibración de Cero** | Próximamente |
| **05** | **Pruebas de Cinemática** | Próximamente |

### 💻 Fase 2: Algoritmos Avanzados y Simulación
| Paso | Descripción | Enlace |
| :---: | :--- | :--- |
| **06** | **Ecosistema ROS** (ROS2) | 🐢 Próximamente |
| **07** | **Entrenamiento de IA** (Hugging Face) | 🤗 Próximamente |
| **08** | **Simulación** (NVIDIA) | 🌌 Próximamente |

---

## 🙌 Referencias y Agradecimientos
El camino del código abierto nunca es solitario. El nacimiento del proyecto reBot-DevArm no sería posible sin el apoyo total de Seeed Studio, la comunidad global de código abierto y excelentes socios de hardware. Expresamos nuestro mayor respeto a los siguientes proyectos y equipos:

### 🌍 Soporte de Ecosistema y Software
*   **[Seeed Studio](https://www.seeedstudio.com/)** - Proporcionando cadena de suministro de hardware integral y soporte técnico.
*   **[Hugging Face LeRobot](https://github.com/huggingface/lerobot)** - Un excelente framework de aprendizaje robótico de extremo a extremo.
*   **[NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim)** - Una potente plataforma de simulación robótica y generación de datos sintéticos.

### ⚙️ Socios de Hardware Principales
Gracias a los siguientes fabricantes por proporcionar soluciones de motores y actuadores de alto rendimiento:
*   **[Damiao Technology](https://www.damiaokeji.com/)**
*   **[Robstride](https://robstride.com/)**
*   **[Fashion Star](https://fashionrobo.com/)**

### 💡 Inspiración
Este proyecto está profundamente inspirado en los siguientes excelentes proyectos de código abierto:
*   **[SO-ARM100](https://github.com/TheRobotStudio/SO-ARM100/tree/main)**
*   **[Mobile ALOHA](https://github.com/tonyzhaozh/aloha)**
*   **[Dummy-Robot (Zhihui Jun)](https://github.com/peng-zhihui/Dummy-Robot)**
*   **[OpenArm](https://openarm.dev/)**
*   **[I2RT](https://i2rt.com/)**
*   **[TRLC-DK1](https://github.com/robot-learning-co/trlc-dk1)**

### 🎃 Colaboradores del Prototipo
- **SeeedStudio AI Robotics Team's**: Yaohui Zhu (yaohui.zhu@seeed.cc)
- **SeeedStudio STU**: Wentao Dong
- **SeeedStudio STU**: Weiwei Xu
- **Departamento de Compras de SeeedStudio**: Fengqun Peng

### 👥 Colaboradores

## Nuestros Principales Colaboradores

<p align="center"><a href="https://github.com/Seeed-Projects/reBot-DevArm/graphs/contributors">
   <img src="https://contributors-img.web.app/image?repo=Seeed-Projects/reBot-DevArm" />
</a></p>

*Próximamente... ¡Bienvenido a enviar PRs para convertirte en colaborador!*

## Historial de Estrellas

[![Gráfico de Historial de Estrellas](https://api.star-history.com/svg?repos=Seeed-Projects/reBot-DevArm&type=date&legend=top-left)](https://www.star-history.com/#Seeed-Projects/reBot-DevArm&type=date&legend=top-left)

# Licencia del Proyecto reBot-DevArm
Copyright (c) [2025] [Seeed Studio AI Robotics Team]

Este trabajo está bajo una **Licencia Internacional Creative Commons Atribución-NoComercial-CompartirIgual 4.0**. Para ver una copia de esta licencia, visita: http://creativecommons.org/licenses/by-nc-sa/4.0/

--------------------------------------------------------------------------------

## Derechos y Restricciones
1. Eres libre de:
    - Compartir: Copiar y redistribuir el material en cualquier medio o formato.
    - Adaptar: Remezclar, transformar y construir a partir del material.

2. Bajo los siguientes términos:
    - Atribución: Debes dar el crédito apropiado, proporcionar un enlace a la licencia e indicar si se realizaron cambios.
    - NoComercial: **No puedes usar el material con fines comerciales**.
      (Incluyendo pero no limitado a vender kits relacionados, vender piezas impresas o integrar este software en productos pagos sin permiso explícito).
    - CompartirIgual: Si remezclas, transformas o construyes a partir del material, debes distribuir tus contribuciones bajo la misma licencia que el original.

3. Autorización Comercial:
    Si deseas utilizar este proyecto con fines comerciales, ponte en contacto con el autor para obtener la autorización comercial.
    Contacto: yaohui.zhu@seeed.cc