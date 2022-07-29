import telebot
from telebot import types
from engine.tool.config import api, is_user, update_hide_mode

from engine.bot.tools import markups as nav
from engine.bot.tools.screenshot import *
from engine.bot.tools.status import get_basic_info
from engine.bot.logs import writer, close_db

import ctypes
import subprocess
import geocoder
import os

bot = telebot.TeleBot(api)


def download(path_file, file_id, filename):
    file_info = bot.get_file(file_id)

    downloaded_file = bot.download_file(file_info.file_path)
    with open(path_file + filename, 'wb') as new_file:
        new_file.write(downloaded_file)


@bot.message_handler(commands=['start'], func=is_user)
def command_start(message: types.Message):
    bot.send_message(message.from_user.id, f"Привет *{message.from_user.first_name}*",
                     parse_mode='Markdown', reply_markup=nav.mainMenu)


@bot.message_handler(commands=['show'], func=is_user)
def command_start(message: types.Message):
    bot.send_message(message.from_user.id, "Будет доступно после перезагрузки")
    update_hide_mode(False)


@bot.message_handler(commands=['hide'], func=is_user)
def command_start(message: types.Message):
    bot.send_message(message.from_user.id, "Будет скрыто после перезагрузки")
    update_hide_mode(True)


@bot.message_handler(commands=['cmd'], func=is_user)
def cmd(message):
    try:
        returned_output = subprocess.check_output(message.text[5:])
        if returned_output == b'':
            bot.send_message(message.chat.id, "Успешно!")
        else:
            bot.send_message(message.chat.id, returned_output.decode("utf-8"))
    except FileNotFoundError:
        bot.send_message(message.chat.id, "Система не может найти указанный файл")
    except OSError:
        bot.send_message(message.chat.id, "Укажите команду после /cmd")
    except subprocess.CalledProcessError as e:
        bot.send_message(message.chat.id, f"command '{e.cmd}' return with error (code {e.returncode}): {e.output}")
    writer(message.date, message.text)


@bot.message_handler(commands=['restart'], func=is_user)
def restart(message):
    bot.send_message(message.chat.id, "Успешно!")
    os.system('shutdown -r -t 0')


@bot.message_handler(commands=['sleep'], func=is_user)
def sleep(message):
    bot.send_message(message.chat.id, "Успешно!")
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


@bot.message_handler(commands=['close'], func=is_user)
def close(message):
    bot.send_message(message.chat.id, "Успешно!")
    os.system('shutdown /p /f')


@bot.message_handler(commands=['/find'], func=is_user)
def find(message):
    g = geocoder.ip("me")
    a = g.latlng
    bot.send_message(message.chat.id, str(a[0]) + ' ' + str(a[1]))


@bot.message_handler(commands=['status'], func=is_user)
def status(message):
    bot.send_message(message.chat.id, get_basic_info())


@bot.message_handler(content_types=['photo', 'document'], func=is_user)
def handle_docs_photo(message):
    path_file = str(os.path.dirname(os.path.realpath(__name__))) + r"\engine\bot\wallpapers"
    if message.document:
        download(path_file, message.document.file_id, r'\wp.jpg')
    else:
        download(path_file, message.photo[-1].file_id, r'\wp.jpg')
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path_file + r'\wp.jpg', 0)
    writer(message.date, "Загружен файл")


@bot.message_handler(func=is_user)
def bot_message(message: types.Message):
    if message.text == "Назад":
        bot.send_message(message.from_user.id, "Главное", reply_markup=nav.mainMenu)
    elif message.text == "📄 Инструкция":
        mess = \
            """
🐦 Бот Симург
    
🕹 /cmd ping google.com - выполнить команду
    
🖌 Отправьте фотографию, чтобы
установить её на рабочий стол
            """

        bot.send_message(message.from_user.id, mess)

    elif message.text == "⚙ Управление":
        bot.send_message(message.from_user.id, "Управление", reply_markup=nav.remoteMenu)
    elif message.text == "📸 Скрин":
        bot.send_document(message.from_user.id, screen())
    elif message.text == "🔎 Найти":
        find(message)
    elif message.text == "ℹ Инфо":
        status(message)
    elif message.text == "🔄 Перезагрузка":
        restart(message)
    elif message.text == "💤 Сон":
        sleep(message)
    elif message.text == "❌ Выключить":
        close(message)
    writer(message.date, message.text)


def app():
    print("Bot run")
    bot.infinity_polling()
    close_db()
