"""
定义一个点类 Pointer
属性是横向坐标 x 与 纵向坐标 y
定义一个圆类 Circle
属性有圆心点 cp 与 半径 radius
方法有：
1.求圆的面积
2.求圆的周长
3.求 指定点与圆的关系
提示：关心有三种：圆内、圆外、圆上
涉及到的数学公式：指定的点与圆心点之间的距离 与 圆的半径进行比较
"""
import math


class Pointer(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle(object):
    def __init__(self, cp: Pointer, radius):
        self.cp = cp
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_length(self):
        return 2 * math.pi * self.radius

    def get_relation(self, p: Pointer):
        """
        求一个点和圆的关系
        :param p: 点
        :return: 点在圆外、点在圆上、点在圆内
        """
        distance = round(math.sqrt((self.cp.x - p.x) ** 2 + (self.cp.y - p.y) ** 2), 6)
        if distance > self.radius:
            return '点在圆外'
        elif distance == self.radius:
            return '点在圆上'
        else:
            return '点在圆内'


p1 = Pointer(1, -2)
cp1 = Pointer(0, 0)
c = Circle(cp1, 2)

print(c.get_area())
print(c.get_length())
print(c.get_relation(p1))
