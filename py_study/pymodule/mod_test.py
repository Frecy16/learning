class Person(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(self.name + "正在吃" + food)

    def sleep(self):
        print(self.name + '在睡觉')


_p1 = Person('李世明')

eat = _p1.eat  # 给对象的eat方法设置一个别名 eat
sleep = _p1.sleep

# 函数名后面如果加括号表示的是调用这个函数，并获取到函数的执行结果
# 不加括号表示函数的别名

# import random
# random.randint(1, 2)
