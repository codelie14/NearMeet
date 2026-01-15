# INDEX - NearMeet

Navigation complète du projet NearMeet.

## 🎯 Commencer

| Document | Description | Pour qui |
|----------|-------------|---------|
| [README.md](README.md) | Présentation du projet | Tous |
| [QUICKSTART.md](QUICKSTART.md) | Démarrage rapide (5 min) | Utilisateurs |
| [INSTALL.md](docs/INSTALL.md) | Installation détaillée | Développeurs |
| [FAQ.md](FAQ.md) | Questions fréquentes | Tous |

## 📚 Documentation

### Utilisateurs
| Document | Contenu |
|----------|---------|
| [QUICKSTART.md](QUICKSTART.md) | Lancer l'application rapidement |
| [FAQ.md](FAQ.md) | Questions et réponses |
| [docs/Cahier_des_Charges.md](docs/Cahier_des_Charges.md) | Spécifications complètes |

### Développeurs
| Document | Contenu |
|----------|---------|
| [docs/INSTALL.md](docs/INSTALL.md) | Installation de l'environnement |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Architecture technique |
| [docs/API.md](docs/API.md) | Documentation des APIs |
| [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) | Guide de contribution |

### Status du Projet
| Document | Contenu |
|----------|---------|
| [PROJECT_STATUS.md](PROJECT_STATUS.md) | État d'avancement détaillé |
| [FINAL_REPORT.md](FINAL_REPORT.md) | Rapport final d'implémentation |
| [CHANGELOG.md](CHANGELOG.md) | Historique des versions |

## 🗂️ Structure du Code

### Modules Principaux

```
src/
├── core/              - Cœur de l'application
│   ├── app.py        - Application principale
│   └── enums.py      - Énumérations
│
├── network/          - Gestion réseau (TCP/UDP)
│   ├── server.py     - Serveur TCP
│   ├── client.py     - Client TCP
│   ├── protocol.py   - Protocole personnalisé
│   ├── handlers.py   - Gestionnaires de messages
│   └── security.py   - Chiffrement
│
├── chat/             - Gestion du chat
│   ├── message.py    - Classe Message
│   ├── manager.py    - Gestionnaire de chat
│   └── formatter.py  - Formatage des messages
│
├── database/         - Base de données SQLite
│   ├── db.py         - Gestion DB
│   ├── models.py     - Modèles de données
│   └── queries.py    - Requêtes SQL
│
├── ui/               - Interface PyQt6
│   ├── main_window.py       - Fenêtre principale
│   ├── dialogs.py           - Boîtes de dialogue
│   ├── widgets.py           - Widgets personnalisés
│   ├── video_window.py      - Fenêtre vidéo
│   └── styles.py            - Styles CSS/QSS
│
├── media/            - Audio/Vidéo
│   ├── audio.py      - Capture audio
│   ├── video.py      - Capture vidéo
│   └── screen.py     - Partage d'écran
│
├── file_sharing/     - Transfert de fichiers
│   ├── manager.py    - Gestionnaire de fichiers
│   └── transfer.py   - Protocole de transfert
│
└── utils/            - Utilitaires
    ├── logger.py     - Logging
    ├── helpers.py    - Fonctions auxiliaires
    └── validators.py - Validation des données
```

## 🧪 Tests

| Fichier | Couverture |
|---------|-----------|
| [tests/test_network.py](tests/test_network.py) | Réseau |
| [tests/test_chat.py](tests/test_chat.py) | Chat et messages |
| [tests/test_validators.py](tests/test_validators.py) | Validation |
| [tests/test_security.py](tests/test_security.py) | Sécurité |

## ⚙️ Configuration

| Fichier | Description |
|---------|------------|
| [.env.example](.env.example) | Variables d'environnement |
| [config/default.json](config/default.json) | Configuration par défaut |
| [src/config.py](src/config.py) | Configuration Python |
| [pyproject.toml](pyproject.toml) | Configuration pyproject |
| [setup.py](setup.py) | Configuration de build |

## 📦 Dépendances

| Fichier | Contenu |
|---------|---------|
| [requirements.txt](requirements.txt) | Toutes les dépendances |
| [setup.py](setup.py) | Installation du package |
| [MANIFEST.in](MANIFEST.in) | Fichiers inclus dans le distribution |

## 🛠️ Scripts

| Script | Utilité |
|--------|---------|
| [scripts/build.py](scripts/build.py) | Compiler l'application |
| [scripts/test.py](scripts/test.py) | Lancer les tests |

## 📄 Fichiers de Gestion

| Fichier | Contenu |
|---------|---------|
| [LICENSE](LICENSE) | Licence MIT |
| [.gitignore](.gitignore) | Fichiers ignorés par Git |
| [CHANGELOG.md](CHANGELOG.md) | Historique des versions |

## 🚀 Démarrage Rapide

### Installez et Lancez

```bash
# 1. Installation (voir docs/INSTALL.md)
git clone https://github.com/codelie14/NearMeet.git
cd NearMeet
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 2. Serveur (machine 1)
python -m src --mode server --port 5000

# 3. Client (machine 2)
python -m src --mode client --host 192.168.1.100 --port 5000 --username "User"
```

Voir [QUICKSTART.md](QUICKSTART.md) pour plus de détails.

## 🔗 Liens Utiles

### Documentation
- [README Complet](README.md)
- [API Reference](docs/API.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Spécifications](docs/Cahier_des_Charges.md)

### Installation
- [Guide d'Installation Complet](docs/INSTALL.md)
- [Démarrage Rapide](QUICKSTART.md)
- [FAQ - Installation](FAQ.md#installation)

### Développement
- [Guide de Contribution](docs/CONTRIBUTING.md)
- [Architecture Technique](docs/ARCHITECTURE.md)
- [Documentation API](docs/API.md)
- [Structure du Projet](PROJECT_STATUS.md)

### Support
- [FAQ - Support](FAQ.md#support)
- [Rapport Final](FINAL_REPORT.md)
- [Historique](CHANGELOG.md)

## 📊 Statistiques

```
Total Fichiers: 35+
Python Files: 23
Documentation: 8
Tests: 4
Lignes de Code: ~5000+
Taux de Complétude: 70%
```

## 🎯 État d'Avancement

| Composant | Status |
|-----------|--------|
| Infrastructure | ✅ 100% |
| Configuration | ✅ 100% |
| Modules Utilitaires | ✅ 100% |
| Réseau (TCP/UDP) | ✅ 100% |
| Chat Texte | ✅ 100% |
| Base de Données | ✅ 100% |
| UI Basique | ✅ 100% |
| Tests | ✅ 100% |
| Documentation | ✅ 100% |
| **Sous-total** | **✅ 100%** |
| Audio/Vidéo | ⏳ 0% |
| Partage d'Écran | ⏳ 0% |
| Transfert de Fichiers | ⏳ 0% |
| UI Avancée | ⏳ 30% |

## 💡 Conseils d'Utilisation

### Pour les Utilisateurs
1. Lisez [QUICKSTART.md](QUICKSTART.md) (5 minutes)
2. Consultez [FAQ.md](FAQ.md) si vous avez des questions
3. Reportez les bugs via GitHub Issues

### Pour les Développeurs
1. Lisez [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
2. Consultez [docs/API.md](docs/API.md)
3. Suivez [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)
4. Exécutez les tests: `python scripts/test.py`

### Pour les Mainteneurs
1. Consultez [PROJECT_STATUS.md](PROJECT_STATUS.md)
2. Mettez à jour [CHANGELOG.md](CHANGELOG.md)
3. Maintenir la documentation à jour
4. Vérifier la couverture de tests

## 🆘 Besoin d'Aide?

1. **Installation?** → [docs/INSTALL.md](docs/INSTALL.md)
2. **Utilisation?** → [QUICKSTART.md](QUICKSTART.md)
3. **Questions?** → [FAQ.md](FAQ.md)
4. **Développement?** → [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)
5. **API?** → [docs/API.md](docs/API.md)

---

**Dernière mise à jour:** 15 janvier 2026
**Version:** 1.0.0
**Status:** 🟢 Opérationnel
