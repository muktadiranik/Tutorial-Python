def set_example():
    a = set()
    a.add(1)
    a.add(2)
    print(a)
    b = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
    print(b)
    b = list(set(b))
    print(b)

def frozen_set():
    a = {1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6}
    a = frozenset(a)
    print(a)

if __name__ == "__main__":
    set_example()
    frozen_set()
