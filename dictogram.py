import random


class Dictogram(dict):
    def __init__(self):
        super(Dictogram, self).__init__()
        self.types = 0
        self.tokens = 0

    def add_word(self, word):
        if word in self:
            self[word] += 1
            self.tokens += 1
        else:
            self[word] = 1
            self.types += 1
            self.tokens += 1

    def next_word(self):
        random_int = random.randint(0, self.tokens-1)
        index = 0
        keys = self.keys()
        for key in keys:
            index += self[key]
            if(index > random_int):
                return key
