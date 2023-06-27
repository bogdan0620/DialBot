from aiogram.dispatcher.filters.state import State, StatesGroup


class GetData(StatesGroup):
    add_data = State()
    getting_weight_up_to = State()
    getting_weight_after = State()


class UpdateData(StatesGroup):
    update_data = State()
    update_weight_up_to = State()
    update_weight_after = State()
    update_total = State()
