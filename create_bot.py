from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from config import token_Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token=token_Bot)
dp = Dispatcher(bot, storage=storage)
