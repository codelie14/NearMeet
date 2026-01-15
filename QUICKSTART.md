# Quickstart - NearMeet

Guide de démarrage rapide pour NearMeet.

## 1. Installation (5 minutes)

### Windows

```bash
# Cloner le projet
git clone https://github.com/codelie14/NearMeet.git
cd NearMeet

# Créer environnement virtuel
python -m venv venv
venv\Scripts\activate

# Installer dépendances
pip install -r requirements.txt

# Configurer
copy .env.example .env
```

### macOS/Linux

```bash
# Cloner le projet
git clone https://github.com/codelie14/NearMeet.git
cd NearMeet

# Créer environnement virtuel
python3 -m venv venv
source venv/bin/activate

# Installer dépendances
pip install -r requirements.txt

# Configurer
cp .env.example .env
```

## 2. Lancer le serveur (sur une machine)

```bash
python -m src --mode server --port 5000
```

Vous verrez:
```
INFO - Server started on 0.0.0.0:5000
```

## 3. Lancer un client (sur d'autres machines du réseau)

Trouvez d'abord l'adresse IP du serveur:

**Windows:**
```bash
ipconfig
# Cherchez "IPv4 Address" : 192.168.1.100
```

**Mac/Linux:**
```bash
ifconfig
# Cherchez "inet" : 192.168.1.100
```

Puis lancez le client:

```bash
python -m src --mode client --host 192.168.1.100 --port 5000 --username "YourName"
```

## 4. Utiliser l'application

1. **Entrer un pseudonyme** dans le champ "Username"
2. **Taper des messages** dans le champ de saisie
3. **Appuyer sur Entrée** ou cliquer "Send"
4. **Voir les messages** dans la zone de chat

### Boutons disponibles:

- **Send** - Envoyer un message
- **Call** - Appel vidéo (à venir)
- **Share Screen** - Partage d'écran (à venir)
- **Send File** - Transfert de fichiers (à venir)

## Configurations communes

### Changer le port

```bash
# Serveur
python -m src --mode server --port 5001

# Client
python -m src --mode client --host 192.168.1.100 --port 5001
```

### Mode debug

```bash
python -m src --debug
```

Les logs s'affichent dans la console et sont sauvegardés dans `logs/nearmeet.log`.

## Fichiers importants

- `src/` - Code source
- `docs/` - Documentation
- `tests/` - Tests unitaires
- `data/` - Base de données (créée à la première exécution)
- `logs/` - Fichiers de log
- `.env` - Configuration locale

## Prochaines étapes

1. Explorez les [docs](docs/) pour des détails
2. Consultez la [documentation API](docs/API.md)
3. Lisez l'[architecture](docs/ARCHITECTURE.md)
4. Regardez les [FAQ](FAQ.md)

## Problèmes?

- **Port déjà utilisé**: Utilisez un port différent (ex: 5001)
- **Connexion impossible**: Vérifiez l'adresse IP avec `ipconfig` ou `ifconfig`
- **Dépendances manquantes**: Réinstallez `pip install -r requirements.txt`

Pour plus d'aide, consultez [INSTALL.md](docs/INSTALL.md)

---

**Enjoy using NearMeet! 🚀**
