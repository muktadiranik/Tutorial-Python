import sys
# tuple
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(a)
print(b)

print(sys.getsizeof(a))
print(sys.getsizeof(b))

del a

a = (
    'a', 'b', 'c', 'd', 'a'
)
print(a)
print(a.__len__())
print(a.count('a'))
b = (1, 2, 3, 4, 5, 6)
c = a.__add__(b)
print(a)
print(a.__add__(b))
print(c)
print(c[1: 4])
print(c[-1])
