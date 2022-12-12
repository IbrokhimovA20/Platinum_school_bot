from audioop import add
from cgitb import text
from gc import callbacks
from unicodedata import category
from unittest.mock import call
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import themes_callback

from loader import dp

german = {'A 1.1':'A1.1g',
        'A 1.2':'A1.2g',
        'A 2.1':'A2.1g',
        'A 2.2':'A2.2g',
        'B 1':'B1g',
        'B 2':'B2g',
        'C 1':'C1g',
        'C 2':'C2g'}

english = {'A 1':'A1e',
    'A 2':'A2e',
    'B 1':'B1e',
    'B 2':'B2e',
    'C 1':'C1e',
    'C 2':'C2e'}

japan = {'A 1':'A1j',
    'A 2':'A2j',
    'B 1':'B1j',
    'B 2':'B2j',
    'C 1':'C1j',
    'C 2':'C2j'}

nazad_ger = InlineKeyboardButton(text='назад', callback_data='nazad_v_german')
nazad_eng = InlineKeyboardButton(text='назад', callback_data='nazad_v_english')
nazad_jap = InlineKeyboardButton(text='назад', callback_data='nazad_v_japan')

german_keyboard_gram = InlineKeyboardMarkup(row_width=1)
for key, value in german.items():
    german_keyboard_gram.insert(InlineKeyboardButton(text=key, callback_data = themes_callback.new(item_name=f"{value}Gramm")))
german_keyboard_gram.insert(nazad_ger)

german_keyboard_lesen = InlineKeyboardMarkup(row_width=1)
for key, value in german.items():
    german_keyboard_lesen.insert(InlineKeyboardButton(text=key, callback_data = themes_callback.new(item_name=f"{value}lesen")))
german_keyboard_lesen.insert(nazad_ger)

german_keyboard_horen = InlineKeyboardMarkup(row_width=1)
for key, value in german.items():
    german_keyboard_horen.insert(InlineKeyboardButton(text=key, callback_data = themes_callback.new(item_name=f"{value}horen")))
german_keyboard_horen.insert(nazad_ger)

german_keyboard_schreiben = InlineKeyboardMarkup(row_width=1)
for key, value in german.items():
    german_keyboard_schreiben.insert(InlineKeyboardButton(text=key, callback_data = themes_callback.new(item_name=f"{value}schreiben")))
german_keyboard_schreiben.insert(nazad_ger)

german_keyboard_wortlatz = InlineKeyboardMarkup(row_width=1)
for key, value in german.items():
    german_keyboard_wortlatz.insert(InlineKeyboardButton(text=key, callback_data = themes_callback.new(item_name=f"{value}wortlatz")))
german_keyboard_wortlatz.insert(nazad_ger)

german_keyboard_musik = InlineKeyboardMarkup(row_width=1)
for key, value in german.items():
    german_keyboard_musik.insert(InlineKeyboardButton(text=key, callback_data = themes_callback.new(item_name=f"{value}musik")))
german_keyboard_musik.insert(nazad_ger)

german_keyboard_film = InlineKeyboardMarkup(row_width=1)
for key, value in german.items():
    german_keyboard_film.insert(InlineKeyboardButton(text=key, callback_data = themes_callback.new(item_name=f"{value}film")))
german_keyboard_film.insert(nazad_ger)


english_keyboard_gram = InlineKeyboardMarkup(row_width=1)
for key, value in english.items():
    english_keyboard_gram.insert(InlineKeyboardButton(text=key, callback_data = themes_callback.new(item_name=f"{value}grammar")))
english_keyboard_gram.insert(nazad_eng)

english_keyboard_reading = InlineKeyboardMarkup(row_width=1)
for key, value in english.items():
    english_keyboard_reading.insert(InlineKeyboardButton(text=key, callback_data = themes_callback.new(item_name=f"{value}reading")))
english_keyboard_reading.insert(nazad_eng)

english_keyboard_listening = InlineKeyboardMarkup(row_width=1)
for key, value in english.items():
    english_keyboard_listening.insert(InlineKeyboardButton(text=key, callback_data = themes_callback.new(item_name=f"{value}listening")))
english_keyboard_listening.insert(nazad_eng)

english_keyboard_writing = InlineKeyboardMarkup(row_width=1)
for key, value in english.items():
    english_keyboard_writing.insert(InlineKeyboardButton(text=key, callback_data = themes_callback.new(item_name=f"{value}writing")))
english_keyboard_writing.insert(nazad_eng)

english_keyboard_vocabulary = InlineKeyboardMarkup(row_width=1)
for key, value in english.items():
    english_keyboard_vocabulary.insert(InlineKeyboardButton(text=key, callback_data = themes_callback.new(item_name=f"{value}vocabulary")))
english_keyboard_vocabulary.insert(nazad_eng)

english_keyboard_musik = InlineKeyboardMarkup(row_width=1)
for key, value in english.items():
    german_keyboard_musik.insert(InlineKeyboardButton(text=key, callback_data = themes_callback.new(item_name=f"{value}musik")))
german_keyboard_musik.insert(nazad_eng)

english_keyboard_film = InlineKeyboardMarkup(row_width=1)
for key, value in english.items():
    english_keyboard_film.insert(InlineKeyboardButton(text=key, callback_data = themes_callback.new(item_name=f"{value}film")))
english_keyboard_film.insert(nazad_eng)