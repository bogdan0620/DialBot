from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def menu_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Добавить данные')
    button2 = KeyboardButton('Изменить данные')
    kb.add(button, button2)
    return kb


def imenu_kb():
    kb = InlineKeyboardMarkup(row_width=2)
    button = InlineKeyboardButton(text='Изменить', callback_data='edit')
    kb.add(button)
    return kb


def imenu_add_kb():
    kb = InlineKeyboardMarkup(row_width=2)
    button = InlineKeyboardButton('Вес до', callback_data='weight_up_to')
    button2 = InlineKeyboardButton('Вес после', callback_data='weight_after')
    back = InlineKeyboardButton('Назад', callback_data='back')
    kb.add(button, button2)
    kb.add(back)
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
