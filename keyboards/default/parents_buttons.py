from cgitb import text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

univers_2  = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Успеваемость'),
            KeyboardButton(text='Посещаемость')
        ],
        [
         KeyboardButton(text='⬅️'),   
        ]
    ], 
resize_keyboard=True

)