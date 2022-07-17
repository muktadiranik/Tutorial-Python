
a = int (input("enter a : "))
b = int (input("enter b : "))
c = int (input("enter c : "))

if a > b :
    if a > c :
        print(f"{a} is greater than {b} and {c}")
    else:
        print(f"{c} is greater than {a} and {b}")

elif b > a :
    if b > c :
        print(f"{b} is greater than {a} and {c}")
    else:
        print(f"{c} is greater than {a} and {b}")
else:
    print(f"{a}, {b} and {c} are equal")