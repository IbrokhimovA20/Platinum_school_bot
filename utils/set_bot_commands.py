from aiogram import types

async def set_default_command(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand('start', 'Нажмите чтобы бот заработал')
        ]
    )
