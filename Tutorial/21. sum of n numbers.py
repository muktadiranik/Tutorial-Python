n = int(input('enter last number:'))
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i + 1
print(sum)

'''sum of even numbers'''
n = int(input('enter last even number:'))
sum = 0
i = int(input('enter starting even number:'))
while i <= n:
    sum = sum + i
    i = i + 2 
print(sum)
