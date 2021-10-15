# 魔法方法，也叫魔术方法，是类里的特殊的一些方法
# 特点：
# 1、不需要手动调用，会在合适的时机自动调用
# 2、这些方法，都是使用 __ 开始，使用 __结束
# 3、方法名都是系统规定好的，在合适的时机自己调用
# import time
import datetime

n = datetime.datetime(2021, 4, 13, 8, 40, 54, 900)
print(n)  # 调用 __str__ 方法
print(repr(n))  # 调用 __repr__ 方法


class Person(object):
    def __init__(self, name, age):
        # 在创建对象时，会自动调用这个方法
        print('__init__方法被调用了')
        self.name = name
        self.age = age

    def __del__(self):
        # 当对象被销毁时，会自动调用这个方法
        print('__del__方法被调用了')

    def __repr__(self):
        return 'hello'

    def __str__(self):
        # return self.name, self.age  # 报错，TypeError: __str__ returned non-string (type tuple)
        return '{} {}'.format(self.name, self.age)

    def __call__(self, *args, **kwargs):
        # print('__call__方法被调用了')
        # args 是一个元组，保存(1, 2)
        # kwargs 是一个字典， 保存{'fn':lambda: x, y: x + y}
        print("args = {}, kwargs = {}".format(args, kwargs))
        fn = kwargs['fn']
        return fn(args[0], args[1])


p = Person('zhangsan', 18)
# 如果不做任何的修改，直接打印一个对象，是文件的__name__.类型 内存地址
# 当打印一个对象的时候，会调用这个对象的__str__ 或者 __repr__ 方法
# 如果这两个方法都写了，选择 __str__
print(p)
# print(repr(p))  # 调用内置函数 repr 会触发对象的 __repr__ 方法
# print(p.__repr__())  # 魔法方法，一般不手动的掉一共
# del p
# time.sleep(5)

# p()  # 对象名() ==> 调用这个对象的 p.__call__() 方法
m = p(1, 2, fn=lambda x, y: x + y)  # 调用这个对象的 p.__call__(1, 2) 方法
# print(m)
