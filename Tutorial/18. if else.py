a = 100
b = 200
if a < b:
    print('a < b')

a = 50
b = 50
if a > b:
    print('a > b')
elif a == b:
    print('a == b')

a = 100
b = 200
if a == b:
    print('a == b')
else:
    print('a < b')

a = 200
b = 100
c = 300
if a > b and c > a:
    print('a > b & c > a')

if a > b or a > c:
    print('a > b')
