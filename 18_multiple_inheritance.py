class Super_Class_1:
    def super_class_1_function(self):
        print('super_class_1')

class Super_Class_2:
    def super_class_2_function(self):
        print('super_class_2')

class Sub_Class_1(Super_Class_1, Super_Class_2):
    def sub_class_function(self):
        print('sub_class_1')


class Super_Class_3:
    def super_class_function(self):
        print('super_class_3')

class Super_Class_4:
    def super_class_function(self):
        print('super_class_4')

class Sub_Class_2(Super_Class_3, Super_Class_4):
    def sub_class_function(self):
        Super_Class_3.super_class_function(self)
        Super_Class_4.super_class_function(self)
        print('sub_class_2')

if __name__ == '__main__':
    sub_1 = Sub_Class_1()
    sub_1.super_class_1_function()
    sub_1.super_class_2_function()
    sub_1.sub_class_function()

    sub_2 = Sub_Class_2()
    sub_2.sub_class_function()
