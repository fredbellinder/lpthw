print("""
You enter a dark room with two doors.
Do you go through door #1 or #2?
""")

door = input("> ")

if door == "1":
    print("There's a giant bear here - eating a cheesecake.")
    print("What do you do?")
    print("1. I take the cake.")
    print("2. I scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off, Good Job!")
    elif bear == "2":
        print("The bear eats your legs off, Good Job!")
    else:
        print(f"Doing {bear} is probably better than #1 or #2")
        print("The bear runs away")

elif door == "2":
    print("You stare in to the abyss of Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck")

else:
    print("You stumble around and fall on a knife and die.")
    print("Good job")
