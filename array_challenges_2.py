def sub_array_given_sum():
    arr = [1, 2, 3, 8]
    s = 5
    test_sum = 0
    i = j = 0
    while test_sum + arr[j] <= s and j < len(arr):
        test_sum = test_sum + arr[j]
        j = j + 1
    if test_sum == s:
        print(i, j - 1)
        return
    while i < j:
        test_sum = test_sum + arr[j]
        while test_sum > s:
            test_sum = test_sum - arr[i]
            i = i + 1
        if test_sum == s:
            print(i, j)
            break

def smallest_positive_missing_number():
    arr = [-2, 0, 1, 3, -5, 6]
    check = []
    for i in range(1000):
        check.append(False)
    for i in range(len(arr)):
        if arr[i] >= 0:
            check[arr[i]] = True
    for i in range(1, 1000):
        if not check[i]:
            print(i)
            return


if __name__ == "__main__":
    sub_array_given_sum()
    smallest_positive_missing_number()

