import math


# when the return is multiple, it will return a tuple directly. And the tuple's parenthesis can be ignored.
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


# return example 1: 151.96152422706632 70.0
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)  # 151.96152422706632 70.0
print('')

#  return example 2: (151.96152422706632, 70.0)
r = move(100, 100, 60, math.pi / 6)
print(r)  # (151.96152422706632, 70.0)
