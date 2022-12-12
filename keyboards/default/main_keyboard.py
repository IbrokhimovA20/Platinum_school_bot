from cgitb import text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu  = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Для учеников🎓')
            ,
        ],
        [KeyboardButton(text='Для родителей👨‍👩‍👦‍👦')
        ],
    ], 
resize_keyboard=True

)