from ast import Call
import logging
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters
from bot import config
from bot.handlers import settings, user, order
from bot.keyboards import user as user_keyboard
from bot.keyboards import order as order_keyboard
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
            MessageHandler(Filters.text(user_keyboard.ORDER_KEY), order.order),
            MessageHandler(Filters.text(user_keyboard.CONTACT_WITH_US_KEY), user.contact_us),
            MessageHandler(Filters.text(user_keyboard.FEEDBACK_KEY), user.feedback),
            MessageHandler(Filters.text(user_keyboard.SETTINGS_KEY), settings.settings),
            MessageHandler(Filters.text(order_keyboard.BACK_KEY), order.back_to_main)
        ],
        states={
            states.CATEGORY: [
                MessageHandler(Filters.text(order_keyboard.BACK_KEY), order.back_to_main),
                MessageHandler(Filters.text & ~Filters.command & ~Filters.text(order_keyboard.BACK_KEY), order.category)],
            states.PRODUCT: [
                MessageHandler(Filters.text(order_keyboard.BACK_KEY), order.back_to_categories)]
        },
        fallbacks=[CommandHandler('start', user.start)],
    )

    dispatcher.add_handler(conv_handler)
    
    updater.start_polling()
    updater.idle()
