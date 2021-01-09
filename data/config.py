import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = "1173390946:AAFd65-o35punvwx7NXT92HtR_-o5a9aTms"
admins = [
    1061732281
]

ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
