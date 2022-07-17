class X:
    def __init__(self, name, a, b):
        self.name = name
        self.a = a
        self.b = b

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.a < other.a

    def __gt__(self, other):
        return self.b > other.b


x = X('name', 0, 0)
print(str(x))
y = X('name', 0, 0)
print(x == y)
a = X('name', 0, 1)
b = X('name', 1, 0)
print(a < b)
print(a > b)








