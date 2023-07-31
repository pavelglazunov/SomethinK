from SomethinKTelegramBot import dp
from SomethinKTelegramBot.forms import AuthForm, SupportForm

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# from SomethinKTelegramBot.api.auth_api import submit_api_token

__all__ = ["dp"]

menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
menu_kb.insert(KeyboardButton("Подтвердить аккаунт"))
menu_kb.insert(KeyboardButton("Обращение в техподдержку"))

cansel_kb = ReplyKeyboardMarkup(resize_keyboard=True)
cansel_kb.insert(KeyboardButton("Отмена"))

# auth_code_state =
storage = MemoryStorage()


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Добро пожаловать в бота SomethinK")
    await message.answer("Выберите необходимое действие", reply_markup=menu_kb)


# @dp.message_handler(state=AuthForm.code)
# async def get_auth_code(message: types.Message, state: FSMContext):
#     if message.text == "Отмена":
#         await message.answer("Подтверждение аккаунта отменено, выберите необходимое действие", reply_markup=menu_kb)
#         await state.finish()
#         return
#     try:
#         code = int(message.text)
#     except ValueError:
#         await message.answer("Некорректный код", reply_markup=cansel_kb)
#         return
#     if not (api_answer := submit_api_token(str(code))):
#         await message.answer(
#             "Учетная запись подтверждена, теперь Вы можете создать своего первого бота\n\nhttps://somethinkbots.ru",
#             reply_markup=menu_kb)
#         await state.finish()
#     else:
#         await message.answer(api_answer, reply_markup=cansel_kb)


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
    # print(message.from_user.id)


@dp.message_handler()
async def all_message(message: types.Message):
    # if message.text == "Подтвердить аккаунт":
    #     await message.answer("Для подтверждения регистрации отправьте сюда код, полученный на сайте",
    #                          reply_markup=cansel_kb)
    #     await AuthForm.code.set()
    if message.text == "Обращение в техподдержку":
        await message.answer("Расскажите о проблеме",
                             reply_markup=cansel_kb)
        await SupportForm.message.set()
