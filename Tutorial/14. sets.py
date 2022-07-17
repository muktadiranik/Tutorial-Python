U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
a = {1, 2, 3}
b = {2, 3, 4, 5, 6}
c = {5, 6, 7, 8, 9}

x = a.union(b)
print(x)

x = a.union(b, c)
print(x)

x = a | b | c
print(x)
