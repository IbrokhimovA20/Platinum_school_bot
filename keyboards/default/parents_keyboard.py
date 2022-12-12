from cgitb import text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

parents  = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📚 Предметы')
        ],
        [
         KeyboardButton(text='назад')
        ]
    ], 
resize_keyboard=True

)