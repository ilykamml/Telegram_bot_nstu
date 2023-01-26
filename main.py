'''
Телеграмм бот для студентов НГТУ НЭТИ
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

import telebot
from defs import *
import requests
import json
import datetime
import time
import sqlite3
import os
import re
from bs4 import BeautifulSoup


if __name__ == '__main__':
    # Токен бота
    with open('token.txt', 'r') as f:
        token = f.read()
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_command(message):
        bot.send_message(message.chat.id, 'Привет, я бот для студентов НГТУ НЭТИ')
        info = f'| {message.from_user.first_name} {message.from_user.last_name}   @{message.from_user.username}\n' \
               f'| ID: {message.from_user.id}\n| First message: {datetime.datetime.fromtimestamp(message.date).strftime("%d.%m.%Y %H:%M:%S")}'
        new_one(message.chat.id, info)


    # запуск бота
    bot.polling()