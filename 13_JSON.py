a = {}
a['a'] = {
    'a': 1,
    'b': 2,
    'c': '3'
}
a['b'] = {
    'a': 1,
    'b': 2,
    'c': '3'
}

import json
s = json.dumps(a)
print(s)
with open('a.json', 'w') as f:
    f.write(s)

r = open('a.json', 'r')
b = r.read()
y = json.loads(b)
print(y)
print(y['a']['a'])
for i, j in y.items():
    print(i, j)

