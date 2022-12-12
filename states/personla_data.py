from aiogram.dispatcher.filters.state import StatesGroup, State

class NewUser(StatesGroup):
    fullname = State()
    phoneNum = State()
    parentsNumber = State()
    subject = State()