# промежуточный файл для взаимо импортов
from aiogram import Bot
from aiogram.dispatcher import Dispatcher

TOKEN = 'your token bot telegram'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)