def handle():
    stuff = input('> ')
    words = stuff. split(' ')

    lexicon = {
        'verbs': ('go'),
        'directions':  ('north', 'west', 'south', 'east'),
        'nouns': ('bear', 'princess', 'princess', 'cabinet'),
    }

    sentence_dict = {}

    for word in words:
        if word in lexicon.verbs:
            pass
        elif word in lexicon.directions:
            pass
        elif word in lexicon.nouns:
            pass
        else:
            try:
                has_to_be_an_int = int(word)
                return has_to_be_an_int
            except ValueError:
                return None
