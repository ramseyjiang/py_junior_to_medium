# define a dict
a = {'a_cup': 35, 'b_cup': 36, 'c_cup': 37}

# define a set, this one way to create a set, in a set, it won't have the same element.
# The element in the parenthesis, it must be a list element.
b = {1, 2, 2, 2, 3, 3}
x = {1, 3, 2, 3, 3, 4, 4, 4}    # This is the other way to create a set
print(x)

# 35
print(a.get('a_cup'))

# dict_values([35, 36, 37])
print(a.values())

# dict_keys(['a_cup', 'b_cup', 'c_cup'])
print(a.keys())

# {'a_cup': 35, 'b_cup': 36, 'c_cup': 37}
print(a)

# pop a key of element, it will pop the value
c = a.pop('b_cup')
print(c)

# it will print keys and values
# dict_items([('a_cup', 35), ('c_cup', 37)])
print(a.items())

# it will print the last item, after it pops, it is a tuple.
d = a.popitem()
print(len(d))
print(d[0])
print(d[1])

# ('c_cup', 37)
print(d)

# {'a_cup': 35}
print(a)

# None
print(a.clear())

# in a set, when print it, it will filter the same value automatically
print(b)

# None, it will add value 4 into the set directly
print(b.add(4))

# {1, 2, 3, 4}
print(b)

# it will remove value 2 out of the set directly
b.remove(2)
print(b)

