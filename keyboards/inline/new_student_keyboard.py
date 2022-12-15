from audioop import add
from cgitb import text
from gc import callbacks
from unicodedata import category
from unittest.mock import call
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import cb

def selecting_subject():
    buttons = [
        InlineKeyboardButton(text='Math', callback_data=cb.new(action="Math")),
        InlineKeyboardButton(text='Japan', callback_data=cb.new(action="Japan")),
        InlineKeyboardButton(text='German', callback_data=cb.new(action="German")),
        InlineKeyboardButton(text='English', callback_data=cb.new(action="English")),
        InlineKeyboardButton(text='Finish', callback_data=cb.new(action="Finish"))
    ]
    selection_subject = InlineKeyboardMarkup(row_width=2)
    selection_subject.add(*buttons)
    return selection_subject