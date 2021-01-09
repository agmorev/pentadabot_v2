from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

calcs_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💶 Вартість фінансової гарантії", callback_data='warranty_calc'),
        ],
        [
            InlineKeyboardButton(text="💵 Розмір суми митних платежів", url='http://www.mdoffice.com.ua/pls/MDOffice/payacc.html'),    
        ],
    ],
)

vehicle_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🚚 Автомобільний", callback_data='auto'),
            InlineKeyboardButton(text="🚂 Залізничний", callback_data='railway'),
        ],
        [
            InlineKeyboardButton(text="🚢 Морський", callback_data='sea'),
            InlineKeyboardButton(text="⛽️ Трубопровідний", callback_data='pipeline'),       
        ],
    ],
)