from ast import Call
import logging
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters
from bot import config
from bot.handlers import user
from bot.keyboards import user as user_keyboard
from bot import states
# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def main() -> None:
    """Start the bot."""
    updater = Updater(config.TOKEN)

    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler('start', user.start),
        ],
        states={
        },
        fallbacks=[CommandHandler('start', user.start)],
    )

    dispatcher.add_handler(conv_handler)
    
    updater.start_polling()
    updater.idle()
