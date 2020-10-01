from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📰 Новини"),
            KeyboardButton(text="💼 Кабінет"),
        ],
        [
            KeyboardButton(text="🧮 Калькулятори"),
            KeyboardButton(text="🏪 Представники"),
        ],
        [
            KeyboardButton(text="☎️ Контакти"),
        ],
    ],
    resize_keyboard=True
)