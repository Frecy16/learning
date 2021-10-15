class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__weight = 50

    def eat(self):
        print(self.name + '正在吃东西')

    def __test(self):
        print('我是Animal类里的test方法')


class Dog(Animal):
    def __demo(self):
        print('我是Dog里的私有的demo方法')


d = Dog('小六', 3)
print(d.name)
d.eat()
# d.__test()
# d._Animal__test()  # 我是Animal类里的test方法，可以通过 对象名._父类名__私有方法  调用
# d._Dog__demo()  # 我是Dog里的私有的demo方法，自己类里定义的私有方法， 对象名._类名__私有方法()
# d._Dog__test()  # 报错，父类的私有方法，子类没有继承

print(d._Animal__weight)  # 50
