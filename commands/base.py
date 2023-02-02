# импорты
from aiogram import types

from commands.list_of_commands import command_list


# обработка команды старт
async def start(message: types.Message) -> None:
    # TODO: обработай стейт
    await message.answer('Привет ☺️')


# обработка команды отмены
async def cancel(message: types.Message) -> None:
    # TODO: обработай стейт
    await message.answer('Отмена ↩️')


#обработка команды помощи
async def help_command(message: types.Message) -> types.Message.answer:
    arg = message.get_args()
    if arg:
        for cmd in command_list:
            if cmd[0] == arg:
                return await message.answer(f'/{cmd[0]}: {cmd[1]}\n\n'
                                            f'{cmd[2]}')
        return await message.answer(f'Такой команды нет')
    else:
        return await message.answer(f'Использование: /help <команда>')


# TODO: выключатель
