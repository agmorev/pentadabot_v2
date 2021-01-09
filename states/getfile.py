from aiogram.dispatcher.filters.state import StatesGroup, State



class Getfile(StatesGroup):
    load_state = State()
    