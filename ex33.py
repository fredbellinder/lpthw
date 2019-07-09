# five = 0

# while five < 5:
#     addon = input("enter anything to add 1 ")
#     if addon:
#         five += 1

# print(f"You added up to {five}")

import time
from sys import exit
i = 0
numbers = []

# while i < 6:
#     print(f"At the top i is {i}")

#     numbers.append(i)

#     i += 1

#     print(f"numbers are now: {numbers}")
#     print(f"At the bottom i is now {i}")

# print("The numbers:")

# for num in numbers:
#     print(num)


def fn(i, stop_value=6):
    input_i = int(i)
    input_stop_value = stop_value if isinstance(
        stop_value, int) else int(stop_value)
    if not isinstance(input_i, int) and not isinstance(input_stop_value, int):
        raise TypeError

    if input_i >= input_stop_value:
        print("""The loop ended before it started, 
        you cant't have a start value larger than or equal to the stop value""")
        pass
    stop = input_stop_value
    while input_i < stop:
        print(f"At the top i is {input_i}")
        numbers.append(input_i)
        input_i += 1
        print(f"numbers are now: {numbers}")
        print(f"At the bottom i is now {input_i}")


def getValues():
    start = input("start value: ")
    stop = input("stop value(optional): ")
    return start, stop


def runFuncs():
    start, stop = getValues()
    fn(start, stop if stop else 6)


try:
    runFuncs()
except TypeError as e:
    print(f"""Only enter integers, not {e} I should have clear about that earlier, perhaps...
    Please do try again""")
    runFuncs()
else:
    print("Try Again? Enter 'Yes' or 'No'")
    another = input("Yes/No: ")
    if another == "No":
        print("B'bye")
        time.sleep(1)
        exit()
    elif another == "Yes":
        print("Try again:")
        runFuncs()
    else:
        print("""As simple as the instructions were, you failed...""")


print(numbers)
if len(numbers) != 0:
    print("The numbers:")

    for num in numbers:
        print(num)
else:
    print("No numbers were ever listed...")
