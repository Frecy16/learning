# 路径分为两种
# 1. 绝对路径：从电脑盼复开始的路径
# 2. 相对路径：当前文件所在的文件夹开始的路径。
# ../ 表示返回到上一级文件夹
# ./ 可以省略不写，表示当前文件夹
# / 不能随便使用
import os

print(os.sep)

# 在python的字符串里， \表示转义字符
# 在非Windows系统里，文件夹之间使用 / 分割。
# 路径书写的三种方式： 1.\\ 2. r'\' 3.'/' ，推荐使用第3中
# file = open(r"C:\\Users\\frecy\\PycharmProjects\\learning\\py_study\\fileOpera\\123.txt", encoding='utf8')
file = open("C:/Users/frecy/PycharmProjects/learning/py_study/fileOpera/123.txt", encoding='utf8')
# file = open(r"C:\Users\frecy\PycharmProjects\learning\py_study\fileOpera\123.txt", encoding='utf8')

print(file.read())

file.close()
