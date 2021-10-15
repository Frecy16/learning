class Singleton(object):
    __instance = None
    __isfirst = True

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            # 申请内存，创建一个对象，并把对象的类型设置为cls
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, a, b):
        if self.__isfirst:
            self.a = a
            self.b = b
            self.__isfirst = False  # 在对象里加了一个__isfirst 对象属性


# 调用 __new__ 方法申请内存
# 如果不重写 __new__方法，会调用 object 的 __new__ 方法
# object的 __new__ 方法会申请内存
# 如果重写了 __new__ 方法，需要自己手动的申请内存
s1 = Singleton('abc', '好的')
s2 = Singleton('hello', '世界')
# print(type(s1))  # <class '__main__.Singleton'>
# print(hex(id(s1)), hex(id(s2)))
print(s1.a, s1.b)  # hello 世界 , s2 把 s1 覆盖了
print(s1 is s2)
