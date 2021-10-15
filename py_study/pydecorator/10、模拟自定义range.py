class MyRange(object):
    def __init__(self, end: int, start: int = 0, step: int = 1):  # 如果只给一个值，start表示结束
        # if start ==0:
        #     self.start = start
        #     self.end = end
        # else:
        #     self.start, self.end = end, start
        if start != 0:
            start, end = end, start
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        # x = self.start  # 判断已经返回的值，应该是上一个start的值
        # self.start += self.step
        # if x < self.end:
        #     return x
        if self.start < self.end:
            self.start += self.step
            return self.start - self.step
        raise StopIteration


m = MyRange(1, 21, 3)

for i in m:
    print(i)

for i in range(10):
    pass
