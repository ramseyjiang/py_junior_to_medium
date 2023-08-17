# Using namedtuple is way shorter than
# defining a class manually:
from collections import namedtuple

# Our new "Car" class works as expected:
# Class name is Car, attributes are color and mileage.
Car = namedtuple('Car', 'color mileage')
my_car = Car('red', 3812.4)

# red 3812.4
print(my_car.color, my_car.mileage)

# Car(color='red', mileage=3812.4)
print(my_car)

# It will have an error. AttributeError: "can't set attribute"
# my_car.color = 'blue'
