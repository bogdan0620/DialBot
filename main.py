from aiogram import Bot, Dispatcher, executor
import buttons
import database
import datetime
from states import GetData
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot('6174832494:AAErOfdtHIJ4yZ-g70_NigY1Rh8uaywn7hI')
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def cmd(message):
    await message.answer('Привет', reply_markup=buttons.menu_kb())


@dp.message_handler(lambda message: message.text == 'Добавить данные')
async def add_data(message):
    await message.answer('Выберите', reply_markup=buttons.menu2_kb())
    await GetData.add_data.set()

@dp.message_handler(content_types=['text'], state=GetData.add_data)
async def menu2(message, state=GetData.add_data):
    if message.text == 'Назад':
        await message.answer('Выберите действие', reply_markup=buttons.menu_kb())
        await state.finish()
        return

    elif message.text == 'Вес до':
        await message.answer('Введите вес до')
        await GetData.getting_weight_up_to.set()

    elif message.text == 'Вес после':
        await message.answer('Введите вес после')
        await GetData.getting_weight_after.set()

    else:
        await message.answer('Выберите действие', reply_markup=buttons.menu2_kb())
        await GetData.add_data.set()


@dp.message_handler(content_types=['text'], state=GetData.getting_weight_up_to)
async def add_weight_up_to(message, state=GetData.getting_weight_up_to):
    database.add_weight_up_to_db(message.from_user.id, message.text, datetime.date.today())
    await state.finish()
    await message.answer('Добавлено', reply_markup=buttons.menu_kb())


@dp.message_handler(content_types=['text'], state=GetData.getting_weight_after)
async def add_weight_up_to(message, state=GetData.getting_weight_after):
    database.add_weight_after_db(message.from_user.id, message.text, datetime.date.today())
    await state.finish()
    await message.answer('Добавлено', reply_markup=buttons.menu_kb())

@dp.message_handler()
async def nothing(message):
    await message.answer('Выберите действие', reply_markup=buttons.menu_kb())





if __name__ == '__main__':
    executor.start_polling(dp)
