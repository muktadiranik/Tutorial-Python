a = {1: 'a', 2: 'b', 'a': 1, 'b': 2, 'x': True, (0, 0): 0}
print(a)

a = {1: {1: 'a', 2: 'b'},
     'a': {'a': 1, 'b': 2},
     'x': {'x': True, (0, 0): 0}
     }
print(a)
print(a[1])
print(a[1][1])
print(a['a']['a'])
print(a['x']['x'])

a['x']['x'] = False
print(a['x']['x'])

del a['x']['x']
print(a)

del a['x']
print(a)
