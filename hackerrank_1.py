a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

x = y = 0
for i in range(len(a)):
    for j in range(len(a)):
        if i == j:
            print(a[i][j])
            x += a[i][j]


for i in range(len(a)):
    for j in range(len(a)):
        if i == j:
            print(a[i][-j - 1])
            y += a[i][-j - 1]
print(abs(x - y))

