# os 模块 os全称 operationSyetem
# os 模块里提供的方法就是用来调用操作系统里的方法
import os

# 获取操作系统的名字  windows系列  ==>nt / 非Windows ==> posix
# print(os.name)  # nt
# print(os.sep)  # \  目录分隔符，非Windows  /

# os 模块里的 path 经常会使用
# print(os.path.abspath('1、导入模块的语法.py'))  # 获取绝对路径

# isdir 判断是否是文件夹
# print(os.path.isdir(r'C:\Users\frecy\PycharmProjects\learning\app1'))  # True 传入文件夹绝对路径
# print(os.path.isdir('xxx'))  # True 判断当前目录下的文件夹
# print(os.path.isdir('py_study')) # False 非当前目录下的所有非绝对路径的文件夹均返回False

# isfile 判断是否文件
# print(os.path.isfile('1、导入模块的语法.py'))  # True
# print(os.path.isfile('xxx'))  # False

# exists 判断是否存在
# print(os.path.exists('1、导入模块的语法.py'))  # True
# print(os.path.exists('123.py'))  # False
# 获取文件名和文件类型
# print(os.path.splitext('2020.2.21.demo.py'))  # ('2020.2.21.demo', '.py')

# os 里其他方法的介绍
# print(os.getcwd())  # 获取当前工作目录
# os.chdir(r'C:\Users\frecy\PycharmProjects\learning\py_study')  # 改变当前脚本工作目录，相当于shell下的cd命令
# print(os.getcwd())
# os.rename('测试123.txt', 'test123.txt')  # 文件重命名
try:
    pass
except FileNotFoundError:
    pass
# os.remove('test123.txt')  # 删除文件
# os.rmdir('demo')  # 删除文件夹
# os.removedirs('xxc')  # 删除空文件夹
# os.mkdir('demo')  # 创建一个文件夹
# print(os.listdir('C:\\'))
# os.name  # 获取操作系统名称  windows ==>nt  Linux/UniX/MacOS ==> posix
# print(os.environ)  # 获取环境变量
print(os.environ.get('PATH'))  # 获取指定的环境变量
