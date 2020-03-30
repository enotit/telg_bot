"""

The only one function checker():
Transmitted expression and code language(ru/en).
Return expression in the desired language.

"""


class CheckLang:
    def __init__(self):
        self.sl = {
            'Задать вопрос':
                'Ask a Quesion',
            'Не знакомое выражение.\n❔Помощь /help':
                'Unfamiliar expression.\n❔Write /help',
            'Ваш запрос был отправлен администрации, ожидайте пожалуйста':
                'Your request has been sent to the administration, please wait',
            'Отлично, ваш язык выбран - русский. Для получения информации введите /help':
                'Great, your language is selected - English. Enter /help for information.',
            'Бот создан для тех.поддержки в разных непонятных ситуациях, прежде прочитайте FAQ, дальше задайте вопрос'
            ' агентам поддержки. Ловите кнопки.':
                'The bot was created for technical support in various incomprehensible situations, first read the FAQ, '
                'then ask a question to support agents. Catch the buttons. ',
            'Задавайте свой вопрос. Если вопросов нет, то просто отправьте точку.':
                'Ask your a Question. If there are no questions, send a point.',
            'Отмена операции: успешно.':
                'Cancel operation succesfull.',
            'Ваш вопрос успешно отправлен модерации. В ближайшее время они пришлют ответ':
                'Your question has been successfully sent to moderation. In the near future they will send an answer',
            'Администратор': 'Administrator', 'ответил вам на вопрос': 'answered your question',
            'Всего доброго, спасибо за обращение к нам.': 'All the best, thanks for contacting us.'
        }

    def checker(self, ans, id_lang):
        return ans if id_lang == 'ru' else self.sl[ans]
