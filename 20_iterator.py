a = ['a', 'b', 'c', 'd']
for i in a:
    print(i)
print(dir(a))
itr = iter(a)
print(itr)
print(next(itr), next(itr), next(itr), next(itr))

itr = reversed(a)
print(next(itr))
