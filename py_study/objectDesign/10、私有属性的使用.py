import datetime


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__money = 1000  # 以两个下划线开始的变量是私有变量

    def test(self):
        self.__money += 10  # 在这里可以访问私有属性

    def get_money(self):
        print('查询余额时间 {}'.format(datetime.datetime.now()))
        return self.__money

    def set_money(self, new_money):
        if type(new_money) == int:
            print('修改余额了')
            self.__money = new_money
        else:
            print('修改余额失败')

    def __demo(self):  # 以两个下划线开始的函数，是私有函数，在外部无法调用
        print('我是demo函数')

    def test_demo(self):
        self.__demo()


p1 = Person('张三', 18)
print(p1.name, p1.age)  # 可以直接获取到
# print(p1.__money)  # 不能够直接获取到私有变量
# p1.__demo()  # 不能直接调用demo函数，它是私有方法
p1._Person__demo()  # 强行调用

# p1.test()
# 获取私有变量的方式：
# 1. 使用 对象._类名__私有变量名获取
# print(p1._Person__money)  # 通过这种方式也能获取到私有属性

# 2. 定义get 和 set 方法来获取
print(p1.get_money())
p1.set_money(2000)
print(p1.get_money())

# 3. 使用property来获取()
