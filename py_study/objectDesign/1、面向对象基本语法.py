# 小明今年18岁，身高 1.75，每天早上跑完步，回去 吃 东西
# 小美今年17岁，身高 1.65，小美不跑步，小美喜欢 吃 东西

# 定义类：类名的定义，使用class 来定义一个类
# class 类名: 类名一般需要遵守大驼峰命名法，每一个单词的首字母都大写
# 1. class <类名>:
# 2. class <类名>(object):


class Student(object):  # 关注这个类有哪些特征和行为
    # 在 __init__ 方法里，以参数的形式定义属性，称之为属性
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def run(self):
        print(f'{self.name}正在跑步')

    def eat(self):
        print(f'{self.name}正在吃东西')


# 使用 Student 类创建了两个实例对象 s1 s2
# s1 和 s2 都会有name,age,height属性，同时都有run和eat 方法
s1 = Student('小明', 18, 1.75)
s2 = Student('小美', 19, 1.65)

# 根据业务逻辑，让不同的对象执行不同的行为
s1.run()
s1.eat()

s2.eat()
