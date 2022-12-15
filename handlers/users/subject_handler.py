from cgitb import text
import logging
from xml.dom.minidom import Document
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message
from keyboards.inline.follow_button import jmath_bot_button
from keyboards.default.each_subject_folders import *
import pandas as pd
from aiogram.types import CallbackQuery

from loader import dp
from loader import bot

@dp.message_handler(text='Math 🧠')
async def handle_subject(message: Message):
    users = pd.read_pickle("users.pickle")
    if users[users['student_id'] ==message.from_user.id]['Math'][0]:
        await message.answer('По приведенной ниже ссылке вы можете перейти на бот J.M.ath', reply_markup = jmath_bot_button)
    else:
        await bot.send_message(chat_id = message.chat.id, text = "У вас нет доступа к боту")

@dp.message_handler(text='Deutsch 🇩🇪')
async def handle_subject(message: Message):
    users = pd.read_pickle("users.pickle")
    if users[users['student_id'] == message.from_user.id]['German'][0]:
        await message.answer('Выберите что вам нужно: ', reply_markup = germany)
    else:
        await bot.send_message(chat_id = message.chat.id, text = "У вас нет доступа к боту")

@dp.message_handler(text='日本語 🇯🇵')
async def handle_subject(message: Message):
    users = pd.read_pickle("users.pickle")
    if users[users['student_id'] ==message.from_user.id]['Japan'][0]:
        await message.answer('Выберите что вам нужно: ', reply_markup = japanese)
    else:
        await bot.send_message(chat_id = message.chat.id, text = "У вас нет доступа к боту")

@dp.message_handler(text='English 🏴󠁧󠁢󠁥󠁮󠁧󠁿')
async def handle_subject(message: Message):
    users = pd.read_pickle("users.pickle")
    if users[users['student_id'] ==message.from_user.id]['English'][0]:
        await message.answer('Выберите что вам нужно: ', reply_markup = england)
    else:
        await bot.send_message(chat_id = message.chat.id, text = "У вас нет доступа к боту")

