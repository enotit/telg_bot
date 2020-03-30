"""

adm(id) - check of list admin. Return true/false
get_list() -  gating the whole list admins. Return list()
adm_add(password, id) - adding in list admin by private password. Return True/False
exit(id) - end work admin ( delete from the list working admins. Not return

"""


class Check:
    def __init__(self):
        self.free_pas = {'adm_11', 'helloworld'}
        self.busy = dict()

    def adm(self, id):
        return True if id in self.busy else False

    def get_list(self):
        return self.busy.keys()

    def adm_add(self, mes, id):
        if mes in self.free_pas:
            self.busy[id] = mes
            self.free_pas.discard(mes)
            return True
        return False

    def exit(self, id):
        self.free_pas.add(self.busy.get(id))
        self.busy.pop(id)
