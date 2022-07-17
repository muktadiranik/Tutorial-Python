a = {'a': 1, 'b': 2, 'c': 2, 'd': 4}
print(a)
print(a['b'])

b = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
print(b)

c = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 'a': 1, 'b': 2, 'c': 2, 'd': 4, 'x': True, (0, 0): 0}
print(c)

x = c.copy()
print(x)

x = len(c)
print(x)

a['a'] = 0
print(a)

a.pop('a')
print(a)

a.clear()
print(a)

del a  # delete a dictionary

a = {
    'a': 1, 'b': 2,
    1: 'a', 2: 'b',
    'x': True, 'y': False
}
print(a)
print(a.get('a', False))
print(a.get('c', False))
print(a.keys())
print(a.keys())
print(a.values())
a.__setitem__('c', 3)
print(a)
print(a.__getitem__('a'))

