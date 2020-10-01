from aiogram import types
from loader import dp, bot


@dp.message_handler(text="☎️ Контакти")
async def bot_contacts(message: types.Message):
    address = "\n".join(
        [
            'ПОВНЕ ТОВАРИСТВО "ПЕНТАДА ТРАНС" ТОВ «ПЕНТАДА ГРУПП» І КОМПАНІЯ»',
            'Код ЄДРПОУ: 36701373',
            '',
            'Юридична адреса:',
            '🗺 04073, м. Київ, пр-т Степана Бандери, 6, офіс 603',
            'Представницький офіс:',
            '🗺 04080, м. Київ, вул. Вікентія Хвойки, 21, офіс 360'
        ]
    )
    phones = "\n".join(
        [
            'Оформлення фінансових гарантій (24/7):',
            '☎️ +38 (067) 447 60 66 (оператори)',
            '📧 zayavka_gd@pentada-trans.com',
            '',
            'Інші питання:',
            '☎️ +38 (067) 447 54 67',
            '☎️ +38 (044) 495 14 75',
            '📧 office@pentada-trans.com'
        ]
    )
    await message.answer('<b>КОНТАКТНА ІНФОРМАЦІЯ</b>')
    await message.answer(address)
    await message.answer_location(50.4854543,30.4863925)
    await message.answer(phones)