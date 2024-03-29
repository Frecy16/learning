# 面向对象编程有三大特性： 封装、继承和多态
# 封装：函数时对语句的封装；类是对函数和变量的封装
# 继承：类和类之间可以人为手动的简历父子关系，父类的属性和方法，子类可以使用
# 多态：是一种技巧，提高代码的灵活度


# 一个个的语句
def test():
    a = 23  # 赋值语句
    a += 3  # 算术运算符表达式语句
    print('hello')
    print('good')


class Persion(object):
    type = '人类'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('吃东西')
