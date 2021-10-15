class Person(object):
    def __init__(self, name, age):  # self 谁调用就指向谁，不调用不指向
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '正在吃东西')

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    # def __ne__(self, other):  # 使用 != 运算符会自动调用这个方法
    #     pass

    # def __gt__(self, other):  # 使用 > 运算符会自动调用这个方法
    #     return self.age > other.age

    # def __ge__(self, other):  # 使用 >= 运算符会自动调用这个方法
    #     return self.age >= other.age

    # def __lt__(self, other):  # 使用 < 运算符会自动调用这个方法
    # def __le__(self, other):  # 使用 <= 运算符会自动调用这个方法
    # def __add__(self, other):  # 使用 + 运算符会自动调用这个方法
    # def __sub__(self, other):  # 使用 - 运算符会自动调用这个方法
    # def __mul__(self, other):  # *
    # def __truediv__(self, other):  # /
    # def __mod__(self, other):  #  取余
    # def __pow__(self, power, modulo=None):  # **

    # def __str__(self):
    #     return 'hello'
    # def __int__(self):
    #     return 5
    # def __float__(self):
    #     return 100.5


p1 = Person('小明', 18)
p2 = Person('小李', 20)

# print(p1 is p2)  # False
# == 运算符本质其实是调用对象的 __eq__ 方法，获取 __eq__方法的返回结果
# a == b => a.__eq__(b)
# print(p1 == p2)  # False  p1.__eq__(p2) 比较内存地址

# != 本质是调用 __ne__方法 (not equal) 或者 __eq__ 方法取反
# print(p1 != p2)  # 未重写 __ne__ 方法False
# print(p1 > p2)  # 未重写__gt__ 方法时会报错（没有这个方法）
# print(p1 >= p2)  # 未重写__ge__方法时会报错

# nums1 = [1, 2, 3]
# nums2 = [1, 2, 3]
# print(nums1 == nums2)  # 系统自动重写了__eq__方法，比较的是值

# str() 将对象转换成为字符串，会自动调用 __str__ 方法
# 1. str() 2. 打印对象也会调用
print(str(p1))  # 转换成为字符串，默认会转换成为类型 + 内存地址
# print(int(p1))  # 调用对象的__int__方法
