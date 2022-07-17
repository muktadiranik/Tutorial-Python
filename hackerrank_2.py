arr = [-4, 3, -9, 0, 4, 1]

positive = negative = zero = 0
x = len(arr)
for i in range(len(arr)):
    if arr[i] > 0:
        positive += 1
    elif arr[i] < 0:
        negative += 1
    else:
        zero += 1
print('{0:.6f}'.format(positive / x))
print('{0:.6f}'.format(negative / x))
print('{0:.6f}'.format(zero / x))
