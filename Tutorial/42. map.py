def multiply(x):
    return x * 5


a = [1, 2, 3, 4, 5]
n = []

for i in a:
    n.append(multiply(i))
print(n)

print(list(map(multiply, a)))


def add(a, b):
    return a + b


x = []
for i in range(1, 6):
    x.append(i)
print(x)
y = []
for i in range(1, 6):
    y.append(i)
print(y)
print(list(map(add, x, y)))
