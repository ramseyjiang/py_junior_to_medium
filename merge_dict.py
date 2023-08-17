x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

# merge x and y
# {'a': 1, 'b': 3, 'c': 4}
a = {**x, **y}
print(a)

# {'b': 2, 'c': 4, 'a': 1}
# So different sort, it will have different result, if they have a or many same key elements.
b = {**y, **x}
print(b)
