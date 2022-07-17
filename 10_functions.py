a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def list_print(x):
    b = []
    for i in x:
        print(i, end=' ')
        if i <= 5:
            b.append(i)
    print(b)


list_print(a)


print([i for i in a])




