# 1、abs 求绝对值
print(abs(-10), abs(5))  # 10, 5

# 2、all 把所有元素转换成布尔值，如果全是True，则返回True，否则返回False
print(all(['hello', 'world', 'everything']))  # True
print(all(['hello', 'world', 0]))  # False

# 3、any 只要有一个元素转换成为布尔值是True，结果就是True
print(any(['hello', None, 0]))  # True

# 4、ascii 把字符转换成ASCII码
print(ascii('a'))  # 'a'

# 5、bin 将数字转换成为二级制
print(bin(-10))  # 0b1

# 6、chr 将字符编码转换成为对应的字符
print(chr(97))  # 'a'

# 7、ord 将字符转换成对应的字符编码
print(ord('A'))  # 65

# 8、dir 列出对象所有的属性和方法
# print(dir(list))  # [...'append', 'clear', 'copy', 'count', 'extend', 'index'... ]

# 9、divmod 求除法的商和余数
print(divmod(12, 5))  # (2, 2)

# 10、exit 以指定的退出码退出程序
# exit(200)

# 11、globals 用来查看所有的全局变量
a = 1
print(globals())


# 12、locals 用来查看所有的局部变量
def foo():
    b = 2
    return b


print(locals())

# 13、help 用来查看帮助文档的
# help(list)

# 14、print 打印内容
# 15、input 让用户输入内容
# x = input('请输入')
# print(x)

# 16、isinstance 用来判断一个对象是否是由一个类创建出来的
# 17、issubclass 用来判断一个类是否是另一个类的子类
# 18、len 获取长度
# 19、iter 获取到可迭代对象的迭代器
# 20、next for...in循环本质就是调用迭代器的next方法
# 21、max 求最大数
# 22、min 求最小数
# 23、open 用来打开一个文件
# 24、pow 幂运算
# 25、round 四舍五入，保留到指定小数位
print(round(3.1415926, 2))
# 26、sum 用来求和
# 27、repr 把一个对象变成一个字符串
person = {'name': 'zhangsan'}
print(repr(person))  # "{'name': 'zhangsan'}"
