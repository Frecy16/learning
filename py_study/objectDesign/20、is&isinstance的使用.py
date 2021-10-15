class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Mammal(object):
    pass


class Student(Person, Mammal):
    pass


p1 = Person('李斯', 18)
p2 = Person('李斯', 18)
# 获取两个对象的内存地址： id(p1) == id(p2)
print(p1 is p2)  # is 身份运算符是用来比较是否是同一个对象

# type(p1)  # 其实获取的就是类对象
print(type(p1) == Person)  # True

s = Student('刘明', 20)

# print(type(s) == Student)  # True
# print(type(s) == Person)  # False

# isinstance 用来判断一个对象是否是由指定的类（或者父类）实例化出来
print(isinstance(s, (Student, Mammal)))  # True
print(isinstance(s, Person))  # True

print(isinstance(p1, Student))  # False
print(isinstance(p1, Person))  # True

# issubclass 用来判断一个类是否是另一个类的子类
print(issubclass(Student, Person))  # True
print(issubclass(Person, Student))  # False
