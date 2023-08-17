names = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# ['Michael', 'Sarah', 'Tracy']
print(names[0:3])

# ['Sarah', 'Tracy']
print(names[1:3])

# ['Michael', 'Sarah', 'Tracy', 'Bob']
print(names[:4])

# ['Jack']
print(names[-1:])

# ['Michael', 'Tracy', 'Jack'], "::2" means interval 2 elements get one.
print(names[::2])

# ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack'], ":" will copy the whole slice.
print(names[:])

# string is a type of slice
strings = 'jiang da wei'
# jia
print(strings[:3])

