
a = int (input("enter a : "))
b = int (input("enter b : "))
c = int (input("enter c : "))

if a > b and a > c :
    print(f"{a} is greater than {b} and {c}")
elif b > a and b > c :
    print(f"{b} is greater than {a} and {c}")
elif c > a and c > b:
    print(f"{c} is greater than {a} and {b}")
else:
    print(f"{a}, {b} and {c} are equal")

x = input("enter an alphabet : ")

if x == "a" or x == "e" or x == "i" or x == "o" or x == "u" :
    print(f"{x} is vowel")
else:
    print(f"{x} is consonant")