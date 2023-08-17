a = '12'
print(isinstance(a, int))  # False
print(isinstance(a, str))  # True
print(type(a) == int)
print(type(a) == str)
print(type(a) == float)
print('')

a = int(a)  # force convert str to int
print(isinstance(a, int))  # True
print(isinstance(a, str))  # False
print(type(a) == int)
print(type(a) == str)
print(type(a) == float)
print('')

a = float(a)  # force convert to float
print(isinstance(a, int))  # False
print(isinstance(a, str))  # False
print(isinstance(a, float))  # True
print(a)  # 12.0
print(type(a) == int)
print(type(a) == str)
print(type(a) == float)
print('')

a = str(a)
print(isinstance(a, int))  # False
print(isinstance(a, str))  # True
print(isinstance(a, float))  # False
print(type(a) == int)
print(type(a) == str)
print(type(a) == float)
print('')

b = ['a', 2, 'c3']
print(b)  # ['a', 2, 'c3']
print(isinstance(b, tuple))  # False
print(isinstance(b, list))  # True
print(isinstance(b, set))  # False
print(isinstance(b, dict))  # False
print(type(b) == tuple)
print(type(b) == list)
print(type(b) == set)
print(type(b) == dict)
print('')

c = tuple(b)
print(c)
print(isinstance(c, tuple))  # True
print(isinstance(c, list))  # False
print(isinstance(c, set))  # False
print(isinstance(c, dict))  # False
print(type(c) == tuple)
print(type(c) == list)
print(type(c) == set)
print(type(c) == dict)
print('')

c = set(b)
print(c)  # {'c3', 'a', 2}
print(isinstance(c, tuple))  # False
print(isinstance(c, list))  # False
print(isinstance(c, dict))  # False
print(isinstance(c, set))  # True
print(type(c) == tuple)
print(type(c) == list)
print(type(c) == set)
print(type(c) == dict)
print('')

d = {'a': 1, 'b': 2, 'c': 3}
print(d)
print(isinstance(d, tuple))  # False
print(isinstance(d, list))  # False
print(isinstance(d, dict))  # True
print(isinstance(d, set))  # False
print(type(d) == tuple)
print(type(d) == list)
print(type(d) == set)
print(type(d) == dict)
print('')