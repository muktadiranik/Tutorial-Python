a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
if a == b:
    if a > c:
        print(a, b)
    elif a < c:
        print(c)
    else:
        print(a, b, c)
elif a == c:
    if a > b:
        print(a, c)
    elif a < b:
        print(b)
    else:
        print(a, b,  c)
elif b == c:
    if b > a:
        print(b, c)
    elif b < a:
        print(a)
    else:
        print(a, b, c)
elif a > b:
    if a > c:
        print(a)
    else:
        print(c)
elif b > a:
    if b > c:
        print(b)
    else:
        print(c)
else:
    print(a, b, c)

if a > b and b > c and a > c:
    print(a)
elif a > b and b < c and a > c:
    print(c)
elif a == b or a == c or b == c:
    print('')
else:
    print(b)
