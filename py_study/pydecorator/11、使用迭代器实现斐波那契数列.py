class Fibonacci(object):
    def __init__(self, n):
        self.n = n
        self.num1 = self.num2 = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.n:
            self.count += 1
            x = self.num1
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            return x
        else:
            raise StopIteration


# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
f = Fibonacci(12)
for i in f:
    print(i)
