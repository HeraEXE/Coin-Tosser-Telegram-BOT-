from random import choice
from __main__ import bot
from keyboards import keyboard_flip
from funcs import FUNCS
from coinimages import COINIMAGES

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '👁', reply_markup=keyboard_flip)


@bot.message_handler(content_types=['text'])
def responce(message):
    func = FUNCS.get(message.text)
    if func is not None:
        exec(func)


def flip(message):
    with open(choice(COINIMAGES), 'rb') as coinside:
        bot.send_photo(message.chat.id, coinside)