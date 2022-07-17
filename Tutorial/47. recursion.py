
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(15)


x = 0


def recursion():
    global x
    print(x)
    x = x + 1
    if x < 5:
        recursion()
    else:
        return False


recursion()



x = 0


def function():
    global x
    x = x + 1
    print('x: ', x)
    function()


function()


def recursion():
    a = int(input('a: '))
    b = int(input('b: '))
    if a < b:
        return recursion()
    else:
        return False


recursion()






