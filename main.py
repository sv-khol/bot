import telebot # Импортируем telebot
from codeword import secrets 
# импортируем словарь с токеном из файла 

from telebot import types # для определения типов
import random # для выбора случайного 
from poet1 import poet1 # коллекция комплиментов

# передаём значение переменной с кодом экземпляру бота
token = secrets.get('BOT_API_TOKEN')
bot = telebot.TeleBot(token)


# хендлер и функция для обработки команды /start
# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id, "Привет ✌️, бот живой!!!!!!")

# хендлер и функция для обработки команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    p1_button = types.KeyboardButton("поехали!")
    p2_button = types.KeyboardButton("поговори со мной, поэт №1")
    markup.add(p1_button, p2_button)
    bot.send_message(message.chat.id, text="Привет, {0.first_name} 👋\nВоспользуйся кнопками".format(message.from_user), reply_markup=markup)

# хендлер для обработки нажатий кнопок
@bot.message_handler(content_types=['text'])
def buttons(message):
    if (message.text == "поехали!"):
        bot.send_message(message.chat.id, text="Я могу побеседовать. Просто попроси об этом")
    elif (message.text == "поговори со мной, поэт №1"):
        bot.send_message(message.chat.id, text=f"{random.choice(poet1)}")
    else:
        bot.send_message(message.chat.id, text="Я могу отвечать только на нажатие кнопок")

# бесконечное выполнение кода
bot.polling(none_stop=True, interval=0) 

