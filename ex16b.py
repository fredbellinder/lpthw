from sys import argv

script, filename = argv

print(f"We're going to erase {filename}")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
# Turns the file to: the given size in bytes or if no argument is given, it's current size
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
target.write(f"{line1}\n{line2}\n{line3}\n")
target.close()
target = open(filename, 'r')
print(f"I'll read your lines in {filename} back to you:")
# does not work, why is that?
# It didn't work cause changes are made ti the file first at .close()
# now it works
print(f"Here ya go: \n{target.read()}")

print("And finally, we close it.")
target.close()
