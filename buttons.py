from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def menu_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Добавить данные')
    button2 = KeyboardButton('Изменить данные')
    kb.add(button, button2)
    return kb


def menu_add_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Вес до')
    button2 = KeyboardButton('Вес после')
    back = KeyboardButton('Назад')
    kb.add(back)
    kb.add(button, button2)
    return kb


def menu_update_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Вес до')
    button2 = KeyboardButton('Итого')
    button3 = KeyboardButton('Вес после')
    back = KeyboardButton('Назад')
    kb.add(back)
    kb.add(button, button2, button3)
    return kb
