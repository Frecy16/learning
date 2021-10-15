# 序列化：将数据从内存持久化保存到硬盘的过程
# 反序列化：将数据从硬盘加载到内存的过程

# write时，只能写入字符串或者二进制
# 1.将数据装换成为字符串：repr/str，使用 json 模块
# 2.将数据转换成为二进制：使用 pickle 模块
import json

file = open('456.txt', 'w', encoding='utf8')
names = ['zhangsan', 'lisi', 'wangwu', 'liuming']

# json里将数据持久化有两个方法：
# dumps： 将数据转换成为json字符串，不会将数据保存到文件里
# dump: 将数据转换成为json字符串，同时写入到指定文件
# x = json.dumps(names)
# print(x)
# file.write(repr(names))
# file.write(x)

json.dump(names, file)
file.close()

# json 反序列化也有两个方法
# loads: 将json字符串加载成为Python里的数据
# load：读取文件，把读取的内容加载成为Python里的数据

m = open('456.txt', 'r', encoding='utf8')
n = '{"name": "zhangsan", "age": 18}'
# p = json.loads(n)
# print(p['name'])
q = json.load(m)
print(q)
print(q[-1])
m.close()

"""
python对象与json字符串的对应关系：
没有对应的类型转换会报错
python          json

dict            object
list,tuple      array
int,float       number
True            true
False           false
None            null  
"""

"""
pickle 和 json 区别？什么情况下使用json，什么情况下使用pickle？

1.pickle 用来将数据原封不动的转换成为二进制，但是这个二进制只能在Python 里识别；
2.json 只能保存一部分信息，作用是用来在不同的平台里传递数据，json里存储的数据都是基本的数据类型
"""
