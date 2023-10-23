from telegram import \
    InlineKeyboardButton, InlineKeyboardMarkup, \
    KeyboardButton, ReplyKeyboardMarkup
from db.functions.order import *
from db.functions.cart import get_cart_via_tg_id

ORDER_KEY = "🛍 Buyurtma berish"

def cart_keyboard(products):
    keyboard = []
    for product in products:
        keyboard.append(
            [InlineKeyboardButton(text=product.name, callback_data="NODATA")]
        )
        keyboard.append(
            [
                InlineKeyboardButton(text='➕', callback_data=f"plus-{product.id}"),
                InlineKeyboardButton(text=f"{product.count}", callback_data="NODATA"),
                InlineKeyboardButton(text='➖', callback_data=f"minus-{product.id}"),
                InlineKeyboardButton(text='❌', callback_data=f"delete-{product.id}")
            ]
        )
    keyboard.append(
        [InlineKeyboardButton(text=ORDER_KEY, callback_data="order")]
    )

    return InlineKeyboardMarkup(keyboard)