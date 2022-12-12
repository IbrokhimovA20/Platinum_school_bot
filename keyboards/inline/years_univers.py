from audioop import add
from cgitb import text
from gc import callbacks
from unicodedata import category
from unittest.mock import call
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import years_callback

year_wiut = {'2015' : 'wiut_2015',
            '2018' : 'wiut_2018',
            '2019' : 'wiut_2019',
            '2020' : 'wiut_2020'} 

year_iut = {'2019' : 'iut_2019',
            '2020' : 'iut_2020',
            '2021' : 'iut_2021',
            '2022': 'iut_2022'} 

year_amity = {'2019' : 'amity_2019',
            '2020' : 'amity_2020',
            '2021' : 'amity_2021'} 

year_gubkina = {'2017' : 'gubkina_2017',
            '2018' : 'gubkina_2018',
            '2019' : 'gubkina_2019',
            '2020' : 'gubkina_2020',
            '2021' : 'gubkina_2021'} 

year_plehanova = {'2019' : 'plehanova_2019',
            '2020' : 'plehanova_2020',
            '2021' : 'plehanova_2021'} 

year_bmu = {'2019' : 'bmu_2019',
            '2020' : 'bmu_2020',
            '2021' : 'bmu_2021'} 

year_lomonosova = {'2019' : 'lomonosova_2019',
            '2020' : 'lomonosova_2020',
            '2021' : 'lomonosova_2021'} 

year_mifi = {'2019' : 'mifi_2019',
            '2020' : 'mifi_2020',
            '2021' : 'mifi_2021'} 

year_national = {'2019' : 'national_2019',
            '2020' : 'national_2020',
            '2021' : 'national_2021'} 

years_wiut = InlineKeyboardMarkup(row_width=1)
for key, value in year_wiut.items():
    years_wiut.insert(InlineKeyboardButton(text=key, callback_data = years_callback.new(item_name=value)))
years_wiut.insert(InlineKeyboardButton(text='назад', callback_data='nazad_years'))

years_iut = InlineKeyboardMarkup(row_width=1)
for key, value in year_iut.items():
    years_iut.insert(InlineKeyboardButton(text=key, callback_data = years_callback.new(item_name=value)))
years_iut.insert(InlineKeyboardButton(text='назад', callback_data='nazad_years'))

years_amity = InlineKeyboardMarkup(row_width=1)
for key, value in year_amity.items():
    years_amity.insert(InlineKeyboardButton(text=key, callback_data = years_callback.new(item_name=value)))
years_amity.insert(InlineKeyboardButton(text='назад', callback_data='nazad_years'))

years_gubkina = InlineKeyboardMarkup(row_width=1)
for key, value in year_gubkina.items():
    years_gubkina.insert(InlineKeyboardButton(text=key, callback_data = years_callback.new(item_name=value)))
years_gubkina.insert(InlineKeyboardButton(text='назад', callback_data='nazad_years'))

years_plehanova = InlineKeyboardMarkup(row_width=1)
for key, value in year_plehanova.items():
    years_plehanova.insert(InlineKeyboardButton(text=key, callback_data = years_callback.new(item_name=value)))
years_plehanova.insert(InlineKeyboardButton(text='назад', callback_data='nazad_years'))

years_bmu = InlineKeyboardMarkup(row_width=1)
for key, value in year_bmu.items():
    years_bmu.insert(InlineKeyboardButton(text=key, callback_data = years_callback.new(item_name=value)))
years_bmu.insert(InlineKeyboardButton(text='назад', callback_data='nazad_years'))

years_lomonosova = InlineKeyboardMarkup(row_width=1)
for key, value in year_lomonosova.items():
    years_lomonosova.insert(InlineKeyboardButton(text=key, callback_data = years_callback.new(item_name=value)))
years_lomonosova.insert(InlineKeyboardButton(text='назад', callback_data='nazad_years'))

years_mifi = InlineKeyboardMarkup(row_width=1)
for key, value in year_mifi.items():
    years_mifi.insert(InlineKeyboardButton(text=key, callback_data = years_callback.new(item_name=value)))
years_mifi.insert(InlineKeyboardButton(text='назад', callback_data='nazad_years'))

years_national = InlineKeyboardMarkup(row_width=1)
for key, value in year_national.items():
    years_national.insert(InlineKeyboardButton(text=key, callback_data = years_callback.new(item_name=value)))
years_national.insert(InlineKeyboardButton(text='назад', callback_data='nazad_years'))