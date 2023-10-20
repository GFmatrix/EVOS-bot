from telegram import Update,  User
from telegram.ext import CallbackContext, ConversationHandler, CallbackContext
from db.functions.user import register
from bot.keyboards.user import *
from bot.translate.text import text
from bot import states
from telegram import ParseMode

def settings(update: Update, context: CallbackContext):
    user = update.message.from_user
    # register(user)
    update.message.reply_text(text.test)
    # return states.ORDER