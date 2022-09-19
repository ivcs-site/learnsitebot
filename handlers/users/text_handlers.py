from data.loader import bot
from telebot.types import Message, ReplyKeyboardRemove
from keyboards.inline import link_1
import time

@bot.message_handler(regexp='🔥 Огонь, что делать дальше?')
def reaction_1(message: Message):
    chat_id = message.chat.id
    img_2 = open('img/img_2.jpg', mode='rb')
    img_3 = open('img/img_3.jpg', mode='rb')

    time.sleep(1)
    bot.send_photo(chat_id, img_2)
    time.sleep(1)
    bot.send_message(chat_id, '''🤩 Не сомневался в тебе! Прыгай к нам <b>в чат</b>, там вот-вот начнется вся движуха!''', parse_mode='html', reply_markup=ReplyKeyboardRemove())
    time.sleep(1)
    bot.send_message(chat_id, '''🔓 Сейчас у тебя откроется доступ <b>к чату</b>, ждем тебя!''', parse_mode='html', reply_markup=link_1())
    time.sleep(15)
    bot.send_photo(chat_id, img_3)
    time.sleep(1)
    bot.send_message(chat_id, '''<i><b>Куратор</b></i> подключился к чату!''', parse_mode='html')
    time.sleep(1)
    bot.send_message(chat_id, '''печатает...''', parse_mode='html')
    time.sleep(5)
    bot.send_message(chat_id, '''Привет! Я буду отслеживать <b>твою успеваемость</> на курсе и выдавать классные подарки!''', parse_mode='html')
    time.sleep(1)
    bot.send_message(chat_id, '''печатает...''', parse_mode='html')
    time.sleep(5)
    bot.send_message(chat_id, '''Тебе нужно будет скидывать сюда <b>кодовые-слова</b> чтобы получать новые уроки!''', parse_mode='html')
    time.sleep(1)
    bot.send_message(chat_id, '''печатает...''', parse_mode='html')
    time.sleep(5)
    bot.send_message(chat_id, '''Их ты будешь узнавать в конце каждого занятия после сдачи <b>домашки</b> наставнику!''', parse_mode='html')
    time.sleep(1)
    bot.send_message(chat_id, '''печатает...''', parse_mode='html')
    time.sleep(5)
    bot.send_message(chat_id, '''Вся необходимая информация о занятиях будет <b>в нашем чате</b>, не пропусти!''', parse_mode='html')

@bot.message_handler(regexp='Компонент')
def completed_1(message: Message):
    chat_id = message.chat.id

    time.sleep(1)
    bot.send_message(chat_id, '''🤩 Отличная работа! Наставник принял твою домашку! Так держать!''')

@bot.message_handler(regexp='Реализация')
def completed_2(message: Message):
    chat_id = message.chat.id

    time.sleep(1)
    bot.send_message(chat_id, '''🤩 Отличная работа! Наставник принял твою домашку! Так держать!''')

@bot.message_handler(regexp='Портфолио')
def completed_3(message: Message):
    chat_id = message.chat.id

    time.sleep(1)
    bot.send_message(chat_id, '''🤩 Отличная работа! Наставник принял твою домашку! Так держать!''')