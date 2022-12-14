from aiogram.types import Message
import pandas as pd
from keyboards.inline.subject_levels import *

from loader import dp
from loader import bot

@dp.message_handler(text='Gramm 🇩🇪')
async def handle_subject(message: Message):
    users = pd.read_pickle("users.pickle")
    print(users)
    if len(users[users['id'] == str(message.chat.id)][users['promocode'].notna()]) != 0:
        await message.answer('Wählen Sie Ihr Niveau: ', reply_markup = german_keyboard_gram)
    else:
        await bot.send_message(chat_id = message.chat.id, text = "У вас нет доступа к боту")

@dp.message_handler(text='Lesen 🇩🇪')
async def handle_subject(message: Message):
    users = pd.read_pickle("users.pickle")
    print(users)
    if len(users[users['id'] == str(message.chat.id)][users['promocode'].notna()]) != 0:
        await message.answer('Выберите что вам нужно: ', reply_markup = german_keyboard_lesen)
    else:
        await bot.send_message(chat_id = message.chat.id, text = "У вас нет доступа к боту")

@dp.message_handler(text='Horen 🇩🇪')
async def handle_subject(message: Message):
    users = pd.read_pickle("users.pickle")
    print(users)
    if len(users[users['id'] == str(message.chat.id)][users['promocode'].notna()]) != 0:
        await message.answer('Выберите что вам нужно: ', reply_markup = german_keyboard_horen)
    else:
        await bot.send_message(chat_id = message.chat.id, text = "У вас нет доступа к боту")

@dp.message_handler(text='Schreiben 🇩🇪')
async def handle_subject(message: Message):
    users = pd.read_pickle("users.pickle")
    print(users)
    if len(users[users['id'] == str(message.chat.id)][users['promocode'].notna()]) != 0:
        await message.answer('Wählen Sie Ihr Niveau: ', reply_markup = german_keyboard_schreiben)
    else:
        await bot.send_message(chat_id = message.chat.id, text = "У вас нет доступа к боту")

@dp.message_handler(text='Wortlatz 🇩🇪')
async def handle_subject(message: Message):
    users = pd.read_pickle("users.pickle")
    print(users)
    if len(users[users['id'] == str(message.chat.id)][users['promocode'].notna()]) != 0:
        await message.answer('Выберите что вам нужно: ', reply_markup = german_keyboard_wortlatz)
    else:
        await bot.send_message(chat_id = message.chat.id, text = "У вас нет доступа к боту")

@dp.message_handler(text='Music 🇩🇪')
async def handle_subject(message: Message):
    users = pd.read_pickle("users.pickle")
    print(users)
    if len(users[users['id'] == str(message.chat.id)][users['promocode'].notna()]) != 0:
        await message.answer('Выберите что вам нужно: ', reply_markup = german_keyboard_musik)
    else:
        await bot.send_message(chat_id = message.chat.id, text = "У вас нет доступа к боту")

@dp.message_handler(text='Film 🇩🇪')
async def handle_subject(message: Message):
    users = pd.read_pickle("users.pickle")
    print(users)
    if len(users[users['id'] == str(message.chat.id)][users['promocode'].notna()]) != 0:
        await message.answer('Выберите что вам нужно: ', reply_markup = german_keyboard_film)
    else:
        await bot.send_message(chat_id = message.chat.id, text = "У вас нет доступа к боту")