class Person(object):
    type = '人类'  # 这个属性定义在类里，函数之外，我们称之为类属性

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 对象 p1 和 p2 是通过 Person 类创建出来的实例对象
# 只要创建了一个实例对象，这个实例对象就有自己的name 和 age 属性
# name 和 age 是对象属性， 在 __init__ 方法里，以参数的形式定义的
# 对象属性：每个实例对象都单独保存的属性
# 每个实例对象之间的属性没有关联、互不影响
p1 = Person('张三', 18)
p2 = Person('李四', 20)
# print(p1.name, p1.age)  # 获取对象的属性

# 类属性可以通过类对象和实例对象获取
# print(Person.type)  # 可以通过类对象获取类属性
# 可以通过实例对象来获取类属性
# print(p1.type)
# print(p2.type)

# 类属性只能通过类对象来修改，实例对象无法修改类属性
p1.type = 'human'  # 并不会修改类属性，而是给实例对象新增了type属性
# print(p1.type)  # human
# print(Person.type)  # 人类

Person.type = '哺乳类'  # 修改了类属性
print(Person.type)  # 哺乳类
print(p2.type)  # 哺乳类
print(p1.type)  # human ,自己有这个属性，取自己的，没有才会去找类属性

# print('p1内存地址: 0x%X, p2内存地址: 0x%X' % (id(p1), id(p2)))  # p1内存地址: 0x1DB33A14B80, p2内存地址: 0x1DB33A8A100
# print('Person类的内存地址： 0x%X' % id(Person))  # Person类的内存地址： 0x1DB31BB6590
