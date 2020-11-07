from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from states.wcalc import Warranty_calculation

from keyboards.inline import calcs_markup, vehicle_markup
import re


@dp.message_handler(text="🧮 Калькулятори")
async def bot_represents(message: types.Message):
    await message.answer('<b>КАЛЬКУЛЯТОРИ</b>')
    await message.answer('Оберіть калькулятор для попереднього розрахунку вартості''',
                         reply_markup=calcs_markup)


#Warranty calculation process
@dp.callback_query_handler(text_contains="warranty_calc")
async def warranty_calculator(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('💶 <b>ВАРТІСТЬ ГАРАНТІЇ</b>')
    await call.message.answer('⚠️Для попереднього розрахунку вартості фінансової гарантії надайте послідовно відповіді на наступні 4 питання')
    await call.message.answer('1️⃣Оберіть вид транспортного засобу:', reply_markup=vehicle_markup)
    await Warranty_calculation.vehicle_state.set()

@dp.callback_query_handler(text=['auto', 'railway', 'sea', 'pipeline'], state=Warranty_calculation.vehicle_state)
async def answer_vehicle(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    if call.data == 'auto':
        vehicle = 'Автомобільний'
    elif call.data == 'railway':
        vehicle = 'Залізничний'
    elif call.data == 'sea':
        vehicle = 'Морський'
    elif call.data == 'pipeline':
        vehicle = 'Трубопровідний'
    await state.update_data(answer1=vehicle)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(vehicle)
    await call.message.answer("2️⃣Введіть код товару на рівні 4-х знаків:")
    await Warranty_calculation.next()

@dp.message_handler(state=Warranty_calculation.cncode_state)
async def answer_cncode(message: types.Message, state: FSMContext):
    if re.match(r'\d{4}', message.text) and len(message.text) == 4:
        cncode = message.text
        await state.update_data(answer2=cncode)
        await message.answer("3️⃣Введіть вагу товарів в кілограмах:")
        await Warranty_calculation.next()
    else:
        await message.answer('❗️Код товару має містити тільки перших 4 знаки (товарна позиція)!!! Очікую на коректний код товару...')  

@dp.message_handler(state=Warranty_calculation.weight_state)
async def answer_weight(message: types.Message, state: FSMContext):
    if re.match(r'^[0-9]+$', message.text):
        weight = message.text
        await state.update_data(answer3=weight)
        await message.answer("4️⃣Введіть вартість товару в гривнях:")
        await Warranty_calculation.next()
    else:
        await message.answer('❗️Вага товару має містити тільки цифри!!! Очікую на коректну вагу товару...')

@dp.message_handler(state=Warranty_calculation.value_state)
async def answer_value(message: types.Message, state: FSMContext):
    if re.match(r'^[0-9]+$', message.text):
        data = await state.get_data()
        vehicle = data.get("answer1")
        cncode = data.get("answer2")
        weight = data.get("answer3")
        value = message.text
        await state.update_data(answer4=value)
        result = 'Вид транспорту: '+str(vehicle)+'\nКод товару: '+str(cncode)+'\nВага товару: '+str(weight)+' кг\nВартість товару: '+str(value)+' грн\n-----------------------------------------------------\nВартість гарантії: '+str(float("{0:.2f}".format(int(weight)/1000*0.20*28)))+' грн'
        await message.answer(result)
        await state.finish()
    else:
        await message.answer('❗️Вартість товару має бути цілим числом!!!!!! Очікую на коректну вартість товару...')














#Customs payments calculation process
@dp.callback_query_handler(text_contains="payments_calc")
async def customs_calculator(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('💵 <b>МИТНІ ПЛАТЕЖІ</b>')
    await call.message.answer('❗️Для попереднього розрахунку митних платежів заповніть наступну форму')