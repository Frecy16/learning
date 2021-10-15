class Person(object):
    type = '人类'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):  # 默认的方法都是对象方法，对象方法有一个参数self，指的是实例对象
        print(self.name + '正在吃' + food)

    # 如果一个方法里面没有用到实例对象的任何属性，也不用类对象，可以将这个方法定义成static 静态方法
    @staticmethod
    def demo():
        print('我是demo方法，我被调用了')

    # 如果这个函数只用到了类属性，可以定义成为一个类方法
    @classmethod
    def test(cls):  # 类方法会有一个参数 cls，也不需要手动的传参，会自动传参，cls指的是类对象: cls is Person
        print('test函数使用了类属性: {}'.format(cls.type))


class Calculator(object):
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def minus(a, b):
        return a - b


# c = Calculator()
# print(c.add(1, 2))
print(Calculator.add(1, 2))

p1 = Person('张三', 18)
p2 = Person('李斯', 20)
# 实例对象在调用对象方法时，不需要给形参self传参，会自动的把实例对象传递给self
# eat 对象方法，可以直接使用实例对象，方法名(参数)调用
# 使用 对象名.方法名(参数) 调用的方式，不需要传递self，会自动将对象名传递给self
p1.eat('樱桃')  # 直接使用实例对象调用方法
p1.demo()

# 对象方法还可以使用 类对象来调用 类名.方法名()
# 这种方式，不会自动传self传参，需要手动的指定self 实例对象
# Person.eat('西红柿鸡蛋面')  # 报错，缺少self参数
Person.eat(p2, '西红柿鸡蛋面')
Person.demo()

# 类方法可以使用实例对象和类对象调用
p1.test()
Person.test()

# print(p1.eat)  # <bound method Person.eat of <__main__.Person object at 0x000001CAD4804B80>>
# print(p2.eat)  # <bound method Person.eat of <__main__.Person object at 0x000001CAD487A100>>
# print(p1.eat is p2.eat)  # False, p1 和 p2 分别绑定函数
# print(Person.eat) # <function Person.eat at 0x0000022C4B5433A0>
