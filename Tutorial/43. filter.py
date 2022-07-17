a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(filter((lambda x: x % 2), a)))
print(list(filter((lambda x: x % 3 == 0), a)))

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(filter((lambda x: x * 0), a)))
print(list(filter((lambda x: x * 1), a)))

x = []
for i in range(1, 100):
    x.append(i)
print(x)

print(list(filter((lambda x: x % 3 == 0 and x <= 30), x)))
print(list(filter((lambda x: x % 9 == 0 and x <= 90), x)))
print(list(filter((lambda x: not x % 3 and x <= 30), x)))
