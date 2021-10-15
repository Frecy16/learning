# python里存入数据只支持存入 字符串 和 二进制
# json：将Python里的数据(str/list/tuple/dict/int/float/bool/None)等转换成为对应的json字符串
# pickle：将Python里任意的对象转换成为二进制

import pickle

# 序列化   dumps: 将Python数据转换成为二进制
#         dump: 将Python数据转换成为二进制，同时保存到指定文件
# 反序列化  loads: 将二进制加载成为Python数据
#          load: 读取文件，并将文件的成为二进制内容加载成为Python数据
names = ['张三', '李四', '杰克', '亨利']


# b_names = pickle.dumps(names)
# # print(b_names)
#
# file = open('names.txt', 'wb')
# file.write(b_names)  # 写入的是二进制，不是纯文本
# file.close()
#
# file1 = open('names.txt', 'rb')
# x = file1.read()
# y = pickle.loads(x)
# print(y)
# file1.close()

# file2 = open('names.txt', 'wb')
# pickle.dump(names, file2)
# file2.close()
#
# file3 = open('names.txt', 'rb')
# y = pickle.load(file3)
# print(y)
#
class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '正在吃东西')


d = Dog('大黄', 2)
pickle.dump(d, open('dog.txt', 'wb'))
d1 = pickle.load(open('dog.txt', 'rb'))
print(d1.name, d1.age)
d1.eat()

"""
pickle 和 json 区别？什么情况下使用json，什么情况下使用pickle？

1.pickle 用来将数据原封不动的转换成为二进制，但是这个二进制只能在Python 里识别；
2.json 只能保存一部分信息，作用是用来在不同的平台里传递数据，json里存储的数据都是基本的数据类型
"""
