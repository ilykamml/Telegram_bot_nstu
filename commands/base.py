# импорты
from aiogram import types
from aiogram.filters import CommandObject

import logging

from commands.list_of_commands import command_list


# обработка команды старт
async def start(message: types.Message) -> None:
    # TODO: обработай стейт
    logging.info(f'Get a new start from @{message.from_user.username} | {message.from_user.id}')
    await message.answer('Привет ☺️')


# обработка команды отмены
async def cancel(message: types.Message) -> None:
    # TODO: обработай стейт
    logging.info(f'Get a cancel from @{message.from_user.username} | {message.from_user.id}')
    await message.answer('Отмена ↩️')


# обработка команды помощи
async def help_command(message: types.Message, command: CommandObject) -> types.Message.answer:
    if command.args:
        for cmd in command_list:
            if cmd[0] == command.args:
                return await message.answer(f'/{cmd[0]}: {cmd[1]}\n\n'
                                            f'{cmd[2]}')
        return await message.answer(f'Такой команды нет')
    else:
        return await message.answer(f'Использование: /help <команда>')


# TODO: выключатель
