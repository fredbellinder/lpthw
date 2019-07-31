from random import randint


def guess(min, max):
    minimi, maximi = min, max
    if isinstance(minimi, int) and isinstance(maximi, int):
        return randint(int(min), int(max))
    else:
        return "input needs to be two integers"
