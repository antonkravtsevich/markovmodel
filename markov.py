from dictogram import Dictogram


class MarkovModel(dict):
    def __init__(self, words=None):
        super(MarkovModel, self).__init__()
        self.types = 0
        self.tokens = 0
        if(words):
            self.update(words)

    def update(self, words):
        for i in range(0, len(words)-1):
            word = words[i]
            next_word = words[i+1]
            if (not(word in self)):
                self[word] = Dictogram()
                self.types += 1
            self[word].add_word(next_word)
            self.tokens += 1

    def get_next_word(self, word):
        return self[word].next_word()
