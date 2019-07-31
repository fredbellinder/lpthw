from ex48 import parser
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
    ('noun', 'cabinet')
]


def scan(stuff, lexicony=lexicon):
    sentence = []
    words = stuff.strip().split(' ')

    def filtery(word):
        if ('verb', word) in lexicony:
            return ('verb', word)
        elif ('direction', word) in lexicony:
            return ('direction', word)
        elif ('noun', word) in lexicony:
            return ('noun', word)
        elif ('stop', word) in lexicony:
            return ('stop', word)
        else:
            try:
                return ('number', int(word)) if len(word) < 10 else ('error', word)
            except ValueError:
                return ('error', word)

    if not isinstance(words, str):
        for word in words:
            sentence.append(filtery(word))
    else:
        sentence.append(word)

    return sentence


# scanned = scan(input("> "))

# parsed = parser.parsery(scanned)
# parsed2 = parser.parse_sentence(scanned)
# print(
#     parsed.obj,
#     parsed.subject,
#     parsed.verb,
# )
# print(
#     parsed2.obj,
#     parsed2.subject,
#     parsed2.verb,
# )
