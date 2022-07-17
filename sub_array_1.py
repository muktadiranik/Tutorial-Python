def print_sub_array():
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            for k in range(i, j + 1):
                print(arr[k], end=" ")
            print()

def maximum_sub_array_sum():
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    max_sum = -1e20
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            sub_arr_sum = 0
            for k in range(i, j + 1):
                sub_arr_sum += arr[k]
            max_sum = max(max_sum, sub_arr_sum)
    print(max_sum)

def cumulative_sub_array_sum():
    arr = [1, -4, 3, 2, 1]
    cum_sum = [0]
    max_sum = -1e20
    for i in range(1, len(arr) + 1):
        cum_sum.append(cum_sum[i - 1] + arr[i - 1])
    for i in range(1, len(arr) + 1):
        for j in range(i):
            curr_sum = cum_sum[i] - cum_sum[j]
            max_sum = max(max_sum, curr_sum)
    return max_sum

def kadane_algorithm(arr):
    max_sum = -1e10
    current_sum = 0
    for i in range(len(arr)):
        current_sum = current_sum + arr[i]
        if current_sum < 0:
            current_sum = 0
        max_sum = max(max_sum, current_sum)
    return max_sum

if __name__ == "__main__":
    print_sub_array()
    maximum_sub_array_sum()
    print(cumulative_sub_array_sum())
    arr = [1, -4, 3, 2, 1]
    print(kadane_algorithm(arr))


