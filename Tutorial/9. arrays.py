from array import *

a = array('i', [1, 2, 3, 4, 5, 6])
print(a)
print(a[0:4])

# for loop
for i in range(6):
    print(a[i])

# memory address
print(a.buffer_info())

# reverse array
a.reverse()
print(a)


print(a.__len__())
a.append(0)
print(a)
a.remove(0)
print(a)

a = array('i', [1, 2, 3, 4, 5, 6])
a.extend([7, 8, 9, 0])
print(a)
for i in range(10):
    print(a[i])

# return the index number of an element
print(a.index(2))

a.insert(0, 12)
print(a)

# pop element at specified position
a.pop(0)
print(a)

a = [1, 2, 3, 4, 5, 6]
a.sort()
print(a)
