from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def answer_1():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton(text='🔥 Огонь, что делать дальше?')
    markup.add(btn)
    return markup