import requests
import json


class Check:
    def __init__(self):
        self.admin_id = {427843213}

    def adm(self):
        info = requests.get(self.api)
        data = json.loads(info.text)['latest']
        return f"{data['confirmed']} - Заражённых\n{data['recovered']} - Выздоровших\n{data['deaths']} - Умерших"
