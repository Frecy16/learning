class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name + '正在睡觉')


class Dog(Animal):  # 继承父类(基类), Dog是Animal子类（派生类),子类可以使用父类的方法
    def bark(self):
        print(self.name + '正在汪汪叫……')


class Student(Animal):
    def study(self):
        print(self.name + '正在好好学习')


# Dog() 调用__new__ 方法，再调用 __init__ 方法
# Dog 里没有 __new__ 方法，会查看父类是否重写了 __new__ 方法
# 如果父类里也没有重写__new__ 方法，会查找父类的父类，找到object

# 调用 __init__ 方法,Dog类没有实现，会自动找 Animal父类
d1 = Dog('大黄', 6)
# print(d1)  # 父类里定义的属性，子类可以直接使用
d1.sleep()  # 父类的方法子类实例对象可以直接调用
d1.bark()

s1 = Student('小明', 18)
s1.sleep()
s1.study()
# s1.bark()  # 报错，Student里没有bark() 方法，父类里也没有
