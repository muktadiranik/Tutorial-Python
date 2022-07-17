
a = [1, 2, 3, 4, 5]
for i in a:
    print(i)

sum = 0
for i in a:
    sum = sum + i
print(sum)

for i in range(1, 6):
    print(i)

a = list(range(1, 6))
print(a)
for i in a:
    print(i)

x = 0
for i in range(1, 6):
    x += i
    print(i, x)
print(x)

x = 0
for i in range(1, 11):
    if i % 2 == 0:
        x += i
        print(i, x)
    print(i, x)
print(x)

a = "Beginners"
for i in a:
    print(i)
