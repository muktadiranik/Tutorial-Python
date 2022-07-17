for i in range(10):
    print(i * '*')


for i in range(0, 20, 2):
    print(i * '*')


for i in range(10):
    print((2 * i - 1) * '*')


n = 10
for i in range(n + 1):
    print((n - i) * ' ', i * '*')


n = 5
for i in range(n + 1):
    print((n - i) * ' ', i * '*', '*', i * '*', (n - i) * ' ')


import random


def recursion():
    a = int(input())
    r = random.randint(0, 5)

    if a == r:
        print(True)
        return False
    else:
        print(False)
        return recursion()


recursion()
