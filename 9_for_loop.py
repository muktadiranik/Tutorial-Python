import numpy as np
a = np.arange(0, 10)
print(a)
x = 0
for i in a:
    x = x + i
print(x)

# break
# continue
for i in a:
    if i < 5:
        print(i)
    elif i == 5:
        print(i)
        continue
    else:
        break

b = np.array([-1, 0.5, 0.25, 0, 10, 50])
for i in b:
    if i < 0:
        print(i)
    elif i == 0:
        continue
    else:
        print(i)

# while
c = np.array([1, 3, 5, 7, 9, -1, -3, -5, -7, -9])
i = 0
while i < len(c):
    print(c[i], end=', ')
    i = i + 1
