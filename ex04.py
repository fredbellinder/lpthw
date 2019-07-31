# integer
cars = 100
# floating point
space_in_a_car = 4.0
# integer
drivers = 30
# integer
passengers = 90
# integer
cars_not_driven = cars - drivers
# integer
cars_driven = drivers
# floating point (integer multiplied by a floating point)
carpool_capacity = cars_driven * space_in_a_car
# floating point (integer divided)
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today")
print("Wee need to put about", average_passengers_per_car, "in each car.")
