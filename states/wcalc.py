from aiogram.dispatcher.filters.state import StatesGroup, State



class Warranty_calculation(StatesGroup):
    vehicle_state = State()
    cncode_state = State()
    weight_state = State()
    value_state = State()