# 有很多可迭代对象： list/tuple/dict/set/str/range/filter/map
# for...in 可迭代对象
# from collections.abc import Iterable


class Demo(object):
    def __init__(self, x):
        self.x = x
        self.count = 0

    def __iter__(self):  # 只要重写了 __iter__ 方法就是一个可迭代对象
        return self

    def __next__(self):  # 每一次for...in  都会调用一次 __next__ 方法，获取返回值
        self.count += 1
        if self.count <= self.x:
            return self.count - 1
        else:
            raise StopIteration  # 让迭代器停止


d = Demo(10)

# isinstance: 用来判断一个实例对象是否是由指定的类创建出来的
# print(isinstance(d, Iterable))  # True

# for...in 循环的本质就是调用可迭代对象的__iter__ 方法，获取到这个方法的返回值
# 这个返回值需要的是一个对象，然后再调用这个对象的 __next__ 方法
# for i in Demo(10):
#     print(i)

# i = d.__iter__()
# print(i.__next__())
# print(i.__next__())

i = iter(d)  # 内置函数 iter 可以获取到一个可迭代对象的迭代器
print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
