# inheritance
print('inheritance')


class Phone:
    def call(self):
        print('call')

    def message(self):
        print('message')


class Samsung(Phone):
    def photo(self):
        print('photo')


p = Phone()
p.call()
p.message()
s = Samsung()
s.call()
s.message()

print(issubclass(Samsung, Phone))

# method overriding
print('\nmethod overriding')


class Phone:
    def __init__(self):
        print('Phone')


class Samsung(Phone):
    def __init__(self):
        Phone().__init__()
        print('Samsung')


class Nokia(Phone):
    def __init__(self):
        super().__init__()
        print('Nokia')


class ZTE(Phone):
    def __init__(self):
        super(ZTE, self).__init__()
        print('ZTE')


s = Samsung()
n = Nokia()
z = ZTE()

# inheritance example
print('\ninheritance example')


class Shape:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        print('method of Shape class')


class Triangle(Shape):
    def area(self):
        area = 0.5 * self.height * self.width
        print('Triangle:', area)


class Rectangle(Shape):
    def area(self):
        area = self.height * self.width
        print('Rectangle:', area)


s = Shape(10, 20)
t = Triangle(10, 20)
r = Rectangle(10, 20)
s.area()
t.area()
r.area()

# multilevel inheritance
print('\nmultilevel inheritance')


class A:
    def A(self):
        print('A')


class B(A):
    def B(self):
        print('B')


class C(B):
    def C(self):
        print('C')


class D(C):
    def D(self):
        super(D, self).A()
        super(D, self).B()
        super(D, self).C()
        print('D')


c = C()
c.A()
c.B()
c.C()
d = D()
d.D()

# multiple inheritance
print('\nmultiple inheritance')


class A:
    def A(self):
        print('A')


class B:
    def B(self):
        print('B')


class C(A, B):
    pass


c = C()
c.A()
c.B()

# abstraction
print('\nabstraction')
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    @abstractmethod
    def area(self):
        pass


class Triangle(Shape):
    def area(self):
        area = 0.5 * self.height * self.width
        print('Triangle:', area)


class Rectangle(Shape):
    def area(self):
        area = self.height * self.width
        print('Rectangle:', area)


t = Triangle(10, 20)
r = Rectangle(10, 20)

t.area()
r.area()


# polymorphism
print('\npolymorphism')

print(len('string'))
print(len([1, 2, 3, 4, 5, 6]))


def add(x, y, z=0):
    return x + y + z


print(add(2, 3))
print(add(2, 3, 4))
