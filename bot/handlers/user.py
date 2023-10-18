
from telegram import Update,  User
from telegram.ext import CallbackContext, ConversationHandler, CallbackContext
from db.functions.user import get_user_lang, register, user_data_reset
from bot.keyboards.user import *
from bot import states
from telegram import ParseMode


def start(update: Update, context: CallbackContext) -> None:
    user: User = update.effective_user
    register(user.id, user.first_name,
             user.last_name)
    try: update.message.reply_text(
        "You are in main menu",
        reply_markup=main_keyboard_markup
    )
    except: 
        query = update.callback_query
        query.edit_message_text(
            "You are in main menu",
            reply_markup=main_keyboard_markup)

    return ConversationHandler.END