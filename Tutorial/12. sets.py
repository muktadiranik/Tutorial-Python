
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
b = set(a)
print(b)

# do not allow duplicate value
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
b = set(a)
print(b)


b.update({10})
print(b)
b.update([10])
print(b)

b.remove(10)
print(b)
b.discard(12)
print(b)

x = set([1, 2, 3, 4])
print(x)
print(1 in x)
print(0 in x)

num1 = {1, 2, 3, 4}
num2 = {1, 2, 3, 4, 5, 6, 7, 8}

print(num1 | num2)
print(num1 & num2)
print(num2 - num1)
