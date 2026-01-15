# API Documentation - NearMeet

## Table des matières

- [Core API](#core-api)
- [Network API](#network-api)
- [Chat API](#chat-api)
- [Database API](#database-api)
- [Security API](#security-api)

---

## Core API

### NearMeetApp

Classe principale de l'application.

```python
from src.core.app import NearMeetApp

app = NearMeetApp(mode="client")
app.run()
```

#### Methods

##### `__init__(mode: str)`
Initialise l'application en mode client ou serveur.

**Parameters:**
- `mode` (str): 'client' ou 'server'

##### `init_gui()`
Initialise l'interface graphique.

**Returns:**
- `MainWindow`: La fenêtre principale

##### `run()`
Lance l'application.

##### `shutdown()`
Arrête l'application.

---

## Network API

### Server

Serveur TCP pour NearMeet.

```python
from src.network.server import Server

server = Server(host="0.0.0.0", port=5000)
server.start()
```

#### Methods

##### `start() -> bool`
Démarre le serveur.

**Returns:**
- `bool`: True si succès, False sinon

##### `stop()`
Arrête le serveur.

##### `broadcast_message(message: str, exclude_address: tuple = None)`
Diffuse un message à tous les clients.

**Parameters:**
- `message` (str): Message à envoyer
- `exclude_address` (tuple, optional): Adresse à exclure

##### `send_to_client(client_address: tuple, message: str) -> bool`
Envoie un message à un client spécifique.

**Parameters:**
- `client_address` (tuple): Adresse du client (host, port)
- `message` (str): Message à envoyer

**Returns:**
- `bool`: True si succès, False sinon

##### `register_message_handler(handler: Callable)`
Enregistre un gestionnaire de messages.

**Parameters:**
- `handler` (Callable): Fonction handler(address, message)

##### `get_client_count() -> int`
Retourne le nombre de clients connectés.

##### `get_connected_clients() -> list`
Retourne la liste des clients connectés.

### Client

Client TCP pour NearMeet.

```python
from src.network.client import Client

client = Client(host="192.168.1.100", port=5000)
if client.connect():
    client.send_message("Hello")
```

#### Methods

##### `connect() -> bool`
Se connecte au serveur.

**Returns:**
- `bool`: True si succès, False sinon

##### `disconnect()`
Se déconnecte du serveur.

##### `send_message(message: str) -> bool`
Envoie un message au serveur.

**Parameters:**
- `message` (str): Message à envoyer

**Returns:**
- `bool`: True si succès, False sinon

##### `send_json(data: dict) -> bool`
Envoie un message JSON au serveur.

**Parameters:**
- `data` (dict): Données JSON à envoyer

**Returns:**
- `bool`: True si succès, False sinon

##### `register_message_handler(handler: Callable)`
Enregistre un gestionnaire de messages.

**Parameters:**
- `handler` (Callable): Fonction handler(message)

##### `is_connected() -> bool`
Vérifie si connecté au serveur.

### Protocol

Protocole de communication personnalisé.

```python
from src.network.protocol import Protocol, Message

msg = Message(sender="john", timestamp="2026-01-15T10:00:00", 
              message_type="TEXT", content={"text": "Hello"})
packed = Protocol.pack_message(msg)
msg_id, payload = Protocol.unpack_message(packed)
```

#### Methods

##### `pack_message(message: Union[Message, bytes], message_id: int = 0) -> bytes`
Empaquète un message pour transmission.

##### `unpack_message(data: bytes) -> tuple[int, bytes]`
Dépaquète un message reçu.

**Returns:**
- `tuple`: (message_id, payload)

##### `create_handshake() -> str`
Crée un message de handshake.

##### `create_ack(message_id: int) -> str`
Crée un message d'acquittement.

##### `create_heartbeat() -> str`
Crée un message de heartbeat.

---

## Chat API

### ChatManager

Gère les messages de chat.

```python
from src.chat.manager import ChatManager
from src.chat.message import Message

manager = ChatManager()

msg = Message(sender="john", content="Hello world")
manager.add_message(msg)

# Récupérer les messages
messages = manager.get_messages(limit=10)

# Rechercher
results = manager.search_messages("hello")
```

#### Methods

##### `add_message(message: Message) -> None`
Ajoute un message au chat.

##### `get_messages(limit: int = None, offset: int = 0) -> List[Message]`
Récupère les messages.

**Parameters:**
- `limit` (int, optional): Nombre maximum de messages
- `offset` (int): Décalage

##### `get_messages_from_user(username: str) -> List[Message]`
Récupère les messages d'un utilisateur.

##### `search_messages(keyword: str, case_sensitive: bool = False) -> List[Message]`
Recherche des messages.

##### `delete_message(message_id: str) -> bool`
Supprime un message.

##### `edit_message(message_id: str, new_content: str) -> bool`
Édite un message.

##### `add_reaction(message_id: str, emoji: str, username: str) -> bool`
Ajoute une réaction à un message.

##### `clear_messages() -> None`
Efface tous les messages.

##### `register_callback(callback: Callable)`
Enregistre un callback pour les nouveaux messages.

### Message

Structure de message.

```python
from src.chat.message import Message
from datetime import datetime

msg = Message(
    sender="john",
    content="Hello",
    timestamp=datetime.now(),
    message_id="unique-id"
)

data = msg.to_dict()
```

#### Properties

- `sender` (str): Auteur du message
- `content` (str): Contenu du message
- `timestamp` (datetime): Date/heure
- `message_id` (str): ID unique
- `is_encrypted` (bool): Message chiffré?
- `attachments` (list): Fichiers attachés
- `reply_to` (str, optional): ID du message répondu
- `reactions` (dict): Réactions (emoji -> [users])

---

## Database API

### Database

Gère la base de données SQLite.

```python
from src.database.db import Database

with Database() as db:
    db.execute("INSERT INTO users (username) VALUES (?)", ("john",))
    users = db.fetch_all("SELECT * FROM users")
```

#### Methods

##### `execute(query: str, params: tuple = ()) -> cursor`
Exécute une requête.

##### `fetch_one(query: str, params: tuple = ())`
Récupère une ligne.

##### `fetch_all(query: str, params: tuple = ())`
Récupère toutes les lignes.

##### `close()`
Ferme la connexion.

---

## Security API

### Encryption

Gère le chiffrement des messages.

```python
from src.network.security import Encryption

# Générer une clé
key = Encryption.generate_key()

# Chiffrer
encrypted = Encryption.encrypt_message("Secret", key)

# Déchiffrer
decrypted = Encryption.decrypt_message(encrypted, key)

# Dériver une clé d'un mot de passe
key, salt = Encryption.derive_key("mypassword")
```

#### Methods

##### `generate_key() -> str`
Génère une nouvelle clé de chiffrement.

##### `derive_key(password: str, salt: bytes = None) -> tuple[str, str]`
Dérive une clé d'un mot de passe.

**Returns:**
- `tuple`: (clé, salt)

##### `encrypt_message(message: str, key: str) -> str`
Chiffre un message.

##### `decrypt_message(encrypted_message: str, key: str) -> str`
Déchiffre un message.

### PasswordHasher

Gère le hachage des mots de passe.

```python
from src.network.security import PasswordHasher

# Hacher
hashed, salt = PasswordHasher.hash_password("password123")

# Vérifier
is_valid = PasswordHasher.verify_password("password123", hashed, salt)
```

#### Methods

##### `hash_password(password: str) -> tuple[str, str]`
Hache un mot de passe.

**Returns:**
- `tuple`: (hash, salt)

##### `verify_password(password: str, hashed: str, salt: str) -> bool`
Vérifie un mot de passe.

---

## Validators API

```python
from src.utils.validators import (
    validate_username,
    validate_email,
    validate_port,
    validate_ip_address,
    validate_password
)

# Valider un nom d'utilisateur
is_valid, error = validate_username("john_doe")
if not is_valid:
    print(error)

# Valider un email
is_valid, error = validate_email("john@example.com")

# Valider un port
is_valid, error = validate_port(5000)

# Valider une adresse IP
is_valid, error = validate_ip_address("192.168.1.100")

# Valider un mot de passe
is_valid, error = validate_password("SecurePass123!")
```

---

## Logging API

```python
from src.utils.logger import get_logger, setup_logging

# Initialiser les logs
setup_logging()

# Obtenir un logger
logger = get_logger(__name__)

# Utiliser
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")
```

---

## Helpers API

```python
from src.utils.helpers import (
    get_local_ip,
    get_hostname,
    get_platform_info,
    calculate_file_hash,
    format_file_size,
    generate_unique_id,
    is_valid_ip,
    is_port_available
)

# Obtenir l'IP locale
ip = get_local_ip()  # "192.168.1.100"

# Obtenir le hostname
hostname = get_hostname()  # "DESKTOP-ABC123"

# Info système
info = get_platform_info()

# Calculer le hash d'un fichier
hash_value = calculate_file_hash("path/to/file.txt")

# Formater la taille d'un fichier
size_str = format_file_size(1024000)  # "1000.00 KB"

# ID unique
unique_id = generate_unique_id()

# Vérifier IP/Port
is_valid_ip("192.168.1.1")  # True
is_port_available(5000)  # True
```

---

Pour plus d'exemples, consultez le [README.md](../README.md)
