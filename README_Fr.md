<div align="center">

# 🦾 reBot-DevArm

**Le bras robotique open source pour tous les développeurs**

<img src="./media/RS5_56.png" alt="reBot-DevArm Banner" width="1000">

<a href="https://certification.oshwa.org/cn000024.html"><img src="./media/certification-mark-CN000024-wide.png" alt="Certification OSHWA" width="180"></a>

[![Licence matérielle : CERN-OHL-W-2.0](https://img.shields.io/badge/License-CERN--OHL--W--2.0--Hardware-green.svg)](./LICENSE)
[![Licence logicielle : Apache-2.0](https://img.shields.io/badge/License-Apache--2.0--Software-pink.svg)](./LICENSE)
[![ROS](https://img.shields.io/badge/ROS-Noetic%20%7C%20Humble-orange.svg)](#feuille-de-route)
[![LeRobot](https://img.shields.io/badge/Framework-LeRobot-yellow.svg)](#feuille-de-route)
[![Isaac Sim](https://img.shields.io/badge/Framework-Isaac%20Sim-yellow.svg)](#feuille-de-route)
[![Commercial](https://img.shields.io/badge/Commercial-Contact%20Us-red.svg)](mailto:yaohui.zhu@seeed.cc)

**100% open source · IA incarnée · Stack complet matériel + logiciel**

🌐 [Page d'accueil](https://279070161-sketch.github.io/reBot/) · 📚 [Centre de tutoriels](https://wiki.seeedstudio.com/robotics_page/) · ▶ [Démo en ligne](https://yang-ci.github.io/Rebot_Arm_AGV/)

[![Discord](https://img.shields.io/discord/1409155673572249672?color=7289DA&label=Discord&logo=discord&logoColor=white)](https://discord.gg/AbGuqJhDpQ)
[![Documentation](https://img.shields.io/badge/Documentation-%F0%9F%93%95-blue)](https://wiki.seeedstudio.com/robotics_page/)

[简体中文](README_zh.md) · [English](README.md) · [日本語](README_JP.md) · [français](README_Fr.md) · [Español](README_es.md)

</div>

---

## 📑 Sommaire

- [📖 Introduction](#introduction)
- [🛒 Obtenez votre reBot Arm](#obtenez-votre-rebot-arm)
- [🚀 Essayez la simulation en ligne](#essayez-la-simulation-en-ligne)
- [🗺️ Feuille de route](#feuille-de-route)
- [⚙️ Spécifications matérielles](#spécifications-matérielles)
- [🌟 Projets de la communauté](#projets-de-la-communauté)
- [🧹 Accessoires optionnels](#accessoires-optionnels)
- [🎓 Écosystème robotique full-stack](#écosystème-robotique-full-stack)
- [🙌 Remerciements et contributeurs](#remerciements-et-contributeurs)
- [📄 Licence](#licence)
- [☎ Contactez-nous](#contactez-nous)

---

## 📖 Introduction

**reBot-DevArm** —— **reBot Arm B601-DM** et **reBot Arm B601-RS** —— est un projet de bras robotique dédié à réduire les barrières d'apprentissage de l'IA incarnée. Nous croyons au « véritable open source » : pas seulement le code, mais tout, publié sans réserve.

- 🦾 **Deux modèles de bras** —— Tous les fichiers de conception du **B601-DM (Damiao)** et du **B601-RS (Robstride)**, deux bras à l'apparence identique.
- 🛠️ **Plans matériels** —— Fichiers sources des pièces en tôle et des pièces imprimées en 3D.
- 🔩 **Liste BOM** —— Détaillée jusqu'à la spécification et au lien d'achat de chaque vis.
- 💻 **Logiciels et algorithmes** —— SDK Python, ROS1/2, Isaac Sim, LeRobot, etc.

## 🛒 Obtenez votre reBot Arm

| Modèle | Boutique officielle | Autres canaux |
| :--- | :--- | :--- |
| **reBot Arm B601-DM** | [SeeedStudio Bazaar](https://www.seeedstudio.com/reBot-Arm-B601-DM-Assembled-Kit-with-Power-Supply-Bundle.html) | [Amazon](https://www.amazon.com/dp/B0H2TWVFSW) · [AliExpress](https://de.aliexpress.com/item/1005012108314029.html) |
| **reBot Arm B601-RS** | [SeeedStudio Bazaar](https://www.seeedstudio.com/reBot-Arm-B601-RS-Bundle-p-6898.html) | [AliExpress](https://www.aliexpress.us/item/3256812343811970.html?gatewayAdapt=deu2usa4itemAdapt) |

### Options de kit B601-DM

Cinq options de kit sont disponibles sur [SeeedStudio.com](https://www.seeedstudio.com/reBot-Arm-B601-DM-Bundle.html) :

- **Kit moteurs du corps du bras** —— Moteurs et faisceaux de câblage uniquement.
- **Kit structure du corps du bras** —— Composants structurels mécaniques uniquement.
- **Kit complet de préhenseur** —— Moteurs, câblage et structure du préhenseur.
- **Kit complet** —— Corps du bras et préhenseur complets.
- **Bras robotique préassemblé** —— Entièrement assemblé, prêt à l'emploi.

> 💡 Le kit n'inclut pas d'adaptateur d'alimentation ni de serre-joints en C de série, car vous pouvez l'alimenter avec des batteries ou le monter sur une base DIY. Achetez séparément une [alimentation](https://www.seeedstudio.com/AC-DC-Power-Adapter-IEC-60320-C14-XT30-Female-24V-4-5A-1200mm-L190-W92-5-H36mm-p-6764.html) et un [cordon d'alimentation](https://www.seeedstudio.com/reServer-AC-US-p-5052.html), ou consultez la solution Mean Well en bas de la [BOM](./hardware/reBot_B601_DM/readme.md#about-power-supply).

### Options de kit B601-RS

Deux options de kit sont disponibles sur [SeeedStudio.com](https://www.seeedstudio.com/reBot-Arm-B601-RS-Assembled-Kit-with-Gripper-p-6865.html) :

- **Kit complet** —— Corps du bras et préhenseur complets, non assemblés.
- **Bras robotique préassemblé** —— Entièrement assemblé, prêt à l'emploi.

> 💡 Nous recommandons l'alimentation [Mean Well 48V 12.5A](https://www.amazon.com/sspa/click?ie=UTF8&spc=MTo0NzgzODk2NzUxNTQ0NzEyOjE3ODE2MTA2NTU6c3BfYXRmOjIwMDExNjA5NjQwMTc5ODo6MDo6&url=%2FLRS-350-48-Price-Switching-Supply-MeanWell%2Fdp%2FB0BP6S5DYR%2Fref%3Dsr_1_1_sspa%3Fcrid%3D27VPQOWNPN9UG%26dib%3DeyJ2IjoiMSJ9.qK84sGJa4-74kbCEX11MOFBju8sSQUdFsbHw6PNvmaEHnhzjX2T7dyhRNJY01mXxpWk8lccGOwnezxmqLKUjqglX_FI26mrxlvZf0KNiLdJ8QnhKsber4KDoyyLHNxWGV451uHCzZbCDXxM0iYXVnubuVourRaRURlyMorRavuLd2a32kABx-BKqyF5Dfr7dV453ecE6QULFqG-UVLBaBRijbxQGTJ2YiNyXAqn3bkM.Bt5mAPOJNAWGnXCC2mwvjdDdccZd1_0-WRXZpP4mR4M%26dib_tag%3Dse%26keywords%3DLRS-350-48%26qid%3D1781610655%26sprefix%3Dlrs-350-%252Caps%252C331%26sr%3D8-1-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9hdGY%26psc%3D1) pour le modèle RS. Pour des performances complètes, optez pour un adaptateur 48V 25A.

### Bras leader (Leader Arm, optionnel)

Achetez le [Leader Arm](https://www.seeedstudio.com/Star-Arm-102-p-6765.html?qid=P2U7IG_yskyak5m_1776415593315) et une [alimentation 12V 10A](https://www.seeedstudio.com/FY1209900-12V-10A-Power-Adapter-12V-10A-p-6496.html) ; l'adaptateur 12V DC du SO-ARM101 convient également.

## 🚀 Essayez la simulation en ligne

Découvrez le jumeau numérique MuJoCo du reBot Arm B601-RS directement dans votre navigateur, sans installation. Basculez entre le bras standard et la configuration AGV, contrôlez les articulations et le TCP, affichez les caméras globale et de poignet D405, puis lancez les démonstrations automatiques de rangement et d'empilage. Le premier chargement du modèle peut prendre un instant ; Chrome ou Edge est recommandé.

<p align="center">
  <a href="https://yang-ci.github.io/Rebot_Arm_AGV/"><strong>▶ Lancer la démo interactive reBot Arm</strong></a>
</p>

## 🗺️ Feuille de route

Nous maintenons et adaptons en continu les principaux écosystèmes de développement robotique. Voici notre progression et notre plan de publication.

### reBot Arm B601-DM

| Écosystème | État | Description | Documentation |
| :--- | :---: | :--- | :--- |
| Utilisation de base des moteurs | ✅ Terminé | Contrôle de mouvement et encapsulation d'API | [Damiao Technology](https://wiki.seeedstudio.com/cn/damiao_series/) |
| Pièces STEP 3D et BOM | ✅ Terminé | Fichiers STEP, BOM et prix de référence | [BOM reBot Arm B601-DM](./hardware/reBot_B601_DM/readme.md) |
| Tests de performance sur machine réelle | ✅ Terminé | Performance en conditions normales et extrêmes | [Performance Testing](./hardware/reBot_B601_DM/performance_testing/Performance_Testing.md) |
| Vidéo d'assemblage | ✅ Terminé | Étapes d'assemblage ultra détaillées et vidéo | [Getting Started](https://wiki.seeedstudio.com/rebot_b601_dm_getting_started/) |
| SDK Python | ✅ Terminé | Lecture/écriture et contrôle tout-en-un des moteurs Robstride, Damiao, Mota, Gaoqing, Hexfellow… | [Motorbridge](https://motorbridge.seeedstudio.com) · [Web UI](https://rebot-devarm.w0x7ce.eu/) |
| Intégration ROS2 | ✅ Terminé | Cinématique, planification de trajectoire et compensation de gravité | [Guide ROS2](https://wiki.seeedstudio.com/rebot_arm_b601_dm_ros2_integration/) |
| Intégration Pinocchio | ✅ Terminé | Cinématique directe/inverse et compensation de gravité | [Guide Pinocchio](https://wiki.seeedstudio.com/rebot_arm_b601_dm_pinocchio_meshcat/) · [Dépôt](https://github.com/Seeed-Projects/reBotArm_control_py) |
| Simulation Isaac Sim | ✅ Terminé | Modèles USD et téléopération simulée | [Wiki](https://wiki.seeedstudio.com/rebot_arm_b601_dm_isaacsim/) |
| Téléopération VR | ✅ Terminé | Téléopération bilatérale basée sur PICO 4 VR | [Dépôt](https://github.com/Eaglewzw/lerobot-teleoperator-rebot-vr) |
| Intégration LeRobot | ✅ Terminé | Framework d'entraînement LeRobot de Hugging Face | [Guide LeRobot](https://wiki.seeedstudio.com/rebot_arm_b601_dm_lerobot/) |
| Intégration caméra de profondeur | ✅ Terminé | Démo de préhension visuelle avec YOLO et caméra de profondeur | [Démo de préhension](https://wiki.seeedstudio.com/rebot_arm_b601_dm_grasping_demo/) |
| Intégration vocale reSpeaker | ✅ Terminé | Réseau reSpeaker Flex à 4 micros, contrôle vocal avec conscience spatiale | [Contrôle vocal](https://wiki.seeedstudio.com/control_rebot_arm_using_voice_with_respeaker_flex/) |
| Derniers algorithmes | ⏳ Prévu | Algorithmes grand public mis à jour progressivement | En cours |
| Série de cours gratuits | ⏳ Prévu | Une série de cours entièrement gratuits | En cours |

#### Contributions des développeurs

| Écosystème | Auteur | Description | Dépôt |
| :--- | :---: | :--- | :--- |
| ROS2 (Humble), intégration tierce, URDF / rebotarm_bringup | [@danieldoradotalaveron-rb](https://github.com/danieldoradotalaveron-rb) | 1. **Moniteur de diagnostics passif** (`rebotarm_monitor_ros2`) —— superposition `/diagnostics` pour `rqt_robot_monitor`, agrégateur serial/CAN ;<br>2. **Stationnement et arrêt sûrs** —— capture de la pose de repos et retour lent à l'arrêt ou via `/rebotarm/park` ;<br>3. **Compensation de gravité (arrêt doux)** —— rampe MIT pour éliminer les à-coups lors de la transition pos/vel ;<br>4. **Téléopération gamepad (IK/FK + sécurité)** —— contrôle de l'effecteur par IK, visualisation RViz (simulation uniquement) ;<br>5. **TF D405 eye-in-hand** —— Xacro sous `end_link` pour visualisation RViz et TF. | [rebotarm_monitor_ros2](https://github.com/danieldoradotalaveron-rb/rebotarm_monitor_ros2) · [reBotArmController_ROS2](https://github.com/danieldoradotalaveron-rb/reBotArmController_ROS2) |

### reBot Arm B601-RS

| Écosystème | État | Description | Documentation |
| :--- | :---: | :--- | :--- |
| Utilisation de base des moteurs | ✅ Terminé | Contrôle de mouvement et encapsulation d'API | [Robstride](https://wiki.seeedstudio.com/cn/robstride_control/) |
| Pièces STEP 3D et BOM | ✅ Terminé | Fichiers STEP, BOM et prix de référence | [BOM reBot Arm B601-RS](./hardware/reBot_B601_RS/README.md) |
| Prise en main | ✅ Terminé | Démarrage rapide du B601-RS | [Getting Started](https://wiki.seeedstudio.com/rebot_b601_rs_getting_started/) |
| Vidéo d'assemblage | ✅ Terminé | Étapes d'assemblage ultra détaillées et vidéo | [Vidéo d'assemblage](https://wiki.seeedstudio.com/rebot_b601_rs_getting_started/) |
| ROS2 (Humble) | ✅ Terminé | Cinématique, planification de trajectoire, compensation de gravité et MoveIt2 | [Guide ROS2](https://wiki.seeedstudio.com/rebot_arm_b601_rs_ros2_integration/) |
| Intégration LeRobot | ✅ Terminé | Framework d'entraînement LeRobot de Hugging Face | [Guide LeRobot](https://wiki.seeedstudio.com/rebot_arm_b601_rs_lerobot/) |
| Intégration Pinocchio | ✅ Terminé | Cinématique directe/inverse et compensation de gravité | [Guide Pinocchio](https://wiki.seeedstudio.com/rebot_arm_b601_rs_pinocchio_meshcat/) · [Dépôt](https://github.com/Seeed-Projects/reBotArm_control_py) |
| Intégration caméra de profondeur | ✅ Terminé | Démo de préhension visuelle avec YOLO et caméra de profondeur | [Démo de préhension](https://wiki.seeedstudio.com/rebot_arm_b601_rs_grasping_demo/) |
| Architecture d'agent incarné | ✅ Terminé | Reçoit des commandes en langage naturel (p. ex. « pick up the red block »), planifie et exécute la préhension automatiquement | [Conception](https://wiki.seeedstudio.com/wrc_demo_tutorial/) · [Code source](https://github.com/TheMoonAstronaut/wrc.git) |
| Simulation Isaac Sim | ✅ Terminé | Modèles USD et téléopération simulée | [Cours DLI](https://www.seeedstudio.com/sim-to-real-with-seeed-rebot-and-nvidia-isaac) · [Dépôt](https://github.com/Seeed-Projects/reBot-Isaacsim) |
| Derniers algorithmes | ⏳ Prévu | Algorithmes grand public mis à jour progressivement | En cours |
| Série de cours gratuits | ⏳ Prévu | Une série de cours entièrement gratuits | En cours |

#### Contributions des développeurs

| Écosystème | Auteur | Description | Dépôt |
| :--- | :---: | :--- | :--- |
| Téléopération par iPhone, HEBI Mobile I/O et Meta Quest | [@ammarjmahmood](https://github.com/ammarjmahmood) | Déplacez un téléphone ou une manette Quest et la pince suit, avec le mappage de pose relative de TidyBot++ (CoRL 2024) : application iPhone native SwiftUI et ARKit, HEBI Mobile I/O, WebXR en passthrough sur Quest, pilote MIT à 200 Hz avec compensation de gravité, cinématique inverse sur l'URDF RS officiel et verrouillages de sécurité. Testé sur un B601-RS avec un iPhone 16 Pro Max. | [rebot-phone-teleop](https://github.com/ammarjmahmood/rebot-phone-teleop) |

## ⚙️ Spécifications matérielles

Conçu pour des applications d'IA incarnée sur bureau, en équilibrant charge utile et flexibilité.

| Paramètre | reBot Arm B601-DM | reBot Arm B601-RS |
| :--- | :--- | :--- |
| Charge utile | 1,5 kg | **2,5 kg** |
| Espace de travail recommandé | 70 % de la portée du bras | 70 % de la portée du bras |
| Portée maximale | 767 mm | **754 mm** |
| Poids | **≈ 4,5 kg** | ≈ 6,7 kg |
| Répétabilité | < 0,2 mm | < 0,2 mm |
| Degrés de liberté | 6 DOF + 1 pince | 6 DOF + 1 pince |
| Écosystèmes pris en charge | ROS1, ROS2, LeRobot, Pinocchio, Isaac Sim, SDK Python | ROS1, ROS2, LeRobot, Pinocchio, Isaac Sim, SDK Python |
| Tension d'alimentation | DC 24V | DC 48V |

## 🌟 Projets de la communauté

|  |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: |
| <a href="https://www.kaggle.com/competitions/gemma-4-good-hackathon/writeups/new-writeup-1778618527713"><img src="/community/GEM-4.png" height="80" alt="GEM-4"></a><br><sub>[De GEM-4](https://www.kaggle.com/competitions/gemma-4-good-hackathon/writeups/new-writeup-1778618527713)</sub> | <a href="https://x.com/Linyan_Fu/status/2056383947341525180"><img src="/community/from_Linyan.png" height="80" alt="Linyan Fu"></a><br><sub>[De Linyan Fu](https://x.com/Linyan_Fu/status/2056383947341525180) · [Apheth D Almeida](https://x.com/Apheth_DAlmeida/status/2053503164507476096)</sub> | <a href="https://x.com/DhruvDiddi/status/2046605015008383284"><img src="/community/from_Diddi.png" height="80" alt="Dhruv Diddi"></a><br><sub>[De Dhruv Diddi](https://x.com/DhruvDiddi/status/2046605015008383284)</sub> | <a href="https://x.com/ed0henderson/status/2055076839002095743"><img src="/community/from_Henderson.jpg" height="80" alt="Ed Henderson"></a><br><sub>[D'Ed Henderson](https://x.com/ed0henderson/status/2055076839002095743)</sub> | <img src="/community/from_Sameer.png" height="80" alt="Sameer"><br><sub>Sameer</sub> |
| <a href="https://x.com/pham_blnh/status/2061994096374505710"><img src="/community/from_Binh_Pham.png" height="80" alt="Binh Pham"></a><br><sub>[De Binh Pham](https://x.com/pham_blnh/status/2061994096374505710)</sub> | <a href="https://www.instagram.com/reel/DY7Ny8OPjVu/?utm_source=ig_web_copy_link&igsh=NTc4MTIwNjQ2YQ=="><img src="/community/from_fangtianchonghui.png" height="80" alt="FangTianChongHui"></a><br><sub>[De FangTianChongHui](https://www.instagram.com/reel/DY7Ny8OPjVu/?utm_source=ig_web_copy_link&igsh=NTc4MTIwNjQ2YQ==)</sub> | <a href="https://x.com/dong1505lin"><img src="/community/from_xensedyl.png" height="80" alt="Xense YaoLin Dong"></a><br><sub>[Xense YaoLin Dong](https://x.com/dong1505lin)</sub> | <a href="https://x.com/ed0henderson/status/2055076839002095743"><img src="/community/from_Henderson_2.png" height="80" alt="Ed Henderson"></a><br><sub>[D'Ed Henderson](https://x.com/ed0henderson/status/2055076839002095743)</sub> | <a href="https://x.com/yoshikai_man/status/2079938975398244705"><img src="/community/YOR_Car.png" height="80" alt="yoshikai_man"></a><br><sub>[De yoshikai_man](https://x.com/yoshikai_man/status/2079938975398244705)</sub> |
| <a href="https://github.com/lipengdong/hei-rebot-lift"><img src="/community/hei-robot-lift-play.gif" height="80" alt="hei-rebot-lift"></a><br><sub>[De hei-rebot-lift](https://github.com/lipengdong/hei-rebot-lift)</sub> | <a href="https://www.linkedin.com/posts/activity-7484390995862781952-TX4m?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE6WUL4BWkFeyUj0TJ5JlGf6IG4iRHAicUo"><img src="/community/VR_with_reBot.png" height="80" alt="Martin Kemka"></a><br><sub>[De Martin Kemka](https://www.linkedin.com/posts/activity-7484390995862781952-TX4m?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE6WUL4BWkFeyUj0TJ5JlGf6IG4iRHAicUo)</sub> | <a href="https://www.linkedin.com/posts/kamil-buczy%C5%84ski-102843301_seeedstudio-rebotarm-seeedprojectofthemonth-ugcPost-7485297094715461633-RV_6/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE6WUL4BWkFeyUj0TJ5JlGf6IG4iRHAicUo"><img src="/community/reBot_grasp_fruit.png" height="80" alt="Kamil Buczyński"></a><br><sub>[De Kamil Buczyński](https://www.linkedin.com/posts/kamil-buczy%C5%84ski-102843301_seeedstudio-rebotarm-seeedprojectofthemonth-ugcPost-7485297094715461633-RV_6/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE6WUL4BWkFeyUj0TJ5JlGf6IG4iRHAicUo)</sub> | <a href="https://www.linkedin.com/posts/doradodaniel_computervision-spatialai-sim2real-share-7474727487374184448-NhwX/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE6WUL4BWkFeyUj0TJ5JlGf6IG4iRHAicUo"><img src="/community/Daniel_Dorado.jpg" height="80" alt="Daniel Dorado"></a><br><sub>[De Daniel Dorado](https://www.linkedin.com/posts/doradodaniel_computervision-spatialai-sim2real-share-7474727487374184448-NhwX/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE6WUL4BWkFeyUj0TJ5JlGf6IG4iRHAicUo)</sub> | <a href="https://www.linkedin.com/posts/asierarranz_nvidia-physicalai-isaaclab-ugcPost-7480271721942417408-YNwu/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE6WUL4BWkFeyUj0TJ5JlGf6IG4iRHAicUo"><img src="/community/Groot_N1.7.png" height="80" alt="Asier"></a><br><sub>[D'Asier](https://www.linkedin.com/posts/asierarranz_nvidia-physicalai-isaaclab-ugcPost-7480271721942417408-YNwu/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE6WUL4BWkFeyUj0TJ5JlGf6IG4iRHAicUo)</sub> |
| <a href="https://x.com/thermalpastor/status/2103842737032458567"><img src="/community/thermalpastor.png" height="80" alt="H"></a><br><sub>[De H](https://x.com/thermalpastor/status/2103842737032458567)</sub> | <a href="https://x.com/Alpha10six/status/2103860758559994216"><img src="/community/alpha_rover.png" height="80" alt="alpha_rover"></a><br><sub>[D'alpha_rover](https://x.com/Alpha10six/status/2103860758559994216)</sub> | <a href="https://x.com/DilumSanjaya/status/2102806161728885145"><img src="/community/DilumSanjaya.png" height="80" alt="Dilum Sanjaya"></a><br><sub>[De Dilum Sanjaya](https://x.com/DilumSanjaya/status/2102806161728885145)</sub> | <a href="https://x.com/pham_blnh/status/2101003855731593544"><img src="/community/pham_blnh.png" height="80" alt="Binh"></a><br><sub>[De Binh](https://x.com/pham_blnh/status/2101003855731593544)</sub> | <a href="https://x.com/LeRobotHF/status/2104519372333048112"><img src="/community/LeRobot.png" height="80" alt="LeRobot"></a><br><sub>[De LeRobot](https://x.com/LeRobotHF/status/2104519372333048112)</sub> |
| <a href="https://x.com/raghav2956/status/2104659668375339475"><img src="/community/Raghav_Kumar.png" height="80" alt="Raghav Kumar"></a><br><sub>[De Raghav Kumar](https://x.com/raghav2956/status/2104659668375339475)</sub> | <a href="https://www.linkedin.com/posts/kamil-buczy%C5%84ski-102843301_seeedstudio-ai-agent-ugcPost-7510738285707776000-1SMQ/?utm_source=social_share_send&utm_medium=android_app&rcm=ACoAAE6WUL4BWkFeyUj0TJ5JlGf6IG4iRHAicUo"><img src="/community/Kamil_Buczynski.png" height="80" alt="Kamil Buczyński"></a><br><sub>[De Kamil Buczyński](https://www.linkedin.com/posts/kamil-buczy%C5%84ski-102843301_seeedstudio-ai-agent-ugcPost-7510738285707776000-1SMQ/?utm_source=social_share_send&utm_medium=android_app&rcm=ACoAAE6WUL4BWkFeyUj0TJ5JlGf6IG4iRHAicUo)</sub> | <a href="https://www.linkedin.com/feed/update/urn:li:activity:7510701008885309440/"><img src="/community/Fictionlab.png" height="80" alt="Fictionlab"></a><br><sub>[De Fictionlab](https://www.linkedin.com/feed/update/urn:li:activity:7510701008885309440/)</sub> | <a href="https://x.com/seeedstudio/status/2101965998954107303"><img src="/community/box2bridge.png" height="80" alt="box2bridge"></a><br><sub>[De box2bridge](https://x.com/seeedstudio/status/2101965998954107303)</sub> | <a href="https://x.com/seeedstudio/status/2095469352976003482"><img src="/community/Fangtian.png" height="80" alt="FangTianChongHui"></a><br><sub>[De FangTianChongHui](https://x.com/seeedstudio/status/2095469352976003482)</sub> |

<p align="center">
  <a href="https://www.seeedstudio.com/sim-to-real-with-seeed-rebot-and-nvidia-isaac"><img src="/community/sim-to-real-vla.gif" height="90" alt="Cours Sim-to-Real VLA"></a><br>
  <sub><a href="https://www.seeedstudio.com/sim-to-real-with-seeed-rebot-and-nvidia-isaac">Seeed reBot Arm × NVIDIA Isaac —— Cours Sim-to-Real VLA</a></sub>
</p>

## 🧹 Accessoires optionnels

### Support de caméra au poignet

Ces supports de caméra au poignet sont communs aux **B601-RS et B601-DM**. Consultez le [catalogue complet des supports et des ressources de collecte de données (en anglais)](hardware/camera-mounts/README.md) pour les modèles, les aperçus et les téléchargements.

| UVC 32×32 | Intel D435i | Intel D405 & Gemini 305 | Gemini 2 |
| :--- | :--- | :--- | :--- |
| <img src="./hardware/reBot_B601_DM/3D_Printed_Parts/images/UVC_camera_mount.png" height="100"> | <img src="./hardware/reBot_B601_DM/3D_Printed_Parts/images/D435i.jpg" height="100"> | <img src="./hardware/reBot_B601_DM/3D_Printed_Parts/images/D405.jpg" height="100"> | <img src="./hardware/reBot_B601_DM/3D_Printed_Parts/images/Gemini2.jpg" height="100"> |
| [STEP](hardware/camera-mounts/b601-camera-mounts/UVC32_mount.step) | [STEP](hardware/camera-mounts/b601-camera-mounts/D435_Gemini2_Mount.step) | [STEP](hardware/camera-mounts/b601-camera-mounts/D405_305_Mount.step) · [notes de conception](https://github.com/bowenszhu/rebot-b601-rs-d405-wrist-mount/tree/v1.0.0) | [STEP](hardware/camera-mounts/b601-camera-mounts/D435_Gemini2_Mount.step) |

### Compatible avec le bras leader

| Star Arm 102-LD | Ouvert à l'intégration et la compatibilité |
| :--- | :--- |
| <img src="./hardware/reBot_B601_DM/3D_Printed_Parts/images/star_arm_102.jpg" height="100"> | [Centre de la série](https://fashionstar.com.hk/robot-arm/star-arm-102/) · [Dépôt GitHub](https://github.com/servodevelop/Star-Arm-102) |

### Doigt souple DIY

| Doigt souple | Intégration compatible ouverte |
| :--- | :--- |
| <img src="./hardware/reBot_B601_DM/3D_Printed_Parts/images/Soft_Finger.png" height="100"> | Bientôt disponible |
| [Support de doigt (ABS/PLA)](hardware/reBot_B601_DM/3D_Printed_Parts/Soft_Gripper_Mount.step) · [Doigt (TPU 95+)](hardware/reBot_B601_DM/3D_Printed_Parts/Soft_Gripper_Finger.step) | Bientôt disponible |

### Matériel optionnel recommandé

| Catégorie | Type | Aperçu | Produit | Lien |
| :--- | :--- | :--- | :--- | :--- |
| **Caméra** | Caméra de profondeur | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/0/-/0-101090144--orbbec-gemini-2-3d-camera.jpg" alt="Orbbec Gemini 2" width="120"> | **Orbbec Gemini 2 3D Camera** | [Seeed Studio](https://www.seeedstudio.com/Orbbec-Gemini-2-3D-Camera-p-6464.html) |
| **Caméra** | Caméra de profondeur | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/1/0/1000000774.png" alt="Orbbec Gemini 336" width="120"> | **Orbbec Gemini 336 Depth Camera** | [Seeed Studio](https://www.seeedstudio.com/Orbbec-Gemini-336-3D-Camera-3D-p-6662.html) |
| **Caméra** | Caméra de profondeur | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/1/-/1-100010971-orbbec-gemini-335-lg.jpg" alt="Orbbec Gemini 335LG" width="120"> | **Orbbec Gemini 335LG 3D Camera** | [Seeed Studio](https://www.seeedstudio.com/Orbbec-Gemini-335LG-3D-Camera-p-6541.html) |
| **Caméra** | Caméra de profondeur | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/0/0/0035718.png" alt="SLAMTEC Aurora S" width="120"> | **SLAMTEC Aurora S** | [Seeed Studio](https://www.seeedstudio.com/SLAMTEC-Aurora-S-AI-Integrated-Spatial-Perception-System-p-6669.html) |
| **Caméra** | Caméra de profondeur | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/i/n/intel_realsense_d435i_34_1_1.jpg" alt="Intel RealSense D435i" width="120"> | **Intel RealSense Depth Camera D435i** | [Seeed Studio](https://www.seeedstudio.com/Intel-RealSense-Depth-Camera-D435i-p-4423.html) |
| **Caméra** | Caméra de profondeur | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/1/-/1-100000540-realsense-d405-3d-camera.jpg" alt="RealSense D405" width="120"> | **RealSense Depth Camera D405** | [Seeed Studio](https://www.seeedstudio.com/RealSense-D405-3D-Camera-p-6758.html) |
| **Caméra** | Caméra monoculaire | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/0/-/0-101090101-3mp-gmsl2-camera-module-190-degree.jpg" alt="Sensing SG3S-ISX031C-GMSL2F" width="120"> | **Sensing SG3S-ISX031C-GMSL2F 3MP GMSL2 Camera** | [Seeed Studio](https://www.seeedstudio.com/SG3S-ISX031C-GMSL2F-p-6245.html) |
| **Caméra** | Caméra monoculaire | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/s/2/s231.1.jpg" alt="ET-S231" width="120"> | **ET-S231 Megapixel 120° grand angle 1080P USB** | [Seeed Studio](https://www.seeedstudio.com/ET-S231-120-USB-Camera-p-6683.html) |
| **Microphone** | Réseau de micros | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/1/-/1-100070894-respeaker-flex-xvf3800-circular-4-with-xiao-esp32s3_1_.jpg" alt="reSpeaker Flex XVF3800" width="120"> | **reSpeaker Flex XVF3800 Circular-4 with XIAO ESP32S3** | [Seeed Studio](https://www.seeedstudio.com/reSpeaker-Flex-XVF3800-Circular-4-with-XIAO-ESP32S3-p-6739.html) |
| **Microphone** | Réseau de micros | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/1/-/1-respeaker-xvf3800-4-mic-array.jpg" alt="reSpeaker XMOS XVF3800" width="120"> | **reSpeaker XMOS XVF3800** | [Seeed Studio](https://www.seeedstudio.com/ReSpeaker-XVF3800-USB-Mic-Array-p-6488.html) |
| **Contrôleur** | Contrôleur embarqué | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/1/1/110110147.jpg" alt="reComputer J3011" width="120"> | **reComputer J3011-Orin Nano 8GB** | [Seeed Studio](https://www.seeedstudio.com/reComputer-J3011-p-5590.html) |
| **Contrôleur** | Contrôleur embarqué | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/7f7f32ef807b8c2c2215b49801c56084/i/m/image-kit-3.png" alt="Jetson AGX Thor" width="120"> | **NVIDIA Jetson AGX Thor Developer Kit** | [Seeed Studio](https://www.seeedstudio.com/NVIDIA-Jetson-AGX-Thor-Developer-Kit-p-9965.html) |

## 🎓 Écosystème robotique full-stack

reBot-DevArm n'est pas seulement un bras robotique, mais une communauté d'apprentissage de la robotique. Nous partageons gratuitement les tutoriels généraux suivants :

**🖥️ Edge Computing & contrôle principal**

- [![Jetson](https://img.shields.io/badge/NVIDIA-reComputer%20Jetson-76B900?style=for-the-badge&logo=nvidia&logoColor=white)](https://wiki.seeedstudio.com/NVIDIA_Jetson/) —— Inférence IA & cœur de calcul
- [![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-4B%20%2F%205-C51A4A?style=for-the-badge&logo=Raspberry%20Pi&logoColor=white)](https://wiki.seeedstudio.com/raspberry-pi-devices/) —— Environnement général de développement Linux
- [![ESP32](https://img.shields.io/badge/MCU-Seeed%20XIAO%20(ESP32)-0091BD?style=for-the-badge&logo=espressif&logoColor=white)](https://wiki.seeedstudio.com/SeeedStudio_XIAO_Series_Introduction/) —— Nœud de contrôle sans fil basse consommation

**📡 Capteurs & périphériques**

- **Moteurs & servomoteurs** —— [Damiao / Gogo / Robstride / Mita / Feite / Fashion Star](https://wiki.seeedstudio.com/robotics_page/)
- **Perception visuelle** —— [Caméras de profondeur / LiDAR / algorithmes de vision](https://wiki.seeedstudio.com/robotics_page/)
- **Interaction vocale** —— [Réseaux de micros reSpeaker / contrôle vocal / perception spatiale (DoA)](https://wiki.seeedstudio.com/control_rebot_arm_using_voice_with_respeaker_flex/)
- **Mouvement & attitude** —— [IMU (6/9 axes) / gyroscopes / magnétomètres](https://wiki.seeedstudio.com/Sensor_accelerometer/)
- **Kits complets** —— [Plus de capteurs robotiques & d'exemples de pilotes](https://wiki.seeedstudio.com/robotics_page/)

> 👉 **[Accédez à la base de connaissances du Wiki](https://wiki.seeedstudio.com/)** —— tous les tutoriels sont consultables gratuitement.

## 🙌 Remerciements et contributeurs

Le chemin de l'open source n'est jamais solitaire. Le projet reBot-DevArm n'existerait pas sans le soutien de Seeed Studio, de la communauté open source mondiale et de nos partenaires matériels.

**🌍 Écosystème & support logiciel**

- [Seeed Studio](https://www.seeedstudio.com/) —— Chaîne d'approvisionnement matérielle et support technique
- [Hugging Face LeRobot](https://github.com/huggingface/lerobot) —— Framework d'apprentissage robotique de bout en bout
- [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim) —— Plateforme de simulation robotique et de données synthétiques

**⚙️ Partenaires matériels principaux**

- [Damiao Technology](https://www.damiaokeji.com/)
- [Robstride](https://robstride.com/)
- [Fashion Star](https://fashionstar.com.hk/wiki/)

**💡 Inspiration**

- [SO-ARM100](https://github.com/TheRobotStudio/SO-ARM100/tree/main)
- [Mobile ALOHA](https://github.com/tonyzhaozh/aloha)
- [Dummy-Robot (Zhihui Jun)](https://github.com/peng-zhihui/Dummy-Robot)
- [OpenArm](https://openarm.dev/)
- [I2RT](https://i2rt.com/)
- [TRLC-DK1](https://github.com/robot-learning-co/trlc-dk1)

**🎃 Contributeurs du prototype**

- Équipe SeeedStudio AI Robotics —— Yaohui Zhu (yaohui.zhu@seeed.cc)
- SeeedStudio STU —— Wentao Dong
- SeeedStudio STU —— Weiwei Xu
- Département des achats de SeeedStudio —— Fengqun Peng

**👥 Contributeurs**

<p align="center"><a href="https://github.com/Seeed-Projects/reBot-DevArm/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=Seeed-Projects/reBot-DevArm" />
</a></p>

*Bientôt disponible… N'hésitez pas à soumettre des PR pour devenir contributeur !*

### ⭐ Historique des étoiles

<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/star-history/star-history-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/star-history/star-history-light.svg">
  <img src="assets/star-history/star-history-light.svg">
</picture>
</p>

## 📄 Licence

- **Conception matérielle** © 2026 Seeed Studio Co., Ltd. —— publiée sous [CERN-OHL-W-2.0](https://ohwr.org/cern_ohl_w_v2.txt)
- **Code du firmware** © 2026 Seeed Studio Co., Ltd. —— publié sous [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)

### Droits et restrictions

Le projet reBot Arm a toujours suivi la philosophie d'**agilité, d'ouverture, de responsabilité et de symbiose** au service de la communauté. Notre vision est de permettre à chaque passionné de maîtriser l'architecture matérielle et les principes logiciels des bras robotiques, et de vivre une expérience immersive avec les algorithmes de pointe de l'intelligence incarnée.

Pendant les cinq premiers mois, le projet a utilisé la licence **CC BY-SA NC (non commerciale)**, afin que les développeurs puissent se concentrer sur l'itération et l'amélioration du produit dans sa phase initiale. Après des mois de perfectionnement, **à compter du 11 mai 2026**, le projet est passé à la licence **CERN-OHL-W 2.0**, atteignant une **open source à 100% sur l'ensemble de la chaîne (matériel et logiciel), avec des droits d'utilisation commerciale complets pour tous les scénarios**.

Le matériel et le logiciel utilisent des licences différentes ; veuillez confirmer les termes applicables à la partie que vous utilisez.

| Élément | Matériel (CERN-OHL-W-2.0) | SDK logiciel (Apache-2.0) |
| :--- | :--- | :--- |
| ✅ Utilisation commerciale | ✅ Autorisée | ✅ Autorisée |
| ✅ Modification | ✅ Autorisée | ✅ Autorisée |
| ✅ Redistribution | ✅ Autorisée | ✅ Autorisée |
| ✅ Intégration en source fermée | ❌ Conditionnelle (voir [CERN-OHL-W-2.0](https://ohwr.org/cern_ohl_w_v2.txt)) | ✅ Autorisée (aucune divulgation requise) |
| ⚠️ Conservation du copyright | ✅ Requise | ✅ Requise |
| ⚠️ Conservation du texte de licence | ✅ Requise | ✅ Requise |
| ⚠️ Mention des modifications | ✅ Requise (date + description) | ✅ Requise (description) |
| ⚠️ Licence de brevet | ✅ Explicite | ✅ Explicite |
| ⚠️ Fourniture des sources à la distribution | ✅ **Obligation** de fournir la « source complète » | ❌ Aucune obligation |
| ⚠️ Compatibilité avec les modules externes/fermés | ✅ Autorisée (Weakly Reciprocal) | ✅ Totalement autorisée |
| 🔗 Relation avec d'autres composants | Les modules d'interface indépendants (External Material) peuvent rester fermés | Aucune restriction |
| 📄 Texte officiel complet | [CERN-OHL-W-2.0](https://ohwr.org/cern_ohl_w_v2.txt) | [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) |

## ☎ Contactez-nous

- **Progrès open source & support technique** —— Yaohui : yaohui.zhu@seeed.cc
- **Collaboration future & personnalisation** —— Elaine : elaine.wu@seeed.cc
