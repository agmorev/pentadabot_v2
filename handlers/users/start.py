from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.default import main_menu

import sqlite3
import datetime
# import smtplib


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    
    #Save information about new user to the database
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    full_name = message.from_user.full_name
    date = datetime.datetime.now()
    print(user_id, first_name, last_name, username, full_name, date)
    try:
        #conn = sqlite3.connect('/home/agmorev/pentadabot_v2/data/pentada.db')
        conn = sqlite3.connect('D:\PYTHON\PROJECTS\Bots\pentadabot_v2\data\pentada.db')
        cursor = conn.cursor()
        print("Successfully Connected to SQLite")
        result = [user_id[0] for user_id in cursor.execute("SELECT user_id FROM teleusers;")]
        conn.commit()
        print(result)
        if str(user_id) in result:
            print("User already exists!!!")
        else:
            query2 = "INSERT INTO teleusers ('user_id', 'first_name', 'last_name', 'username', 'full_name', 'date') VALUES (?, ?, ?, ?, ?, ?);"
            variables = (user_id, first_name, last_name, username, full_name, date)
            cursor.execute(query2, variables)
            conn.commit()
            print("Record inserted successfully into teleusers table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("The SQLite connection is closed")
    
    # #Send email about new user
    # gmail_user = 'agmorev@pentada-trans.com'
    # gmail_password = 'Hmi38#296Pw'
    
    # sent_from = gmail_user
    # to = ['agmorev@pentada-trans.com', 'agmorev@gmail.com']
    # subject = 'НОВИЙ КОРИСТУВАЧ в PentadaBot'
    # body = 'В PentadaBot тільки но було зареєстровано нового користувача:\n %s %s %s %s %s %s!!!' % (user_id, first_name, last_name, username, full_name, date)
    # email_text = '''\
    #     Від: %s
    #     До: %s
    #     Тема: %s

    #     %s
    #     ''' % (sent_from, ", ".join(to), subject, body)
    # try:
    #     server = smtplib.SMTP_SSL('mail.pentada-trans.com', 465)
    #     server.login(gmail_user, gmail_password)
    #     server.sendmail(sent_from, to, email_text)
    #     server.quit()
    #     print('Email sent!')
    # except:
    #     print('Something went wrong with sending email....')
    
    #Hello message to user
    await message.answer(f'Вітаємо Вас, {message.from_user.full_name}!', reply_markup=main_menu)
