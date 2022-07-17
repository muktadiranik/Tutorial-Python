def kadane(arr):
    curr_sum = 0
    max_sum = -1e10
    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum < 0:
            curr_sum = 0
        max_sum = max(max_sum, curr_sum)
    return max_sum

def circular_max_sub_array_sum(arr):
    total_sum = 0
    non_wrap_sum = kadane(arr)
    for i in range(len(arr)):
        total_sum = total_sum + arr[i]
        arr[i] = -arr[i]

    wrap_sum = total_sum + kadane(arr)
    return max(wrap_sum, non_wrap_sum)

if __name__ == "__main__":
    arr = [4, -4, 6, -6, 10, -11, 12]
    print(circular_max_sub_array_sum(arr))
