from telegramAuthBot import dp
from aiogram import types

from telegramAuthBot.api.auth_api import submit_api_token

__all__ = ["dp"]


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Добро пожаловать в SomethinK бота")
    await message.answer("Для подтверждения регистрации отправьте сюда код, полученный на сайте")


@dp.message_handler()
async def all_message(message: types.Message):
    try:
        code = int(message.text)
    except ValueError:
        await message.answer("Некорректный код")
        return
    if not (api_answer := submit_api_token(str(code))):
        await message.answer(
            "Учетная запись подтверждена, теперь Вы можете создать своего первого бота\n\nhttps://somethinkbots.ru")
    else:
        await message.answer(api_answer)
