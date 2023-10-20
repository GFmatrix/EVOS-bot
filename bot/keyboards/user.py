from telegram import \
    InlineKeyboardButton, InlineKeyboardMarkup, \
    KeyboardButton, ReplyKeyboardMarkup

ORDER_KEY = '🛍 Buyurtma berish'
CONTACT_WITH_US_KEY = '☎️ Biz bilan aloqa'
FEEDBACK_KEY = '✍️ Fikr bildirish'
SETTINGS_KEY = '⚙️ Sozlamalar'

main_keyboard = [
    [ORDER_KEY],
    [
        CONTACT_WITH_US_KEY,
        FEEDBACK_KEY
    ],
    [SETTINGS_KEY],
]

main_keyboard_markup = ReplyKeyboardMarkup(main_keyboard, resize_keyboard=True)