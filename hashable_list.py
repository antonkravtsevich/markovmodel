class HList(list):
    def __hash__(self):
        temp = ''
        for item in self:
            temp += item
        return temp.__hash__()
