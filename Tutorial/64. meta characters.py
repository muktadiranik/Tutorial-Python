import re

pattern = r"dis..led"
text = "disabled"

if re.match(pattern, text):
    print(True)
else:
    print(False)

pattern = r"^dis..led$"
text = "disabled"
if re.match(pattern, text):
    print(True)
else:
    print(False)

pattern = r"(dis)*"  # * means 0 or more
text = "disabled"
if re.match(pattern, text):
    print(True)
else:
    print(False)


pattern = r"(dis)+"  # + means 1 or more
text = "disabled"
if re.match(pattern, text):
    print(True)
else:
    print(False)


pattern = r"d*i+s+"  # + means 1 or more
text = "disabled"
if re.match(pattern, text):
    print(True)
else:
    print(False)

pattern = r"di(-)?s"  # ? means 0 or 1
text = "disabled"
if re.match(pattern, text):
    print(True)
else:
    print(False)

pattern = r"d{1,2}$"  # + means 1 or more
text = "d"
if re.match(pattern, text):
    print(True)
else:
    print(False)

pattern = r"[dis]"
text = "disabled"

if re.match(pattern, text):
    print(True)
else:
    print(False)


pattern = r"[A-Z][a-z][0-9]"
text = "Aa0"

if re.match(pattern, text):
    print(True)
else:
    print(False)
