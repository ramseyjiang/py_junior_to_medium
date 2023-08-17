from collections.abc import Iterable

print(isinstance('abc', Iterable))  # True
print(isinstance([1, 2, 3], Iterable))  # True
print(isinstance(123, Iterable))  # False

'''
0 A
1 B
2 C
'''
for key, value in enumerate(['A', 'B', 'C']):
    print(key, value)

'''
1 1
2 4
3 9
'''
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

