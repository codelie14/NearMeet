# **Cahier des Charges – NearMeet**
**Version :** 1.0
**Date :** 15 janvier 2026
**Rédigé par :** InformatiX AI
**Projet :** Application de communication locale multi-fonctions

---

## **1. Introduction**
### **1.1 Contexte**
NearMeet est une application de communication locale conçue pour permettre aux utilisateurs de discuter, partager des fichiers, passer des appels vidéo/audio, et collaborer en temps réel sur un même réseau local (LAN). Elle vise à offrir une alternative sécurisée et légère aux outils de communication en ligne, idéale pour les entreprises, les écoles, ou les communautés locales.

### **1.2 Objectifs**
- Faciliter la communication instantanée en réseau local.
- Intégrer des fonctionnalités avancées (appels vidéo, partage d’écran, messages audio).
- Garantir une interface intuitive et une expérience utilisateur fluide.
- Assurer la confidentialité et la sécurité des échanges.

### **1.3 Public cible**
- **Entreprises** : Pour les réunions internes et le partage de documents.
- **Écoles/Universités** : Pour les cours en ligne ou les projets collaboratifs.
- **Communautés locales** : Pour les échanges entre voisins ou associations.
- **Développeurs** : Pour les tests en environnement local ou les démonstrations techniques.

---

## **2. Spécifications Fonctionnelles**
### **2.1 Fonctionnalités principales**
| **Fonctionnalité**          | **Description**                                                                                     | **Priorité** |
|------------------------------|-----------------------------------------------------------------------------------------------------|--------------|
| **Connexion locale**         | Communication via sockets TCP/IP sur un réseau local (LAN).                                        | Haute        |
| **Pseudonymes**              | Chaque utilisateur choisit un pseudo pour s’identifier dans les discussions.                       | Haute        |
| **Historique des messages**  | Sauvegarde des messages (fichier JSON ou base de données SQLite).                                   | Haute        |
| **Notifications**            | Alertes sonores et visuelles pour les nouveaux messages/appels.                                    | Moyenne      |
| **Partage de fichiers**      | Envoi de fichiers (PDF, images, documents) via le réseau local.                                   | Haute        |
| **Appels vidéo**             | Communication vidéo en temps réel (1:1 ou en groupe).                                              | Haute        |
| **Partage d’écran**          | Diffusion de l’écran d’un utilisateur aux autres participants.                                      | Moyenne      |
| **Messages audio**           | Enregistrement et envoi de messages vocaux.                                                        | Moyenne      |
| **Appels de groupe (Meet)**  | Créer des salles de discussion vidéo/audio pour plusieurs utilisateurs.                            | Basse        |
| **Salons de discussion**     | Créer des canaux thématiques (ex : "Travail", "Loisirs").                                           | Basse        |
| **Chiffrement**              | Chiffrement des messages pour garantir la confidentialité (AES ou RSA).                            | Moyenne      |
| **Statut utilisateur**       | Afficher le statut des utilisateurs (En ligne, Absent, Occupé).                                     | Basse        |
| **Recherche dans l’historique** | Filtrer les messages par mot-clé, utilisateur ou date.                                           | Basse        |

---

### **2.2 Exigences techniques**
| **Composant**               | **Technologie/Outils**                                                                              |
|-----------------------------|------------------------------------------------------------------------------------------------------|
| **Interface graphique**      | PyQt6 (Python)                                                                                       |
| **Communication réseau**     | Sockets TCP/IP, `PyQt6.QtNetwork`                                                                   |
| **Audio**                   | `pyaudio`, `sounddevice`, `pygame`                                                                 |
| **Vidéo**                   | `OpenCV`, `PyQt6.QtMultimedia`                                                                      |
| **Partage d’écran**         | `mss` (capture d’écran), `Pillow` (traitement d’images)                                            |
| **Base de données**         | SQLite (pour l’historique des messages)                                                            |
| **Notifications**           | `plyer` (notifications système)                                                                     |
| **Chiffrement**             | `cryptography` (AES/RSA)                                                                            |
| **Gestion des threads**      | `QThread` (PyQt6) ou `threading` (Python)                                                           |

---

## **3. Spécifications Techniques**
### **3.1 Architecture logicielle**
- **Client-Serveur** :
  - Un utilisateur hôte lance le serveur NearMeet.
  - Les autres utilisateurs se connectent en tant que clients.
- **Protocole de communication** :
  - Utilisation de sockets TCP pour les messages texte.
  - Streaming UDP pour la vidéo/audio (pour réduire la latence).
- **Stockage** :
  - Historique des messages : Base de données SQLite.
  - Fichiers partagés : Stockés temporairement dans un dossier local (`/NearMeet_SharedFiles`).

### **3.2 Environnement de développement**
- **Langage** : Python 3.11+
- **Bibliothèques** :
  - `PyQt6` (UI)
  - `opencv-python` (vidéo)
  - `pyaudio` (audio)
  - `mss` (partage d’écran)
  - `sqlite3` (base de données)
  - `cryptography` (chiffrement)
- **OS supportés** : Windows, macOS, Linux.

---

## **4. Maquettes et Interface Utilisateur**
### **4.1 Fenêtre principale**
- **Zone de discussion** : Affichage des messages (texte, audio, fichiers).
- **Barre de saisie** : Champ pour écrire un message + bouton d’envoi.
- **Liste des utilisateurs** : Affichage des pseudos et statuts.
- **Boutons d’action** :
  - Appel vidéo/audio
  - Partage d’écran
  - Envoi de fichier
  - Accès aux salons

### **4.2 Fenêtre d’appel vidéo**
- **Affichage vidéo** : Webcam locale et distante.
- **Contrôles** : Microphone, caméra, partage d’écran, quitter l’appel.

### **4.3 Exemple de maquettes (à réaliser avec Figma ou draw.io)**
- **Maquette 1** : Fenêtre de chat avec liste des utilisateurs.
- **Maquette 2** : Fenêtre d’appel vidéo avec contrôles.

*(Je peux te générer des maquettes visuelles si tu veux !)*

---

## **5. Planification et Livrables**
### **5.1 Phases du projet**
| **Phase**               | **Durée estimée** | **Livrables**                                                                 |
|-------------------------|-------------------|--------------------------------------------------------------------------------|
| **Conception**          | 1 semaine         | Cahier des charges, maquettes, architecture technique.                          |
| **Développement UI**    | 2 semaines        | Interface graphique fonctionnelle (PyQt6).                                      |
| **Chat texte**          | 1 semaine         | Échange de messages, pseudos, historique.                                      |
| **Partage de fichiers** | 3 jours           | Fonctionnalité d’envoi/réception de fichiers.                                   |
| **Appels audio**        | 1 semaine         | Intégration de `pyaudio` pour les appels vocaux.                                |
| **Appels vidéo**        | 2 semaines        | Capture et streaming vidéo avec `OpenCV`.                                       |
| **Partage d’écran**     | 1 semaine         | Capture et diffusion de l’écran avec `mss`.                                    |
| **Tests et corrections**| 1 semaine         | Correction des bugs, optimisation des performances.                            |
| **Documentation**       | 3 jours           | Guide utilisateur, documentation technique.                                    |

### **5.2 Livrables finaux**
- **Application exécutable** : Pour Windows, macOS, Linux.
- **Code source** : Sur GitHub (ou autre dépôt).
- **Documentation** :
  - Guide d’installation.
  - Manuel utilisateur.
  - Documentation technique (API, architecture).

---

## **6. Risques et Contraintes**
### **6.1 Risques identifiés**
| **Risque**                          | **Impact**               | **Mitigation**                                                                 |
|--------------------------------------|--------------------------|--------------------------------------------------------------------------------|
| Latence dans les appels vidéo        | Expérience utilisateur dégradée | Optimiser le streaming (UDP, compression).                                   |
| Problèmes de compatibilité multi-OS  | Limitation des utilisateurs | Tester sur plusieurs OS dès le début.                                         |
| Sécurité des données                 | Fuites ou piratage       | Chiffrement des messages, authentification des utilisateurs.                 |
| Complexité du partage d’écran        | Bugs ou ralentissements  | Utiliser des bibliothèques optimisées (`mss`).                                |

### **6.2 Contraintes**
- **Réseau local obligatoire** : NearMeet ne fonctionne que sur un même réseau LAN.
- **Performances** : Dépendantes de la puissance des machines et de la bande passante du réseau.
- **Droits d’accès** : Nécessite l’autorisation d’accès au microphone, à la caméra et à l’écran.

---

## **7. Budget et Ressources**
### **7.1 Ressources humaines**
- **1 développeur principal** (toi !) pour le code et les tests.
- **1 designer UI/UX** (optionnel) pour les maquettes.

### **7.2 Coûts**
- **Gratuit** : Toutes les bibliothèques utilisées sont open-source.
- **Hébergement** : Aucun coût (application locale).
- **Matériel** : Ordinateurs pour les tests (déjà disponibles).

---

## **8. Conclusion**
NearMeet est un projet ambitieux qui combine **chat local, appels vidéo, partage d’écran et collaboration en temps réel**. Ce cahier des charges définit les objectifs, les fonctionnalités, l’architecture technique et le plan de développement.
