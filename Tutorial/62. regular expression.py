import re

pattern = r"Color"
if re.match(pattern, "Color is color"):
    print(pattern)
else:
    print(0)

pattern = r"is"
if re.search(pattern, "Color is color"):
    print(pattern)
else:
    print(0)

pattern = r"color"
print(re.findall(pattern, "Color is color and Color is color"))

pattern = r"play"
text = "Chat Replay is disabled"
match = re.search(pattern, text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())

pattern = r"disabled"
text = "Chat Replay is disabled"
print(re.sub(pattern, "enabled", text))

pattern = r"disabled"
text = "Chat Replay is disabled and Chat Replay is disabled"
print(re.sub(pattern, "enabled", text, count=1))
