i = 1
while i <= 100:
    print(i)
    i = i + 1
    if i == 40:
        break
print('end')

i = 1
while i <= 100:
    i = i + 1
    if i % 2 == 1:
        continue
    print(i)
print('end')
