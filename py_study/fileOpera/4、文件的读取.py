# Python里使用 open 内置函数来打开一个文件
# file:文件的路径，相对路径和绝对路径
# mode：打开文件的模式。 r:只读 w:写入 b:二进制  t:文本形式打开
# mode 默认使用的是 rt
# encoding：用来指定文件的编码方式。Windows系统里，默认是gbk

# file = open('xxx.txt')  # 报错，默认是以rt 打开，如果文件不存在，会报错
# file = open('sss.txt', 'w', encoding='utf8')  # 创建一个新的文件
# file.write('你好')

# file = open('yyy.txt', encoding='utf8')
# print(file.read())  # 将所有的数据都读取出来
# print(file.readline())  # 只读取一行数据
# print(file.readlines())  # 读取所有行的数据，保存到一个列表里
# x = file.read(20)  # 数字指的是读取的长度
# print(x)

# while True:
#     print(file.readline())
#     if file.readline() == '':
#         break
file1 = open('D:/视频/VID_20191001_111726.mp4', 'rb')
# 优化：没有绝对的优化，除非提升硬件
# 软件优化：时间 / 空间
while True:
    content = file1.read(1024)
    if not content:
        break
    print(content)

# file.close()
file1.close()
