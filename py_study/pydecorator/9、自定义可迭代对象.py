# 可迭代对象并不是继承自Iterable 类，而是对象重写了 __iter__ 方法
from collections.abc import Iterable


class Person(object):
    def __init__(self, name, x):
        self.x = x
        self.name = name
        self.count = 0

    def __iter__(self):
        # 必须要返回一个迭代器，for...in循环时，会获取到这个返回值对象，调用它的 __next__ 方法
        return self

    def __next__(self):
        self.count += 1
        if self.count <= self.x:
            return self.count - 1
        else:
            raise StopIteration


p1 = Person('李明', 10)
# 只要一个类重写了 __iter__ 方法，它就是一个可迭代对象
# 可迭代对象可以使用for...in 循环遍历
# __iter__ 方法到底做了什么工作呢？
# iter() returned non-iterable of type 'NoneType'
# iter 方法返回的记过是空（NoneType），它是一个 非iterator(迭代器)

# 判断一个对象是否是迭代器 isinstance(p1, Iterable)
# 一个对象要想变成一个迭代器，需要重写 __iter__ 和 __next__ 方法
print(isinstance(p1, Iterable))

# for...in循环的本质是，获取到可迭代对象的迭代器，然后不断的调用迭代器的 next 方法
# __iter__ 方法的返回值必须是一个迭代器
# for i in p1:
#     print(i)


print(p1.__iter__().__next__())
print(p1.__iter__().__next__())
print(p1.__iter__().__next__())
print(p1.__iter__().__next__())
print(p1.__iter__().__next__())
print(p1.__iter__().__next__())
print(p1.__iter__().__next__())

# next 和 iter
print(next(iter(p1)))
# i = iter(p)  # 等价于 p.__iter__() 获取到迭代器
# next(i)  # 等价于p.__iter__().__next__() 调用迭代器的 __next__ 方法

# for y in 10:  # 'int' object is not iterable
#     print(y)
