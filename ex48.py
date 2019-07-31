
stuff = input('> ')
words = stuff.split(' ')

lexicon = [
    ('verb', 'go'),
    ('verb', 'stop'),
    ('verb', 'kill'),
    ('verb', 'eat'),
    ('direction', 'north'),
    ('direction', 'west'),
    ('direction', 'south'),
    ('direction', 'east'),
    ('direction', 'up'),
    ('direction', 'down'),
    ('direction', 'back'),
    ('direction', 'left'),
    ('direction', 'right'),
    ('stop', 'the'),
    ('stop', 'of'),
    ('stop', 'in'),
    ('stop', 'from'),
    ('stop', 'at'),
    ('stop', 'it'),
    ('noun', 'bear'),
    ('noun', 'door'),
    ('noun', 'princess'),
    ('noun', 'cabinet'),
]

sentence_dict = {}


def scan(words, lexicony=lexicon):
    def filtery(word):
        if ('verb', word) in lexicony:
            print('word in verbs')
            return ('verb', word)
        elif ('direction', word) in lexicony:
            print('word in directions')
            return ('direction', word)
        elif ('noun', word) in lexicony:
            print('word in nouns')
            return ('noun', word)
        elif ('stop', word) in lexicony:
            print('word in stops')
            return ('stop', word)
        else:
            try:
                has_to_be_an_int = int(word)
                print(has_to_be_an_int)
            except ValueError:
                return (False, word)

    if not isinstance(words, str):
        for word in words:
            sentence = filtery(word, lexicon)
            print('is not instance: ', not isinstance(words, str), sentence)
    else:
        sentence = filtery(words, lexicon)
        print(sentence)

    return sentence


scan(words)
