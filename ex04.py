
#assigning value of 100 to cars
cars = 100
#assigning area of car, or maybe seats
space_in_car = 4.0
#assigning number of drivers
drivers = 30
#assigning number of passengers
passengers = 90
#subraticing variables to figure out how many cars not used
cars_not_driven = cars - drivers
#not sure why we'd make this, but whatever
cars_driven = drivers
#how many passengers can we fit in each car. 
carpool_capacity = cars_driven * space_in_car
#how many people per car. Really space should be n - 1 because a driver is a person
average_passengers_per_car = passengers / cars_driven

print "there are", cars, "cars available"
print "there are only", drivers, "drivers available"
print "there will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "we have", passengers, "to carpool today"
print "we need to put about", average_passengers_per_car, "in each car!"
