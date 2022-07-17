def matrix_search(arr, x):
    n = len(arr)
    m = len(arr[0])
    row = 0
    column = m - 1
    while row < n and column >= 0:
        if arr[row][column] == x:
            return True
        elif arr[row][column] > x:
            column -= 1
        else:
            row += 1
    return False

if __name__ == "__main__":
    arr = [[1, 4, 7, 10],
           [2, 5, 8, 11],
           [3, 6, 9, 12]]
    x = 12
    print(matrix_search(arr, x))
