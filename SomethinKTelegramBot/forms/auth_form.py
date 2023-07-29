from aiogram.dispatcher.filters.state import StatesGroup, State


class AuthForm(StatesGroup):
    code = State()
