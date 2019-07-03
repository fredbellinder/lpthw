# the_count = list(range(1, 6))
the_count = [*range(1, 6)]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

for number in the_count:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"Type of fruit: {fruit}")

for i in change:
    print(f"I got {i}")
# building lists starting with an empty one
elements = []

for i in range(0, 6):
    print(f"Adding {i} to the elements list")
    elements.append(i)
    elements.insert(0, i)

elements.sort()

for element in elements:
    print(f"Element: {element}")
2
