from sys import argv

# Creates a call for arguments from command line (and the filename that is running is stored in "script")
script, filename = argv

# opens a file that has been named from command line, can take more than one argument, filename and  mode, returns a file object.
txt = open(filename)

print(f"Here's your file {filename}:")
# Collects the content of "txt" and prints it  
print(txt.read())

print("Type the filename again:")
# prompts a user for a filename
file_again = input("> ")

# opens file with above prompted filename
txt_again = open(file_again)

# prints above opened files content
print(txt_again.read())

txt.close()
txt_again.close()

