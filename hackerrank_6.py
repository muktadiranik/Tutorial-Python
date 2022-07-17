def countApplesAndOranges(s, t, a, b, apples, oranges):
    a_apples = []
    b_oranges = []

    for i in apples:
        a_apples.append(a + i)

    for i in oranges:
        b_oranges.append(b + i)

    apples_count = oranges_count = 0

    for i in a_apples:
        if s <= i <= t:
            apples_count += 1

    for i in b_oranges:
        if s <= i <= t:
            oranges_count += 1

    print(apples_count)
    print(oranges_count)


def kangaroo(x1, v1, x2, v2):
    if v1 > v2 and (x2 - x1) % (v1 - v2) == 0:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    countApplesAndOranges(0, 0, 4, 8, [10, -4, 8], [8, 12, -4])
    print(kangaroo(1571, 4240, 9023, 4234))
