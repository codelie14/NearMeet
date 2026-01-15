# FAQ - NearMeet

Frequently Asked Questions sur NearMeet.

## Installation

### Q: Comment installer NearMeet?
**A:** Consultez le [guide d'installation](docs/INSTALL.md) pour les instructions détaillées par OS.

### Q: Quels sont les prérequis?
**A:** Python 3.11+, pip, et un réseau local. Voir [prérequis](docs/INSTALL.md#prérequis).

### Q: Puis-je utiliser NearMeet sans internet?
**A:** Oui! NearMeet fonctionne uniquement sur réseau local (LAN) et ne nécessite pas internet.

## Utilisation

### Q: Comment lancer le serveur?
**A:**
```bash
python -m src --mode server --port 5000
```

### Q: Comment me connecter en tant que client?
**A:**
```bash
python -m src --mode client --host 192.168.1.100 --port 5000 --username "JohnDoe"
```

### Q: Quelle est l'adresse IP à utiliser?
**A:** Utilisez `ipconfig` (Windows) ou `ifconfig` (Mac/Linux) pour trouver votre IPv4 locale.

## Fonctionnalités

### Q: Quelles fonctionnalités sont disponibles?
**A:** Actuellement:
- Chat texte en temps réel
- Historique des messages
- Recherche dans les messages
- Chiffrement des données

Fonctionnalités à venir:
- Appels vidéo/audio
- Partage d'écran
- Transfert de fichiers

### Q: Quand les appels vidéo seront-ils disponibles?
**A:** Nous travaillons dessus pour la v1.1. Restez à l'écoute!

## Dépannage

### Q: L'application ne démarre pas
**A:**
1. Vérifiez que vous êtes dans le bon répertoire
2. Assurez-vous que l'environnement virtuel est activé
3. Vérifiez que toutes les dépendances sont installées: `pip install -r requirements.txt`

### Q: Erreur "Port already in use"
**A:** Le port est déjà utilisé. Essayez:
```bash
python -m src --mode server --port 5001
```

### Q: Je ne peux pas me connecter au serveur
**A:**
1. Vérifiez l'adresse IP du serveur: `ipconfig` ou `ifconfig`
2. Assurez-vous que le serveur est en cours d'exécution
3. Vérifiez le pare-feu: il pourrait bloquer les connexions

### Q: Les messages sont lents
**A:**
1. Assurez-vous que vous êtes sur le même réseau local
2. Vérifiez la qualité de votre connexion réseau
3. Consultez les logs: `tail -f logs/nearmeet.log`

## Performance

### Q: Combien de clients le serveur peut-il supporter?
**A:** Actuellement configurable à 100 clients maximum. Peut être augmenté.

### Q: La vidéo fonctionnera-t-elle correctement sur une connexion lente?
**A:** La vidéo utilise UDP pour minimiser la latence. Une bande passante de 1Mbps est recommandée.

## Sécurité

### Q: Mes messages sont-ils sécurisés?
**A:** Oui, les messages sont chiffrés en AES-256-GCM par défaut.

### Q: Où sont stockés mes messages?
**A:** Les messages sont stockés localement dans `data/nearmeet.db` (SQLite).

### Q: Puis-je désactiver le chiffrement?
**A:** Non recommandé, mais possible via `.env`:
```
ENCRYPTION_ENABLED=False
```

## Contribution

### Q: Comment puis-je contribuer?
**A:** Consultez [CONTRIBUTING.md](docs/CONTRIBUTING.md) pour les directives.

### Q: Comment signaler un bug?
**A:** Créez une [issue sur GitHub](https://github.com/codelie14/NearMeet/issues).

### Q: Puis-je proposer une fonctionnalité?
**A:** Oui! Ouvrez une issue avec le tag "enhancement".

## Licence

### Q: Sous quelle licence NearMeet est-il distribué?
**A:** MIT License. Voir [LICENSE](LICENSE) pour les détails.

## Support

### Q: Où puis-je obtenir de l'aide?
**A:**
1. Consultez la [documentation](docs/)
2. Créez une [issue](https://github.com/codelie14/NearMeet/issues)
3. Contactez: contact@indralabs.ai

---

Vous n'avez pas trouvé votre réponse? [Créez une issue!](https://github.com/codelie14/NearMeet/issues)
