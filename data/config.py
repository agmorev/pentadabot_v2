import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = "1499901925:AAF8IgAQfQNj9zGXFdacpFogNMvdMKqt8Lo"
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
