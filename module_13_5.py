from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.dispatcher import FSMContext
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
# kb = ReplyKeyboardMarkup(resize_keyboard=True)
# button = KeyboardButton(text='Информация')
# button_1 = KeyboardButton(text='Рассчитать')
# kb.add(button)
# kb.add(button_1)

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Информация'),
         KeyboardButton(text='Рассчитать')
         ]
    ], resize_keyboard=True
)


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
    await message.answer('Привет! Я бот помогающий твоему здоровью. ', reply_markup=start_menu)


@dp.message_handler(text='Информация')
async def inform(message):
    await message.answer('Информация о боте')


@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст: ')
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
    await message.answer('Введите команду /start чтобы начать общение.')


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

