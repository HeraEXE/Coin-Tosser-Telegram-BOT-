from telebot.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_flip = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
bflip = KeyboardButton('🔄FLIP')
keyboard_flip.add(bflip)