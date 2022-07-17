a = ['a', 'b', 'c', 'd']
x = [1, 2, 3, 4]
print(a[0])

print(list(zip(a, x)))
print(list(zip('1234', a, x)))

a = [('1', 'a', 1), ('2', 'b', 2), ('3', 'c', 3), ('4', 'd', 4)]

print(list(zip(*a)))
print(list(zip(*a))[0])
print(list(zip(*a))[1])
print(list(zip(*a))[2])

a = ['a', 'b', 'c', 'd']
x = [1, 2, 3, 4]
z = [False, True, True, False]
print(list(zip(a, x, z)))

