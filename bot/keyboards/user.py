from telegram import InlineKeyboardButton, InlineKeyboardMarkup

ORDER_KEY = 'order'
CONTACT_WITH_US_KEY = 'contact_with_us'
FEEDBACK_KEY = 'feedback'
SETTINGS_KEY = 'settings'

main_keyboard = [
    [InlineKeyboardButton("🛍 Buyurtma berish",callback_data=ORDER_KEY),],
    [
        InlineKeyboardButton("☎️ Biz bilan aloqa", callback_data=CONTACT_WITH_US_KEY),
        InlineKeyboardButton("✍️ Fikr bildirish", callback_data=FEEDBACK_KEY) 
    ],
    [InlineKeyboardButton("⚙️ Settings", callback_data=SETTINGS_KEY)],
]

main_keyboard_markup = InlineKeyboardMarkup(main_keyboard)