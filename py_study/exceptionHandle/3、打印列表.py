class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'hello'

    def __repr__(self):
        return '姓名：{}，年龄：{}'.format(self.name, self.age)


p1 = Person('zhangsan', 18)
p2 = Person('lisi', 20)

print(p1)  # 调用 __str__ 或者 __repr__ 方法

person = [p1, p2]

# 直接打印列表，会调用列表里的 __repr__ 方法
print(person)  # 直接打印一个列表，会把列表里的每一个对象的内存地址打印出来
