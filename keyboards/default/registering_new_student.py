from cgitb import text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

selecting_subject  = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Math'),
            KeyboardButton(text='English'),
            KeyboardButton(text='Japan'),
            KeyboardButton(text='German'),
        ],
        [
            KeyboardButton(text='Назад'),
        ]
    ], 
resize_keyboard=True

)