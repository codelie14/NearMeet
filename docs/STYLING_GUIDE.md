# 🎨 Style & Widgets Improvement Guide - NearMeet

## ✨ Nouveautés Visuelles

Le projet a été amélioré avec un **design moderne et professionnel** :

### 1. **Thème Sombre Avancé** 🌙
- Palette de couleurs moderne (Microsoft Fluent Design)
- Transitions fluides et hover effects
- Support du thème clair optionnel

### 2. **Widgets Personnalisés**

#### MessageBubble
Affiche les messages avec style bubble moderne.

```python
from src.ui.widgets import MessageBubble

bubble = MessageBubble(
    sender="Alice",
    message="Bonjour! Comment ça va?",
    timestamp="14:30",
    is_own=False
)
```

#### UserItem
Liste des utilisateurs avec indicateurs de statut.

```python
from src.ui.widgets import UserItem

user = UserItem(
    username="Bob",
    status="online",  # online, offline, away
)
user.clicked.connect(on_user_clicked)
```

#### RoundedButton
Boutons modernes avec animations.

```python
from src.ui.widgets import RoundedButton

btn = RoundedButton(
    "Appeler",
    style="primary"  # primary, secondary, danger, success
)
```

#### StatusBadge
Badge de statut avec couleurs.

```python
from src.ui.widgets import StatusBadge

badge = StatusBadge("En ligne", status_type="success")
```

#### ChatHeaderFrame
En-tête professionnel pour le chat.

```python
from src.ui.widgets import ChatHeaderFrame

header = ChatHeaderFrame(
    title="NearMeet",
    subtitle="Connected to server.local"
)
```

### 3. **Fichiers de Style QSS**

Deux thèmes disponibles dans `src/ui/styles.py`:

- **Dark Theme** (défaut) - `get_stylesheet("dark")`
- **Light Theme** - `get_stylesheet("light")`

## 🎯 Comment Utiliser les Nouveaux Styles

### Appliquer le thème à l'application

```python
from src.ui.styles import get_stylesheet
from PyQt6.QtWidgets import QApplication

app = QApplication([])
app.setStyleSheet(get_stylesheet("dark"))
```

### Utiliser les widgets personnalisés

```python
from src.ui.widgets import MessageBubble, UserItem, RoundedButton

# Dans votre fenêtre principale
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Ajouter un message
        msg = MessageBubble("Alice", "Salut!")
        layout.addWidget(msg)
        
        # Ajouter un utilisateur
        user = UserItem("Bob", "online")
        layout.addWidget(user)
        
        # Ajouter un bouton
        btn = RoundedButton("Envoyer", style="primary")
        layout.addWidget(btn)
```

## 🎨 Couleurs Principales

### Thème Sombre
```
Background Principal:  #1e1e1e (noir profond)
Background Secondaire: #2d2d2d (gris sombre)
Accent Principal:      #0078d4 (bleu Microsoft)
Accent Succès:         #107c10 (vert)
Accent Danger:         #d13438 (rouge)
Accent Warning:        #f7630c (orange)
Texte:                 #ffffff (blanc)
Texte Secondaire:      #a0a0a0 (gris clair)
Bordure:               #404040 (gris moyen)
```

### Thème Clair
```
Background Principal:  #f3f3f3 (blanc cassé)
Background Secondaire: #ffffff (blanc)
Accent Principal:      #0078d4 (bleu Microsoft)
Texte:                 #000000 (noir)
Bordure:               #e0e0e0 (gris léger)
```

## 📱 Composants Disponibles

| Widget | Description | Utilisation |
|--------|-------------|------------|
| `MessageBubble` | Affiche messages | Chat display |
| `UserItem` | Utilisateur avec statut | User list |
| `RoundedButton` | Bouton moderne | Actions |
| `StatusBadge` | Badge coloré | Statut |
| `ChatHeaderFrame` | En-tête chat | Header |
| `AnimatedLabel` | Label animé | Notifications |
| `SeparatorLine` | Ligne de séparation | Layout |

## 🎬 Animations

### Fade-in Animation

```python
from src.ui.widgets import AnimatedLabel

label = AnimatedLabel("Message")
label.animate_in()  # Démarre l'animation
```

### Hover Effects

Tous les boutons et éléments cliquables ont des transitions au survol.

## 🔧 Personnalisation des Styles

### Modifier les couleurs

Éditez `src/ui/styles.py` et changez les valeurs hex:

```python
DARK_STYLESHEET = """
QPushButton {
    background-color: #FF5733;  /* Votre couleur */
    ...
}
"""
```

### Ajouter un nouveau thème

```python
CUSTOM_STYLESHEET = """
/* Votre CSS personnalisé */
"""

def get_stylesheet(theme: str = "dark") -> str:
    if theme == "custom":
        return CUSTOM_STYLESHEET
    return ...
```

## 📐 Layout Recommandé

Structure moderne pour les applications chat:

```
┌─────────────────────────────┐
│  ChatHeaderFrame            │  Header avec titre
├──────────┬──────────────────┤
│ UserList │  Chat Display    │
│          │  ───────────────│
│ UserItem │  MessageBubble  │
│ UserItem │  MessageBubble  │
│ UserItem │  ───────────────│
│          │  MessageInput   │
├──────────┴──────────────────┤
│  Buttons (primary)          │
├──────────────────────────────┤
│  Status Bar                  │
└──────────────────────────────┘
```

## 🚀 Optimisations de Performance

- CSS est compilé et mis en cache
- Animations utiliseront GPU si disponible
- Updates minimales au repaint

## ✅ Checklist Implémentation

- [x] Dark theme stylesheet
- [x] Light theme stylesheet
- [x] MessageBubble widget
- [x] UserItem widget
- [x] RoundedButton widget
- [x] StatusBadge widget
- [x] ChatHeaderFrame widget
- [x] AnimatedLabel widget
- [x] SeparatorLine widget
- [x] Integration dans main_window.py
- [ ] Advanced dialogs (coming soon)
- [ ] Video window styling (coming soon)
- [ ] Settings UI (coming soon)

## 🎓 Ressources

- [PyQt6 Stylesheet Reference](https://doc.qt.io/qt-6/stylesheet-reference.html)
- [Microsoft Fluent Design](https://www.microsoft.com/design/fluent)
- [Qt Color Names](https://doc.qt.io/qt-6/qcolor.html#predefined-colors)

---

**Version:** 1.0.0  
**Last Updated:** 15 January 2026  
**Status:** 🟢 Ready for use
