f = open('test.txt', 'w')
f.write('Python')
f.close()
f = open('test.txt', 'a')
f.write('\nC++')
f.close()
f = open('test.txt', 'r')
a = f.read()
print(a)
f.close()
f = open('test.txt', 'r')
a = f.read()
for i in a:
    print(i)
f.close()
f = open('python.txt', 'r')
for i in f:
    print(i)
f.close()
f = open('python.txt', 'r')
for i in f:
    tokens = i.split(' ')
    print(tokens)
f.close()
f = open('python.txt', 'r')
for i in f:
    tokens = i.split(' ')
    print(str(tokens))
f.close()
f = open('python.txt', 'r')
for i in f:
    tokens = i.split(' ')
    print(len(tokens))
f.close()
f = open('python.txt', 'r')
e = open('python_count.txt', 'w')
for i in f:
    tokens = i.split(' ')
    e.write(str(len(tokens)) + '\n' + i)
f.close()
e.close()

