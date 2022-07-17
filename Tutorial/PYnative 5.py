a = 76542
b = 0
while a > 0:
    reminder = a % 10
    b = b * 10 + reminder
    a = a // 10
print(b)

a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range(len(a)):
    if i % 2 != 0:
        print(a[i])

for i in range(0, 6):
    print(i, pow(i, 3), sep=', ')

for i in range(6):
    print(i * '*')
for i in range(4, 0, -1):
    print(i * '*')

a = -5
while True:
    if a < 0:
        print(abs(a) * '*')
    elif a > 0:
        print(a * '*')
        if a == 5:
            break
    a = a + 1

a = 0
b = 0
while True:
    if a < 5:
        print(a * '*')
    elif a >= 5:
        print((a - b) * '*')
        b = b + 2
        if a == 10:
            break
    a = a + 1



