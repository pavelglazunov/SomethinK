from SomethinKTelegramBot import dp, bot
from SomethinKTelegramBot.forms import SupportForm

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage

__all__ = ["dp"]

menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
# menu_kb.insert(KeyboardButton("Подтвердить аккаунт"))
menu_kb.insert(KeyboardButton("Обращение в техподдержку"))

cansel_kb = ReplyKeyboardMarkup(resize_keyboard=True)
cansel_kb.insert(KeyboardButton("Отмена"))

storage = MemoryStorage()


# async def send_letter_of_happiness():
#     await bot.send_message(1163900032, "Новый пользователь на сайте (ノ^∇^)")


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Добро пожаловать в бота SomethinK")
    await message.answer("Выберите необходимое действие", reply_markup=menu_kb)


@dp.message_handler(state=SupportForm.message)
async def get_support_message(message: types.Message, state: FSMContext):
    if message.text == "Отмена":
        await message.answer("Обращение отменено, выберите необходимое действие", reply_markup=menu_kb)
        await state.finish()
        return

    message_for_admin = "Новое обращение:\n\n"
    message_for_admin += message.text + "\n\n"
    message_for_admin += "Получено от: " + message.from_user.mention + f" ({message.from_user.id}) " + message.from_user.url
    await message.bot.send_message(1163900032, message_for_admin)
    await message.answer("Спасибо за обратную связь!")


@dp.message_handler()
async def all_message(message: types.Message):
    if message.text == "Обращение в техподдержку":
        await message.answer("Расскажите о проблеме",
                             reply_markup=cansel_kb)
        await SupportForm.message.set()
