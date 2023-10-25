from telegram import ReplyKeyboardMarkup, Update,  User
from telegram.ext import CallbackContext, ConversationHandler, CallbackContext
from bot.config import DEFAULT_IMG
from db.functions.user import lang
from db.functions.cart import add_to_cart, get_cart_via_tg_id, get_product_price, remove_from_cart
from db.functions.product import get_product_by_name, get_product_by_id, update_product_count
from db.functions.order import get_categories, get_products_from_cat_name
import bot.handlers.order as order_handler
import bot.keyboards.order as order_keyboard
import bot.keyboards.cart as cart_keyboard
from bot.translate.text import jtext, text
from bot import states
from telegram import ParseMode

def add_cart(update: Update, context: CallbackContext):
    count = update.message.text
    userid = update.message.from_user.id
    if not count.isdigit() or len(count)>9:
        update.message.reply_text(jtext["pls_enter_number"][lang(userid)])
        return states.PRODUCT_COUNT
    
    product = context.user_data["product"]
    products_button = order_keyboard.products_keyboard(context.user_data['category'])
    add_to_cart(product.id, update.message.text, userid)
    update.message.reply_text(jtext["added_to_cart"][lang(userid)], reply_markup=ReplyKeyboardMarkup(products_button, resize_keyboard=True))
    return states.PRODUCT

def cart(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    products = get_cart_via_tg_id(user_id)
    if not products: 
        update.message.reply_text(jtext["cart_is_empty"][lang(user_id)])
        return states.CATEGORY
    else:
        text = jtext["cart_text"][lang(user_id)].format(
            list=''.join([
                jtext["list_text"][lang(user_id)].format(
                        name=product.name, count=product.count, 
                        price='{:,}'.format(product.price), 
                        total_price='{:,}'.format(int(product.count)*int(product.price))
                    ) for product in products]),
            total_price='{:,}'.format(sum([int(product.count)*int(product.price) for product in products]))
            )
        update.message.reply_text(text, parse_mode=ParseMode.HTML,
        reply_markup=cart_keyboard.cart_keyboard(products)
        )
        return states.CART

def minus_product(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    product_id = query.data.split('-')[1]
    
    if update_product_count(product_id) <= 1:
        delete_product(update, context)
    product = update_product_count(product_id, count=update_product_count(product_id)-1)
    
    user_id = query.from_user.id
    products = get_cart_via_tg_id(user_id)
    if not products: 
        query.edit_message_text(jtext["cart_is_empty"][lang(user_id)])
        return states.CATEGORY
    else:
        text = jtext["cart_text"][lang(user_id)].format(
            list=''.join([
                jtext["list_text"][lang(user_id)].format(
                        name=product.name, count=product.count, 
                        price='{:,}'.format(product.price), 
                        total_price='{:,}'.format(int(product.count)*int(product.price))
                    ) for product in products]),
            total_price='{:,}'.format(sum([int(product.count)*int(product.price) for product in products]))
            )
        query.edit_message_text(text, parse_mode=ParseMode.HTML,
        reply_markup=cart_keyboard.cart_keyboard(products)
        )
        return states.CART

def plus_product(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    product_id = query.data.split('-')[1]
    
    product = update_product_count(product_id, count=update_product_count(product_id)+1)
    
    user_id = update.message.from_user.id
    products = get_cart_via_tg_id(user_id)
    if not products: 
        query.edit_message_text(jtext["cart_is_empty"][lang(user_id)])
        return states.CATEGORY
    else:
        text = jtext["cart_text"][lang(user_id)].format(
            list=''.join([
                jtext["list_text"][lang(user_id)].format(
                        name=product.name, count=product.count, 
                        price='{:,}'.format(product.price), 
                        total_price='{:,}'.format(int(product.count)*int(product.price))
                    ) for product in products]),
            total_price='{:,}'.format(sum([int(product.count)*int(product.price) for product in products]))
            )
        query.edit_message_text(text, parse_mode=ParseMode.HTML,
        reply_markup=cart_keyboard.cart_keyboard(products)
        )
        return states.CART

def delete_product(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    product_id = query.data.split('-')[1]
    remove_from_cart(product_id)
    
    user_id = query.from_user.id
    products = get_cart_via_tg_id(user_id)
    if not products: 
        query.edit_message_text(jtext["cart_is_empty"][lang(user_id)])
        return states.CATEGORY
    else:
        text = jtext["cart_text"][lang(user_id)].format(
            list=''.join([
                jtext["list_text"][lang(user_id)].format(
                        name=product.name, count=product.count, 
                        price='{:,}'.format(product.price), 
                        total_price='{:,}'.format(int(product.count)*int(product.price))
                    ) for product in products]),
            total_price='{:,}'.format(sum([int(product.count)*int(product.price) for product in products]))
            )
        query.edit_message_text(text, parse_mode=ParseMode.HTML,
        reply_markup=cart_keyboard.cart_keyboard(products)
        )
        return states.CART

def back_to_products(update: Update, context: CallbackContext):
    products_button = order_keyboard.products_keyboard(context.user_data['category'])
    update.message.reply_text(jtext['select_product'][lang(update.message.from_user.id)], reply_markup=ReplyKeyboardMarkup(products_button, resize_keyboard=True))
    return states.PRODUCT
    
    
    
    