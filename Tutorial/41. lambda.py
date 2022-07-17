def function(a, b, c):
    return a * b * c


print(function(2, 4, 6))

n = (lambda x, y, z: x * y * z)(2, 4, 6)
print(n)

a = []
for i in range(100):
    a.append(i)

print(a)

print(list(filter((lambda x: x % 2 != 0 and x <= 40), a)))
