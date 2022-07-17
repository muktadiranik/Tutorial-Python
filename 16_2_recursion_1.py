def is_sorted(arr):
    flag = False
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)):
        flag = True

    return flag

def increasing(n):
    if n == 0:
        return
    increasing(n - 1)
    print(n, end=" ")

def decreasing(n):
    if n == 0:
        return
    print(n, end=" ")
    decreasing(n - 1)

def first_occurrence(arr, i, key):
    if i == len(arr):
        return -1
    if arr[i] == key:
        return i
    return first_occurrence(arr, i + 1, key)

def last_occurrence(arr, i, key):
    if i == len(arr):
        return -1
    rest_arr = last_occurrence(arr, i + 1, key)
    if rest_arr != -1:
        return rest_arr
    if arr[i] == key:
        return i
    return -1

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    arr = [1, 2, 3, 4, 5, 2, 6, 7, 8, 2, 9, 0]
    print(first_occurrence(arr, 0, 2))
    print(last_occurrence(arr, 0, 2))
