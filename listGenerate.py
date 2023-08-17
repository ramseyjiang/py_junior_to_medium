'''
It is used to display how to generate list.
'''

a = []
for x in range(1, 11):
    a.append(x * x)

print(a)

b = [x * x for x in range(1, 11)]
print('')
print(b)

c = [x * x for x in range(1, 11) if x % 2 == 0]
print('')
print(c)

d = [m + n for m in 'ABCDEFG' for n in 'MNOPXYZ']
print('')
print(d)

e = {'x': 'A', 'y': 'B', 'z': 'C'}
f = [k + '=' + v for k, v in e.items()]
print('')
print(f)

# When generate a list, in the square parenthesis, it can have if and for.
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s for s in L1 if (type(s) == str)]
L3 = [s for s in L1 if (isinstance(s, str))]
print('')
print(L2)
print(L3)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num + 3 for num in numbers if num % 2 == 0]  # It should %2 == 0 first, then the number result need to add 3.
print(result)
