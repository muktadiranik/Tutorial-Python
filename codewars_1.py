
a = str(9119)
b = str(0)
b.format()
for i in a:
    b = b + str(int(i) ** 2)
print(int(b))

a = [2, 4, 8, 6, 2, 8]
print(sorted(a))
b = sorted(a)

for i in range(len(b)):
    if b[i] == 2:
        b[i] = 0
print(b)

a = [0.25, 0.50, -2, 4, 8, 16]
b = sorted(a)
print(type(a[0]))
print(b.index(4))
for i in range(len(b) - 1, -1, -1):
    print(b[i])
for i in range(len(b) - 1, -1, -1):
    if b[i] < 0 or type(b[i]) is float:
        del b[i]
print(b)
print(sum(b[:2]))
