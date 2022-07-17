a = 2
if type(a) is int:
    print(a)
if a % 2 == 0:
    print(a)

print(type(a))

import numpy as np
a = np.arange(0, 10)
b = np.arange(10, 20)
c = np.arange(20, 30)

x = int(input('x: '))
if x in a:
    print(a)
elif x in b:
    print(b)
elif x in c:
    print(c)
else:
    print(x)
