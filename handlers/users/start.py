from distutils.util import change_root
from itertools import count
import sqlite3
from xml.dom.domreg import registered
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import USERS
from keyboards.default.main_keyboard import menu
from keyboards.inline.follow_button import follow_inline_button
from aiogram.types import Message
from keyboards.inline.callback_data import follow_callback
from aiogram.types import CallbackQuery
from data.config import CHANNEL_ID
from keyboards.default.contact_taker import take_contact
import os
import pandas as pd
from data.config import ADMINS

from loader import dp, bot

def check_sub_channel(chat_member):
    if chat_member['status'] != 'left':
        return True
    else: 
        return False

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if os.path.exists("new_users.pickle"):
        users = pd.read_pickle("new_users.pickle")
        if  message.from_user.id in users['id'].values:
            if check_sub_channel(await bot.get_chat_member(chat_id = CHANNEL_ID, user_id = message.chat.id)):
                await bot.send_message(chat_id = message.chat.id, text = f"Здравствуйте уважаемый {message.chat.first_name}, добро пожаловать на бот Platinum School! приятного пользования", reply_markup=menu)
                await message.delete()
            else:
                await message.answer(f"Здравствуйте уважаемый {message.from_user.full_name}, добро пожаловать на бот Platinum School! для того чтобы пользоваться ботом подпишитесь на канал Platinum school", reply_markup=follow_inline_button)
        else:
            await bot.send_message(chat_id = message.chat.id, text = f"Здравствуйте уважаемый {message.chat.first_name}, Поделитесь своим контактом пожалуйста", reply_markup = take_contact)
    else:
        await bot.send_message(chat_id = message.chat.id, text = f"Здравствуйте уважаемый {message.chat.first_name}, Поделитесь своим контактом пожалуйста", reply_markup = take_contact)
        
@dp.callback_query_handler(follow_callback.filter(item_name = 'followed'))
async def chech_following(call: CallbackQuery, callback_data: dict):
    if check_sub_channel(await bot.get_chat_member(chat_id = CHANNEL_ID, user_id = call.from_user.id)):
        await bot.send_message(chat_id = call.from_user.id, text = f"Здравствуйте уважаемый {call.from_user.full_name}, добро пожаловать на бот Platinum school! приятного пользования", reply_markup=menu)
        await call.message.delete()
    else:
        await bot.send_message(chat_id = call.from_user.id,text = f"Здравствуйте уважаемый {call.from_user.full_name}, добро пожаловать на бот Platinum school! для того чтобы пользоваться ботом подпишитесь на канал Platinum school", reply_markup=follow_inline_button)
        await call.message.delete()



    
