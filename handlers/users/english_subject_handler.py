from aiogram.types import Message
import pandas as pd
from keyboards.inline.subject_levels import *

from loader import dp
from loader import bot

@dp.message_handler(text='Grammar 🏴󠁧󠁢󠁥󠁮󠁧󠁿')
async def handle_subject(message: Message):
    users = pd.read_pickle("users.pickle")
    print(users)
    if len(users[users['id'] == str(message.chat.id)][users['promocode'].notna()]) != 0:
        await message.answer('Wählen Sie Ihr Niveau: ', reply_markup = english_keyboard_gram)
    else:
        await bot.send_message(chat_id = message.chat.id, text = "У вас нет доступа к боту")

@dp.message_handler(text='Reading 🏴󠁧󠁢󠁥󠁮󠁧󠁿')
async def handle_subject(message: Message):
    users = pd.read_pickle("users.pickle")
    print(users)
    if len(users[users['id'] == str(message.chat.id)][users['promocode'].notna()]) != 0:
        await message.answer('Выберите что вам нужно: ', reply_markup = english_keyboard_reading)
    else:
        await bot.send_message(chat_id = message.chat.id, text = "У вас нет доступа к боту")

@dp.message_handler(text='Listening 🏴󠁧󠁢󠁥󠁮󠁧󠁿')
async def handle_subject(message: Message):
    users = pd.read_pickle("users.pickle")
    print(users)
    if len(users[users['id'] == str(message.chat.id)][users['promocode'].notna()]) != 0:
        await message.answer('Выберите что вам нужно: ', reply_markup = english_keyboard_listening)
    else:
        await bot.send_message(chat_id = message.chat.id, text = "У вас нет доступа к боту")

@dp.message_handler(text='Writing 🏴󠁧󠁢󠁥󠁮󠁧󠁿')
async def handle_subject(message: Message):
    users = pd.read_pickle("users.pickle")
    print(users)
    if len(users[users['id'] == str(message.chat.id)][users['promocode'].notna()]) != 0:
        await message.answer('Wählen Sie Ihr Niveau: ', reply_markup = english_keyboard_writing)
    else:
        await bot.send_message(chat_id = message.chat.id, text = "У вас нет доступа к боту")

@dp.message_handler(text='Vocabulary 🏴󠁧󠁢󠁥󠁮󠁧󠁿')
async def handle_subject(message: Message):
    users = pd.read_pickle("users.pickle")
    print(users)
    if len(users[users['id'] == str(message.chat.id)][users['promocode'].notna()]) != 0:
        await message.answer('Выберите что вам нужно: ', reply_markup = english_keyboard_vocabulary)
    else:
        await bot.send_message(chat_id = message.chat.id, text = "У вас нет доступа к боту")

@dp.message_handler(text='Music 🏴󠁧󠁢󠁥󠁮󠁧󠁿')
async def handle_subject(message: Message):
    users = pd.read_pickle("users.pickle")
    print(users)
    if len(users[users['id'] == str(message.chat.id)][users['promocode'].notna()]) != 0:
        await message.answer('Выберите что вам нужно: ', reply_markup = english_keyboard_musik)
    else:
        await bot.send_message(chat_id = message.chat.id, text = "У вас нет доступа к боту")

@dp.message_handler(text='Film 🏴󠁧󠁢󠁥󠁮󠁧󠁿')
async def handle_subject(message: Message):
    users = pd.read_pickle("users.pickle")
    print(users)
    if len(users[users['id'] == str(message.chat.id)][users['promocode'].notna()]) != 0:
        await message.answer('Выберите что вам нужно: ', reply_markup = english_keyboard_film)
    else:
        await bot.send_message(chat_id = message.chat.id, text = "У вас нет доступа к боту")