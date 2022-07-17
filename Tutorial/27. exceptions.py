a = int(input('a: '))
b = int(input('b: '))

try:
    print(a / b)
except Exception as e:
    print(e)
print(a, b)


a = int(input('a: '))
b = int(input('b: '))

try:
    print('begin')
    print(a / b)
except Exception as e:
    print(e)
finally:
    print('end')
print(a, b)

a = int(input('a: '))
b = int(input('b: '))

try:
    print('begin')
    print(a / b)
    x = int(input('x: '))
except ZeroDivisionError as z:
    print(z)
except ValueError as v:
    print(v)
finally:
    print('end')
print(a, b)

a = int(input('a: '))
b = int(input('b: '))

try:
    print('begin')
    print(a / b)
    x = int(input('x: '))
except Exception as e:
    print(e)
finally:
    print('end')
print(a, b, x)


def f(x):
    if x < 20:
        raise Exception('Exception')
    return True


print(f(20))
print(f(22))
try:
    print(f(18))
except Exception as e:
    print(e)
finally:
    print('end')
