from gettext import dpgettext
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp

from states.personla_data import PersonlaData

@dp.message_handler(Command('anketa'))
async def bot_info(message: types.Message):
    await message.answer('enter name')
    await PersonlaData.fullname.set()

