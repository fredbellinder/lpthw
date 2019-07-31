from datetime import date

# things = ['a', 'b', 'c', 'd', 'e', 'f']

# print(things[1])

# things[1] = 'z'

# print(things[1])

# print(things)
year = date.today().year
stuff = {'name': 'Fred', 'age': (year - 1986), 'height': int(183 / 2.54 / 12)}
print(stuff)

stuff['city'] = {'Stockholm': 'STHLM'}

print("Hi, I'm {} at {} years of age and {} feet tall. I'm from {}".format(
    *stuff.values()))

stuff[0] = 'Will this get indexed?'

print(stuff, stuff[0])

del stuff[0]

print(stuff)

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Fransisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['OR'] = 'Portland'
cities['NY'] = 'New York'

print('-'*10)
print('NY state has', cities['NY'])
print('OR state has', cities['OR'])

print('-' * 10)
print(f"Michigans abbreviation is {states['Michigan']}")
print(f"Floridas abbreviation is {states['Florida']}")

print('-' * 10)
print('Michigan has: ', cities[states['Michigan']])
print('Florida has: ', cities[states['Florida']])

print('-' * 10)
for state, abbr in list(states.items()):
    print(f"{abbr} is short for {state}")

print('-' * 10)
for abbr, city in list(cities.items()):
    print(f"{abbr} has the city of {city}")

print('-' * 10)


def print_some_jibberish(states: dict, cities: dict, yolo: int) -> int:
    print(yolo)
    print("+"*10)
    for state, abbr in list(states.items()):
        print(f"{abbr} is short for {state}")
        print(f"and has the city of {cities[abbr]}")
    print("+"*10)
    return yolo


try:
    yolo = print_some_jibberish(
        states, cities,
        "this should be an int and it would raise an error in other flavors of python, like mypy, or so I've heard")
    print("yolo printing", yolo)
except Exception as e:
    print('wtf', e)

print('-' * 10)
state = states.get('Texas')
if not state:
    print('No such state')

print('-' * 10)
try:
    state2 = states['Idaho']
    print(state2)
except Exception as e:
    print('Eggcepshon', e)

print('-' * 10)
state_to_get = "Arkansas"
city = cities.get(state_to_get, "Does not exist")
print(f"The city of {state_to_get} is: {city}")
