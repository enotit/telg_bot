from pass_adm import Check
from lang import CheckLang
from impr_bd import BD
import telebot
from telebot import apihelper, types
import logging

# logging info
logging.basicConfig(#format=u'%(filename)s[LINE:%(lineno)d]#%(levelname)-8s[%(asctime)s] %(message)s',
                    level=logging.DEBUG, filename='info.log')
apihelper.proxy = {'https': 'socks5h://localhost:9050'}  # proxy
Token = '1105649584:AAH2ljq-IhIHqGpQLAtdxEoxpyo8JuO3224'
bot = telebot.TeleBot(Token)  # Connect to Telegram
ch, lang, bd = Check(), CheckLang(), BD()
#      Admin_check / Convert text of lang. / DataBase about questing
adm_log = dict()
# id admins queue of busy`s questing
users, peop = dict(), set()
# {id: 'en/ru'} | busy users w/questions
print('life')
logging.info('start')


# end work admin
@bot.message_handler(commands=['exit'])
def _ex(message):
    if ch.adm(message.from_user.id):
        ch.exit(message.from_user.id)
        bot.send_message(message.from_user.id, 'Успешно вышли из системы')


# get all questions
@bot.message_handler(commands=['getall'])
def _fres(message):
    if ch.adm(message.from_user.id):
        markup = types.ReplyKeyboardMarkup(True, True, row_width=1)
        b = bd.get_all()
        for i in b:
            markup.add(types.KeyboardButton(i))
        bot.send_message(message.from_user.id, f'Свободных вопросов {len(b) - 1}', reply_markup=markup)


# choose language
@bot.message_handler(commands=['start'])
def send_start(message):
    markup = types.ReplyKeyboardMarkup(True, True, row_width=2)
    item1 = types.KeyboardButton('ru 🇷🇺')
    item = types.KeyboardButton('en 🇬🇧')
    markup.add(item1, item)
    bot.send_message(message.from_user.id, 'Choose your language, please\n'
                                           'Выберите язык, пожалуйста', reply_markup=markup)


def faq(mes):
    pass


# help words
@bot.message_handler(commands=['help', 'command'])
def send_help(message):
    if message.from_user.id in users:
        markup = types.ReplyKeyboardMarkup(True, row_width=2)
        item1 = types.KeyboardButton(lang.checker('Задать вопрос', users[message.from_user.id]))
        item = types.KeyboardButton('FAQ')
        markup.add(item1, item)
        bot.send_message(message.from_user.id, lang.checker(
            'Бот создан для тех.поддержки в разных непонятных ситуациях, прежде прочитайте FAQ, дальше задайте вопрос'
            ' агентам поддержки. Ловите кнопки.', users[message.from_user.id]),
                         reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # check availability in admin list in queue answer of quests
    if message.from_user.id in adm_log:
        anon = users[int(adm_log[message.from_user.id])]
        text = lang.checker('Администратор', anon) + f'({str(message.from_user.id)[-3:]})' + ' ' + \
               lang.checker('ответил вам на вопрос', anon) + '\n' + \
               message.text + '\n' + lang.checker('Всего доброго, спасибо за обращение к нам.', anon)
        bot.send_message(adm_log[message.from_user.id], text)
        bot.send_message(message.from_user.id, 'Ваш ответ доставлен')
        bd.delete(int(adm_log[message.from_user.id]))
        adm_log.pop(message.from_user.id)
    # check availability in main list 'users'
    elif message.from_user.id in users or (message.text == 'ru 🇷🇺' or message.text == 'en 🇬🇧'):
        # Choose language
        if message.text == 'ru 🇷🇺' or message.text == 'en 🇬🇧':
            users[message.from_user.id] = 'ru' if message.text == 'ru 🇷🇺' else 'en'
            bot.send_message(message.from_user.id, lang.checker(
                'Отлично, ваш язык выбран - русский. Для получения информации введите /help',
                users[message.from_user.id]))
            send_help(message)
        # Answer admin of quest
        elif str(message.text).startswith('<#>') and ch.adm(message.from_user.id):
            now_text = str(message.text).split(':')[0][3:]
            bot.send_message(message.from_user.id, f'{now_text}\n{bd.get(int(now_text))}')
            adm_log[message.from_user.id] = now_text
        # Message processing
        elif message.text == 'Задать вопрос' or message.text == 'Ask a Quesion':
            bot.reply_to(message, lang.checker(
                'Задавайте свой вопрос. Если вопросов нет, то просто отправьте точку.', users[message.from_user.id]))
            peop.add(message.from_user.id)
        elif str(message.text).startswith('pas '):
            if ch.adm(message.from_user.id):
                bot.reply_to(message, 'Вы и так зашли как администратор.')
            else:
                if ch.adm_add(str(message.text).split()[1], message.from_user.id) and len(message.text) > 4:
                    bot.send_sticker(message.from_user.id,
                                     'CAACAgIAAxkBAAI52l5_FPbznPr3FTU6LEFd3ztE3o98AALzAgACnNbnCuAuBHGFD8ECGAQ')
                else:
                    bot.send_sticker(message.from_user.id,
                                     'CAACAgIAAxkBAAI53F5_FP3GtYhh15hR_HcMR-_m8vz5AAIlAwACnNbnCgAB0udXwyXKPxgE')
        elif str(message.text).startswith('FAQ'):
            pass
        else:
            if message.from_user.id in peop:
                if message.text == '.':
                    bot.reply_to(message, lang.checker(
                        'Отмена операции: успешно.', users[message.from_user.id]))
                else:
                    bd.add(message.from_user.id, message.from_user.first_name + ' : ' + message.text)
                    bot.reply_to(message, lang.checker('Ваш вопрос успешно отправлен модерации. '
                                                       'В ближайшее время они пришлют ответ',
                                                       users[message.from_user.id]))
                    for i in list(ch.get_list()):
                        bot.send_message(i, '❗ Новый вопрос ❗\n--> /getall')
                peop.discard(message.from_user.id)
            else:
                bot.send_message(message.from_user.id, 'Write please | Пожалуйста напишите \n/help')
    else:
        bot.send_message(message.from_user.id, 'Write please | Пожалуйста напишите \n/start')


bot.polling(none_stop=True, interval=0, timeout=120)


