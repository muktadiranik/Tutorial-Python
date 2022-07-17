import numpy as np
a = ([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

b = ([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(np.add(a, b))
print(np.subtract(a, b))
print(np.multiply(a, b))
print(np.dot(a, b))

from numpy import *
a = array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
c = mat(a)

b = array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
d = mat(b)


print(dot(c, d))

x = mat([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
y = mat([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(dot(x, y))
