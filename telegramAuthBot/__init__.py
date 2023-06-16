from aiogram import Bot
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import BaseConfig

storage = MemoryStorage()

bot = Bot(BaseConfig.TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)

from .hendlers.base_hendlers import dp
