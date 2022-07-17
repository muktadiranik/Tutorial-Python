class Super_Class:
    def super_class_function(self):
        print('super_class')

class Sub_Class_1(Super_Class):
    def __init__(self):
        print('sub_class_1')
        self.name = 'sub_class_1'
        self.number = 1

    def sub_class_function(self):
        self.super_class_function()
        print(self.name, self.number)

class Sub_class_2(Super_Class):
    def __init__(self):
        print('sub_class_2')
        self.name = 'sub_class_2'
        self.number = 2

    def sub_class_function(self):
        self.super_class_function()
        print(self.name, self.number)


if __name__ == '__main__':
    sub_1 = Sub_Class_1()
    sub_1.sub_class_function()
    sub_2 = Sub_class_2()
    sub_2.sub_class_function()
