from cgitb import text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

take_contact = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Поделиться контактом", request_contact = True)

        ]
    ],
resize_keyboard = True
)