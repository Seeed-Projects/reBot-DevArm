<img width="354" height="94" alt="image" src="https://github.com/user-attachments/assets/5eee1c33-b1b3-458e-838d-651fbbee655e" />
# 🦾 reBot-DevArm: Open Source Robotic Arm for All Developers

<p align="center">
  <img src="./media/v1.5.jpg" alt="reBot-DevArm Banner">
</p>

<p align="center">
    <!-- Remplacé par le badge CC BY-NC-SA 4.0, indiquant explicitement l'usage non commercial -->
    <a href="./LICENSE">
        <img src="https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg" alt="License: CC BY-NC-SA 4.0">
    </a>
    <img src="https://img.shields.io/badge/Commercial-Contact%20Us-red.svg" alt="yaohui.zhu@seeed.cc">
    <img src="https://img.shields.io/badge/ROS-Noetic%20%7C%20Humble-orange.svg" alt="ROS Support">
    <img src="https://img.shields.io/badge/Framework-LeRobot-yellow.svg" alt="LeRobot">
    <img src="https://img.shields.io/badge/Framework-Isaac Sim-yellow.svg" alt="LeRobot">
</p>

<p align="center">
  <strong>100% Entièrement Open Source · IA Incarnée (Embodied AI) · Intégration Logiciel-Matériel · Gratuit pour Personnel/Éducation · Usage Commercial sous Licence</strong>
</p>

<p align="center">
  <strong>
    <a href="./README_zh.md">简体中文</a> &nbsp;|&nbsp;
    <a href="./README.md">English</a> &nbsp;|&nbsp;
    <a href="./README_JP.md">日本語</a>&nbsp;|&nbsp;
    <a href="./README_Fr.md">français</a>
  </strong>
</p>

<p align="center">
<a href="https://discord.gg/AbGuqJhDpQ">
    <img src="https://img.shields.io/discord/1409155673572249672?color=7289DA&label=Discord&logo=discord&logoColor=white"></a>
<a href="https://wiki.seeedstudio.com/robotics_page/">  
    <img src="https://img.shields.io/badge/Documentation-📕-blue" alt="robotics wiki"></a>
</p

## 📖 Introduction

**reBot-DevArm (Total Open Source Arm)** est un projet de bras robotique dédié à abaisser la barrière d'apprentissage de l'intelligence artificielle incarnée (Embodied AI). Nous prônons le **"Véritable Open Source"** — pas seulement le code, nous partageons tout sans réserve :

- 🛠️ **Plans Matériels** : Fichiers sources pour les pièces de tôlerie et d'impression 3D.
- 🔩 **Liste BOM** : Détaillée jusqu'aux spécifications de chaque vis et liens d'achat.
- 💻 **Logiciels et Algorithmes** : SDK Python, ROS1/2, Isaac Sim, LeRobot, etc.

**⚠️ Note : Ce projet vise à promouvoir l'éducation et l'apprentissage personnel. Toutes les ressources sont entièrement gratuites pour les développeurs individuels, les étudiants et les établissements d'enseignement. Cependant, toute utilisation commerciale non autorisée (y compris, mais sans s'y limiter, la vente directe de kits ou l'intégration dans un produit commercial) est strictement interdite.**

## 🗺️ Feuille de Route et Statut (Roadmap & Status)

Nous nous engageons à maintenir et à adapter continuellement le projet aux écosystèmes de développement robotique grand public. Voici notre progression actuelle et notre calendrier de publication prévu :

| Écosystème Adapté | Statut | Description / Date Prévue | Documentation |
| :--- | :---: | :--- | :--- |
| **Utilisation de base des moteurs** | ✅ Terminé | Contrôle de mouvement de base et encapsulation API | [Voir Docs](https://wiki.seeedstudio.com/cn/damiao_series/) |
| **Nouvelle Version STEP Structure 3D & BOM** | 🚧 En Cours | Fichiers STEP pour toutes les nouvelles pièces, BOM composants, et prix de référence pour toutes les pièces usinées | [Prévu 2026.02] |
| **Vidéo d'Assemblage** | 🚧 En Cours | Étapes d'assemblage ultra-détaillées et vidéo | [Prévu 2026.02] |
| **ROS2 (Humble)** |⏳ Prévu | Pilote principal terminé, optimisation de MoveIt2 en cours |[Prévu 2026.03]|
| **Adaptation LeRobot** | ⏳ Prévu | Adaptation au framework d'entraînement Hugging Face LeRobot | [Prévu 2026.03]|
| **Adaptation Pinocchio** | ⏳ Prévu | Adaptation au framework Pinocchio, implémentation de la cinématique directe/inverse et compensation de gravité dynamique | [Prévu 2026.03]|
| **Simulation Isaac Sim** | ⏳ Prévu | Importation de modèles USD et implémentation de la téléopération en simulation | [Prévu 2026.03]|
| **Mise à jour progressive des algorithmes** | ⏳ Prévu | Mise à jour progressive des algorithmes grand public | En continu |
| **Lancement de cours entièrement gratuits** | ⏳ Prévu | Tutoriels étape par étape | En continu |

---


### 🎓 Écosystème Robotique Full-Stack
reBot-DevArm n'est pas seulement un bras robotique, mais une communauté d'apprentissage en robotique. Nous partageons gratuitement les tutoriels généraux suivants :

#### 🖥️ Informatique en périphérie et Contrôle Principal
*   [![Jetson](https://img.shields.io/badge/NVIDIA-reComputer%20Jetson-76B900?style=for-the-badge&logo=nvidia&logoColor=white)](https://wiki.seeedstudio.com/NVIDIA_Jetson/) —— **Inférence IA et Cœur de Calcul**
*   [![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-4B%20%2F%205-C51A4A?style=for-the-badge&logo=Raspberry%20Pi&logoColor=white)](https://wiki.seeedstudio.com/raspberry-pi-devices/) —— **Environnement de développement Linux général**
*   [![ESP32](https://img.shields.io/badge/MCU-Seeed%20XIAO%20(ESP32)-0091BD?style=for-the-badge&logo=espressif&logoColor=white)](https://wiki.seeedstudio.com/SeeedStudio_XIAO_Series_Introduction/) —— **Nœud de contrôle sans fil basse consommation**

#### 📡 Capteurs et Périphériques
*   **🚗 Moteurs et Servos** : [Damiao / Gogo / Robstride / Mita / Feite / Fashion Star](https://wiki.seeedstudio.com/robotics_page/)
*   **👁️ Perception Visuelle** : [Caméras de profondeur / LiDAR / Algorithmes de vision](https://wiki.seeedstudio.com/robotics_page/)
*   **👂 Interaction Auditive** : [Réseaux de micros ReSpeaker / Reconnaissance vocale](https://wiki.seeedstudio.com/ReSpeaker_Mic_Array_v2.0/)
*   **🧭 Mouvement et Attitude** : [IMU (6 axes/9 axes) / Gyroscopes / Magnétomètres](https://wiki.seeedstudio.com/Sensor/IMU/)
*   **🤖 Kits Complets** : [Plus d'exemples de capteurs et pilotes robotiques](https://wiki.seeedstudio.com/robotics_page/)


> 👉 **[Cliquez pour entrer dans la base de connaissances Wiki](https://wiki.seeedstudio.com/)** (Tous les tutoriels sont consultables gratuitement)

---

## ⚙️ Spécifications Matérielles (Specifications)

reBot-DevArm est conçu pour les applications d'IA incarnée de bureau, alliant capacité de charge et flexibilité.

| Paramètre | Valeur / Description |
| :--- | :--- |
| **Charge Utile (Payload)** | **1.5+ kg** |
| **Portée Max (Reach)** | **650 mm** |
| **Poids Propre (Weight)** | Env. 4.0 kg |
| **Répétabilité** | < 0.2 mm |
| **Degrés de Liberté (DOF)** | 6 DOF + 1 Pince (Gripper servo CAN et gripper moteur articulaire open source en route) |
| **Plateformes/Écosystèmes Supportés** | ROS1, ROS2, LeRobot, Pinocchio, Isaac Sim, SDK Python |
| **Tension d'Alimentation** | DC 24V |

---

## 📂 Open Source (Hardware Source)

Nous croyons que l'open source matériel favorise l'innovation. Vous pouvez trouver tout le nécessaire pour fabriquer ce bras dans les répertoires suivants :

*   [`/hardware/STEP`](./hardware/cad): Tous les fichiers STEP/STL des structures mécaniques, y compris les pièces imprimées, les pièces métalliques et les articles achetés.
*   [`/hardware/bom`](./hardware/bom): **Liste BOM** (Contient les modèles de composants achetés, les paramètres moteurs, les vendeurs recommandés).
*   [`/tutorial/ROS`](./tutorial/ROS/): Code source et tutoriels pour **ROS1/2 Noetic/Humble**.
*   [`/tutorial/Lerobot`](./tutorial/lerobot/): Code source et tutoriels pour **LeRobot**.
*   [`/tutorial/Isaac`](./tutorial/Isaac/): Code source et tutoriels pour **Isaac Sim**.
---

## 🚀 Démarrage Rapide (Getting Started)

Nous avons prévu pour vous un parcours d'apprentissage complet, du déballage à la simulation IA :

### 🛠️ Phase 1 : Construction Matérielle et Bases
| Étape | Description | Lien |
| :---: | :--- | :--- |
| **01** | **Utilisation de base des moteurs** (Basic Learning of Motors) | [📄 Cliquez pour voir](https://wiki.seeedstudio.com/cn/damiao_series/) |
| **02** | **Déballage** (Unboxing) | À venir |
| **03** | **Guide d'assemblage** (Assemble) | À venir |
| **04** | **Calibration du zéro** (Calibration) | À venir |
| **05** | **Test cinématique** (Kinematics) | À venir |

### 💻 Phase 2 : Algorithmes Avancés et Simulation
| Étape | Description | Lien |
| :---: | :--- | :--- |
| **06** | **Écosystème ROS** (ROS2) | 🐢 À venir |
| **07** | **Entraînement IA** (Hugging Face) | 🤗 À venir |
| **08** | **Simulation** (NVIDIA) | 🌌 À venir |

---


## 🙌 Références et Remerciements
Le chemin de l'open source n'est jamais solitaire. La naissance du projet reBot-DevArm ne serait pas possible sans le soutien total de Seeed Studio, de la communauté open source mondiale et d'excellents partenaires matériels. Nous rendons hommage aux projets et équipes suivants :

### 🌍 Écosystème et Support Logiciel
*   **[Seeed Studio](https://www.seeedstudio.com/)** - Fourniture d'une chaîne d'approvisionnement matériel complète et d'un support technique.
*   **[Hugging Face LeRobot](https://github.com/huggingface/lerobot)** - Un excellent framework d'apprentissage robotique de bout en bout.
*   **[NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim)** - Une puissante plateforme de simulation robotique et de données synthétiques.

### ⚙️ Partenaires Matériels Principaux
Merci aux fabricants suivants pour leurs solutions de moteurs et d'actionneurs haute performance :
*   **[Damiao Technology](https://www.damiaokeji.com/)**
*   **[Robstride](https://robstride.com/)**
*   **[Fashion Star](https://fashionrobo.com/)**

### 💡 Inspiration
Ce projet est profondément inspiré par les excellents projets open source suivants :
*   **[SO-ARM100](https://github.com/TheRobotStudio/SO-ARM100/tree/main)**
*   **[Mobile ALOHA](https://github.com/tonyzhaozh/aloha)**
*   **[Dummy-Robot (Zhihui Jun)](https://github.com/peng-zhihui/Dummy-Robot)**
*   **[OpenArm](https://openarm.dev/)**
*   **[I2RT](https://i2rt.com/)**
*   **[TRLC-DK1](https://github.com/robot-learning-co/trlc-dk1)**

### 🎃 Contributeurs Prototype
- **SeeedStudio AI Robotics Team's**: Yaohui Zhu (yaohui.zhu@seeed.cc)
- **SeeedStudio STU**: Wentao Dong
- **SeeedStudio STU**: Weiwei Xu
- **SeeedStudio Purchasing Department**: Fengqun Peng


### 👥 Autres Contributeurs (Contributors)

## Our Top Contributors 
<p align="center"><a href="https://github.com/Seeed-Projects/reBot-DevArm/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=Seeed-Projects/reBot-DevArm" />
</a></p>



*Bientôt disponible... Bienvenue pour soumettre des PR et devenir contributeur !*

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Seeed-Projects/reBot-DevArm&type=date&legend=top-left)](https://www.star-history.com/#Seeed-Projects/reBot-DevArm&type=date&legend=top-left)


# Licence du Projet reBot-DevArm
Copyright (c) [2025] [Seeed Studio AI Robotics Team]

Cette œuvre est mise à disposition selon les termes de la **Licence Creative Commons Attribution - Pas d’Utilisation Commerciale - Partage dans les Mêmes Conditions 4.0 International**.
Pour consulter une copie de cette licence, visitez : http://creativecommons.org/licenses/by-nc-sa/4.0/

--------------------------------------------------------------------------------

## Droits et Restrictions
1. Vous êtes libre de :
   - Partager : Copier et redistribuer le matériel par tout moyen et sous tout format.
   - Adapter : Remixer, transformer et créer à partir du matériel.

2. Selon les conditions suivantes :
   - Attribution : Vous devez créditer l'œuvre, intégrer un lien vers la licence et indiquer si des modifications ont été effectuées.
   - Pas d’Utilisation Commerciale : **Vous n'êtes pas autorisé à faire un usage commercial de cette œuvre**.
     (Y compris, mais sans s'y limiter, la vente de kits associés, la vente de pièces imprimées ou l'intégration de ce logiciel dans des produits payants sans autorisation explicite).
   - Partage dans les Mêmes Conditions : Dans le cas où vous effectuez un remix, que vous transformez, ou créez à partir du matériel composant l'œuvre originale, vous devez diffuser l'œuvre modifiée dans les même conditions, c'est à dire avec la même licence avec laquelle l'œuvre originale a été diffusée.

3. Autorisation Commerciale :
   Si vous souhaitez utiliser ce projet à des fins commerciales, veuillez contacter l'auteur pour obtenir une autorisation commerciale.
   Contact : yaohui.zhu@seeed.cc
