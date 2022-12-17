from cgitb import text
import logging
import re
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.types import CallbackQuery
import pandas as pd
import numpy as np
from data.config import ADMINS
import os
from aiogram.types import ContentType
from aiogram import types
from keyboards.default.main_keyboard import menu
from states.personla_data import NewUser
from aiogram.dispatcher import FSMContext
from keyboards.inline.callback_data import *
from keyboards.inline.new_student_keyboard import selecting_subject
from loader import dp, bot 
from aiogram.utils.exceptions import MessageNotModified

@dp.message_handler(text='platinum', chat_id = ADMINS)
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
    await bot.send_message(chat_id=message.from_user.id, text="В какой предмет вы бы хотели зарегистрировать", reply_markup=selecting_subject())
    await NewUser.subject.set()

@dp.callback_query_handler(cb.filter(action=['Math', 'Japan', 'German', 'English']), chat_id = ADMINS, state=NewUser.subject)
async def check_answers(call: CallbackQuery, callback_data : dict,state=FSMContext):
    action = callback_data.get('action')
    if action == "Math":
        user_datas = await state.get_data()
        name = user_datas.get("fullname")    
        num = user_datas.get("phonenum")
        phonenum_parent = user_datas.get("phonenum_parent")
        if os.path.exists("users.pickle") and os.path.exists("new_users.pickle"):
            users = pd.read_pickle("users.pickle")
            all_users = pd.read_pickle("new_users.pickle")
            if num in list(users['phone_number']):
                users['Math'] = np.where(users['phone_number'] == num, True, users['Math'])
            elif num in list(all_users['phone_number']):
                if phonenum_parent in list(all_users['phone_number']):
                    id = all_users[all_users['phone_number'] == num]['id'][0]
                    parent_id = all_users[all['phone_number'] == phonenum_parent]['id'][0]
                    users.loc[len(users.index)] = [name, num,phonenum_parent, id,parent_id, True, False, False, False]
                    users.to_pickle("users.pickle")
                else:
                    id = all_users[all_users['phone_number'] == num]['id'][0]
                    users.loc[len(users.index)] = [name, num,None, id,parent_id, False, False, True, False]
                    users.to_pickle("users.pickle")

        elif os.path.exists("new_users.pickle"):
            new_users = pd.read_pickle("new_users.pickle")
            if num in list(new_users['phone_number']):
                if phonenum_parent in list(new_users['phone_number']):
                    id = new_users[new_users['phone_number'] == num]['id'][0]
                    parent_id = new_users[new_users['phone_number'] == phonenum_parent]['id'][0]
                    users_info = {"name":name, "phone_number":num,"parent_number":phonenum_parent, "student_id" : id, "parent_id":parent_id, "Math":True, "Japan" : False, "German":False, "English" : False}
                    users_info = pd.DataFrame(users_info, index=[0])
                    users_info.to_pickle("users.pickle")
                else:
                    id = new_users[new_users['phone_number'] == num]['id'][0]
                    users_info = {"name":name, "phone_number":num,"parent_number":phonenum_parent, "student_id" : id, "parent_id":None, "Math":True, "Japan" : False, "German":False, "English" : False}
                    users_info = pd.DataFrame(users_info, index=[0])
                    users_info.to_pickle("users.pickle")
        else:
            users_info = {"name":name, "phone_number":num,"parent_number":None, "student_id" : None, "parent_id":None, "Math":True, "Japan" : False, "German":False, "English" : False}
            users_info = pd.DataFrame(users_info, index=[0])
            users_info.to_pickle("users.pickle")
        await call.answer()
    
    if action == "German":
        user_datas = await state.get_data()
        name = user_datas.get("fullname")    
        num = user_datas.get("phonenum")
        phonenum_parent = user_datas.get("phonenum_parent")
        if os.path.exists("users.pickle") and os.path.exists("new_users.pickle"):
            users = pd.read_pickle("users.pickle")
            all_users = pd.read_pickle("new_users.pickle")
            if num in list(users['phone_number']):
                users['German'] = np.where(users['phone_number'] == num, True, users['German'])
                users.to_pickle('users.pickle')
            elif num in list(all_users['phone_number']):
                if phonenum_parent in list(all_users['phone_number']):
                    id = all_users[all_users['phone_number'] == num]['id'][0]
                    parent_id = all_users[all['phone_number'] == phonenum_parent]['id'][0]
                    users.loc[len(users.index)] = [name, num,phonenum_parent, id,parent_id, False, False, True, False]
                    users.to_pickle("users.pickle")
                else:
                    id = all_users[all_users['phone_number'] == num]['id'][0]
                    users.loc[len(users.index)] = [name, num,None, id,parent_id, False, False, True, False]
                    users.to_pickle("users.pickle")

        elif os.path.exists("new_users.pickle"):
            new_users = pd.read_pickle("new_users.pickle")
            if num in list(new_users['phone_number']):
                if phonenum_parent in list(new_users['phone_number']):
                    id = new_users[new_users['phone_number'] == num]['id'][0]
                    parent_id = new_users[new_users['phone_number'] == phonenum_parent]['id'][0]
                    users_info = {"name":name, "phone_number":num,"parent_number":phonenum_parent, "student_id" : id, "parent_id":parent_id, "Math":False, "Japan" : False, "German":True, "English" : False}
                    users_info = pd.DataFrame(users_info, index=[0])
                    users_info.to_pickle("users.pickle")
                else:
                    id = new_users[new_users['phone_number'] == num]['id'][0]
                    users_info = {"name":name, "phone_number":num,"parent_number":phonenum_parent, "student_id" : id, "parent_id":None, "Math":False, "Japan" : False, "German":True, "English" : False}
                    users_info = pd.DataFrame(users_info, index=[0])
                    users_info.to_pickle("users.pickle")
        else:
            users_info = {"name":name, "phone_number":num,"parent_number":None, "student_id" : None, "parent_id":None, "Math":False, "Japan" : False, "German":True, "English" : False}
            users_info = pd.DataFrame(users_info, index=[0])
            users_info.to_pickle("users.pickle")
        await call.answer()

    if action == "Japan":
        user_datas = await state.get_data()
        name = user_datas.get("fullname")    
        num = user_datas.get("phonenum")
        phonenum_parent = user_datas.get("phonenum_parent")
        if os.path.exists("users.pickle") and os.path.exists("new_users.pickle"):
            users = pd.read_pickle("users.pickle")
            all_users = pd.read_pickle("new_users.pickle")
            if num in list(users['phone_number']):
                users['Japan'] = np.where(users['phone_number'] == num, True, users['Japan'])
                users.to_pickle('users.pickle')
            elif num in list(all_users['phone_number']):
                if phonenum_parent in list(all_users['phone_number']):
                    id = all_users[all_users['phone_number'] == num]['id'][0]
                    parent_id = all_users[all['phone_number'] == phonenum_parent]['id'][0]
                    users.loc[len(users.index)] = [name, num,phonenum_parent, id,parent_id, False, True, False, False]
                    users.to_pickle("users.pickle")
                else:
                    id = all_users[all_users['phone_number'] == num]['id'][0]
                    users.loc[len(users.index)] = [name, num,None, id,parent_id, False, True, False, False]
                    users.to_pickle("users.pickle")

        elif os.path.exists("new_users.pickle"):
            new_users = pd.read_pickle("new_users.pickle")
            if num in list(new_users['phone_number']):
                if phonenum_parent in list(new_users['phone_number']):
                    id = new_users[new_users['phone_number'] == num]['id'][0]
                    parent_id = new_users[new_users['phone_number'] == phonenum_parent]['id'][0]
                    users_info = {"name":name, "phone_number":num,"parent_number":phonenum_parent, "student_id" : id, "parent_id":parent_id, "Math":False, "Japan" : True, "German":False, "English" : False}
                    users_info = pd.DataFrame(users_info, index=[0])
                    users_info.to_pickle("users.pickle")
                else:
                    id = new_users[new_users['phone_number'] == num]['id'][0]
                    users_info = {"name":name, "phone_number":num,"parent_number":phonenum_parent, "student_id" : id, "parent_id":None, "Math":False, "Japan" : True, "German":False, "English" : False}
                    users_info = pd.DataFrame(users_info, index=[0])
                    users_info.to_pickle("users.pickle")
        else:
            users_info = {"name":name, "phone_number":num,"parent_number":None, "student_id" : None, "parent_id":None, "Math":False, "Japan" : True, "German":False, "English" : False}
            users_info = pd.DataFrame(users_info, index=[0])
            users_info.to_pickle("users.pickle")
        await call.answer()
    
    if action == "English":
        user_datas = await state.get_data()
        name = user_datas.get("fullname")    
        num = user_datas.get("phonenum")
        phonenum_parent = user_datas.get("phonenum_parent")
        if os.path.exists("users.pickle") and os.path.exists("new_users.pickle"):
            users = pd.read_pickle("users.pickle")
            all_users = pd.read_pickle("new_users.pickle")
            if num in list(users['phone_number']):
                users['English'] = np.where(users['phone_number'] == num, True, users['English'])
                users.to_pickle('users.pickle')
            elif num in list(all_users['phone_number']):
                if phonenum_parent in list(all_users['phone_number']):
                    id = all_users[all_users['phone_number'] == num]['id'][0]
                    parent_id = all_users[all['phone_number'] == phonenum_parent]['id'][0]
                    users.loc[len(users.index)] = [name, num,phonenum_parent, id,parent_id, False, False, False, True]
                    users.to_pickle('users.pickle')
                else:
                    id = all_users[all_users['phone_number'] == num]['id'][0]
                    users.loc[len(users.index)] = [name, num,None, id,parent_id, False, False, False, True]
                    users.to_pickle("users.pickle")

        elif os.path.exists("new_users.pickle"):
            new_users = pd.read_pickle("new_users.pickle")
            if num in list(new_users['phone_number']):
                if phonenum_parent in list(new_users['phone_number']):
                    id = new_users[new_users['phone_number'] == num]['id'][0]
                    parent_id = new_users[new_users['phone_number'] == phonenum_parent]['id'][0]
                    users_info = {"name":name, "phone_number":num,"parent_number":phonenum_parent, "student_id" : id, "parent_id":parent_id, "Math":False, "Japan" : False, "German":False, "English" : True}
                    users_info = pd.DataFrame(users_info, index=[0])
                    users_info.to_pickle('users.pickle')
                else:
                    id = new_users[new_users['phone_number'] == num]['id'][0]
                    users_info = {"name":name, "phone_number":num,"parent_number":phonenum_parent, "student_id" : id, "parent_id":None, "Math":False, "Japan" : False, "German":False, "English" : True}
                    users_info = pd.DataFrame(users_info, index=[0])
                    users.to_pickle('users.pickle')
        # elif os.path.exists("users.pickle"):
        #     users = pd.read_pickle("users.pickle")

        else:
            users_info = {"name":name, "phone_number":num,"parent_number":None, "student_id" : None, "parent_id":None, "Math":False, "Japan" : False, "German":False, "English" : True}
            users_info = pd.DataFrame(users_info, index=[0])
            users_info.to_pickle("users.pickle")
        await call.answer()

@dp.message_handler(content_types = ContentType.CONTACT)
async def check_answers(message: Message):
    if os.path.exists('new_users.pickle') and os.path.exists("users.pickle"):
        users = pd.read_pickle('users.pickle')
        if message.contact.phone_number in list(users['phone_number']):
            users['student_id'] = np.where(users['phone_number'] == message.contact.phone_number,message.from_user.id,users['student_id'])
            users.to_pickle('users.pickle')
        elif message.contact.phone_number in list(users['parent_number']):
            users['parent_id'] = np.where(users['parent_number'] == message.contact.phone_number,message.from_user.id,users['parent_id'])
            users.to_pickle('users.pickle')
        else:
            new_users = pd.read_pickle('new_users.pickle')
            new_users.loc[len(users.index)] = [message.contact.phone_number, message.from_user.id]
        await bot.send_message(chat_id = message.chat.id, text = f"Здравствуйте уважаемый {message.chat.first_name}, добро пожаловать на бот Platinum School! приятного пользования", reply_markup=menu)
        await message.delete()
    elif os.path.exists("new_users.pickle"):
        users = pd.read_pickle("new_users.pickle")
        users.loc[len(users.index)] = [message.contact.phone_number, message.from_user.id]
        await bot.send_message(chat_id = message.chat.id, text = f"Здравствуйте уважаемый {message.chat.first_name}, добро пожаловать на бот Platinum School! приятного пользования", reply_markup=menu)
        await message.delete()
    elif os.path.exists("users.pickle"):
        users = pd.read_pickle("users.pickle")
        users_info = {"phone_number" : message.contact.phone_number,"id" : message.from_user.id}
        users_info = pd.DataFrame(users_info, index=[0])
        users_info.to_pickle('new_users.pickle')
        print(users)
        if message.contact.phone_number in list(users['phone_number']):
            users['student_id'] = np.where(users['phone_number'] == message.contact.phone_number,message.from_user.id,users['student_id'])
            users.to_pickle('users.pickle')
        elif message.contact.phone_number in list(users['parent_number']):
            users['parent_id'] = np.where(users['parent_number'] == message.contact.phone_number,message.from_user.id,users['parent_id'])
            users.to_pickle('users.pickle')
        await bot.send_message(chat_id = message.chat.id, text = f"Здравствуйте уважаемый {message.chat.first_name}, добро пожаловать на бот Platinum School! приятного пользования", reply_markup=menu)
        await message.delete()
    else:
        users_info = {"phone_number" : message.contact.phone_number,"id" : message.from_user.id}
        users_info = pd.DataFrame(users_info, index=[0])
        users_info.to_pickle('new_users.pickle')
        await bot.send_message(chat_id = message.chat.id, text = f"Здравствуйте уважаемый {message.chat.first_name}, добро пожаловать на бот Platinum School! приятного пользования", reply_markup=menu)
        await message.delete()

@dp.callback_query_handler(cb.filter(action=['Finish']), chat_id = ADMINS, state=NewUser.subject)
async def check_answers(call: CallbackQuery, callback_data : dict,state=FSMContext):
    await bot.edit_message_reply_markup(
                    chat_id=call.message.chat.id,
                    message_id=call.message.message_id, 
                    reply_markup=None
                )
    await call.answer()
    await state.reset_state()
    await bot.send_message(chat_id=call.message.chat.id, text="saved")