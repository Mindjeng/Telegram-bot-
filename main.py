import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from config.config import TELEGRAM_TOKEN, TEAMS

# Configurer le logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    """Envoyez un message de démarrage lorsque la commande /start est émise."""
    update.message.reply_text('Bonjour! Je suis le bot de prédiction des scores FIFA Penalty 18. Envoyez /teams pour voir les équipes disponibles ou /predict pour obtenir des prédictions.')

def list_teams(update: Update, context: CallbackContext) -> None:
    """Envoyez la liste des équipes disponibles lorsque la commande /teams est émise."""
    teams_list = "\n".join([f"{i+1}) {team}" for i, team in enumerate(TEAMS)])
    update.message.reply_text(f"Voici les équipes disponibles :\n{teams_list}")

def main() -> None:
    """Démarrez le bot."""
    # Créez l'Updater et passez-lui le token du bot.
    updater = Updater(TELEGRAM_TOKEN)

    # Obtenez le dispatcher pour enregistrer les gestionnaires.
    dispatcher = updater.dispatcher

    # Commandes
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("teams", list_teams))

    # Démarrez le Bot
    updater.start_polling()

    # Exécutez le bot jusqu'à ce que vous appuyiez sur Ctrl-C ou que le processus reçoive SIGINT, SIGTERM ou SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()