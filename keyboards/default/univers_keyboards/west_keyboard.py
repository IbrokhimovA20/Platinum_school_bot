from cgitb import text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

west  = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='WIUT exam samples'),
            KeyboardButton(text='WIUT Lyceum exam samples')
        ],
        [
         KeyboardButton(text='back')
        ]],
resize_keyboard=True

)