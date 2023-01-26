'''
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
'''

from aiogram import Bot, Dispatcher, executor, types
import logging
from defs import *


if __name__ == '__main__':
    # Токен бота
    with open('token.txt', 'r') as f:
        token = f.read()
    bot = Bot(token=token)
    dp = Dispatcher(bot)

    # Логирование
    logging.basicConfig(level=logging.INFO)

    # Команда /start
    @dp.message_handler(commands=['start'])
    async def start_command(message: types.Message):
        await message.answer('Привет, я бот для студентов НГТУ НЭТИ')
        info = {'first_name': message.from_user.first_name, 'last_name': message.from_user.last_name,
                'username': message.from_user.username, 'id': message.from_user.id,
                'first message': str(message.date)}
        new_one(message.chat.id, info)

    # запуск бота
    executor.start_polling(dp)