from dictogram import Dictogram
from hashable_list import HList
import random

class MarkovModel(dict):
    def __init__(self, words=None, window=1):
        super(MarkovModel, self).__init__()
        self.types = 0
        self.tokens = 0
        if(words):
            self.update(words, window)

    def update(self, words, window):
        for i in range(window, len(words)-1):
            hlist = HList()
            for j in reversed(range(0, window)):
                hlist.append(words[i-j])
            next_word = words[i+1]
            if (not(hlist in self)):
                self[hlist] = Dictogram()
                self.types += 1
            self[hlist].add_word(next_word)
            self.tokens += 1

    def get_next_word(self, token):
        return self[token].next_word()

    def get_random_start(self):
        keys = self.keys()
        start_keys = [key for key in keys if key.is_start_elem()]
        return random.choice(start_keys)

    def generate_sentense(self):
        res = ''
        key_token = self.get_random_start()
        # printing start token
        words = key_token[1:]
        for word in words:
            res += word + ' '

        word = self.get_next_word(key_token)
        while word != '*END*':
            res += word + ' '
            key_token.move(word)
            word = self.get_next_word(key_token)
        return res