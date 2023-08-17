family = ['May', 'Ramsey', 'Davy']
classmates = ('Michael', 'Bob', family)
print('classmates =', classmates)
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])
print('')

# cannot modify tuple:
family = ['May', 'Davy', 'Mamba']
print('classmates[2] =', classmates[2])  # classmates[2] = ['May', 'Ramsey', 'Davy']
print(classmates)  # ('Michael', 'Bob', ['May', 'Ramsey', 'Davy'])
print(family)  # ['May', 'Davy', 'Mamba']
