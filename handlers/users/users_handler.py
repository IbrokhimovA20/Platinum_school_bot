from cgitb import text
import logging
import re
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.types import CallbackQuery
import pandas as pd
import numpy as np
from data.config import ADMINS
from datetime import datetime,timedelta
import os
from aiogram.types import ContentType
from aiogram import types
from keyboards.default.main_keyboard import menu
from states.personla_data import NewUser
from aiogram.dispatcher import FSMContext
from keyboards.default.registering_new_student import selecting_subject

from loader import dp, bot 

# @dp.message_handler(content_types = ContentType.CONTACT)
# async def save_number(message: types.Contact):
#     if os.path.exists("users.pickle"):
#         users = pd.read_pickle("users.pickle")
#         if message.from_user.id in users['id'].values:
#             await bot.send_message(chat_id = message.chat.id, text = f"Здравствуйте уважаемый {message.chat.first_name}, добро пожаловать на бот Platinum School! приятного пользования", reply_markup=menu)
#             await message.delete()
#         else:
#             users.loc[len(users.index)] = [str(datetime.now().date()), message.from_user.id, message.contact.phone_number, False] 
        
#     else:
#         users_info = {"datetime" : str(datetime.now().date()), "id" : message.from_user.id, "phone_number" : message.contact.phone_number,"parent_number" : None, "bot" : False, "Math" : False, "Japan":False,"German":False, "English":False}
#         users_info = pd.DataFrame(users_info, index=[0])
#         print(users_info)
#         users_info.to_pickle('users.pickle')
#         await bot.send_message(chat_id = message.chat.id, text = f"Здравствуйте уважаемый {message.chat.first_name}, добро пожаловать на бот Platinum School! приятного пользования", reply_markup=menu)
#         await message.delete()


@dp.message_handler(text_contains='platinum', chat_id = ADMINS)
async def check_answers(message: Message):
        await bot.send_message(chat_id = message.chat.id,text = "Введите полное имя пользователя")
        await NewUser.fullname.set()

@dp.message_handler(chat_id = ADMINS, state=NewUser.fullname)
async def check_answers(message: Message, state=FSMContext):
    name = message.text
    await state.update_data(
        {'fullname' : name}
    )
    await bot.send_message(chat_id=message.from_user.id, text="Введите номер телефона пользователя")
    await NewUser.phoneNum.set()

@dp.message_handler(chat_id = ADMINS, state=NewUser.phoneNum)
async def check_answers(message: Message, state=FSMContext):
    num = message.text
    await state.update_data(
        {'phonenum' : num}
    )
    await bot.send_message(chat_id=message.from_user.id, text="Введите номер телефона родителя пользователя")
    await NewUser.parentsNumber.set()


@dp.message_handler(chat_id = ADMINS, state=NewUser.parentsNumber)
async def check_answers(message: Message, state=FSMContext):
    parent_num = message.text
    await state.update_data(
        {'phonenum_parent' : parent_num}
    )
    await bot.send_message(chat_id=message.from_user.id, text="В какой предмет вы бы хотели зарегистрировать", reply_markup=selecting_subject)
    await NewUser.subject.set()

@dp.message_handler(text = "Math",chat_id = ADMINS, state=NewUser.subject)
async def check_answers(message: Message, state=FSMContext):
    subject = message.text
    await state.update_data(
        {'subject' : subject}
    )
    user_datas = await state.get_data()
    name = user_datas.get("fullname")    
    num = user_datas.get("phonenum")
    phonenum_parent = user_datas.get("phonenum_parent")
    subject = user_datas.get("subject")
    if os.path.exists("users.pickle") and os.path.exists("new_users.pickle"):
        users = pd.read_pickle("users.pickle")
        all_users = pd.read_pickle("new_users.pickle")
        if num in list(users['phone_number']):
            if users[users['phone_number'] == num]:
                users['Math'] = np.where(users['phone_number'] == num, True, users['Math'])
        elif num in list(all_users['phone_number']):
            if phonenum_parent in list(all_users['phone_number']):
                id = all_users[all_users['phone_number'] == num]['id'][0]
                parent_id = all_users[all['phone_number'] == phonenum_parent]['id'][0]
                users.loc[len(users.index)] = [name, num,phonenum_parent, id,parent_id, True, False, False, False]

    elif os.path.exists("new_users.pickle"):
        new_users = pd.read_pickle("new_users.pickle")
        if num in list(new_users['phone_number']):
            if phonenum_parent in list(new_users['phone_number']):
                id = new_users[new_users['phone_number'] == num]['id'][0]
                parent_id = new_users[new_users['phone_number'] == phonenum_parent]['id'][0]
                users_info = {"name":name, "phone_number":num,"parent_number":phonenum_parent, "student_id" : id, "parent_id":parent_id, "Math":True, "Japan" : False, "German":False, "English" : False}
            else:
                id = new_users[new_users['phone_number'] == num]['id'][0]
                print(id)
                users_info = {"name":name, "phone_number":num,"parent_number":phonenum_parent, "student_id" : id, "parent_id":None, "Math":True, "Japan" : False, "German":False, "English" : False}
        else:
            users_info = {"name":name, "phone_number":num,"parent_number":None, "student_id" : None, "parent_id":None, "Math":True, "Japan" : False, "German":False, "English" : False}
        users_info = pd.DataFrame(users_info, index=[0])
        print(users_info)
        users_info.to_pickle("users.pickle")

@dp.message_handler(content_types = ContentType.CONTACT)
async def check_answers(message: Message):
    if os.path.exists('new_users.pickle') and os.path.exists("users.pickle"):
        users = pd.read_pickle('users.pickle')
        if message.contact.phone_number in list(users['student_phone_number']):
            users['student_id'] = np.where(users['student_phone_number'] == message.contact.phone_number,message.from_user.id,users['student_id'])
        elif message.contact.phone_number in list(users['parent_phone_number']):
            users['parent_id'] = np.where(users['parent_phone_number'] == message.contact.phone_number,message.from_user.id,users['parent_id'])
        else:
            new_users = pd.read_pickle('new_users.pickle')
            users.loc[len(users.index)] = [message.contact.phone_number, message.from_user.id]
        await bot.send_message(chat_id = message.chat.id, text = f"Здравствуйте уважаемый {message.chat.first_name}, добро пожаловать на бот Platinum School! приятного пользования", reply_markup=menu)
        await message.delete()
    elif os.path.exists("new_users.pickle"):
        users = pd.read_pickle("new_users.pickle")
        users.loc[len(users.index)] = [message.contact.phone_number, message.from_user.id]
        await bot.send_message(chat_id = message.chat.id, text = f"Здравствуйте уважаемый {message.chat.first_name}, добро пожаловать на бот Platinum School! приятного пользования", reply_markup=menu)
        await message.delete()
    else:
        users_info = {"phone_number" : message.contact.phone_number,"id" : message.from_user.id}
        users_info = pd.DataFrame(users_info, index=[0])
        users_info.to_pickle('new_users.pickle')
        await bot.send_message(chat_id = message.chat.id, text = f"Здравствуйте уважаемый {message.chat.first_name}, добро пожаловать на бот Platinum School! приятного пользования", reply_markup=menu)
        await message.delete()