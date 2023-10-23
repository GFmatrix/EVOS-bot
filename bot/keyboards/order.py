from telegram import \
    InlineKeyboardButton, InlineKeyboardMarkup, \
    KeyboardButton, ReplyKeyboardMarkup
from db.functions.order import *
from db.functions.cart import get_cart_via_tg_id

BACK_KEY = "🔙 Ortga qaytish"
CART_KET = "📥 Savatcha"

def categories_keyboard_markup(telegram_id) -> ReplyKeyboardMarkup:
    '''
    Returns categories keyboard markup
    '''
    categories = get_categories()
    
    if not categories:
        return None
    
    categories_keyboard = []
    
    if get_cart_via_tg_id(telegram_id):
        categories_keyboard.append([CART_KET])
    
    for i in range(0, len(categories), 2):
        categories_keyboard.append(categories[i:i + 2])
        
    categories_keyboard.append([BACK_KEY])
    
    return ReplyKeyboardMarkup(categories_keyboard, resize_keyboard=True)

def product_count() -> ReplyKeyboardMarkup:
    '''
    Returns product count keyboard markup
    '''
    product_count = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], [BACK_KEY]]
    return ReplyKeyboardMarkup(product_count, resize_keyboard=True)

def products_keyboard(category_name) -> list:
    '''
    Returns products keyboard list for a given category name
    '''
    products = get_products_from_cat_name(category_name)
    
    if not products:
        return None
    
    __products_keyboard = []

    for i in range(0, len(products), 2):
        __products_keyboard.append(products[i:i + 2])
    __products_keyboard.append([BACK_KEY])
    
    return __products_keyboard