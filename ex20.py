from sys import argv

script, input_file = argv

# function takes an opened file as an arg and reads and prints its whole content


def print_all(f):
    print(f.read())

# function takes an opened file as an argument and returns to the 0 byte, the start of the file


def rewind(f):
    f.seek(0)

# function takes an integer, and an opened file as arguments and prints the integer and a line from the file
# the integer is non related to which line is to be read but it's possible too keep track yourself, outside the function.


def print_a_line(line_count, f):
    print(line_count, f.readline())


current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind it like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
