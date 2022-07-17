arr = [1, 3, 5, 7, 9]

print(sum(arr))
a = sum(arr)
sum_arr = []
for i in range(len(arr)):
    sum_arr.append(a - arr[i])
print(f'{min(sum_arr)}  {max(sum_arr)}')

