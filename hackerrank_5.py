candles = [4, 4, 1, 3]
a = max(candles)
max_count = 0
for i in range(len(candles)):
    if candles[i] == a:
        max_count += 1

print(max_count)

def timeConversion(s):
    h = s.split(':')[0]
    m = s.split(':')[1]
    sec = s.split(':')[2][:2]
    c = s.split(':')[2][2:4]
    if c == 'PM':
        if h == '12':
            return h + ':' + m + ':' + sec
        h = int(h)
        h = (h + 12) % 24
        if h == 0:
            h = str(h)
            h = '0' + h
        h = str(h)
    if c == 'AM':
        if h == '12':
            h = '00'
    p = h + ':' + m + ':' + sec
    return p

print(timeConversion('12:40:22AM'))

import math
a = [33, 44, 66, 84]
def gradingStudents(grades):
    for i in range(len(grades)):
        if math.ceil(grades[i] / 5) * 5 >= 40:
            if (math.ceil(grades[i] / 5) * 5) - grades[i] < 3:
                grades[i] = math.ceil(grades[i] / 5) * 5
    return grades
print(a)
print(gradingStudents(a))




