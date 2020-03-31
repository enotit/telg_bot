class Faq:
    def __init__(self):
        self.main = {
            'Кто ты такой?':
                'Я бот, который помогает в различных вопросах, связывает с администрацией, а также отвечаю на '
                'распространнёные вопросы, к примеру - этот.',
            'Кому ты принадлежишь?':
                'Мой создатель enotit - в случае, если нужно связаться - напишите "Контакты" или нажмите на одноимённую'
                ' кнопку.',
            'Что по ценам?':
                'Поддержка бота(изменение текстовой информации) и сам код - 600 рублей. Вы получаете папку с 5 файлами'
                'кода + лог файл, куда будут вписана история работы с ботом.\nТакже, можете поспользоваться услугой'
                'поставки бота на ВАШ хостинг, всего за 200 рублей.',
            'Контакты':
            'Email - mn1vitech@gmail.com\nGit-hub - github.com/enotit'
        }
        self.main_lang = {
            'Who is you?':
                'I am a bot that helps in various issues, connects with the administration, and also answers to '
                'common questions, for example, this one.',
            'Who do you belong to?':
                'My father enotit - in case you need to contact - write "Contacts" or click on the button of the same.'
                'name.',
            'What price?':
                'Support for the bot (changing text information) and the code itself - 600 rubles. You get a folder '
                'with 5 files of code + a log file, where the history of working with the bot will be entered.\nYou '
                'can also use the service of delivering the bot to YOUR hosting for only 200 rubles.',
            'Contacts.':
            'Email - mn1vitech@gmail.com\nGit-hub - github.com/enotit'
        }

    def get_all(self, id_lang):
        return self.main.keys() if id_lang == 'ru' else self.main_lang.keys()

    def post(self, msg, id_lang):
        return self.main.get(msg) if id_lang == 'ru' else self.main_lang.get(msg)