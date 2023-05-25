from telebot import types
import telebot
from random import randint
import logging


bot = telebot.TeleBot("")
telebot.logger.setLevel(logging.INFO)

markup = types.ReplyKeyboardMarkup(row_width=1)
btn_game = types.KeyboardButton('Игра')
markup.add(btn_game)


storage = dict()


def init_storage(user_id):
    storage[user_id] = dict(attempt=None, random_digit=None)


def set_data_storage(user_id, key, value):
    storage[user_id][key] = value


def get_data_storage(user_id):
    return storage[user_id]


@bot.message_handler(commands=['start', 'help'])
def send_welcome(mes):
    bot.send_message(mes.from_user.id,
                     "Привет, я бот Загадайка.", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text.lower() == "игра")
def games_gues(mes):
    init_storage(mes.chat.id)
    attempt = 0
    set_data_storage(mes.chat.id, "attempt", attempt)
    bot.send_message(mes.chat.id, 'Я загадал число от 1 до 1000. Угадай его.')
    bot_number = randint(1, 1000)
    set_data_storage(mes.chat.id, "random_number", bot_number)
    bot.register_next_step_handler(mes, games_step)


def games_step(message):
    user_number = message.text
    if not user_number.isdigit():
        msg = bot.reply_to(
            message, 'Вы ввели не число. Введите число.')
        bot.register_next_step_handler(msg, games_step)
        return
    attempt = get_data_storage(message.chat.id)["attempt"]
    random_number = get_data_storage(message.chat.id)["random_number"]

    if int(user_number) > random_number:
        attempt += 1
        set_data_storage(message.chat.id, "attempt", attempt)
        bot.send_message(message.chat.id, 'Загаданное число меньше!')
        bot.register_next_step_handler(message, games_step)
        return
    elif int(user_number) < random_number:
        attempt += 1
        set_data_storage(message.chat.id, "attempt", attempt)
        bot.send_message(message.chat.id, 'Загаданное число больше!')
        bot.register_next_step_handler(message, games_step)
        return
    else:
        bot.send_message(
            message.chat.id, f'Вы угадали число {random_number} за {attempt +1} попыток!')
        init_storage(message.chat.id)
        return


bot.polling()
