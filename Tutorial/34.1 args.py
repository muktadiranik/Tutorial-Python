def function(*args):
    a = 1
    for i in args:
        a = a * i
    return a


print(function(1, 2, 3, 4, 5))


def function(*n):
    a = 0
    for i in n:
        a = a + i
    return a


print(function(1, 2, 3, 4, 5))
