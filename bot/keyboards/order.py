from telegram import \
    InlineKeyboardButton, InlineKeyboardMarkup, \
    KeyboardButton, ReplyKeyboardMarkup
from db.functions.order import *

BACK_KEY = "🔙 Ortga qaytish"

def categories_keyboard_markup() -> ReplyKeyboardMarkup:
    '''
    Returns categories keyboard markup
    '''
    categories = get_categories()
    
    if not categories:
        return None
    
    categories_keyboard = []

    for i in range(0, len(categories), 2):
        categories_keyboard.append(categories[i:i + 2])
        
    categories_keyboard.append([BACK_KEY])
    
    return ReplyKeyboardMarkup(categories_keyboard, resize_keyboard=True)



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