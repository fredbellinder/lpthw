from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.")

# We could do the following in one line, how?
# like this, but how do I close the file then? Dunno.
# According to the book Python should handle closing automatically once that line runs.
# indata = open(from_file, "r").read()
in_file = open(from_file, "r")
in_data = in_file.read()
# print(f"The input file is {len(in_data)} bytes long")

# print(f"Does the output file exist? {exists(to_file)}")
# print(f"Ready, hit RETURN to continue , CTRL-c to abort.")
# input()

out_file = open(to_file, "w")
out_file.write(in_data)

print("Alright, all done")

out_file.close()
in_file.close()
