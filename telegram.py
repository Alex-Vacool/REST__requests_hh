import os
from os import *
from os.path import exists

# библиотека для загрузки данных из env
from dotenv import load_dotenv
import telebot

# файл для парсинга данных
from pars_HTML_2 import parce

# метода ищет файл env и переменные из него
load_dotenv()

# достает из файла переменную token
token = getenv('token')
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    text = message.text.split()[1]
    bot.reply_to(message, text[::-1])


@bot.message_handler(commands=['parse'])
def parse_site(message):
    text = message.text.split()[1]
    chat_id = message.chat.id
    q = parce(text)
    for it in q[:20]:
        bot.send_message(chat_id, f'{it[0]} - {it[1]}')


@bot.message_handler(commands=['file'])
def send_file(message):
    chat_id = message.chat.id
    if exists('base.csv'):
        with open('base.csv') as f:
            bot.send_document(chat_id, f)
    else:
        bot.send_message(chat_id, 'Файл не сформирован. Используйте команду /parse для его формирования')


@bot.message_handler(func=lambda m: True)
def echo(message):
    print(message)
    bot.reply_to(message, message.text.upper())


@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    FILE_ID = 'CAADAgADPQMAAsSraAsqUO_V6idDdBYE'
    bot.send_sticker(message.chat.id, FILE_ID)


# Команда администратора
@bot.message_handler(commands=['admin'], func=lambda message: message.from_user.username == '亚历山大')
def admin(message):
    print(message)
    info = os.name
    bot.reply_to(message, info)


@bot.message_handler(commands=['admin2'])
def admin2(message):
    if message.from_user.username == 'DanteOnline':
        info = os.name
        bot.reply_to(message, info)
    else:
        bot.reply_to(message, 'Метод недоступен, нет прав')


@bot.message_handler(commands=['restart'])
def restart_server(message):
    # выполнить команду операционки из python
    os.system('notepad')
    bot.reply_to(message, 'ура!')


bot.infinity_polling()
