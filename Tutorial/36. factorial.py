def factorial(a):
    initial = 1
    for i in range(1, a + 1):
        initial = initial * i
    print(initial)


factorial(5)

a = 5
initial = 1
for i in range(1, a + 1):
    initial = initial * i
print(initial)

import math

a = 5
print(math.factorial(a))

a = 5
initial = 1
while a > 0:
    initial = initial * a
    a = a - 1
print(initial)

a = 5
initial = 1
i = 1
while i <= a:
    initial = initial * i
    i = i + 1
print(initial)
