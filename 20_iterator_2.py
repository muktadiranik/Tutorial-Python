class Iteration:
    def __init__(self):
        self.element = ['A', 'B', 'C', 'D']
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.element):
            raise StopIteration
        return self.element[self.index]

if __name__ == '__main__':
    i = Iteration()
    itr = iter(i)
    print(next(i), next(i))


