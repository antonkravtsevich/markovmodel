# -*- coding: utf-8 -*-

import re
import codecs
from markov import MarkovModel
from hashable_list import HList
import re


short_words = ['но', 'и', 'не', 'как', 'так', 'в', 'из', 'по', 'то',
               'некоторый', 'некоторая', 'некоторые', 'некоторых',
               'некоторыми', 'некоторым', 'на', 'что', 'а',
               'вновь', 'своего', 'свой', 'своих', 'от', 'был', 'еще', '—',
               'с', 'под', 'раз', 'из', '–', 'над', 'под', 'из', 'за', 'уж',
               'же', 'о', 'со']


def short_words_processing(str, words):
    for word in words:
        str = str.replace(' '+word+' ', ' '+word+'_')
        str = str.replace('_'+word+' ', '_'+word+'_')
    return str


def prepare_words(str):
    str = str.strip(' ')
    # str = short_words_processing(str, short_words)
    str = '*START* '+str+' *END*'
    return str.split(' ')

def post_processing(str):
    str = str.replace('_', ' ')
    return str

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
    f = codecs.open(filename, 'r', 'utf-8')
    return f.read()


def main():
    text = get_data_from_file('games_of_thrones.txt')
    prep = prepare_corpuse(text)
    
    mm1 = MarkovModel(words=prep, window=3)

    sentense = mm1.generate_sentense()
    psentense = post_processing(sentense)
    print(psentense)


if __name__ == '__main__':
    main()
