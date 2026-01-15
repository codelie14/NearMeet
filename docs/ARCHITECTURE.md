# Architecture - NearMeet

## Vue d'ensemble

NearMeet utilise une architecture **client-serveur** avec une communication **par sockets TCP/IP** pour les messages texte et les métadonnées, et **UDP** pour les flux vidéo/audio afin de minimiser la latence.

## Architecture Générale

```
┌─────────────────────────────────────────────────────────────┐
│                   NearMeet Application                       │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────┐                    ┌──────────────┐       │
│  │     UI       │◄──────────────────►│  Core App    │       │
│  │   (PyQt6)    │                    │   Manager    │       │
│  └──────────────┘                    └──────────────┘       │
│         ▲                                   ▲                 │
│         │                                   │                 │
│  ┌──────▼──────────────────────────────────▼─────┐           │
│  │              Signal Manager                    │           │
│  │  (Événements inter-modules)                    │           │
│  └──────┬──────────────────────────────────┬─────┘           │
│         │                                   │                 │
│  ┌──────▼──────┐  ┌──────────┐  ┌─────────▼──────┐          │
│  │   Network   │  │   Chat   │  │   Database     │          │
│  │   Layer     │  │  Manager │  │                │          │
│  └──────┬──────┘  └──────────┘  └────────────────┘          │
│         │                                                      │
│  ┌──────▼──────────────────┐                                 │
│  │  Protocol Handler       │                                 │
│  │  - TCP Messages         │                                 │
│  │  - UDP Streaming        │                                 │
│  │  - Encryption           │                                 │
│  └──────┬──────────────────┘                                 │
│         │                                                      │
│         ▼                                                      │
│  ┌──────────────────────────────────────┐                    │
│  │    Network (Sockets)                 │                    │
│  │    [TCP : Messages]                  │                    │
│  │    [UDP : Streaming]                 │                    │
│  └──────────────────────────────────────┘                    │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

## Modules Principaux

### 1. **Core (`src/core/`)**
- **app.py** : Application principale
- **enums.py** : Énumérations (statuts, types de messages, etc.)

Responsabilités:
- Initialisation de l'application
- Gestion du cycle de vie
- Coordination entre modules

### 2. **Network (`src/network/`)**
- **server.py** : Implémentation du serveur TCP
- **client.py** : Implémentation du client TCP
- **protocol.py** : Protocole de communication personnalisé
- **handlers.py** : Traitement des messages
- **security.py** : Chiffrement et sécurité

Responsabilités:
- Gestion des connexions TCP/IP
- Encodage/décodage des messages
- Chiffrement des données
- Validation des protocoles

### 3. **Chat (`src/chat/`)**
- **message.py** : Classe Message
- **manager.py** : Gestionnaire de chat
- **formatter.py** : Formatage des messages

Responsabilités:
- Stockage des messages en mémoire
- Formatage pour l'affichage
- Recherche et filtrage
- Gestion des réactions/éditions

### 4. **Database (`src/database/`)**
- **db.py** : Gestion SQLite
- **models.py** : Modèles de données
- **queries.py** : Requêtes SQL

Responsabilités:
- Persistance des données
- Historique des messages
- Gestion des utilisateurs
- Gestion des sessions

### 5. **UI (`src/ui/`)**
- **main_window.py** : Fenêtre principale PyQt6
- **dialogs.py** : Boîtes de dialogue
- **widgets.py** : Widgets personnalisés
- **video_window.py** : Fenêtre d'appel vidéo

Responsabilités:
- Interface utilisateur
- Affichage des messages
- Gestion des événements utilisateur
- Mise à jour de l'interface

### 6. **Media (`src/media/`)**
- **audio.py** : Capture/streaming audio
- **video.py** : Capture/streaming vidéo
- **screen.py** : Partage d'écran

Responsabilités:
- Capture audio/vidéo
- Encodage des flux
- Gestion des périphériques

### 7. **File Sharing (`src/file_sharing/`)**
- **manager.py** : Gestion des transferts
- **transfer.py** : Protocole de transfert

Responsabilités:
- Transfert de fichiers
- Gestion des permissions
- Checksum et validation

### 8. **Utils (`src/utils/`)**
- **logger.py** : Système de logging
- **helpers.py** : Fonctions utilitaires
- **validators.py** : Validation des données

Responsabilités:
- Logging et debugging
- Fonctions utilitaires
- Validation des entrées

## Flux de Communication

### Envoi d'un message texte (Client → Serveur → Clients)

```
1. Utilisateur tape un message
         ↓
2. UI appelle ChatManager.add_message()
         ↓
3. ChatManager notifie les callbacks enregistrés
         ↓
4. Network.Client.send_message() encode et envoie
         ↓
5. Server reçoit et décode
         ↓
6. Handlers traitent le message
         ↓
7. Server broadcast à tous les clients
         ↓
8. Chaque client reçoit et affiche
```

### Structure d'un message

```json
{
  "message_id": "123e4567-e89b-12d3-a456-426614174000",
  "sender": "john_doe",
  "timestamp": "2026-01-15T10:30:00.000000",
  "message_type": "TEXT",
  "content": {
    "text": "Hello world!"
  },
  "is_encrypted": false
}
```

### Structure du protocole TCP

```
┌─────────────────────────────────────┐
│ Protocole NearMeet TCP              │
├─────────────────────────────────────┤
│ Magic Number (4 bytes):   "NEAR"    │
│ Version (1 byte):         1         │
│ Message ID (4 bytes):     <id>      │
│ Payload Size (4 bytes):   <size>    │
│ Reserved (7 bytes):       0x00      │
├─────────────────────────────────────┤
│ Payload (JSON, variable size)       │
└─────────────────────────────────────┘
Total Header: 20 bytes
```

## Patterns et Principes

### 1. **Observer Pattern**
Les modules utilisent des callbacks pour notifier les changements:
```python
chat_manager.register_callback(on_message_received)
```

### 2. **Singleton Pattern**
Les gestionnaires globaux (Database, Logger):
```python
db = Database()  # Instance unique
logger = get_logger(__name__)
```

### 3. **Thread Safety**
Utilisation de locks pour les accès concurrents:
```python
self.lock = threading.Lock()
with self.lock:
    # Accès à la ressource partagée
```

### 4. **Configuration Centralisée**
Tous les paramètres dans `config.py`:
```python
from src.config import ServerConfig
port = ServerConfig.PORT
```

## Securité

### Chiffrement

- **Algorithme** : AES-256-GCM (Fernet)
- **Dérivation de clé** : PBKDF2 avec SHA256
- **Hachage des mots de passe** : Argon2

```python
from src.network.security import Encryption
encrypted = Encryption.encrypt_message(message, key)
```

### Validation

Tous les inputs utilisateur sont validés:
```python
from src.utils.validators import validate_username
is_valid, error = validate_username(username)
```

## Performance

### Optimisations

1. **Compression des données** :
   - Messages texte: UTF-8
   - Vidéo/Audio: Codecs optimisés

2. **Buffering** :
   - Buffer TCP : 4 KB
   - Buffer audio : 1024 samples

3. **Threading** :
   - Serveur: Thread par client
   - Client: Thread séparé pour réception

4. **Caching** :
   - Cache des utilisateurs connectés
   - Cache du historique des messages

## Évolutivité

### Scalabilité horizontale

Pour supporter plus de clients:

1. **Load Balancer** :
   - HAProxy ou Nginx pour distribuer les connexions

2. **Sharding** :
   - Diviser les utilisateurs par groupes
   - Serveurs par groupe

3. **Replication** :
   - Réplication de la base de données
   - Sync entre serveurs

## Déploiement

### Mode développement
```bash
python -m src --mode server --debug
```

### Mode production
```bash
export APP_LOG_LEVEL=ERROR
python -m src --mode server
```

## Monitoring

### Logs

Les logs sont écrits dans:
- Console (DEBUG et supérieur)
- Fichier: `logs/nearmeet.log` (rotation 10MB)

### Métriques

À implémenter:
- Nombre de clients connectés
- Nombre de messages par seconde
- Utilisation CPU/RAM
- Latence réseau

---

Pour plus de détails, consultez la documentation API.
