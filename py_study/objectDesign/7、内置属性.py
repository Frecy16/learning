class Person(object):
    """
    这是一个人类
    """
    __slots__ = ('name', 'age')  # 限制对象能够拥有的属性

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '正在吃东西')


# 'name':'zhangsan', 'age':18, 'eat':<function>
p1 = Person('zhangsan', 18)
print(dir(p1))
# print(p1.__class__)  # <class '__main__.Person'>
# print(p1.__dict__)  # {'name': 'zhangsan', 'age': 18}，把对象的属性和值转换成为一个字典
# print(p1.__dir__())  # 相当于dir(p1)
# print(p1.__doc__)  # 对象名.__doc__ , 类的说明
# print(Person.__doc__)  # 类名.__doc__
# print(p1.__module__)  # __main__

# print(range.__doc__)  # range的说明
