for i in range(5):
    for j in range(5):
        if i == 0 or i == 4:
            print('#', end='')
        else:
            if j == 0 or j == 4:
                print('#', end='')
            else:
                print(' ', end='')
    print()

for i in range(5, 0, -1):
    print('#' * i)

for i in range(1, 6):
    print(' ' * (5 - i), '#' * i)

for i in range(6):
    print(f'{i}' * i, end='\n')

a = 0
for i in range(6):
    for j in range(i):
        print(a, end='')
        a += 1
    print()

for i in range(5):
    print('#' * i + ' ' * (4 - i) + ' ' * (4 - i) + '#' * i)
for i in range(5):
    print('#' * (4 - i) + ' ' * i + ' ' * i + '#' * (4 - i))

for i in range(6, 1, -1):
    for j in range(1, i):
        print(j, end=' ')
    print()


for i in range(6):
    for j in range(i):
        if (i + j) % 2 != 0:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()

for i in range(5):
    print(' ' * (5 - i) + '#' * 5)

for i in range(5):
    for j in range(5, i, -1):
        print(' ', end='')
    for j in range(i):
        print(str(j) + ' ', end='')
    print()

for i in range(5):
    for j in range(5, i, -1):
        print(' ', end=' ')
    a = i
    for j in range(-1, i):
        print(str(a), end=' ')
        a = a - 1
    a = 0
    for j in range(i):
        a = a + 1
        print(str(a), end=' ')
    print()


for i in range(5):
    print(' ' * (5 - i), end='')
    print('#' * i, end='')
    print('#' * (i + 1), end='\n')
for i in range(5, -1, -1):
    print(' ' * (5 - i), end='')
    print('#' * (i + 1), end='')
    print('#' * i, end='\n')
print()
for i in range(3):
    for j in range(9):
        if i % 2 == 0 and j % 2 == 0:
            if (i + j) % 4 == 0:
                print('X', end=' ')
            else:
                print('O', end=' ')
        else:
            if (i + j) % 2 == 0:
                print('X', end=' ')
            else:
                print('O', end=' ')
    print()

a = 5
for i in range(a, 0, -1):
    print(i)
print(a)

def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x - 1)

print(factorial(5))

