from data.loader import bot
from telebot.types import Message
from keyboards.reply import answer_1
import time

@bot.message_handler(commands=['start'])
def command_start(message: Message):
    chat_id = message.chat.id
    user_name = message.from_user.first_name
    img_1 = open('img/img_1.jpg', mode='rb')

    bot.send_message(chat_id, 'Секунду...')
    time.sleep(1)
    bot.send_message(chat_id, f'Привет, <b>{user_name}</b>! Как дела?', parse_mode='html')
    bot.send_photo(chat_id, img_1)
    time.sleep(1)
    bot.send_message(chat_id, '''🥳 Поздравляю с успешной <b>регистрацией</b> на наш долгожданный бесплатный курс по Разработке сайтов!''', parse_mode='html')
    time.sleep(3)
    bot.send_message(chat_id, '''💻 Всего <b>за 3 дня</b> продуктивной работы мы с тобой и другими участниками курса <b>с нуля</b> создадим небольшое, но сочное портфолио <b>Разработчика сайтов</b> и научимся работать в <b>figma</b> и <b>tilda</b>! У нас будет <b>проверка домашек</b>, <b>наставничество</b>, <b>подарки</b> и многое другое!''', parse_mode='html')
    time.sleep(3)
    bot.send_message(chat_id, '''🤔 Ну, что скажешь?''', reply_markup=answer_1())
