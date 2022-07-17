
a = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]
b = [x % 3 != 0 for x in a]
print(b)
c = [x for x in a if x % 3 == 0 and x < 30]
print(c)
