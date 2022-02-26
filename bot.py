import telebot
from settings import TOKEN
from requests import get
from random import choice
from pictures import pictures


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/picture":
        bot.send_message(message.from_user.id, "Сейчас я отправлютебе дурацкую картинку:)")
        bot.send_photo(message.chat.id, get(choice(pictures)).content)
        bot.send_message(message.from_user.id, "Хочешь еще одну? Напиши /picture")
    else:
        bot.send_message(message.from_user.id, "Привет, я бот, которые отправляет тупые картинки! Чтобы получить картинку нажми /picture")


bot.polling(none_stop=True, interval=0)
