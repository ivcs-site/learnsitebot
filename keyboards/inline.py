from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def link_1():
    markup = InlineKeyboardMarkup(row_width=1)
    btn = InlineKeyboardButton(text='✅ Войти в чат', url='https://t.me/+KK1vOXz_aaQwZGZi')
    markup.add(btn)
    return markup