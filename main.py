# -*- coding: utf-8 -*-

import re
from markov import MarkovModel


short_words = ['но', 'и', 'не', 'как', 'так', 'в', 'из', 'по', 'то',
               'некоторый', 'некоторая', 'некоторые', 'некоторых',
               'некоторыми', 'некоторым', 'на', 'что', 'а', 'ее', 'его', 'их',
               'вновь', 'своего', 'свой', 'своих', 'от', 'был', 'еще', '—',
               'с', 'под', 'раз', 'из']


def short_words_processing(str, words):
    for word in words:
        str = str.replace(' '+word+' ', ' '+word+'_')
        str = str.replace('_'+word+' ', '_'+word+'_')
    return str


def prepare_words(str):
    str = str.strip(' ')
    str = short_words_processing(str, short_words)
    str = '*START* '+str+' *END*'
    return str.split(' ')


def prepare_corpuse(text):
    # to lowercase
    text = text.lower()
    # remove \n
    text = text.replace('\n', ' ')
    # remove [...]
    text = re.sub('\[.*?\]', '', text)
    # remove extra spaces
    text = re.sub('\s+', ' ', text)
    # remove « and »
    text = text.replace('«', '')
    text = text.replace('»', '')
    # change ё to е
    text = text.replace('ё', 'е')
    sentenses = re.split('\.|\?|\!', text)
    sentenses = [sentense for sentense in sentenses if (sentense and (sentense != ' '))]
    res = []
    for sentense in sentenses:
        words = prepare_words(sentense)
        for word in words:
            res.append(word)
    return res


def get_data_from_file(filename):
    f = open(filename)
    return f.read()


def main():
    text = get_data_from_file('input')
    # print(text)
    prep = prepare_corpuse(text)
    mm1 = MarkovModel(prep)
    word = mm1.get_next_word('*START*')
    while word != '*END*':
        print(word, end=' ')
        word = mm1.get_next_word(word)


if __name__ == '__main__':
    main()
