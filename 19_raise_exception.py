try:
    raise Exception('exception')
except Exception as e:
    print(e)

class Error(Exception):
    def __init__(self, message):
        self.message = message

    def print_exception(self):
        print(self.message)

    def handle_exception(self):
        print(self.message, 'handle_exception')

try:
    raise Error('error')
except Error as e:
    e.print_exception()

try:
    raise Error('error')
except Error as e:
    e.handle_exception()
finally:
    print('pass')

f = open('a.json', 'r')
f.close()
try:
    f = open('a.json', 'r')
    print(5 / 0)
    raise Exception('divide by zero')
except Exception as e:
    print(e)
finally:
    for i in f:
        print(i)
    f.close()

