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
                'Great, your language is selected - English. Enter / help for information.'
        }

    def checker(self, ans, id_lang):
        return ans if id_lang == 'ru' else self.sl[ans]

