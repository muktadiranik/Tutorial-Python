for i in range(10):
    print(i, i - 1, i + (i - 1))

a = 'characters'
for i in a:
    print(i, end=' ')

print(len(a))
for i in range(0, len(a)):
    if i % 2 == 0:
        print(a[i], end=' ')

print('\n')


def remove_chars(word, n, m):
    x = word[n:m]
    return x


print(remove_chars('characters', 0, 5))

a = [10, 20, 30, 40, 10]
b = [75, 65, 35, 75, 30]

print(len(a))
print(a[-1])
print(a[4])


def first_last_same(x):
    first_num = x[0]
    last_num = x[-1]

    if first_num == last_num:
        return True
    else:
        return False


print(first_last_same(a))
print(first_last_same(b))

a = [10, 20, 33, 46, 55]

for i in range(0, len(a)):
    if a[i] % 5 == 0:
        print(a[i], end=' ')

str_x = "Emma is good developer. Emma is a writer"
print(str_x.count("Emma"))

for i in range(1, 6):
    for j in range(0, i):
        print(i, end=' ')
    print(' ')

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]


a = list(filter((lambda x: x % 2 != 0), list1))
print(a)
b = list(filter((lambda x: x % 2 == 0), list2))
print(b)
c = a + b
print(c)

a = 7536
print(a)
while a > 0:
    x = a % 10
    a = a // 10
    print(x, end=' ')


def income_tax(x):
    print('income:', x)
    tax = 0
    y = 0
    if x <= 10000:
        tax = 0
        return tax
    elif x <= 20000:
        y = x - 10000
        tax = y * 10 / 100
        return tax
    else:
        tax = 10000 * 10 / 100
        tax += (x - 20000) * 20 / 100
        return tax


print(income_tax(45000))
print(income_tax(30000))

for i in range(5, 0, -1):
    print(i * '*')


def exponent(base, exp):
    return base ** exp


print(exponent(2, 5))
print(exponent(5, 4))
