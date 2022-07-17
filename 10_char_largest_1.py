def largest_word():
    arr = input("arr: ")
    arr = arr.split(" ")
    arr_len = [len(i) for i in arr]
    arr_sorted = [x for y, x in sorted(zip(arr_len, arr))]
    print(arr_sorted[-1])

def largest():
    arr = "large"
    i = 0
    curr_len = 0
    max_len = 0
    while i < len(arr):
        if arr[i] == " " or arr[i] == arr[-1]:
            if curr_len > max_len:
                max_len = curr_len + 1
                end = i
            curr_len = 1
        else:
            curr_len += 1
        i += 1
    start = end - max_len + 1
    for i in range(max_len):
        print(arr[i + start], end="")
    print()
    print(max_len)

if __name__ == "__main__":
    largest()
