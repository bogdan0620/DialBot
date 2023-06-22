from aiogram.dispatcher.filters.state import State, StatesGroup


class GetData(StatesGroup):
    add_data = State()
    getting_weight_up_to = State()
    getting_weight_after = State()
