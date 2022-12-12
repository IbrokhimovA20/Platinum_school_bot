from cgitb import text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

rus_books  = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📑 Предметы'),
        ],
        [
            KeyboardButton(text='Назад ⬆️')
        ]
    ], 
resize_keyboard=True

)