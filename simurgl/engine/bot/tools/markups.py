from telebot.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton("Назад")

# --- Main Menu ---
manual = KeyboardButton("📄 Инструкция")
remoteMenu = KeyboardButton("⚙ Управление")
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(manual, remoteMenu)

# --- Remote Menu ---
screen = KeyboardButton('📸 Скрин')
find = KeyboardButton('🔎 Найти')
info = KeyboardButton('ℹ Инфо')

restart = KeyboardButton('🔄 Перезагрузка')
sleep = KeyboardButton('💤 Сон')
close = KeyboardButton('❌ Выключить')
remoteMenu = ReplyKeyboardMarkup(resize_keyboard=True).row(screen, find, info)
remoteMenu.row(restart, sleep, close)
remoteMenu.row(btnMain)
