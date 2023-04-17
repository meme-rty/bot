from aiogram import Bot, Dispatcher, executor, types
from config import list_anek, list_citati


bot = Bot(token = '5922289974:AAGs0ZYwwjrgc_aawHK_t-if_F8tpiHqtIY')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
    #await потому что мы асинхронно мутим
async def welcome(message: types.Message):
    await message.answer('дарова, бандит')
    await message.answer('/anek и будет тебе счастье(/sovet_day /dice)')


@dp.message_handler(commands=['sovet_day'])
async def frazi(message: types.Message):
     await message.answer(list_citati[0])
     del list_citati[0]

@dp.message_handler(commands=['dice'])
async def cmd_dice(message: types.Message):
    await message.answer_dice()

@dp.message_handler(commands=['anek'])
async def anek(message: types.Message):
    await message.answer(list_anek[0])
    del list_anek[0]

if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)


