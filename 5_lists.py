a = 'a'
b = 'b'
c = 'c'
x = ['a', 'b', 'c']
print(x)
x[0] = 'A'
print(x)
print(x[-1])
x.append('d')
print(x)
x.insert(1, 'a')
print(x)
y = [1, 2, 3, 4, 5]
print(x + y)
x.extend(y)
print(x)
print('A' in x)
print('B' not in x)
