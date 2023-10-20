from telegram import Update,  User
from telegram.ext import CallbackContext, ConversationHandler, CallbackContext
from db.functions.user import lang
from db.functions.order import get_categories, get_products_from_cat_name
import bot.handlers.user as user_handler
import bot.keyboards.order as order_keyboard
from bot.translate.text import jtext, text
from bot import states
from telegram import ParseMode
from telegram import \
    KeyboardButton, ReplyKeyboardMarkup

def order(update: Update, context: CallbackContext):
    keyboard_markup = order_keyboard.categories_keyboard_markup()
    if keyboard_markup != None:
        update.message.reply_text(jtext['select_needed_category'][lang(update.effective_user.id)], reply_markup=keyboard_markup)
        return states.CATEGORY
    else:
        update.message.reply_text(jtext['no_category'][lang(update.effective_user.id)])
        return ConversationHandler.END
    
def category(update: Update, context: CallbackContext):
    categories = get_categories()
    mes = update.message.text
    user_id = update.effective_user.id
    products_button = order_keyboard.products_keyboard(mes)
    if mes not in categories:
        update.message.reply_text(jtext['category_not_found'][lang(user_id)])
        return states.CATEGORY
    else:
        if products_button:
            update.message.reply_text(jtext['select_product'][lang(user_id)], reply_markup=ReplyKeyboardMarkup(products_button, resize_keyboard=True))
            return states.PRODUCT
        else:
            update.message.reply_text(jtext['no_product_in_category'][lang(user_id)])
            return states.CATEGORY

def back_to_main(update: Update, context: CallbackContext):
    # update.message.reply_text(jtext['back_to_main'][lang(update.effective_user.id)])
    user_handler.start(update, context)
    return ConversationHandler.END

def back_to_categories(update: Update, context: CallbackContext):
    order(update, context)
    return states.CATEGORY