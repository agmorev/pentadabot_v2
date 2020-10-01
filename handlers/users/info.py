from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from loader import dp


@dp.message_handler(Command(['info']))
async def bot_info(message: types.Message):
    await message.answer(f'Информация о Вас! {message.from_user.id}\n')