def is_safe(arr, x, y, n):
    if x < n and y < n and arr[x][y] == 1:
        return True
    return False

def rat_in_maze(arr, x, y, n, sol_arr):
    if x == n - 1 and y == n - 1:
        sol_arr[x][y] = 1
        return True
    if is_safe(arr, x, y, n):
        sol_arr[x][y] = 1
        if rat_in_maze(arr, x + 1, y, n, sol_arr):
            return True
        if rat_in_maze(arr, x, y + 1, n, sol_arr):
            return True
        sol_arr[x][y] = 0
        return False
    return False
import numpy as np
if __name__ == "__main__":
    sol_arr = np.array(np.zeros((5, 5)))
    arr = [[1, 0, 1, 0, 1],
           [1, 1, 1, 1, 1],
           [0, 1, 0, 1, 0],
           [1, 0, 0, 1, 1],
           [1, 1, 1, 0, 1]]
    if rat_in_maze(arr, 0, 0, 5, sol_arr):
        print(sol_arr)

