
a = int(input('a: '))
for i in range(2, a):
    if a % i == 0:
        print('non-prime')
        break
else:
    print('prime')

a = int(input('a: '))
flag = False
for i in range(2, a):
    if a % i == 0:
        flag = True
        break

if flag:
    print('non-prime')
else:
    print('prime')


a = int(input('a: '))
i = 2
while i < a:
    if a % i == 0:
        print('non-prime')
        break
    i = i + 1
else:
    print('prime')
