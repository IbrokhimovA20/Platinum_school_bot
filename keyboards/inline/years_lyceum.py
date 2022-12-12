from audioop import add
from cgitb import text
from gc import callbacks
from unicodedata import category
from unittest.mock import call
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import years_callback

year_wiut_l = {'2015' : 'wiut_l_2015',
            '2018' : 'wiut_l_2018',
            '2019' : 'wiut_l_2019',
            '2021' : 'wiut_l_2021'} 

year_iut_l = {'2019' : 'iut_l_2019',
            '2020' : 'iut_l_2020',
            '2021' : 'iut_l_2021',
            '2022': 'iut_l_2022'} 

year_amity_l = {'2019' : 'amity_l_2019',
            '2020' : 'amity_l_2020',
            '2021' : 'amity_l_2021'} 

year_gubkina_l = {'2017' : 'gubkina_l_2017',
            '2018' : 'gubkina_l_2018',
            '2019' : 'gubkina_l_2019',
            '2020' : 'gubkina_l_2020',
            '2021' : 'gubkina_l_2021'} 

year_plehanova_l = {'2019' : 'plehanova__l2019',
            '2020' : 'plehanova_l_2020',
            '2021' : 'plehanova_l_2021'} 

year_bmu_l = {'2019' : 'bmu_l_2019',
            '2020' : 'bmu_l_2020',
            '2021' : 'bmu_l_2021'} 

year_lomonosova_l = {'2019' : 'lomonosova_l_2019',
            '2020' : 'lomonosova_l_2020',
            '2021' : 'lomonosova_l_2021'} 

year_mifi_l = {'2019' : 'mifi_l_2019',
            '2020' : 'mifi_l_2020',
            '2021' : 'mifi_l_2021'} 

year_national_l = {'2019' : 'national_l_2019',
            '2020' : 'national_l_2020',
            '2021' : 'national_l_2021'} 

years_wiut_l = InlineKeyboardMarkup(row_width=1)
for key, value in year_wiut_l.items():
    years_wiut_l.insert(InlineKeyboardButton(text=key, callback_data = years_callback.new(item_name=value)))
years_wiut_l.insert(InlineKeyboardButton(text='назад', callback_data='nazad_years'))

years_iut_l = InlineKeyboardMarkup(row_width=1)
for key, value in year_iut_l.items():
    years_iut_l.insert(InlineKeyboardButton(text=key, callback_data = years_callback.new(item_name=value)))
years_iut_l.insert(InlineKeyboardButton(text='назад', callback_data='nazad_years'))

years_amity_l = InlineKeyboardMarkup(row_width=1)
for key, value in year_amity_l.items():
    years_amity_l.insert(InlineKeyboardButton(text=key, callback_data = years_callback.new(item_name=value)))
years_amity_l.insert(InlineKeyboardButton(text='назад', callback_data='nazad_years'))

years_gubkina_l = InlineKeyboardMarkup(row_width=1)
for key, value in year_gubkina_l.items():
    years_gubkina_l.insert(InlineKeyboardButton(text=key, callback_data = years_callback.new(item_name=value)))
years_gubkina_l.insert(InlineKeyboardButton(text='назад', callback_data='nazad_years'))

years_plehanova_l = InlineKeyboardMarkup(row_width=1)
for key, value in year_plehanova_l.items():
    years_plehanova_l.insert(InlineKeyboardButton(text=key, callback_data = years_callback.new(item_name=value)))
years_plehanova_l.insert(InlineKeyboardButton(text='назад', callback_data='nazad_years'))

years_bmu_l = InlineKeyboardMarkup(row_width=1)
for key, value in year_bmu_l.items():
    years_bmu_l.insert(InlineKeyboardButton(text=key, callback_data = years_callback.new(item_name=value)))
years_bmu_l.insert(InlineKeyboardButton(text='назад', callback_data='nazad_years'))

years_lomonosova_l = InlineKeyboardMarkup(row_width=1)
for key, value in year_lomonosova_l.items():
    years_lomonosova_l.insert(InlineKeyboardButton(text=key, callback_data = years_callback.new(item_name=value)))
years_lomonosova_l.insert(InlineKeyboardButton(text='назад', callback_data='nazad_years'))

years_mifi_l = InlineKeyboardMarkup(row_width=1)
for key, value in year_mifi_l.items():
    years_mifi_l.insert(InlineKeyboardButton(text=key, callback_data = years_callback.new(item_name=value)))
years_mifi_l.insert(InlineKeyboardButton(text='назад', callback_data='nazad_years'))

years_national_l = InlineKeyboardMarkup(row_width=1)
for key, value in year_national_l.items():
    years_national_l.insert(InlineKeyboardButton(text=key, callback_data = years_callback.new(item_name=value)))
years_national_l.insert(InlineKeyboardButton(text='назад', callback_data='nazad_years'))