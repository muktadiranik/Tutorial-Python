def spiral_order_matrix():
    arr = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 8, 7, 6],
           [5, 4, 3, 2]]
    i = j = 0
    while j < 4:
        print(arr[i][j], end=" ")
        j = j + 1
    print()
    j = j - 1
    while i < 4:
        print(arr[i][j], end=" ")
        i = i + 1
    print()
    i = i - 1
    while j > -1:
        print(arr[i][j], end=" ")
        j = j - 1
    print()
    j = j + 1
    while i > -1:
        print(arr[i][j], end=" ")
        i = i - 1
    print()
    i = i + 1

def spiral_order_for_loop():
    arr = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 8, 7, 6],
           [5, 4, 3, 2]]

    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], end=" ")
        print()
    row_start = column_start = 0
    row_end = column_end = len(arr) - 1
    while row_start <= row_end and column_start <= column_end:
        for i in range(column_start, column_end + 1):
            print(arr[row_start][i], end=" ")
        row_start += 1

        for i in range(row_start, row_end + 1):
            print(arr[i][column_end], end=" ")
        column_end -= 1

        for i in range(column_end, column_start - 1, -1):
            print(arr[row_end][i], end=" ")
        row_end -= 1

        for i in range(row_end, row_start - 1, -1):
            print(arr[i][column_start], end=" ")
        column_start += 1

if __name__ == "__main__":
    spiral_order_matrix()
    print()
    spiral_order_for_loop()
