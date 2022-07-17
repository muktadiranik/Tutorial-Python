def array_1():
    a = [88, -88, 102, 2002, -404, 888]
    max_till_i = -88888888
    for i in range(len(a)):
        max_till_i = max(max_till_i, a[i])
        print(max_till_i, end=' ')

def sub_array_sum():
    arr = [2, 4, 6, 8, 10, 12, 14, 16]
    n = len(arr)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum = current_sum + arr[j]
            print(current_sum, end=' ')

def consecutive_difference():
    arr = [22, 44, 24, 12, 28, 12]
    for i in range(len(arr) - 1):
        print(arr[i] - arr[i + 1], end=' ')

def longest_arithmetic_sub_array():
    arr = [2, 4, 6, 88, 102, 104, 106, 108, 222, 224, 228]
    prev_diff = arr[1] - arr[0]
    ans = 2
    curr = 2
    for i in range(2, len(arr)):
        if prev_diff == arr[i] - arr[i - 1]:
            curr += 1
        else:
            prev_diff = arr[i] - arr[i - 1]
            curr = 2
        ans = max(ans, curr)
    return ans

def array_2(arr):
    n = len(arr)
    ans = 0
    max_arr = -1
    if n == 1:
        return 1
    for i in range(n - 1):
        if arr[i] > max_arr and arr[i] > arr[i + 1]:
            ans += 1
        max_arr = max(max_arr, arr[i])
    return ans


if __name__ == '__main__':
    array_1()
    print()
    sub_array_sum()
    print()
    consecutive_difference()
    print()
    print(longest_arithmetic_sub_array())
    arr = [0, 2, 6, 2, 0, 8, -1]
    print(array_2(arr))
