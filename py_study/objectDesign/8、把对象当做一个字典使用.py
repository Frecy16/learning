class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]


p1 = Person('张三', 18)
# print(p1.__dict__)  # 将对象转换成为字典 {'name': '张三', 'age': 18}
# [] 语法会调用对象的__setitem__ 方法
p1['name'] = 'lisi'  # 未写__setitem__会报错，不能直接把一个对象当做字典来使用
print(p1.name)  # lisi
print(p1['name'])  # 调用 __getitem__ 方法
