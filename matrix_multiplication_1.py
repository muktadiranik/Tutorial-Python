def matrix_multiplication():
    a = [[1, 2, 3],
         [4, 5, 6]]
    b = [[1, 2],
         [3, 4],
         [5, 6]]
    c = [[0, 0],
         [0, 0]]

    for i in range(len(c)):
        for j in range(len(a)):
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]

    for i in range(len(c)):
        for j in range(len(c)):
            print(c[i][j], end=" ")
        print()

if __name__ == "__main__":
    matrix_multiplication()
