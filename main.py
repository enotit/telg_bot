from pass_adm import Check
from lang import CheckLang
import telebot
from telebot import apihelper, types

apihelper.proxy = {'https': 'socks5h://localhost:9050'}
Token = '1105649584:AAH2ljq-IhIHqGpQLAtdxEoxpyo8JuO3224'
bot = telebot.TeleBot(Token)
ch = Check()
lang = CheckLang()
users = dict()
print('life')


@bot.message_handler(commands=['start'])
def send_help(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton('ru 🇷🇺')
    item = types.KeyboardButton('en 🇬🇧')
    markup.add(item1, item)
    bot.send_message(message.from_user.id, 'Choose your language, please\n'
                                           'Выберите язык, пожалуйста', markup)


@bot.message_handler(commands=['help', 'command'])
def send_help(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton(lang.checker('Задать вопрос', users[message.from_user.id]))
    item = types.KeyboardButton('FAQ')
    markup.add(item1, item)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'ru 🇷🇺' or message.text == 'en 🇬🇧':
        users[message.from_user.id] = 'ru' if message.text == 'ru 🇷🇺' else 'en'
        bot.send_message(message.from_user.id, lang.checker(
            'Отлично, ваш язык выбран - русский. Для получения информации введите /help', users[message.from_user.id]))
    else:
        bot.send_message(message.from_user.id, 'Не знакомое выражение.\n❔Помощь /help')


bot.polling(none_stop=True, interval=0, timeout=120)
