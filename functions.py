def sum(n):
    return (n * (n + 1)) / 2

def reverse_number(x):
    reverse = 0
    while x > 0:
        reminder = x % 10
        reverse = reverse * 10 + reminder
        x = x // 10
    return reverse

def binary_search(arr, x):
    left_index = 0
    right_index = len(arr) - 1
    mid_index = (left_index + right_index) // 2
    mid_index_number = arr[mid_index]
    while left_index < right_index:
        if mid_index_number == x:
            return mid_index
        if mid_index_number > x:
            right_index = mid_index - 1
        else:
            left_index = mid_index + 1
    return -1

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

def bubble_sort_2(arr):
    n = len(arr)
    counter = 0
    while counter < n - 1:
        for i in range(n - counter - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
        counter += 1
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(i, n):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        current = arr[i]
        j = i - 1
        while arr[j] > current and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr

if __name__ == '__main__':
    print(sum(5))
    print(reverse_number(137))
    a = [2, 4, 6, 8, 10]
    print(binary_search(a, 6))
    a = [88, 102, 2, -2, 86]
    print(bubble_sort(a))
    print(bubble_sort_2(a))
    print(selection_sort(a))
    print(insertion_sort(a))
