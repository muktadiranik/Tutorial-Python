class Human:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def do_work(self):
        if self.occupation == 'player':
            print(self.name, 'play')
        elif self.occupation == 'actor':
            print(self.name, 'act')

class Class:
    def __init__(self, var_1, var_2):
        self.var_1 = var_1
        self.var_2 = var_2

    def class_function(self):
        if self.var_2 == 'a':
            print(self.var_1, 'var__a')
        elif self.var_2 == 'b':
            print(self.var_1, 'var__b')


if __name__ == '__main__':
    c = Class(1, 'a')
    c.class_function()
    d = Class(2, 'b')
    d.class_function()



