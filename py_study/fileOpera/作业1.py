"""
1. 设计两个类：
一个点类，属性包括x,y坐标
一个Rectangle类（矩形），属性有左上角和右下角的坐标
方法：1. 计算矩形的面积；2.判断点是否在矩形内
实例化一个点对象，一个矩形对象，输出矩形的面积，输出点是否在矩形内
"""


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle(object):
    def __init__(self, top_left: Point, bottom_right: Point):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def calc_area(self):
        length = abs(self.top_left.y - self.bottom_right.y)
        width = abs(self.bottom_right.x - self.top_left.x)
        return length * width

    def is_inside(self, p):
        if self.bottom_right.x > self.top_left.x:
            return self.bottom_right.x >= p.y >= self.top_left.x and self.top_left.y >= p.y >= self.bottom_right.y
        else:
            return self.top_left.x >= p.y >= self.bottom_right.x and self.bottom_right.y >= p.y >= self.top_left.y


# pt = Point(0, 0)
# p1 = Point(-1, -3)
# p2 = Point(-3, -1)
# square = Rectangle(p1, p2)
# print(square.calc_area())
# print(square.is_inside(pt))


# 2. 写一个计算器类，可以进行加、减、乘、除计算


class Calculator(object):
    def add(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


# calc = Calculator()
# print(calc.div(3, 123))

# 3.创建一个Person类，添加一个类字段用来统计Person类的对象的个数


class Person(object):
    count = 0

    def __init__(self, name, age):
        Person.count += 1
        self.name = name
        self.age = age


# p1 = Person('lily', 16)
# p2 = Person('lucy', 18)
# print(Person.count)


# 4. 建立一个汽车类Auto，包括轮胎个数，汽车颜色，车身重量，速度等属性，并通过不同的构造方法创建实例。
# 至少要求汽车能够 加速、减速、停车。再定义一个小汽车类CarAuto 继承 Auto 并添加空调、CD属性，并且重新实现方法覆盖加速、减速的方法。


class Auto(object):
    def __init__(self, tyre_num, color, weight, speed):
        self.tyre_num = tyre_num
        self.color = color
        self.weight = weight
        self.speed = speed

    def speedUp(self, v):
        self.speed += v
        # return  # return后面不传值，表示函数结束

    def speedDown(self, v):
        self.speed -= v

    def stop(self):
        pass


class CarAuto(Auto):
    def __init__(self, tyre_num, color, weight, speed, air_condition, CD):
        super().__init__(tyre_num, color, weight, speed)
        self.air_condition = air_condition
        self.CD = CD

    def speedUp(self, v):
        pass

    def speedDown(self, v):
        pass


# 5. 有一个银行账户类Account，包括名字、余额等属性，方法有存钱、取钱、查询余额的操作，要求：
#    （1）. 在存钱时，注意存款的数据格式
#    （2）. 取钱时，要判断余额是否充足，余额不够的时候要提示余额不足


class Account(object):
    def __init__(self, name):
        self.name = name
        self.remain = 0

    def save_money(self, money):
        if type(money) != int:
            return '金额有误'
        elif money <= 0:
            return '您要存的钱必须大于0'
        elif len(str(money).rpartition('.')[1]) > 2:
            return '金额有误'
        else:
            self.remain += money

    def withdraw_money(self, money):
        if money > self.remain:
            return '余额不足'
        else:
            self.remain -= money

    def get_money(self):
        return self.remain


ac = Account('李明')
# print(ac.get_money())
# # print(ac.withdraw_money(100))
print(ac.save_money(0))
print(ac.get_money())
# ac.withdraw_money(50)
# print(ac.get_money())
