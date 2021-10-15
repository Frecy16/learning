"""
多态是基于继承，通过子类重写父类的方法，达到不同的子类对象调用相同的父类方法，
得到不同的结果，提高代码的灵活度
"""


class Dog(object):
    def work(self):
        print('狗正在工作')


class PoliceDog(Dog):
    def work(self):
        print('警犬正在攻击坏人')


class GuideDog(Dog):
    def work(self):
        print('导盲犬正在领路')


class DetectionDog(Dog):
    def work(self):
        print('缉毒犬正在搜索毒品')


class Person(object):
    def __init__(self, name):
        self.dog = None
        self.name = name

    def work_with_dog(self):
        if self.dog is not None and isinstance(self.dog, Dog):
            self.dog.work()


pd = PoliceDog()
gd = GuideDog()
dd = DetectionDog()
p1 = Person('张sir')
p1.dog = pd
p1.work_with_dog()

p1.dog = gd
p1.work_with_dog()

p1.dog = dd
p1.work_with_dog()
