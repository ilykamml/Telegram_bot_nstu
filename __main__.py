"""
Телеграмм бот на библиотеке aiogram для студентов НГТУ НЭТИ
Главные возможности:
TODO: 1. добавление в общий чат группы
TODO: 2. расписание занятий
TODO: 3. расписание экзаменов
TODO: 4. расписание преподавателей
TODO: 5. расписание аудиторий
TODO: 6. новости НГТУ НЭТИ
TODO: 7. работа с домашними заданиями
TODO: 7.1. добавление домашнего задания
TODO: 7.2. уведомление о домашнем задании за установленное время до пары
"""

import asyncio
import os
import logging

from aiogram import Bot, Dispatcher

from aiogram.types import BotCommand

from commands import *

# логгирование
logger = logging.getLogger(__name__)

# хэндлеры и форматирование
log_file_handler = logging.FileHandler(f'bot.log', 'w')
log_console_handler = logging.StreamHandler()
log_formatter = logging.Formatter(f'%(levelname)s: %(asctime)s - %(name)s - %(message)s')

# назначение хэндлеров
log_file_handler.setFormatter(log_formatter)
log_console_handler.setFormatter(log_formatter)
logging.basicConfig(handlers=[log_file_handler, log_console_handler],
                    level=logging.INFO)


# супер-мега главная функция
async def main() -> None:
    # логгирование
    logger.info('Starting bot')

    # инициализация бота
    bot = Bot(token=os.getenv('token'))
    dp = Dispatcher()

    register_user_commands(dp)

    # регистрация комманд
    await set_commands(bot)

    logger.info(f'Bot started')

    # пуллинг
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
