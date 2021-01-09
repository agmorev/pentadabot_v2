from aiogram.dispatcher.filters.state import StatesGroup, State



class Login(StatesGroup):
    email_state = State()
    password_state = State()