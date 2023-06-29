import telebot
from telebot import types

bot = telebot.TeleBot('6297252263:AAER2PdsJ8W3tegZiSXnrdIV-verjPs_Zew')

@bot.message_handler(commands=['hello'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Мой ТГ💝')
    markup = types.ReplyKeyboardMarkup()
    btn2 = types.KeyboardButton('Мой YT🧛')
    markup = types.ReplyKeyboardMarkup()
    btn3 = types.KeyboardButton('Мой TTV👾')
    markup = types.ReplyKeyboardMarkup()
    btn4 = types.KeyboardButton('Help👍')
    markup = types.ReplyKeyboardMarkup()
    btn5 = types.KeyboardButton('Личный сайт(soon)')
    markup.row(btn4)
    markup.row(btn1, btn2, btn3, btn5)
    bot.send_message(message.chat.id, f"Привет {message.from_user.first_name},рад тебя видеть)", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text.lower() == 'help👍':
        bot.send_message(message.chat.id, 'Я явлюсь собственностью моего хозяина,ссылки на которого вы можете найти здесь')
    elif message.text.lower() == 'мой тг💝':
        bot.send_message(message.chat.id, "https://t.me/forgotmeeee")
    elif message.text.lower() == 'мой yt🧛':
        bot.send_message(message.chat.id, "https://www.youtube.com/channel/UCoHD0po-RI7yxYi5RnOyhAA")
    elif message.text.lower() == 'мой ttv👾':
        bot.send_message(message.chat.id, "https://www.twitch.tv/merc1kle")
    elif message.text == 'Личный сайт(soon)':
        bot.send_message(message.chat.id, f"На данный момент сайт находится в разработке,но скоро он будет готов(или нет)")


bot.polling(none_stop=True)