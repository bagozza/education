from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text='Информация')
button_1 = KeyboardButton(text='Рассчитать')
kb.add(button)
kb.add(button_1)
kb_1 = InlineKeyboardMarkup()
button_2 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_3 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_1.add(button_2)
kb_1.add(button_3)


# @dp.message_handler(commands=['start'])
# async def start_message(message):
#     print('Start message')
#     await message.answer('Я бот помогающий твоему здоровью.\n'
#                          'Нажми на эту кнопочку: \n/Calories чтобы все заработало :)')


# @dp.message_handler(commands=['help'])
# async def process_help_command(message):
#     await message.answer("")


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью. ', reply_markup=kb_1)


# @dp.callback_query_handler(text='info')
# async def info(call):
#     await call.message.answer('Информация о боте')
#     await call.answer()


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:')
    await message.answer()


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст: ')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост: ')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес: ')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    try:
        calories = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age']) + 5
        await message.answer(f'Ваша норма калорий - {calories}')
    except ValueError:
        await message.answer('Используй циферки))')
        await state.finish()
    await state.finish()


@dp.message_handler()
async def all_message(message):
    print('Мы получили сообщение! ')
    await message.answer('Нажми на эту кнопочку: \n/start чтобы все заработало :)')


# class UserState(StatesGroup):
#     adress = State()
#
#
# @dp.message_handler(text='заказать'.title())
# async def buy(message):
#     await message.answer('Отправь нам свой адрес, пожалуйста')
#     await UserState.adress.set()
#
#
# @dp.message_handler(state=UserState.adress)
# async def fsm_handler(message, state):
#     await state.update_data(first=message.text)
#     data = await state.get_data()
#     await message.answer('Доставка будет отправлена на %s' % data['first'])
#     await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)