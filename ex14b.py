from sys import argv

script, user_first_name, user_last_name = argv
prompt = '> '

print(f"Hi {user_first_name} of House {user_last_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_first_name}?")
likes = input(prompt)

print(f"Where do you live {user_first_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright {user_first_name} , so you said {likes} about liking me.
You live in {lives}. Dunno where that is.
And for a computer you use a {computer}. Nice.
""")


