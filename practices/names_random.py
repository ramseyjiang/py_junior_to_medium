import random

names_string = input("Please input names, separated by a comma.")

names = names_string.split(", ")
names_len = len(names)-1
random_number = random.randint(0, names_len)
print(names[random_number])