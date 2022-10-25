
import os
import logging

from aiogram import Bot, Dispatcher, executor, types

from config import TOKEN  
#TOKEN = os.getenv('TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

rules_translite = trans_dict = {'А':'A', 'Б':'B', 'В':'V', 'Г':'G', 'Д':'D', 'Е':'E', 'Ё':'E', 'Ж':'ZH', 'З':'Z', 'И':'I', 'Й':'I', 'К':'К', 'Л':'L', 'М': 'М',
                                'Н':'N', 'О':'O', 'П':'P', 'Р':'R', 'С':'S', 'Т':'T', 'У':'U', 'Ф':'F', 'Х':'KH', 'Ц':'TS', 'Ч':'CH', 'Ш':'SH', 'Щ':'SHCH','Ы':'Y',
                                'Ь':'', 'Ъ':'IE', 'Э':'E', 'Ю':'IU', 'Я':'IA',
                                'а':'a', 'б':'b', 'в':'v', 'г':'g', 'д':'d', 'е':'e', 'ё':'e', 'ж':'zh', 'з':'z', 'и':'i', 'й':'i', 'к':'k', 'л':'l', 'м':'m', 
                                'н':'n', 'о':'o', 'п':'p', 'р':'r', 'с':'s', 'т':'t', 'у':'u', 'ф':'f', 'х':'kh', 'ц':'ts', 'ч':'ch', 'ш':'sh', 'щ':'shch', 'ы':'y',
                                'ъ':'ie', 'ь':'', 'э':'e', 'ю':'iu', 'я':'ia'}


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f"Hello, {user_name}, напиши свои ФИО на кириллице."
    logging.info(f"{user_name=} {user_id=} sent message: {message.text}")
    await message.reply(text)

@dp.message_handler()
async def send_echo(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text_kir = message.text
    text_lat = text_kir
    for let in rules_translite.keys():
        text_lat = text_lat.replace(let, str(rules_translite[let]))
    logging.info(f"{user_name=} {user_id=} sent message: {text_kir} {text_lat}")
    await bot.send_message(user_id, text_lat)
    

if __name__ == '__main__':
    executor.start_polling(dp)

