__all__ = ['register_user_commands', 'command_list', 'set_commands']

from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand

from commands.base import start, cancel, help_command
from commands.list_of_commands import command_list


# регистрация хендлеров
def register_user_commands(dp: Dispatcher):
    dp.register_message_handler(start, commands='start', state='*')
    dp.register_message_handler(cancel, commands='cancel', state='*')
    dp.register_message_handler(help_command, commands='help', state='*')


# регистрация команд
async def set_commands(bot: Bot):
    cmds = []
    for cmd in command_list:
        cmds.append(BotCommand(cmd[0], cmd[1]))
    await bot.set_my_commands(cmds)
