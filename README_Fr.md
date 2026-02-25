# 🦾 reBot-DevArm : Bras robotique open source pour tous les développeurs

<p align="center">
  <img src="./media/v2.0.png" alt="reBot-DevArm Banner">
</p>

<p align="center">
    <!-- Remplacé par le badge CC BY-NC-SA 4.0, indiquant explicitement l'usage non commercial -->
    <a href="./LICENSE">
        <img src="https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg" alt="Licence : CC BY-NC-SA 4.0">
    </a>
    <img src="https://img.shields.io/badge/Commercial-Contactez--nous-red.svg" alt="yaohui.zhu@seeed.cc">
    <img src="https://img.shields.io/badge/ROS-Noetic%20%7C%20Humble-orange.svg" alt="Support ROS">
    <img src="https://img.shields.io/badge/Framework-LeRobot-yellow.svg" alt="LeRobot">
    <img src="https://img.shields.io/badge/Framework-Isaac Sim-yellow.svg" alt="LeRobot">
</p>

<p align="center">
  <strong>100 % Open Source · IA incarnée · Intégration matériel-logiciel · Gratuit pour usage personnel/éducation · Utilisation commerciale soumise à autorisation</strong>
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

## 📖 Introduction

**reBot-DevArm** est un projet de bras robotique dédié à l'abaissement de la barrière à l'apprentissage de l'IA incarnée (Embodied AI). Nous nous concentrons sur le **"Vrai Open Source"** — pas seulement le code, nous ouvrons tout sans réserve :
- 🦾 **Deux versions du bras robotique** : Nous fournirons tous les fichiers open source pour deux versions du bras robotique ayant la même apparence : **Robostride** et **Damiao**.
- 🛠️ **Plans matériels** : Fichiers sources pour les pièces en tôlerie et les pièces imprimées en 3D.
- 🔩 **Liste BOM** : Détails précis jusqu'aux spécifications et liens d'achat pour chaque vis.
- 💻 **Logiciels et algorithmes** : SDK Python, ROS1/2, Isaac Sim, LeRobot, etc.

**⚠️ Remarque : Ce projet est destiné à promouvoir l'éducation et l'apprentissage personnel. Toutes les ressources sont entièrement gratuites pour les développeurs individuels, les étudiants et les institutions éducatives. Cependant, toute utilisation commerciale non autorisée (y compris, mais sans s'y limiter, la vente directe de kits ou l'utilisation comme partie d'un produit commercial) est strictement interdite.**

**Nous assouplirons la licence d'utilisation commerciale gratuite après avoir terminé toutes les évaluations de performance matérielle, de précision et de sécurité.**

## ☎ Contactez-nous
- **Progrès Open-Source et support technique** - Yaohui : yaohui.zhu@seeed.cc
- **Future collaboration et personnalisation** - Elaine : elaine.wu@seeed.cc

## 🗺️ Feuille de route et état d'avancement

> [!WARNING]
> En raison des vacances du Nouvel An chinois, la plupart des fournisseurs et des entreprises partenaires ont suspendu leurs activités, ce qui a impacté la progression de nos tests d'échantillons de bras robotiques. Nous ne publierons les fichiers open source **qu'après avoir terminé toutes les validations de performance et de précision**, le calendrier open source sera donc retardé d'environ un mois.

Nous nous engageons à maintenir et à adapter continuellement le projet aux principaux écosystèmes de développement robotique. Voici notre progression actuelle et le calendrier de sortie prévu :

| Écosystème | État | Description / Date prévue | Documentation |
| :--- | :---: | :--- | :--- |
| **Utilisation basique des moteurs** | ✅ Terminé | Contrôle de mouvement de base et encapsulation de l'API | [Robostride](https://wiki.seeedstudio.com/robstride_control/) [Damiao](https://wiki.seeedstudio.com/damiao_series/)|
| **Nouvelle version Structure 3D STEP & BOM** | 🚧 En cours | Fichiers STEP pour toutes les nouvelles pièces, liste BOM et prix de référence pour les pièces usinées | [Retard Mars 2026] |
| **Vidéo de montage** | 🚧 En cours | Étapes de montage ultra-détaillées et vidéo | [Retard Mars 2026] |
| **ROS2 (Humble)** |⏳ Prévu | Pilote de base terminé, optimisation de MoveIt2 en cours |[Prévu Avril 2026]|
| **Adaptation LeRobot** | ⏳ Prévu | Adaptation au framework d'entraînement Hugging Face LeRobot | [Prévu Avril 2026]|
| **Adaptation Pinocchio** | ⏳ Prévu | Adaptation au framework Pinocchio, implémentation de la cinématique directe/inverse et compensation de gravité dynamique | [Prévu Avril 2026]|
| **Simulation Isaac Sim** | ⏳ Prévu | Importation de modèles USD et implémentation de la téléopération en simulation | [Prévu Avril 2026]|
| **Mises à jour graduelles des algorithmes** | ⏳ Prévu | Mise à jour progressive des algorithmes grand public | Continu |
| **Lancement de cours entièrement gratuits** | ⏳ Prévu | Tutoriels étape par étape | Continu |

---

### 🎓 Écosystème robotique Full-Stack
reBot-DevArm n'est pas seulement un bras robotique, c'est une communauté d'apprentissage de la robotique. Nous partageons gratuitement les tutoriels généraux suivants :

#### 🖥️ Informatique de bord et contrôle maître
*   [![Jetson](https://img.shields.io/badge/NVIDIA-reComputer%20Jetson-76B900?style=for-the-badge&logo=nvidia&logoColor=white)](https://wiki.seeedstudio.com/NVIDIA_Jetson/) —— **Inférence IA et cœur de calcul**
*   [![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-4B%20%2F%205-C51A4A?style=for-the-badge&logo=Raspberry%20Pi&logoColor=white)](https://wiki.seeedstudio.com/raspberry-pi-devices/) —— **Environnement de développement Linux général**
*   [![ESP32](https://img.shields.io/badge/MCU-Seeed%20XIAO%20(ESP32)-0091BD?style=for-the-badge&logo=espressif&logoColor=white)](https://wiki.seeedstudio.com/SeeedStudio_XIAO_Series_Introduction/) —— **Nœud de contrôle sans fil basse consommation**

#### 📡 Capteurs et périphériques
*   **🚗 Moteurs et Servomoteurs** : [Damiao / Gogo / Robstride / Mita / Feite / Fashion Star](https://wiki.seeedstudio.com/robotics_page/)
*   **👁️ Perception visuelle** : [Caméras de profondeur / LiDAR / Algorithmes de vision](https://wiki.seeedstudio.com/robotics_page/)
*   **👂 Interaction auditive** : [Matrices de micros ReSpeaker / Reconnaissance vocale](https://wiki.seeedstudio.com/ReSpeaker_Mic_Array_v2.0/)
*   **🧭 Mouvement et attitude** : [IMU (6 axes/9 axes) / Gyroscopes / Magnétomètres](https://wiki.seeedstudio.com/Sensor/IMU/)
*   **🤖 Kits complets** : [Plus de capteurs robotiques et exemples de pilotes](https://wiki.seeedstudio.com/robotics_page/)

> 👉 **[Cliquez pour entrer dans la base de connaissances Wiki](https://wiki.seeedstudio.com/)** (Tous les tutoriels sont en accès libre)

---

## ⚙️ Spécifications matérielles

reBot-DevArm est conçu pour les applications d'IA incarnée sur bureau, équilibrant capacité de charge et flexibilité.

| Paramètre | Valeur / Description |
| :--- | :--- |
| **Charge utile (Payload)** | **1,5+ kg** |
| **Portée max** | **650 mm** |
| **Poids** | Env. 4,0 kg |
| **Répétabilité** | < 0,2 mm |
| **Degrés de liberté (DOF)** | 6 DOF + 1 Pince (Pince servo CAN open source et pince moteur de joint bientôt disponibles) |
| **Plateformes/Écosystèmes supportés** | ROS1, ROS2, LeRobot, Pinocchio, Isaac Sim, SDK Python |
| **Tension d'alimentation** | DC 24V |

---

## 📂 Open Source (Sources matérielles)

Nous pensons que l'open source matériel favorise l'innovation. Vous trouverez tout le nécessaire pour construire ce bras dans les répertoires suivants :

*   [`/hardware/STEP`](./hardware/cad) : Fichiers STEP/STL pour toutes les structures mécaniques, y compris les pièces imprimées, les pièces métalliques et les articles achetés.
*   [`/hardware/bom`](./hardware/bom) : **Liste BOM** (Comprend les modèles de composants achetés, les paramètres des moteurs, les fournisseurs recommandés).
*   [`/tutorial/ROS`](./tutorial/ROS/) : Code source et tutoriels pour **ROS1/2 Noetic/Humble**.
*   [`/tutorial/Lerobot`](./tutorial/lerobot/) : Code source et tutoriels pour **LeRobot**.
*   [`/tutorial/Isaac`](./tutorial/Isaac/) : Code source et tutoriels pour **Isaac Sim**.

---

## 🚀 Guide de démarrage

Nous avons prévu un parcours d'apprentissage complet pour vous, du déballage à la simulation IA :

### 🛠️ Phase 1 : Construction matérielle et bases
| Étape | Description | Lien |
| :---: | :--- | :--- |
| **01** | **Apprentissage de base des moteurs** | [Robostride](https://wiki.seeedstudio.com/robstride_control/) [Damiao](https://wiki.seeedstudio.com/damiao_series/)|
| **02** | **Déballage** | Bientôt disponible |
| **03** | **Guide d'assemblage** | Bientôt disponible |
| **04** | **Calibration du zéro** | Bientôt disponible |
| **05** | **Tests cinématiques** | Bientôt disponible |

### 💻 Phase 2 : Algorithmes avancés et simulation
| Étape | Description | Lien |
| :---: | :--- | :--- |
| **06** | **Écosystème ROS** (ROS2) | 🐢 Bientôt disponible |
| **07** | **Entraînement IA** (Hugging Face) | 🤗 Bientôt disponible |
| **08** | **Simulation** (NVIDIA) | 🌌 Bientôt disponible |

---

## 🙌 Références et remerciements
Le chemin de l'open source n'est jamais solitaire. La naissance du projet reBot-DevArm ne serait pas possible sans le soutien total de Seeed Studio, de la communauté open source mondiale et d'excellents partenaires matériels. Nous rendons hommage aux projets et équipes suivants :

### 🌍 Support écosystème et logiciel
*   **[Seeed Studio](https://www.seeedstudio.com/)** - Fourniture de la chaîne d'approvisionnement matérielle complète et support technique.
*   **[Hugging Face LeRobot](https://github.com/huggingface/lerobot)** - Un excellent framework d'apprentissage robotique de bout en bout.
*   **[NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim)** - Une plateforme puissante de simulation robotique et de données synthétiques.

### ⚙️ Partenaires matériels clés
Merci aux fabricants suivants pour la fourniture de solutions de moteurs et d'actionneurs haute performance :
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

### 🎃 Contributeurs du prototype
- **Équipe Robotique IA SeeedStudio** : Yaohui Zhu (yaohui.zhu@seeed.cc)
- **SeeedStudio STU** : Wentao Dong
- **SeeedStudio STU** : Weiwei Xu
- **Département des achats SeeedStudio** : Fengqun Peng

### 👥 Contributeurs

## Nos principaux contributeurs

<p align="center"><a href="https://github.com/Seeed-Projects/reBot-DevArm/graphs/contributors">
   <img src="https://contributors-img.web.app/image?repo=Seeed-Projects/reBot-DevArm" />
</a></p>

*Bientôt disponible... Bienvenue pour soumettre des PR et devenir contributeur !*

## Historique des étoiles (Star History)

[![Star History Chart](https://api.star-history.com/svg?repos=Seeed-Projects/reBot-DevArm&type=date&legend=top-left)](https://www.star-history.com/#Seeed-Projects/reBot-DevArm&type=date&legend=top-left)

# Licence du projet reBot-DevArm
Copyright (c) [2025] [Seeed Studio AI Robotics Team]

Cette œuvre est sous licence **Creative Commons Attribution - Pas d'Utilisation Commerciale - Partage dans les Mêmes Conditions 4.0 International**. Pour consulter une copie de cette licence, visitez : http://creativecommons.org/licenses/by-nc-sa/4.0/

--------------------------------------------------------------------------------

## Droits et restrictions
1. Vous êtes libre de :
    - Partager : Copier et redistribuer le matériel sur n'importe quel support ou format.
    - Adapter : Remixez, transformez et développez le matériel.

2. Selon les conditions suivantes :
    - Attribution : Vous devez donner le crédit approprié, fournir un lien vers la licence et indiquer si des modifications ont été apportées.
    - Pas d'Utilisation Commerciale : **Vous ne pouvez pas utiliser le matériel à des fins commerciales**.
      (Y compris, mais sans s'y limiter, la vente de kits associés, la vente de pièces imprimées ou l'intégration de ce logiciel dans des produits payants sans autorisation explicite).
    - Partage dans les Mêmes Conditions : Si vous remixez, transformez ou développez le matériel, vous devez distribuer vos contributions sous la même licence que l'original.

3. Autorisation commerciale :
    Si vous souhaitez utiliser ce projet à des fins commerciales, veuillez contacter l'auteur pour obtenir une autorisation commerciale.
    Contact : yaohui.zhu@seeed.cc