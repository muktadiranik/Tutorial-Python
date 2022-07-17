def f(x, y):
    print(__name__)
    return x * y

def calculate_area(base, height):
    print(__name__)
    return (1 / 2) * base * height

if __name__ == '__main__':
    a = 5
    b = 10
    print(f(a, b))
    print(calculate_area(a, b))
