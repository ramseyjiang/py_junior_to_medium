def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


enroll('May', 'Female')
print('')
enroll('Davy', 'Male', city='Auckland')
print('')


# Number of Arguments
# in calc1, the param is a list or tuple.
# it can be number of arguments.
# But before invoke calc1, a list or tuple should define first.
def calc1(numbers):
    num_sum1 = 0
    for n in numbers:
        num_sum1 += n * n
    return num_sum1


# 14
nums = [1, 2, 3]
print(calc1(nums))
print('')

# 30
nums.append(4)
print(calc1(nums))
print('')


# Arbitrary Arguments
# in calc2, the param cannot be changed. It always point to numbers.
# when invoke it, it can be passed 0 or many arguments, it is called arbitrary arguments.
# all arguments will be arranged as a tuple.
# But if no param transfer in calc1, it won't work. print(calc1()), it will have an error.
def calc2(*numbers):
    num_sum2 = 0
    for n in numbers:
        num_sum2 += n * n
    return num_sum2


# 5
print(calc2(1, 2))
print('')

# 0
print(calc2())
print('')


# Keyword Arguments
# all arguments of Keyword Arguments will be arranged as a dict first.
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


print('')
print(person('Michael', 30))
print('')
print(person('Bob', 35, city='Beijing'))
print('')
print(person('Adam', 45, gender='M', job='Engineer'))


# if a function will restrict arguments name, it can use *.
# Then all arguments after *, it means these arguments must have when invoke the func.
# City and Job, they can have a default value, when define the function.
def person1(name, age, *, city, job):
    print(name, age, city, job)


# if a function has had a keyword arguments already,
# then it don't need to have other * followed to restrict arguments names.
def person2(name, age, *args, city, job):
    print(name, age, args, city, job)

