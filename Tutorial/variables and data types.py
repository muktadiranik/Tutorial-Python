string = "X"
int = 0
float = 0.0

print("string variable is", string)
print("integer variable is", int)
print("float variable is", float)

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print(' ')

n = 5
for i in range(n):
    for j in range(n - i, 0, -1):
        print(j, end=' ')
    print(' ')

for i in range(5):
    for j in range(1, i + 1):
        print(j, end=' ')
    print(' ')
else:
    print(True)

for i in range(5):
    print(i, end=' ')
    print()


for i in range(25, 50):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=' ')
