# for y in 10:  # 数字不是可迭代对象
#     print(y)

# for x in 'hello':  # 字符串是可迭代对象
#     print(x)
from collections.abc import Iterable


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('瑶瑶', 18)
# print(isinstance(p1, Person))  # True

a = 'hello'
b = ['婷婷', '明明', '佳佳', '坤坤', '琳琳', '梦凡']
c = ('yes', 'good', 'ok', 'well')
d = {1, 2, 3, 4}
pe = {'name': '玥玥'}
nums = range(0, 10)
# 判断一个对象是否是可迭代对象

# Iterable 类 用来判断一个对象是否是可迭代对象
print(isinstance(a, Iterable))
print(isinstance(b, Iterable))
print(isinstance(c, Iterable))
print(isinstance(d, Iterable))
print(isinstance(pe, Iterable))
print(isinstance(nums, Iterable))
