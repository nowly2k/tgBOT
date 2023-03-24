from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

API_TOKEN: str = '5502666138:AAGN1bG1ThT10N-0j0wO-Eb-VLEE7WMltfY'

bot: Bot = Bot(API_TOKEN)
dp: Dispatcher = Dispatcher()


async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь.')

async def process_help_command(message: Message):
    await message.answer('Напиши что нибудь мне, а в ответ я пришлю твое сообщение.')

    
async def process_message(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text='Ошибка')
    
    
dp.message.register(process_start_command, Command(commands=["start"]))
dp.message.register(process_help_command, Command(commands=['help']))
dp.message.register(process_message)

if __name__ == '__main__':
    dp.run_polling(bot)