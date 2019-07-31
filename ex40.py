import ex25
from copy import deepcopy


class Mystuff(object):
    def __init__(self,):
        self.tangerine = "And now a thousand years between"

    def apples(self):
        print("How do you like them apples!?")


# boing = Mystuff()

# boing.apples()
# print(boing.tangerine)
# boing.going_loco = "down in Acapulco, if you stay too long!"
# print(boing.going_loco)
# poop = "💩"
# print(poop)


class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


ledin = Song([
    "Sommaren är kort",
    "Det mesta regnar bort", "Men nu är den här",
    "Så ta för dig, solen skiner...",
    "...kanske bara idag",
])
# ledin.sing_me_a_song()

foo = Song([
    "All my life I've been searching for something",
    "Something never comes never leads to nothing",
    "Nothing satisfies but I'm getting close",
    "Closer to the prize at the end of the rope",
    "All night long I dream of the day",
    "When it comes around and it taken away",
    "Leaves me with the feeling that I feel the most",
    "Feel it come to life when I see your ghost",
])

# foo.sing_me_a_song()

letter = dict({"enter": 'raccoon'})

one = deepcopy(letter)

# two = ex25.copy()

one['hound'] = 'cat'

print(one, letter)
