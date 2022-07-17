a = int(input("enter number : "))

if a >= 80:
    print("A+")
elif a >= 70:
    print("A")
elif a >= 60:
    print("A-")
elif a >= 50:
    print("B")
elif a >= 40:
    print("C")
elif a >= 33:
    print("D")
else:
    print(f"{a} is below 33")
