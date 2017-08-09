from markov import MarkovModel


def prepare_words(str):
    str = str.strip(' ')
    str = '*START* '+str+' *END*'
    return str.split(' ')


def prepare_corpuse(text):
    text = text.lower()
    sentenses = text.split('.')
    sentenses = filter(None, sentenses)
    res = []
    for sentense in sentenses:
        words = prepare_words(sentense)
        for word in words:
            res.append(word)
    return res


def main():
    str1 = 'Today you are you. That is truer than true. There is no one alive who is you-er than you.'
    str2 = 'You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose. You’re on your own.'
    str3 = 'The more that you read, the more things you will know. The more that you learn, the more places you’ll go.'
    str4 = 'Think left and think right and think low and think high. Oh, the thinks you can think up if only you try.'
    str = str1+' '+str2+' '+str3+' '+str4
    prep = prepare_corpuse(str)
    mm1 = MarkovModel(prep)
    word = mm1.get_next_word('*START*')
    while word != '*END*':
        print(word, end=' ')
        word = mm1.get_next_word(word)
    


if __name__ == '__main__':
    main()
