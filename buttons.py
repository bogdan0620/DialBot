from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def menu_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = KeyboardButton('Добавить данные')
    kb.add(button)
    return kb

def menu2_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = KeyboardButton('Вес до')
    button2 = KeyboardButton('Вес после')
    back = KeyboardButton('Назад')
    kb.add(back)
    kb.add(button, button2,)
    return kb
