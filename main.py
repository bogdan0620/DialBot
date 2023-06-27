from aiogram import Bot, Dispatcher, executor
import buttons, database, datetime
from states import GetData, UpdateData
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardRemove

bot = Bot('6174832494:AAErOfdtHIJ4yZ-g70_NigY1Rh8uaywn7hI')
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def cmd(message):
    await message.answer('Привет', reply_markup=buttons.menu_kb())


@dp.message_handler(lambda message: message.text == 'Добавить данные')
async def add_data(message):
    await message.answer('Выберите', reply_markup=buttons.menu_add_kb())
    await GetData.add_data.set()


@dp.message_handler(content_types=['text'], state=GetData.add_data)
async def menu_add(message, state=GetData.add_data):
    if message.text == 'Назад':
        await message.answer('Выберите действие', reply_markup=buttons.menu_kb())
        await state.finish()
        return

    elif message.text == 'Вес до':
        await message.answer('Введите вес до', reply_markup=ReplyKeyboardRemove())
        await GetData.getting_weight_up_to.set()

    elif message.text == 'Вес после':
        await message.answer('Введите вес после', reply_markup=ReplyKeyboardRemove())
        await GetData.getting_weight_after.set()

    else:
        await message.answer('Выберите действие', reply_markup=buttons.menu_add_kb())
        await GetData.add_data.set()


@dp.message_handler(content_types=['text'], state=GetData.getting_weight_up_to)
async def add_weight_up_to(message, state=GetData.getting_weight_up_to):
    database.add_weight_up_to_db(message.from_user.id, float(message.text.replace(',', '.')), datetime.date.today())
    db = database.checker_db(message.from_user.id, datetime.date.today())
    await state.finish()
    await message.answer('Добавлено', reply_markup=buttons.menu_kb())
    out = ''
    if db:
        for i in db:
            if i[2] == None:
                out += f'{i[0]}\n{round(i[1], 1)}'
            else:
                out += f'{i[0]}\n{round(i[1], 1)}\n{i[2]}'
        await message.answer(out)


@dp.message_handler(content_types=['text'], state=GetData.getting_weight_after)
async def add_weight_after(message, state=GetData.getting_weight_after):
    database.add_weight_after_db(message.from_user.id, float(message.text.replace(',', '.')), datetime.date.today())
    await state.finish()
    await message.answer('Добавлено', reply_markup=buttons.menu_kb())


@dp.message_handler(lambda message: message.text == 'Изменить данные')
async def update_data(message):
    db = database.checker_db(message.from_user.id, datetime.date.today())
    out = ''
    if db == 'Данных пока не достаточно':
        await message.answer('Данных пока не достаточно', reply_markup=buttons.menu_update_kb())

    elif db:
        for i in db:
            if i[2] == None:
                out += f'{i[0]}\n{round(i[1], 1)}'
            else:
                out += f'{i[0]}\n{round(i[1], 1)}\n{i[2]}'
        await message.answer(out)
        await message.answer('Выберите что хотите изменить', reply_markup=buttons.menu_update_kb())
        await UpdateData.update_data.set()


@dp.message_handler(content_types=['text'], state=UpdateData.update_data)
async def menu_update(message, state=UpdateData.update_data):
    if message.text == 'Назад':
        await message.answer('Выберите действие', reply_markup=buttons.menu_kb())
        await state.finish()
        return

    elif message.text == 'Вес до':
        await message.answer('Введите вес до', reply_markup=ReplyKeyboardRemove())
        await UpdateData.update_weight_up_to.set()

    elif message.text == 'Вес после':
        await message.answer('Введите вес после', reply_markup=ReplyKeyboardRemove())
        await UpdateData.update_weight_after.set()

    elif message.text == 'Итого':
        await message.answer('Введите вес итого', reply_markup=ReplyKeyboardRemove())
        await UpdateData.update_total.set()

    else:
        await message.answer('Выберите действие', reply_markup=buttons.menu_update_kb())
        await UpdateData.update_data.set()


@dp.message_handler(content_types=['text'], state=UpdateData.update_weight_up_to)
async def update_weight_up_to(message, state=UpdateData.update_weight_up_to):
    database.add_weight_up_to_db(message.from_user.id, float(message.text.replace(',', '.')), datetime.date.today())
    db = database.checker_db(message.from_user.id, datetime.date.today())
    await state.finish()
    await message.answer('Изменено', reply_markup=buttons.menu_kb())
    out = ''
    if db:
        for i in db:
            if i[2] == None:
                out += f'{i[0]}\n{round(i[1], 1)}'
            else:
                out += f'{i[0]}\n{round(i[1], 1)}\n{i[2]}'
        await message.answer(out)


@dp.message_handler(content_types=['text'], state=UpdateData.update_weight_after)
async def update_weight_after(message, state=UpdateData.update_weight_after):
    db = database.add_weight_after_db(message.from_user.id, float(message.text.replace(',', '.')), datetime.date.today())
    await state.finish()
    await message.answer('Изменено', reply_markup=buttons.menu_kb())
    out = ''
    if db:
        for i in db:
            if i[2] == None:
                out += f'{i[0]}\n{round(i[1], 1)}'
            else:
                out += f'{i[0]}\n{round(i[1], 1)}\n{i[2]}'
        await message.answer(out)


@dp.message_handler(content_types=['text'], state=UpdateData.update_total)
async def update_total(message, state=UpdateData.update_total):
    db = database.checker2_db(message.from_user.id, datetime.date.today(), output=float(message.text.replace(',', '.')))
    await state.finish()
    await message.answer('Изменено', reply_markup=buttons.menu_kb())
    out = ''
    if db:
        for i in db:
            if i[2] == None:
                out += f'{i[0]}\n{round(i[1], 1)}'
            else:
                out += f'{i[0]}\n{round(i[1], 1)}\n{i[2]}'
        await message.answer(out)


@dp.message_handler()
async def nothing(message):
    await message.answer('Выберите действие', reply_markup=buttons.menu_kb())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
