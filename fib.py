import types


# fill in this function
def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b


if isinstance(fib(), types.GeneratorType):
    print("Good, The fib function is a generator.")
    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break
