__all__ = ['register_user_commands', 'command_list', 'set_commands']

from aiogram import Dispatcher, Bot, Router
from aiogram.types import BotCommand
from aiogram.filters import Command

from commands.base import start, cancel, help_command
from commands.list_of_commands import command_list


# регистрация хендлеров
def register_user_commands(router: Router):
    router.message.register(start, Command(commands=['start']))
    router.message.register(cancel, Command(commands=['cancel']))
    router.message.register(help_command, Command(commands=['help']))


# регистрация команд
async def set_commands(bot: Bot):
    cmds = []
    for cmd in command_list:
        cmds.append(BotCommand(command=cmd[0], description=cmd[1]))
    await bot.set_my_commands(cmds)
