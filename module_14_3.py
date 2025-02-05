from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

api = '7857648084:AAHxQwNbI1Pjg46lW_FP33P9gsa1mCXpy40'
bot = Bot(token= api)
dp = Dispatcher(bot, storage= MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text='Рассчитать')
b2 = KeyboardButton(text='Информация')
b3 = KeyboardButton(text='Купить')
kb.add(b1, b2, b3)

ikb = InlineKeyboardMarkup()
ib1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
ib2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
ikb.add(ib1,ib2)

ikb2 = InlineKeyboardMarkup()
ibp1 = InlineKeyboardButton(text='Product 1', callback_data='product_buying')
ibp2 = InlineKeyboardButton(text='Product 2', callback_data='product_buying')
ibp3 = InlineKeyboardButton(text='Product 3', callback_data='product_buying')
ibp4 = InlineKeyboardButton(text='Product 4', callback_data='product_buying')
ikb2.add(ibp1, ibp2, ibp3, ibp4)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=ikb)

@dp.callback_query_handler(text = 'formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for i in range(1, 5):
        with open(f'img_{i}.png', 'rb') as img:
            await message.answer_photo(img, f'Название: Product{i} | Описание: описание {i} | Цена: {i * 100}')
    else:
        await message.answer('Выберите продукт для покупки:', reply_markup= ikb2)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)

@dp.callback_query_handler(text = 'calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state= UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age']) + 5
    await message.answer(f'Ваша норма калорий: {calories}')
    await state.finish()

@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)