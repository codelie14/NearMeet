# Contributing to NearMeet

Merci de votre intérêt pour contribuer à NearMeet! Ce document fournit les lignes directrices pour les contributions.

## Code of Conduct

Soyez respectueux et professionnel. Nous valorisons les contributions de tout le monde.

## Comment contribuer

### 1. Signaler un bug

Créez une issue avec:
- Description claire du bug
- Étapes pour reproduire
- Comportement attendu
- Comportement réel
- Environnement (OS, Python, etc.)

### 2. Suggérer une amélioration

Créez une issue avec:
- Description de l'amélioration
- Cas d'usage
- Implémentation suggérée (optionnel)

### 3. Soumettre du code

#### Prérequis

- Forked le dépôt
- Branché from `main`
- Python 3.11+
- Tous les tests passent

#### Processus

1. **Fork le dépôt**

```bash
git clone https://github.com/codelie14/NearMeet.git
cd NearMeet
```

2. **Créer une branche**

```bash
git checkout -b feature/my-feature
# ou
git checkout -b bugfix/my-bugfix
```

3. **Faire des changements**

- Respectez le style de code (voir ci-dessous)
- Écrivez des tests pour vos changements
- Documentez vos changements

4. **Tester localement**

```bash
python -m pytest tests/
python -m pytest tests/ --cov=src
```

5. **Committer**

```bash
git commit -m "Description claire du changement"
```

Utilisez des messages de commit descriptifs:
- ✨ Nouvelle fonctionnalité: `feat: Add user authentication`
- 🐛 Bug fix: `fix: Resolve connection timeout issue`
- 📖 Documentation: `docs: Update API documentation`
- 🎨 Style: `style: Format code with black`
- ♻️ Refactor: `refactor: Extract message handler logic`
- ✅ Tests: `test: Add unit tests for encryption`

6. **Push et créer une Pull Request**

```bash
git push origin feature/my-feature
```

Décrivez vos changements dans la PR.

## Style de code

### Python

Utilisez [Black](https://github.com/psf/black) pour le formatage:

```bash
black src/
```

Utilisez [isort](https://github.com/PyCPA/isort) pour les imports:

```bash
isort src/
```

Vérifiez avec [flake8](https://github.com/PyCF/flake8):

```bash
flake8 src/
```

### Conventions

- Noms de variables: `snake_case`
- Noms de classes: `PascalCase`
- Noms de constantes: `UPPER_CASE`
- Indentation: 4 espaces
- Ligne max: 100 caractères

### Docstrings

Utilisez le format Google:

```python
def send_message(self, message: str) -> bool:
    """
    Send a message to the server.
    
    Args:
        message: The message text to send.
    
    Returns:
        True if successful, False otherwise.
    
    Raises:
        ConnectionError: If not connected to server.
    """
```

## Tests

Tous les contributions doivent inclure des tests:

```bash
# Exécuter tous les tests
python -m pytest tests/

# Avec couverture
python -m pytest tests/ --cov=src --cov-report=html

# Test spécifique
python -m pytest tests/test_chat.py -v
```

### Écrire des tests

```python
import pytest
from src.chat.manager import ChatManager
from src.chat.message import Message


class TestChatManager:
    """Tests for ChatManager"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.manager = ChatManager()
    
    def test_add_message(self):
        """Test adding a message"""
        message = Message(sender="test", content="Hello")
        self.manager.add_message(message)
        
        assert self.manager.get_message_count() == 1
    
    def test_search_messages(self):
        """Test searching messages"""
        msg1 = Message(sender="user1", content="Hello world")
        msg2 = Message(sender="user2", content="Goodbye")
        
        self.manager.add_message(msg1)
        self.manager.add_message(msg2)
        
        results = self.manager.search_messages("Hello")
        assert len(results) == 1
        assert results[0].content == "Hello world"
```

## Documentation

Mise à jour de la documentation pour les changements:

- **README.md** : Si changements majeurs
- **docs/API.md** : Nouvelles APIs publiques
- **docs/ARCHITECTURE.md** : Changements d'architecture
- **Docstrings** : Dans le code

## Pull Request Checklist

Avant de soumettre:

- [ ] Code formaté avec Black et isort
- [ ] Pas d'erreurs flake8
- [ ] Tests ajoutés/mis à jour
- [ ] Tous les tests passent
- [ ] Documentation mise à jour
- [ ] Messages de commit clairs
- [ ] Pas de conflits avec `main`

## Démarrer le développement

### Setup l'environnement de développement

```bash
# Clone le dépôt
git clone https://github.com/codelie14/NearMeet.git
cd NearMeet

# Créer un environnement virtuel
python -m venv venv

# Activer (Windows)
venv\Scripts\activate

# Activer (macOS/Linux)
source venv/bin/activate

# Installer les dépendances de développement
pip install -r requirements.txt
pip install black flake8 isort pytest pytest-cov

# Vérifier que tout fonctionne
python -m pytest tests/
```

### Outils de développement recommandés

- **IDE** : VS Code, PyCharm
- **Extensions VS Code** : Python, Pylance, Black Formatter
- **Git** : Git Bash ou GitHub Desktop

## Questions?

- Ouvrez une issue pour les questions
- Rejoignez notre communauté Slack (si disponible)
- Envoyez un email aux mainteneurs

## Remerciements

Merci de contribuer à NearMeet! Votre aide est précieuse.

---

**Happy coding! 🚀**
