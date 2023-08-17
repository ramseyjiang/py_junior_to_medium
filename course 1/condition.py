age = 20
if age >= 18:
    print('your age is', age)
    print('adult')


age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')


age = 12
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')


birth = int(input('birth: '))
if birth < 2000:
    print('before 2000')
else:
    print('after 2000')