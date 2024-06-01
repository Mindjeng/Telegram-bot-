# FIFA Penalty Bot

Ce projet met en place un bot Telegram qui prédit les scores des matchs FIFA Penalty 18. Le bot offre des commandes pour démarrer une conversation, lister les équipes disponibles et obtenir des prédictions de scores.

## Fonctionnalités

- **/start** : Démarre une conversation avec le bot.
- **/teams** : Liste les équipes disponibles.
- **/predict** : Prédictions de scores de matchs (à implémenter).

## Structure du Projet

fifa_penalty_bot/
├── config/
│   └── config.py
├── data/
│   └── data_preparation.py
├── models/
│   └── model.py
├── scripts/
│   └── fetch_results.py
├── services/
│   └── gpt3_service.py
├── README/
│   └── README.md
├── licence/
│   └── LICENCE.md
├── .gitignore
├── main.py
├── Procfile
└── requirements.txt

## Déploiement rapide sur Heroku

Cliquez sur le bouton ci-dessous pour déployer cette application sur Heroku :

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://www.heroku.com/deploy?template=https://github.com/prgofficial/URLuploader-with-Hotstar)

## Configuration

### Variables d'Environnement

Assurez-vous de configurer les variables d'environnement suivantes sur Heroku :

- `TELEGRAM_TOKEN` : Le token de votre bot Telegram.

### Fichiers essentiels

#### `.gitignore`

```plaintext
# Python
*.pyc
__pycache__/

# Environnement virtuel
env/
venv/

# Configurations locales
config.py

# Jupyter Notebooks
.ipynb_checkpoints

# Systèmes d'exploitation
.DS_Store
Thumbs.db

# Autres
*.log
*.sqlite3
