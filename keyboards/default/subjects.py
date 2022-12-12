from cgitb import text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

center_subjects  = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Math 🧠'),
            KeyboardButton(text='Deutsch 🇩🇪'),
            KeyboardButton(text='日本語 🇯🇵'),
            KeyboardButton(text='English 🏴󠁧󠁢󠁥󠁮󠁧󠁿'), 
        ],
        [
         KeyboardButton(text='🔼'),   
        ]
    ], 
resize_keyboard=True

)