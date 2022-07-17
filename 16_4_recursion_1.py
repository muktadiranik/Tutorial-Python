def permutation(string, ans):
    if len(string) == 0:
        print(ans)
        return
    for i in range(len(string)):
        ch = string[i]
        rest_s = string[0: i] + string[i + 1:]
        permutation(rest_s, ans + ch)

def count_path(start, end):
    if start == end:
        return 1
    if start > end:
        return 0
    dice = 6
    count = 0
    for i in range(1, dice + 1):
        count += count_path(start + i, end)
    return count

def count_path_maze(n, i, j):
    if i == n and j == n:
        return 1
    if i >= n - 1 or j >= n - 1:
        return 0
    return count_path_maze(n, i + 1, j) + count_path_maze(n, i, j + 1)

def knapsack(value, weight, n, W):
    if n == 0 or W == 0:
        return 0
    if weight[n - 1] > W:
        return knapsack(value, weight, n - 1, W)
    return max(knapsack(value, weight, n - 1, W - weight[n - 1]) + value[n - 1], knapsack(value, weight, n - 1, W))

if __name__ == "__main__":
    # permutation("ABC", "")
    # print(count_path(1, 4))
    # print(count_path_maze(4, 0, 0))
    value = [50, 150, 250, 350]
    weight = [10, 20, 30, 40]
    W = 60
    n = 4
    print(knapsack(value, weight, n, W))
