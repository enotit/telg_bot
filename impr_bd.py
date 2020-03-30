"""
Temporary memory database
get_all() - returns a list of unanswered questions. Return list()
get(id) - by the id of the user who asked the question, the question itself is returned. Return String
delete(id) - delete the questions, when answered
add(id, quest) - adding quest in the main list.
"""


class BD:
    def __init__(self):
        self.quests = {'123/': '====='}

    def get_all(self):
        a = []
        for i in self.quests.keys():
            if i == '123/':
                a.append('/help')
            else:
                tr = self.quests.get(i).split(' : ')[1]
                a.append(f'<#>{i}: {tr if len(tr[:15]) < 15 else tr[:15] + "..."}')
        return a

    def get(self, id):
        return self.quests.get(id)

    def delete(self, id):
        self.quests.pop(id)

    def add(self, id, que):
        self.quests[id] = que
