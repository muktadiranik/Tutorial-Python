import functools


def add(a, b):
    return a + b


x = []
for i in range(1, 11):
    x.append(i)
print(x)
print(functools.reduce(add, x))
