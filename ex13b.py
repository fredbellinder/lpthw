from sys import argv

script, make, model, year, style = argv

print(f"""
The motorcycle is a {make}, {model}.
It was made in {year}.
It is a {style} type of bike. 
""")
