with open('test.txt', 'r') as a:
    lines = a.readlines()

with open('new_file.txt', 'w') as b:
    count = 0
    for line in lines:
        if count == 4:
            count += 1
            continue
        else:
            b.write(line)
        count += 1
