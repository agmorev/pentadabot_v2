from utils.set_bot_commands import set_default_commands
# import os
# from loader import bot
# from data import config
# import logging


# WEBHOOK_HOST = 'https://pentadabot.herokuapp.com'  # name your app
# WEBHOOK_PATH = '/webhook/'
# WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# WEBAPP_HOST = '127.0.0.0'
# WEBAPP_PORT = '8443'


# async def on_startup(dp):
#     await bot.set_webhook(WEBHOOK_URL)
#     logging.info(dp)


# async def on_shutdown(dp):
#     logging.info(dp)

async def on_startup(dp):
    import filters
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)
    await set_default_commands(dp)

if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
    # executor.start_webhook(dispatcher=dp, webhook_path=WEBHOOK_PATH,
    #               on_startup=on_startup, on_shutdown=on_shutdown,
    #               host=WEBAPP_HOST, port=WEBAPP_PORT,)
