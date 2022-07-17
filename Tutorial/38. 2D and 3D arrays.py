from numpy import *

a = array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(a)
print(a.dtype)
print(a.ndim)
print(a.shape)
print(a.size)

b = array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(b)

c = b.flatten()
print(c)

d = c.reshape(3, 3)
print(d)

e = array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
])
print(e)

f = e.reshape(2, 3, 2)
print(f)
print(e.ndim)
e = e.reshape(2, 3, 2)
print(e)
print(e.ndim)

x = array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
x = x.reshape(2, 2, 4)
print(x)
print(x.ndim)


