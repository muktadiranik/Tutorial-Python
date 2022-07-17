a = float(input("enter marks : "))

if a >= 80 and a <= 100:
    print("A+")
elif a >= 70 and a < 80:
    print("A")
elif a >= 60 and a < 70:
    print("A-")
elif a >= 50 and a < 60:
    print("B")
elif a >= 40 and a < 50:
    print("C")
elif a >= 33 and a < 40:
    print("D")
elif a >= 0 and a < 33:
    print("F")
else:
    print("invalid marks input")

a = float(input("enter marks : "))

if 80 <= a <= 100:
    print("A+")
elif 70 <= a < 80:
    print("A")
elif 60 <= a < 70:
    print("A-")
elif 50 <= a < 60:
    print("B")
elif 40 <= a < 50:
    print("C")
elif 33 <= a < 40:
    print("D")
elif 0 <= a < 33:
    print("F")
else:
    print("invalid marks input")
