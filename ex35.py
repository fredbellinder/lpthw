from sys import exit


def gold_room():
    print("This room is full of gold")
    choice = input("> ")

    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn how to type a number")

    if how_much < 50:
        print("Good, you're not that greedy!")
        exit()
    else:
        dead("You greedy bastard!")


def bear_room():
    print("""There's a bear in here.
    The bear does have a bunch of honey.
    The fat Bear is in front of another door.
    How will you move the bear?""")

    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear look at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("""The bear has moved from the door.
            You can go through it now.""")
            bear_moved = True
        elif (choice == "taunt bear") and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("Try again, didn't get that at all...")


def cthulhu_room():
    print("""
    Here you see the great evil Cthulhu.
    He, it or whatever, stares at you and you go insane.
    Do you flee for your life our devour your own head.
    """)

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(msg):
    print(msg, "Good Job!")
    exit()


def start():
    print("""
    You're in a dark room.
    There are two doors, one to your left and one to your right.
    Which one do you choose?
    """)

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve, the lack of water prolly gets you first though")


start()
