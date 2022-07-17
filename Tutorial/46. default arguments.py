def function(a, b=5):  # default argument b=5
    return a * b


print(function(2))
print(function(2, 2))  # user defined argument b=2


def function(x='x'):
    print(x)


function()
function('a')

a = [2, 4, 6]
print(max(a))
print(min(a))
print(sorted(a)[1])

x = []
for i in range(1, 50):
    x.append(i)

print(x)
print(len(x))

y = list(filter((lambda x: not x % 2), x))
print(y)

print(max(y))
print(min(y))
print(sorted(y)[(len(y) / 2).__floor__()])
print(sorted(y)[(len(y) / 2).__ceil__()])



