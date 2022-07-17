a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(a)
a.pop()
print(a)
print(a.__getitem__(0))
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while a:
    a.pop()
    print(a)

from collections import deque
a = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(a)
a.popleft()
print(a)
while a:
    a.popleft()
    print(a)


def stack():
    a = input()
    a = a.split()
    b = deque(a)
    for i in a:
        print(i, sep=', ', end=' ')

    while a:
        a.pop()
        print(a)

    while b:
        b.popleft()
        print(b)



stack()
