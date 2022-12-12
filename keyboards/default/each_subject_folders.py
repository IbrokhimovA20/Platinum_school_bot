from cgitb import text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

germany  = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Gramm 🇩🇪'),
            KeyboardButton(text='Lesen 🇩🇪'),
            KeyboardButton(text='Horen 🇩🇪'),
        ],
        [
            KeyboardButton(text='Schreiben 🇩🇪'),
            KeyboardButton(text='Wortlatz 🇩🇪'),
        ],
        [
            KeyboardButton(text='Music 🇩🇪'),
            KeyboardButton(text='Film 🇩🇪'),
        ],
        [
        KeyboardButton(text='Назад ⬆️')
        ]
    ],
resize_keyboard=True
)

japanese  = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Темы 🇯🇵'),
            KeyboardButton(text='Слова 🇯🇵'),
            KeyboardButton(text='Чтение 🇯🇵')
        ],
        [
            KeyboardButton(text='Песни 🇯🇵'),
            KeyboardButton(text='Фильмы 🇯🇵'),
        ],
        [
        KeyboardButton(text='Назад ⬆️')
        ]
    ],
resize_keyboard=True
)

england  = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Grammar 🏴󠁧󠁢󠁥󠁮󠁧󠁿'),
            KeyboardButton(text='Reading 🏴󠁧󠁢󠁥󠁮󠁧󠁿'),
            KeyboardButton(text='Listening 🏴󠁧󠁢󠁥󠁮󠁧󠁿')
        ],
        [
            KeyboardButton(text='Writing 🏴󠁧󠁢󠁥󠁮󠁧󠁿'),
            KeyboardButton(text='Vocabulary 🏴󠁧󠁢󠁥󠁮󠁧󠁿'),
        ],
        [
            KeyboardButton(text='Music 🏴󠁧󠁢󠁥󠁮󠁧󠁿'),
            KeyboardButton(text='Film 🏴󠁧󠁢󠁥󠁮󠁧󠁿'),
        ],
        [
        KeyboardButton(text='Назад ⬆️')
        ]
    ],
resize_keyboard=True
)