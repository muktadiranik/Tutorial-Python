def generator():
    yield "A"
    yield "B"
    yield "C"

def fibonacci(n):
    a = 0
    b = 1
    c = 0
    print(a, b, sep=" ", end=" ")
    while c <= n:
        c = a + b
        a = b
        b = c
        print(c, end=" ")

def fibonacci_yield():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    itr = generator()
    for i in range(3):
        print(next(itr), end=" ")
    print()
    for i in generator():
        print(i, end=" ")
    print()
    for i in fibonacci_yield():
        print(i, end=" ")
        if i > 55:
            break
