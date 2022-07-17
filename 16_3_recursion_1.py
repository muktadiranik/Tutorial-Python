def reverse(string):
    if len(string) == 0:
        return
    rest_str = string[1:]
    reverse(rest_str)
    print(string[0], end="")

def replace(string):
    if len(string) == 0:
        return
    if string[0] == 'p' and string[1] == 'i':
        print("3.1416", end="")
        replace(string[2:])
    else:
        print(string[0], end="")
        replace(string[1:])

def tower_of_hanoi(n, src, des, helper):
    if n == 0:
        return
    tower_of_hanoi(n - 1, src, helper, des)
    print(src, " to ", des)
    tower_of_hanoi(n - 1, helper, des, src)

def remove_duplicate(string):
    if len(string) == 0:
        return ""
    ch = string[0]
    removed = remove_duplicate(string[1:])
    if len(removed) != 0 and ch == removed[0]:
        return removed
    return ch + removed

def move_all_to_end(string, x):
    if len(string) == 0:
        return ""
    ch = string[0]
    rest_s = move_all_to_end(string[1:], x)
    if ch == x:
        return rest_s + ch
    return ch + rest_s

def subsequence(string, ans):
    if len(string) == 0:
        print(ans)
        return
    ch = string[0]
    rest_s = string[1:]
    subsequence(rest_s, ans)
    subsequence(rest_s, ans + ch)

def subsequence_ascii(string, ans):
    if len(string) == 0:
        print(ans)
        return
    ch = string[0]
    rest_s = string[1:]
    value = ord(ch)
    subsequence_ascii(rest_s, ans)
    subsequence_ascii(rest_s, ans + ch)
    subsequence_ascii(rest_s, ans + str(value))

key_arr = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
def keypad(string, ans):
    if len(string) == 0:
        print(ans)
        return
    ch = string[0]
    rest_s = string[1:]
    value = key_arr[ord(ch) - ord('0')]
    for i in range(len(value)):
        keypad(rest_s, ans + value[i])

if __name__ == "__main__":
    s = "pippxxpippxxpi"
    keypad("23", "")


