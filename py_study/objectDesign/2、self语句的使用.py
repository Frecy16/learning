class Student(object):
    # 这个属性直接定义在类里，是一个元组，用来规定对象可以存在的属性
    __slots__ = ('name', 'age')

    def __init__(self, x, y):
        self.name = x
        self.age = y

    def sayHello(self):
        print('大家好，我是', self.name)


# Student('张三', 18) 这段代码具体做了什么呢？
# 1. 调用 __new__方法，用来申请内存空间
# 2. 调用__init__ 方法传入参数，并让self 指向申请好的那段内存空间，填充数据
# 3. 让变量 s1 也指向创建好的这段内存空间
s1 = Student('张三', 18)
# print('0x%X:'% id(s1))  # 查看地址
print('s1 的名字是', s1.name)
# 谁调用self，self就是谁
s1.sayHello()
# 如果没有这个属性会报错
# print(s1.height)

# 直接使用等号给一个属性赋值
# 如果这个属性以前不存在，会给对象添加一个新的属性
# 动态属性
s1.city = '上海'  # 给对象添加了一个city属性

# 如果这个属性以前存在，会修改这个属性对应的值
s1.name = '刘明'
print(s1.name)  # '刘明'
