U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
a = {1, 2, 3}
b = {2, 3, 4, 5, 6}
c = {5, 6, 7, 8, 9}

x = U.intersection(a, b)
print(x)

x = U.difference(a)
print(x)

x = a.symmetric_difference(b)
print(x)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
b = a + [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(a)

x = set(b)
print(x)
x = list(set(b))
print(x)

U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
a = [1, 2, 3]
b = {2, 3, 4, 5, 6}
c = {5, 6, 7, 8, 9}

x = set(a).difference(b)
print(x)

U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
a = {1, 2, 3}
b = {2, 3, 4, 5, 6}
c = {5, 6, 7, 8, 9}

x = U.symmetric_difference(a)
print(x)
