# 定义一个类属性，记录通过这个类创建了多少个对象
class Person(object):
    __count = 0

    # def __new__(cls, *args, **kwargs):
    #     instance = object.__new__(cls)
    #     cls.__count += 1
    #     return instance

    def __init__(self, name, age):
        Person.__count += 1
        self.name = name
        self.age = age

    @classmethod
    def get_count(cls):
        return cls.__count


# 每次创建对象，都会调用 __new__ 和 __init__ 方法
# 调用 __new__ 方法，用来申请内存
# 如果不重写 __new__ 方法，它会自动找 object 的 __new__
# object 的 __new__ 方法， 默认实现是申请了一段内存，创建一个对象
p1 = Person('张三', 18)
p2 = Person('李斯', 20)
p3 = Person('王武', 21)
p4 = object.__new__(Person)
p4.__init__('刘明', 22)

print(p1, p2, p3, p4)
print(Person.get_count())
