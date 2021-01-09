from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


login_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔐 Увійти...", callback_data='login'),
        ],
    ],
)

cabinet_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📑 Заявки", callback_data='orders'),
        ],
        [
            InlineKeyboardButton(text="📊 Звіти 🛠", callback_data='reports'),    
        ],
        [
            InlineKeyboardButton(text="🏦 Реквізити гаранта", callback_data='requisits'),    
        ],
        [
            InlineKeyboardButton(text="👨‍💻 Контактні особи", callback_data='officials'),    
        ],
    ],
)

order_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📝 Оформити заявку онлайн", url='https://docs.google.com/forms/d/e/1FAIpQLSfGdRHW5FzDVcPqTCnwVkKf57ryfD3llzfqnDbcWTThDU3eSQ/viewform?usp=sf_link'),
        ],
        [
            InlineKeyboardButton(text="📥 Завантажити бланк заявки", callback_data='order_download'),
        ],
        [
            InlineKeyboardButton(text="📤 Відправити готову заявку", callback_data='order_send'),    
        ],
    ],
)