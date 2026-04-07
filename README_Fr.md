# 🦾 reBot-DevArm : bras robotique open source pour tous les développeurs

<p align="center">
  <img src="./media/v1.0.png" alt="Bannière reBot-DevArm">
</p>

<p align="center">
    <!-- Replaced with CC BY-NC-SA 4.0 badge, explicitly indicating non-commercial use -->
    <a href="./LICENSE">
        <img src="https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg" alt="Licence : CC BY-NC-SA 4.0">
    </a>
    <img src="https://img.shields.io/badge/Commercial-Contact%20Us-red.svg" alt="yaohui.zhu@seeed.cc">
    <img src="https://img.shields.io/badge/ROS-Noetic%20%7C%20Humble-orange.svg" alt="Support ROS">
    <img src="https://img.shields.io/badge/Framework-LeRobot-yellow.svg" alt="LeRobot">
    <img src="https://img.shields.io/badge/Framework-Isaac Sim-yellow.svg" alt="LeRobot">
</p>

<p align="center">
  <strong>100 % entièrement open source · IA incarnée · Intégration matériel-logiciel · Gratuit pour un usage personnel/éducatif · L’utilisation commerciale nécessite une autorisation</strong>
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
    <img src="https://img.shields.io/badge/Documentation-📕-blue" alt="wiki robotique"></a>
</p>

## 📖 Introduction

**reBot-DevArm (reBot Arm B601 DM et reBot Arm B601 RS)** est un projet de bras robotique dédié à réduire les barrières d’apprentissage de l’IA incarnée. Nous mettons l’accent sur le **« véritable open source »** — pas seulement le code, nous ouvrons absolument tout sans réserve :
- 🦾 **Deux versions du bras robotique**：Nous fournirons tous les fichiers open source pour deux versions du bras robotique ayant la même apparence : **Robostride** et **Damiao**.
- 🛠️ **Plans matériels** : fichiers sources pour les pièces en tôle et les pièces imprimées en 3D.
- 🔩 **Liste BOM** : détails complets jusqu’aux spécifications et aux liens d’achat de chaque vis.
- 💻 **Logiciels & algorithmes** : SDK Python, ROS1/2, Isaac Sim, LeRobot, etc.

Vous pouvez acheter les pièces restantes sur le magasin SeeedStudio en fonction des composants que vous possédez déjà (mise en vente prévue le 15 avril 2026).

[Laissez vos informations ici, nous vous enverrons à l’avance le lien de pré-commande en quantité limitée.](https://forms.gle/1MwdVKUqkuGu3C7L7)

## 🗺️ Feuille de route & état

Nous nous engageons à maintenir et à adapter en continu les principaux écosystèmes de développement robotique. Voici notre état actuel d’adaptation et le calendrier de publication prévu :

### reBot Arm B601 DM
| Écosystème pris en charge | État | Description / date de publication estimée | Documentation associée |
| :--- | :---: | :--- | :--- |
| **Utilisation de base des moteurs** | ✅ Terminé | Contrôle de mouvement de base et encapsulation d’API | [Damiao Technology](https://wiki.seeedstudio.com/cn/damiao_series/) |
| **Open source des nouvelles pièces structurelles STEP 3D et de la BOM** | ✅ Terminé | Fichiers STEP de toutes les pièces de la nouvelle version, BOM des pièces et prix de référence de toutes les pièces usinées | [reBot Arm B601-DM BOM](./hardware/reBot_B601_DM/readme_fr.md) |
| **Référence pour les tests de performance sur machine réelle** | ✅ Terminé  | Référence de performance du bras robotisé en fonctionnement normal et extrême |[Performance Testing](./hardware/reBot_B601_DM/performance_testing/Performance_Testing_Fr.md) |
| **Vidéo d’assemblage** | 🚧 En cours | Étapes d’assemblage ultra détaillées et vidéo | [Prévu : 2026.04.10] |
| **ROS2 (Humble)** | 🚧 En cours  | Les pilotes principaux sont terminés, et MoveIt2 est actuellement en cours d’optimisation | [Prévu : 2026.04.10] |
| **SDK Python** | 🚧 En cours  |  | [Prévu : 2026.04.10] |
| **Intégration Pinocchio** | 🚧 En cours  | Adaptation au framework Pinocchio, permettant la cinématique directe/inverse et la compensation gravitationnelle pour le bras robotique | [Dépôt GitHub](https://github.com/vectorBH6/reBotArm_control_py/tree/main) Mise à jour continue |
| **Simulation Isaac Sim** | 🚧 En cours  | Importation de modèles USD et activation de la téléopération simulée | [Prévu : 2026.04.20] |
| **Intégration LeRobot** | 🚧 En cours  | Adaptation au framework d’entraînement Hugging Face LeRobot | [Prévu : 2026.04.30] |
| **Mises à jour progressives des derniers algorithmes** | ⏳ Planifié | Les algorithmes grand public seront mis à jour progressivement | En continu |
| **Lancement d’une série de cours entièrement gratuits** | ⏳ Planifié | Les algorithmes grand public seront mis à jour progressivement | En continu |



### reBot Arm B601 RS

| Écosystème pris en charge | État | Description / date de publication estimée | Documentation associée |
| :--- | :---: | :--- | :--- |
| **Utilisation de base des moteurs** | ✅ Terminé | Contrôle de mouvement de base et encapsulation d’API | [Robstride](https://wiki.seeedstudio.com/cn/robstride_control/) |
| **Open source des nouvelles pièces structurelles STEP 3D et de la BOM** | 🚧 En cours | Fichiers STEP de toutes les pièces de la nouvelle version, BOM des pièces et prix de référence de toutes les pièces usinées | Prévu [2026.04.31] |
| **Vidéo d’assemblage** | 🚧 En cours | Étapes d’assemblage ultra détaillées et vidéo | [Prévu 2026.05.10] |
| **ROS2 (Humble)** | ⏳ Planifié | Les pilotes principaux sont terminés, et MoveIt2 est actuellement en cours d’optimisation | [Prévu 2026.05] |
| **Intégration LeRobot** | ⏳ Planifié | Adaptation au framework d’entraînement Hugging Face LeRobot | [Prévu 2026.05] |
| **Intégration Pinocchio** | ⏳ Planifié | Adaptation au framework Pinocchio, permettant la cinématique directe/inverse et la compensation gravitationnelle pour le bras robotique | [Prévu 2026.05] |
| **Simulation Isaac Sim** | ⏳ Planifié | Importation de modèles USD et activation de la téléopération simulée | [Prévu 2026.05] |
| **Mises à jour progressives des derniers algorithmes** | ⏳ Planifié | Les algorithmes grand public seront mis à jour progressivement | En continu |
| **Lancement d’une série de cours entièrement gratuits** | ⏳ Planifié | Les algorithmes grand public seront mis à jour progressivement | En continu |


---


### 🎓 Écosystème robotique full-stack
reBot-DevArm n’est pas seulement un bras robotique, mais une communauté d’apprentissage de la robotique. Nous partageons gratuitement les tutoriels généraux suivants :

#### 🖥️ Edge Computing & contrôle principal
*   [![Jetson](https://img.shields.io/badge/NVIDIA-reComputer%20Jetson-76B900?style=for-the-badge&logo=nvidia&logoColor=white)](https://wiki.seeedstudio.com/NVIDIA_Jetson/) —— **Inférence IA & cœur de calcul**
*   [![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-4B%20%2F%205-C51A4A?style=for-the-badge&logo=Raspberry%20Pi&logoColor=white)](https://wiki.seeedstudio.com/raspberry-pi-devices/) —— **Environnement général de développement Linux**
*   [![ESP32](https://img.shields.io/badge/MCU-Seeed%20XIAO%20(ESP32)-0091BD?style=for-the-badge&logo=espressif&logoColor=white)](https://wiki.seeedstudio.com/SeeedStudio_XIAO_Series_Introduction/) —— **Nœud de contrôle sans fil basse consommation**

#### 📡 Capteurs & périphériques
*   **🚗 Moteurs & servomoteurs** : [Damiao / Gogo / Robstride / Mita / Feite / Fashion Star](https://wiki.seeedstudio.com/robotics_page/)
*   **👁️ Perception visuelle** : [Caméras de profondeur / LiDAR / algorithmes de vision](https://wiki.seeedstudio.com/robotics_page/)
*   **👂 Interaction auditive** : [Réseaux de micros ReSpeaker / reconnaissance vocale](https://wiki.seeedstudio.com/ReSpeaker_Mic_Array_v2.0/)
*   **🧭 Mouvement & attitude** : [IMU (6 axes/9 axes) / gyroscopes / magnétomètres](https://wiki.seeedstudio.com/Sensor/IMU/)
*   **🤖 Kits complets** : [Plus de capteurs robotiques & d’exemples de pilotes](https://wiki.seeedstudio.com/robotics_page/)


> 👉 **[Cliquez pour accéder à la base de connaissances du Wiki](https://wiki.seeedstudio.com/)** (Tous les tutoriels sont consultables gratuitement)

---

## ⚙️ Spécifications matérielles

reBot-DevArm est conçu pour des applications d’IA incarnée sur bureau, en équilibrant la capacité de charge utile et la flexibilité.

| Paramètre | reBot Arm B601-DM |
| :--- | :--- |
| **Charge continue recommandée** | Moins de 1,5 kg dans 70 % de l’espace de travail de portée du bras |
| **Charge utile recommandée** | **1,5 kg** |
| **Portée maximale** | **650 mm** |
| **Poids** | Environ 4,5 kg |
| **Répétabilité** | < 0,2 mm |
| **Degrés de liberté (DOF)** | 6 DOF + 1 pince (pince servo CAN open source et pince à moteur d’articulation bientôt disponibles) |
| **Plateformes/écosystèmes pris en charge** | ROS1, ROS2, LeRobot, Pinocchio, Isaac Sim, SDK Python |
| **Tension d’alimentation** | DC 24V |

## 🙌 Références & remerciements
Le chemin de l’open source n’est jamais solitaire. La naissance du projet reBot-DevArm n’aurait pas été possible sans le soutien total de Seeed Studio, de la communauté open source mondiale et d’excellents partenaires matériels. Nous exprimons notre plus profond respect aux projets et équipes suivants :

### 🌍 Écosystème & support logiciel
*   **[Seeed Studio](https://www.seeedstudio.com/)** - Fournit un support complet en chaîne d’approvisionnement matériel et en assistance technique.
*   **[Hugging Face LeRobot](https://github.com/huggingface/lerobot)** - Un excellent framework d’apprentissage robotique de bout en bout.
*   **[NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim)** - Une puissante plateforme de simulation robotique et de données synthétiques.

### ⚙️ Partenaires matériels principaux
Merci aux fabricants suivants pour avoir fourni des solutions de moteurs et d’actionneurs hautes performances :
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
- **Équipe SeeedStudio AI Robotics** : Yaohui Zhu (yaohui.zhu@seeed.cc)
- **SeeedStudio STU** : Wentao Dong
- **SeeedStudio STU** : Weiwei Xu
- **Département des achats de SeeedStudio** : Fengqun Peng


### 👥 Contributeurs

## Nos principaux contributeurs 
<p align="center"><a href="https://github.com/Seeed-Projects/reBot-DevArm/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=Seeed-Projects/reBot-DevArm" />
</a></p>



*Bientôt disponible... N’hésitez pas à soumettre des PR pour devenir contributeur !*

## Historique des étoiles

[![Star History Chart](https://api.star-history.com/svg?repos=Seeed-Projects/reBot-DevArm&type=date&legend=top-left)](https://www.star-history.com/#Seeed-Projects/reBot-DevArm&type=date&legend=top-left)

# Licence du projet reBot-DevArm
Copyright (c) [2025] [Seeed Studio]

Ce travail est concédé sous la **Licence internationale Creative Commons Attribution-NonCommercial-ShareAlike 4.0**.
Pour consulter une copie de cette licence, visitez : http://creativecommons.org/licenses/by-nc-sa/4.0/

--------------------------------------------------------------------------------

## Déclaration des droits et restrictions

L’objectif principal de ce projet open source est de promouvoir le partage des connaissances et de permettre aux développeurs et aux passionnés d’accéder aux technologies de pointe des bras robotiques et de les apprendre à un coût minimal. Nous fournissons une documentation et des tutoriels vidéo entièrement gratuits et accessibles au public afin d’aider les utilisateurs à démarrer rapidement, à mener des recherches approfondies et à promouvoir conjointement la popularisation et l’application pratique de la robotique.

### I. Politique d’utilisation non commerciale

Tout le contenu open source de ce projet est entièrement disponible pour l’apprentissage personnel, la recherche et l’usage non commercial. Les utilisateurs individuels sont autorisés à :

* Consulter et étudier la documentation, le code et les tutoriels open source du projet ;
* Modifier et déboguer le contenu open source à des fins d’apprentissage personnel et de recherche ;
* Assembler des bras robotiques pour un usage personnel ou mener un développement secondaire basé sur le contenu open source à des fins non commerciales.

### II. Politique d’utilisation commerciale

Nous encourageons et soutenons activement les développeurs, les passionnés de robotique et les plateformes tierces à mener un développement secondaire basé sur le bras robotique reBot et à promouvoir des applications concrètes dans le monde réel. Ce qui suit décrit les activités commerciales autorisées et interdites :

#### (1) Activités commerciales autorisées

Nous respectons les efforts et les revenus légitimes de chaque développeur. Si vous achetez le bras robotique reBot série B601 auprès de Seeed et apportez votre propre contribution, vous pouvez commercialiser les résultats de vos efforts, y compris mais sans s’y limiter :

* Développer des systèmes logiciels orientés application et les promouvoir ou les vendre commercialement ;
* Créer des cours éducatifs structurés (en ligne/hors ligne) et proposer des formations payantes ou des services de transmission de connaissances ;
* Mener dans le monde entier des activités hors ligne d’éducation, de formation et de vulgarisation technologique ;
* D’autres activités commerciales qui contribuent à la communauté open source, à la diffusion des connaissances et à l’application concrète des technologies robotiques.

Pour les activités commerciales conformes ci-dessus, vous êtes les bienvenus pour nous contacter. Nous fournirons une autorisation commerciale, un support de mise en œuvre et une assistance promotionnelle. Nous pourrons également annoncer publiquement votre autorisation afin d’aider votre projet à réussir.

#### (2) Activités commerciales interdites

Il est interdit d’apporter de légères modifications au produit de ce projet, de remplacer la propriété intellectuelle, les logos ou les identifiants associés, puis de le vendre sous une marque auto-détenue. De telles actions ne constituent pas une innovation technique substantielle et ne profitent ni au développement des développeurs, ni à la communauté open source, ni au projet lui-même. Ces comportements sont considérés comme des violations, et nous nous réservons le droit d’agir.

### III. Collaboration & contact

Nous espérons collaborer avec tous les développeurs et partenaires dans un cadre conforme afin de promouvoir la maturité et le déploiement du projet de bras robotique reBot. Pour les individus et les organisations intéressés par la concrétisation d’applications robotiques dans le monde réel, nous proposons :

* Un support pour les licences commerciales et la conformité en matière de propriété intellectuelle ;
* Une assistance pour la promotion des solutions du projet ;
* Des services de développement sur mesure pour les bras robotiques et les solutions associées ;
* Des opportunités conjointes de R&D et de co-développement.

Si vous êtes intéressé par une collaboration commerciale ou avez des besoins connexes, n’hésitez pas à nous contacter. Travaillons ensemble pour faire progresser l’adoption et l’industrialisation des technologies robotiques.


## ☎ Contactez-nous
- **Progrès open source & support technique**-Yaohui : yaohui.zhu@seeed.cc
- **Collaboration future & personnalisation**-Elaine : elaine.wu@seeed.cc

