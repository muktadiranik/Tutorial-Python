a = open('a.txt', 'r')
x = a.readlines()
print(x)
a = open('a.txt', 'r')
print(a.readable())
print(a.writable())
print(a.read())
print(a.mode)
print(len(a.read()))  # file size
a = open('a.txt', 'r')
print(a.readline())
a = open('a.txt', 'r')
print(a.readlines()[0])
a = open('a.txt', 'r')
print(a.readlines()[1])

a = open('a.txt', 'r')
for i in a:
    print(i)

a.close()



