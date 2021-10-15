class Fibonacci(object):
    def __init__(self, n):
        self.n = n
        self.num1 = self.num2 = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count <= self.n:
            x = self.num1
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            return x
        else:
            raise StopIteration


# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
f = Fibonacci(12)
# print(f)
for i in f:
    print(i)

# 有列表了，为什么还要有生成器呢？
# 迭代器: 占时间，不占用空间，以时间换空间，有极限
# 列表: 占空间，不占时间，以空间换时间

# 会申请一块内存空间，用来保存 1~1000000 的数字
# nums = [i for i in range(1000000)]
# print(nums)

# 不会开辟内存空间存储数据
for j in range(1000000):
    print(j)
