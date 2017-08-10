class HList(list):
    def __hash__(self):
        temp = ''
        for item in self:
            temp += item
        return temp.__hash__()

    def is_start_elem(self):
        return (self[0] == '*START*')

    def move(self, word):
        self.pop(0)
        self.append(word)