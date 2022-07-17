def biggest_number(s):
    a = [str(int(i)) for i in s]
    a = sorted(a, reverse=True)
    a = "".join(a)
    return a

def max_count_char(s):
    count_dict = {}
    for i in s:
        if i in count_dict.keys():
            count_dict[i] = count_dict[i] + 1
        else:
            count_dict[i] = 1
    return sorted([(value, key) for (key, value) in count_dict.items()], reverse=True)[0]

if __name__ == "__main__":
    s = "12345"
    print(biggest_number(s))
    s = "ABCABCABCA"
    print(max_count_char(s))

