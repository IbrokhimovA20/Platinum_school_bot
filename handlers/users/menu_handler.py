from cgitb import text
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentType
import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.main_keyboard import menu
from keyboards.inline.callback_data import themes_callback
from keyboards.default.subjects import center_subjects
from keyboards.default.parents_keyboard import parents
from keyboards.default.students_keyboard import rus_books
from keyboards.inline.follow_button import follow_inline_button

from aiogram.types import CallbackQuery
from data.config import ADMINS,USERS
from data.config import CHANNEL_ID

from loader import dp, bot

def check_sub_channel(chat_member):
    if chat_member['status'] != 'left':
        return True
    else: 
        return False

@dp.message_handler(content_types=['file'], chat_id = USERS)
async def see_what(message:Message):
    print(message)

@dp.message_handler(content_types=ContentType.DOCUMENT, chat_id = ADMINS)
async def download(message: Message):
    # print(message)
    print(message.document.file_name[:-4])
    doc_id = message.document.file_id
    # await bot.send_message(chat_id = message.chat.id,text = f"{doc_id}")


@dp.message_handler(text='Для родителей👨‍👩‍👦‍👦')
async def send_libray(message: Message):
    if check_sub_channel(await bot.get_chat_member(chat_id = CHANNEL_ID, user_id = message.chat.id)):
        await message.answer("Choose", reply_markup=parents)
    else:
        await bot.send_message(chat_id = message.chat.id,text = f"Здравствуйте уважаемый {message.chat.first_name}, добро пожаловать на бот Platinum school! для того чтобы пользоваться ботом подпишитесь на канал J.M.ath", reply_markup=follow_inline_button)
        await message.delete()

@dp.message_handler(text='Назад ⬆️')
async def send_lesson(message: Message):
    await message.answer('Выберите предмет: ', reply_markup = center_subjects)

@dp.message_handler(text='🔼')
async def send_lesson(message: Message):
    await message.answer("Выберите ", reply_markup=menu)

@dp.message_handler(text='Для учеников🎓')
async def select_class(message: Message):
    if check_sub_channel(await bot.get_chat_member(chat_id = CHANNEL_ID, user_id = message.chat.id)):
        await message.answer('Выберите предмет: ', reply_markup = center_subjects)
    else:
        await bot.send_message(chat_id = message.chat.id,text = f"Здравствуйте уважаемый {message.chat.first_name}, добро пожаловать на бот Platinum school! для того чтобы пользоваться ботом подпишитесь на канал J.M.ath", reply_markup=follow_inline_button)
        await message.delete()