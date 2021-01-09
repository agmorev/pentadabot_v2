from aiogram import types
from loader import dp, bot
from aiogram.dispatcher import FSMContext

from states.login import Login
from states.getfile import Getfile
from keyboards.inline.cabinet_markup import cabinet_markup, login_markup, order_markup
import datetime
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ContentType
import re
import sqlite3
import smtplib


user_email=''
user_password=''
user_company=''
user_fullname=''

@dp.message_handler(text="💼 Кабінет")
async def bot_info(message: types.Message):
    await message.answer('⚠️ Особистий кабінет користувача передбачає додаткові можливості для наших клієнтів. Доступ до кабінету відкривається гарантом після укладення договору.')    
    await message.answer('Для доступу в кабінет необхідно натиснути кнопку "Увійти...", ввести адресу електронної пошти користувача та пароль.', reply_markup=login_markup)

@dp.callback_query_handler(text_contains="login")
async def cabinet_login(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await Login.email_state.set()
    await call.message.answer('📧 Введіть email:')
    
@dp.message_handler(state=Login.email_state)
async def answer_email(message: types.Message, state: FSMContext):
    if re.match(r'[\w\.-]+@[\w\.-]+(\.[\w]+)+', message.text):
        user_email = message.text
        await state.update_data(answer1=user_email)
        await message.answer("🔑 Введіть пароль:")
        await Login.next()
    else:
        await message.answer('❗️Введене Вами не відповідає формату адреси електронної пошти!!! Очікую на коректний email...')  

@dp.message_handler(state=Login.password_state)
async def answer_password(message: types.Message, state: FSMContext):
    data = await state.get_data()
    global user_email, user_password
    user_email = data.get("answer1")
    user_password = message.text
    await state.update_data(answer2=user_password)
    
    #Verifying login and password with information from database
    try:
        #conn = sqlite3.connect('/home/agmorev/pentadabot_v2/data/pentada.db')
        conn = sqlite3.connect('D:\PYTHON\PROJECTS\Bots\pentadabot_v2\data\pentada.db')
        cursor = conn.cursor()
        print('-----------------CABINET-------------------')
        print("Cabinet successfully connected to SQLite by | ", user_email,' | ', datetime.datetime.now())
        cursor.execute('SELECT * FROM users WHERE email=? AND password=?;', (user_email, user_password))
        found = cursor.fetchone()
        if found:
            global user_fullname, user_company
            user_fullname = found[3]+' '+found[4]
            user_company = found[5]
            await message.answer('<b>ОСОБИСТИЙ КАБІНЕТ</b>')
            await message.answer("Оберіть необхідну функцію", reply_markup=cabinet_markup)
        else:
            await message.answer('⛔️У доступі до особистого кабінету відмовлено. Введені Вами адреса електронної пошти та/або пароль є некоректними!!!')
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to work with sqlite table users", error)
    finally:
        if (conn):
            conn.close()
            print("The SQLite connection is closed")

    await state.finish()

@dp.callback_query_handler(text_contains="orders")
async def cabinet_orders(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('📑 <b>ЗАЯВКИ</b>')
    await call.message.answer('Оформлення та направлення заявки на видачу фінансової гарантії.', reply_markup=order_markup)

@dp.callback_query_handler(text_contains="order_download")
async def cabinet_order_send(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('📤 <b>ЗАВАНТАЖЕННЯ ЗАЯВКИ</b>')
    await call.message.answer('Заявку буде завантажено в файлі order.xlsx. Ви можете скористатися цим бланком для заповнення і відправити готову заявку через відповідний сервіс Кабінету.')


@dp.callback_query_handler(text_contains="order_send")
async def cabinet_order_send(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await Getfile.load_state.set()
    await call.message.answer('📤 <b>НАПРАВЛЕННЯ ЗАЯВКИ</b>')
    await call.message.answer('Відправлення підготовленої заявки в форматі doc, docx або митної декларації в форматі imfx. Завантажте необхідний файл, використовуючи меню Telegram.')

@dp.message_handler(state=Getfile.load_state, content_types=ContentType.DOCUMENT)
async def load_file(message: types.Message, state: FSMContext):
    await message.document.download()
    order_fileid = message.document.file_id
    order_filename = message.document.file_name
    ext = ('doc', 'docx', 'imfx')
    if order_filename.endswith(ext):
        await state.update_data(answer=order_fileid)    
        await bot.send_message("-400711737", f"‼️ Нова ЗАЯВКА від користувача {user_fullname} ({user_email}) компанії {user_company}")
        await message.forward("-400711737")
        await message.reply(f"Заявку завантажено у файлі {order_filename} та направлено оператору для обробки.")
        await state.finish()      
    else:
        await message.reply('❗️Завантажений Вами файл не відповідає формату doc, docx, imfx!!! Очікую на завантаження коректного файлу...')      
    
@dp.message_handler(state=Getfile.load_state, content_types=ContentType.ANY)
async def load_file(message: types.Message, state: FSMContext):
    await message.reply('❗️Введене Вами не є файлом та/або файл не відповідає формату doc, docx, imfx!!! Очікую на завантаження файлу...')    

@dp.callback_query_handler(text_contains="reports")
async def cabinet_reports(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('📊 <b>ЗВІТИ</b>')
    await call.message.answer('Направлення запитів на отримання звітів про видані клієнту гарантії впродовж зазначеного періоду часу.')

@dp.callback_query_handler(text_contains="requisits")
async def cabinet_requisits(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('🏦 <b>РЕКВІЗИТИ ГАРАНТА</b>')
    await call.message.answer('Основні реквізити ПТ "ПЕНТАДА ТРАНС".')
    requisits_info = "\n".join(
        [
            '<b>ПТ «ПЕНТАДА ТРАНС»</b>',
            '',
            '04080, Україна, м. Київ',
            'вул. Хвойки Вікентія, буд. 21, офіс 360',
            'код ЄДРПОУ 36701373',
            'ІПН 367013726544',
            '',
            'П/Р: UA693808050000000026006586065',
            'БАНК: АТ «Райффайзен Банк Аваль»',
            'МФО: 380805',
            'П/Р: UA043005060000026006001053834',
            'БАНК: АТ «ПЕРШИЙ ІНВЕСТИЦІЙНИЙ БАНК»',
            'МФО: 300506',
            '',
            'тел.: +38 (067) 447 60 66',
            'email: office@pentada-trans.com'
        ]
    )
    await call.message.answer(requisits_info)

@dp.callback_query_handler(text_contains="officials")
async def cabinet_officials(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('👨‍💻 <b>КОНТАКТНІ ОСОБИ</b>')
    await call.message.answer('Контактні особи ПТ "ПЕНТАДА ТРАНС", уповноважені на обмін інформацією та документами з клієнтом.')
    officials_contacts = "\n".join(
        [
            'Морев Олексій Геннадійович, заступник директора',
            '☎️ +380674769791', 
            '📧 agmorev@pentada-trans.com;',
            '',
            'Бабайцева Вероніка Ігорівна, заступник директора',
            '☎️ +380674475467', 
            '📧 bvi@pentada-trans.com;',
            '',
            'Тараненко Світлана Олександрівна, головний бухгалтер',
            '☎️ +380671657517', 
            '📧 fin@pentada-trans.com;',
            '',
            'Кузнецов Андрій Петрович, начальник відділу логістики та гарантування',
            '☎️ +380674769780', 
            '📧 akuznetsov@pentada-trans.com;',
            '',
            'Менеджери з логістики та гарантування (оператори) - 24/7',
            '☎️ +380674476066', 
            '📧 zayavka_gd@pentada-trans.com.'
        ]
    )
    await call.message.answer(officials_contacts)