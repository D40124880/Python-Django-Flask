class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *x):
        if isinstance(x, list) or isinstance(x, tuple):
            for num in range(0, len(x)):
                self.result += num
        else:
            self.result += num
        return self
    def subtract(self, *y):
        for num in y:
            self.result -= num
        return self

md = MathDojo()

print md.add(2, [2, 5, 3, 6, 8, 3]).add(2, 5, 24352, 2345, [23, 45, 12]).subtract(3, 1234, 134, 13514).result