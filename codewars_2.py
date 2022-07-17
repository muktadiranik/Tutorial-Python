def duplicate_encode(word):
    word = word.lower()
    a = []
    for i in word:
        b = 0
        for j in word:
            if i == j:
                b += 1
            else:
                pass
        a.append(b)
    c = ''
    for i in range(len(word)):
        if a[i] == 1:
            c += '('
        else:
            c += ')'
    return c

print(duplicate_encode('Success'))

def find_outlier(integers):
    odd = even = 0
    for i in range(len(integers)):
        if integers[i] % 2 == 0:
            even += 1
        else:
            odd += 1
    if even > odd:
        for i in range(len(integers)):
            if integers[i] % 2 != 0:
                return integers[i]
    else:
        for i in range(len(integers)):
            if integers[i] % 2 == 0:
                return integers[i]

a = [2, 4, 0, 100, 4, 11, 2602, 36]
b = [160, 3, 1719, 19, 11, 13, -21]
print(find_outlier(a))
print(find_outlier(b))

def order(sentence):
    o = []
    sentence = sentence.split(' ')
    for i in sentence:
        for j in i:
            if 48 < ord(j) < 58:
                o.append(ord(j) - 49)

    p = [x for y, x in sorted(zip(o, sentence))]
    p = ' '.join([i for i in p])

    return p

a = "4of Fo1r pe6ople g3ood th5e the2"
print(order(a))


