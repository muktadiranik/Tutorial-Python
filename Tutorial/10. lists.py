
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(a)

b = [1, [2, 3, 4, 5], 6, 7, 8, 9, 0]
print(b)
print(b[0])
print(b[1])
print(b[1][1])

a = a + [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(a)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
a.remove(0)
print(a)

b = [1, [2, 3, 4, 5], 6, 7, 8, 9, 0]
print(b)
b.remove(b[1])
print(b)

b = [1, [2, 3, 4, 5], 6, 7, 8, 9, 0]
print(b.count([2, 3, 4, 5]))
print(b.count(6))


a = list(input('a: '))

print(a)
a = input('a: ')
list = a.split()
print(list)
for i in list:
    print(i)
