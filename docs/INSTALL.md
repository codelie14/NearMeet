# Guide d'Installation - NearMeet

## Installation Complète

### Prérequis

Avant d'installer NearMeet, assurez-vous que vous disposez de:

- **Python 3.11 ou supérieur** - [Télécharger Python](https://www.python.org/downloads/)
- **pip** - Inclus avec Python 3.4+
- **Git** (optionnel) - Pour cloner le dépôt
- Accès à un terminal/invite de commande
- Au moins 500 MB d'espace disque libre

### Vérifier les prérequis

Pour vérifier que Python est correctement installé:

```bash
python --version
pip --version
```

### Windows

#### 1. Cloner le dépôt

```bash
git clone https://github.com/codelie14/NearMeet.git
cd NearMeet
```

Ou télécharger le fichier ZIP et l'extraire.

#### 2. Créer un environnement virtuel

```bash
python -m venv venv
venv\Scripts\activate
```

#### 3. Installer les dépendances

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### 4. Configurer l'application

Copier le fichier d'exemple:
```bash
copy .env.example .env
```

Éditer `.env` avec vos paramètres (optionnel).

#### 5. Lancer l'application

En mode client:
```bash
python -m src
```

En mode serveur:
```bash
python -m src --mode server --port 5000
```

### macOS

#### 1. Cloner le dépôt

```bash
git clone https://github.com/codelie14/NearMeet.git
cd NearMeet
```

#### 2. Créer un environnement virtuel

```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Installer les dépendances

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Sur macOS, vous pourriez avoir besoin d'installer des dépendances système:

```bash
brew install portaudio
```

#### 4. Configurer l'application

```bash
cp .env.example .env
```

#### 5. Lancer l'application

```bash
python -m src
```

### Linux (Ubuntu/Debian)

#### 1. Cloner le dépôt

```bash
git clone https://github.com/codelie14/NearMeet.git
cd NearMeet
```

#### 2. Installer les dépendances système

```bash
sudo apt-get update
sudo apt-get install python3-pip python3-venv
sudo apt-get install portaudio19-dev
sudo apt-get install libopencv-dev python3-opencv
```

#### 3. Créer un environnement virtuel

```bash
python3 -m venv venv
source venv/bin/activate
```

#### 4. Installer les dépendances Python

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### 5. Configurer l'application

```bash
cp .env.example .env
```

#### 6. Lancer l'application

```bash
python3 -m src
```

## Résolution des problèmes courants

### Erreur: "ModuleNotFoundError: No module named 'PyQt6'"

**Solution:**
```bash
pip install --upgrade PyQt6
```

### Erreur: "No module named 'cv2' (OpenCV)"

**Solution:**

Windows/macOS:
```bash
pip install --upgrade opencv-python
```

Linux:
```bash
sudo apt-get install python3-opencv
pip install opencv-contrib-python
```

### Erreur: "No module named 'pyaudio'"

**Solution:**

Windows:
```bash
pip install pipwin
pipwin install pyaudio
```

macOS:
```bash
brew install portaudio
pip install pyaudio
```

Linux:
```bash
sudo apt-get install portaudio19-dev
pip install pyaudio
```

### L'application ne démarre pas

Vérifiez que vous êtes dans le bon répertoire et que l'environnement virtuel est activé:

Windows:
```bash
where python
```

macOS/Linux:
```bash
which python
```

### Problèmes de permission sur Linux

Si vous obtenez une erreur de permission:

```bash
chmod +x src/__main__.py
```

## Configuration initiale

### 1. Créer un fichier `.env` personnalisé

```bash
cp .env.example .env
```

Éditer `.env` et modifier les paramètres selon vos besoins:

```env
SERVER_HOST=192.168.1.100
SERVER_PORT=5000
APP_LOG_LEVEL=INFO
AUDIO_ENABLED=True
VIDEO_ENABLED=True
```

### 2. Lancer le serveur

Sur une machine (host):
```bash
python -m src --mode server --port 5000
```

### 3. Se connecter en tant que client

Sur d'autres machines du réseau:
```bash
python -m src --mode client --host 192.168.1.100 --port 5000 --username "JohnDoe"
```

## Utilisation dans un réseau local

NearMeet fonctionne uniquement sur un réseau local (LAN). Pour trouver votre adresse IP:

### Windows
```bash
ipconfig
```

Cherchez "IPv4 Address" (par exemple: 192.168.1.100)

### macOS/Linux
```bash
ifconfig
```

Cherchez "inet" (par exemple: 192.168.1.100)

## Désinstallation

Pour supprimer NearMeet:

### Windows
```bash
rmdir /s NearMeet
```

### macOS/Linux
```bash
rm -rf NearMeet
```

## Support et aide

Si vous rencontrez des problèmes:

1. Consultez la [documentation](../docs/README.md)
2. Créez une [issue sur GitHub](https://github.com/yourusername/NearMeet/issues)
3. Vérifiez les [FAQ](FAQ.md)

---

Pour toute autre question, veuillez consulter [README.md](../README.md)
