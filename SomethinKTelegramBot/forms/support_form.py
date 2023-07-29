from aiogram.dispatcher.filters.state import StatesGroup, State


class SupportForm(StatesGroup):
    message = State()
