
from telegram import Update,  User
from telegram.ext import CallbackContext, ConversationHandler, CallbackContext
from db.functions.user import register
from bot.keyboards.user import *
from bot.translate.text import text
from bot import states
from telegram import ParseMode


def start(update: Update, context: CallbackContext) -> None:
    user: User = update.effective_user
    register(user.id, user.first_name,
             user.last_name)
    try: update.message.reply_text(
        text.start.uz,
        reply_markup=main_keyboard_markup
    )
    except: 
        query = update.callback_query
        query.edit_message_text(
            text.start.uz,
            reply_markup=main_keyboard_markup)

    return ConversationHandler.END
    
def feedback(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text.test)
    # return states.FEEDBACK
def contact_us(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text.test)