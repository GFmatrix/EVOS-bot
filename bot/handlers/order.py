from telegram import Update,  User
from telegram.ext import CallbackContext, ConversationHandler, CallbackContext
from bot.config import DEFAULT_IMG
from db.functions.user import lang
from db.functions.product import get_product_by_name
from db.functions.order import get_categories, get_products_from_cat_name
import bot.handlers.user as user_handler
import bot.keyboards.order as order_keyboard
from bot.translate.text import jtext, text
from bot import states
from telegram import ParseMode
from telegram import \
    KeyboardButton, ReplyKeyboardMarkup

def order(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    keyboard_markup = order_keyboard.categories_keyboard_markup(user_id)
    if keyboard_markup != None:
        update.message.reply_text(jtext['select_needed_category'][lang(user_id)], reply_markup=keyboard_markup)
        return states.CATEGORY
    else:
        update.message.reply_text(jtext['no_category'][lang(user_id)])
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
            context.user_data['category'] = mes
            update.message.reply_text(jtext['select_product'][lang(user_id)], reply_markup=ReplyKeyboardMarkup(products_button, resize_keyboard=True))
            return states.PRODUCT
        else:
            update.message.reply_text(jtext['no_product_in_category'][lang(user_id)])
            return states.CATEGORY

def product(update: Update, context: CallbackContext):
    product = get_product_by_name(update.message.text)
    if product:
        update.message.reply_photo(photo=product.photo if product.photo else DEFAULT_IMG, caption=jtext['product_info'][lang(update.effective_user.id)].format(
            name=product.name, price='{:,}'.format(product.price)), parse_mode=ParseMode.HTML,
            reply_markup=order_keyboard.product_count())
        context.user_data['product'] = product
        return states.PRODUCT_COUNT
    else:
        update.message.reply_text(jtext['product_not_found'][lang(update.effective_user.id)])
        return states.PRODUCT

def back_to_main(update: Update, context: CallbackContext):
    # update.message.reply_text(jtext['back_to_main'][lang(update.effective_user.id)])
    user_handler.start(update, context)
    return ConversationHandler.END

def back_to_categories(update: Update, context: CallbackContext):
    order(update, context)
    return states.CATEGORY