with open("ex37.txt") as open_file:
    print(open_file.read())

"""
Why to create strong password?
Because it makes the chances of hackers bruteforcing your password to almost 0%
Simply to not get hacked!
"""

import random
import string

# Password level is Strong!
# Creates a alphanumeric password of `n` chars 
def create_password(n):
    allChars = list(string.ascii_letters) + list(string.digits) + list(string.punctuation)
    print(list(string.ascii_letters))
    passphrase = []
    for i in range(n):
        tmp = random.choice(allChars)
        passphrase.append(tmp)
    
    res = "".join(passphrase)
    return res
    
# Test 1
def getLength():
    while True:
        try:    
            length = int(input("Length desired:"))
        except Exception as e:
            print("Your input needs to be a number.")
            continue
        if isinstance(length, int):    
            if length <=50 and length != 0:
                break
            elif length == 0: 
                print("The length of your password cannot be 0")
            else: 
                print("""Your desired length was out of allowed range, min = 1 and max = 50.""")
    print(length) 
    return length
test1 = create_password(getLength())
print(test1, len(test1))

# Test 2 
# test2 = create_password(32)
# print(test2)