def pair_sum(arr, k):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == k:
                print(i, j)
                return True
    return False


def pair_sum_efficient(arr, k):
    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] + arr[j] == k:
            print(i, j)
            return True
        if arr[i] + arr[j] > k:
            i = i + 1
        else:
            j = j - 1
        if i == j:
            break
    return False



if __name__ == "__main__":
    arr = [1, 5, 9, 11, 15, 30]
    k = 20
    print(pair_sum(arr, k))
    print(pair_sum(arr, k))
    for i in range(5, 0, -1):
        print(i)
