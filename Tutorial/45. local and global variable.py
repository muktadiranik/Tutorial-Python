a = 100  # global variable


def function():
    a = 500  # local variable
    print(a)
    print(id(a))


function()


def function():
    global a
    a = a + 100
    print(a)
    print(id(a))


function()

x = 1000  # global variable


def function():
    y = x + 500
    print(y)
    print(id(x))
    print(id(y))


function()
