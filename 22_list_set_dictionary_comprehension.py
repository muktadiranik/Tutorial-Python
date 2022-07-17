def list():
    a = [1, 2, 3, 4, 5, 6]
    b = [i for i in a if i % 2 == 0]
    c = [i ** 2 for i in a]
    print(c)


def set_comprehension():
    a = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    b = {i for i in a if i % 2 == 0}
    c = {i ** 2 for i in a}
    print(c)


def dict_comprehension():
    a = ["A", "B", "C"]
    b = [1, 2, 3]
    c = zip(a, b)
    d = {a: b for a, b in zip(a, b)}
    print(d)


if __name__ == "__main__":
    dict_comprehension()
