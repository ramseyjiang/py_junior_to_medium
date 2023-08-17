import random
random_int = random.randint(1, 10)
print(random_int)

# This file cannot be named random.py, if it made that name, it won't find the random which be imported.
# random float's scope is from 0 to 1, so if want to get float over 1, use ramdom.random()*int to solve it.
random_float = random.random()
print(random_float)
