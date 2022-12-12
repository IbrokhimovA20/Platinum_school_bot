from email.message import Message
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.dispatcher.filters.builtin import ContentTypeFilter
from aiogram.dispatcher.filters import Regexp

from loader import dp

e_mail = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
@dp.message_handler(Regexp(e_mail))
async def emailhandler(msg: types.Message):
    await msg.answer('this is e_mail')