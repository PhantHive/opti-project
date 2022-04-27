import json


class Language:

    def __init__(self, lg):
        self.lg = lg
        self.lang = json.load(open("src/lang/lang.json"))

    def get_lang(self):
        print(self.lang[self.lg])
        return self.lang[self.lg]