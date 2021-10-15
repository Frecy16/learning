# mode 指的是文件的打开方式，默认使用的是 rt
# r:只读模式，默认，打开文件以后，只能读取，不能写入
# w：写入模式，打开文件以后，只能写入，不能读取，如果文件存在，会覆盖文件；如果文件不存在，会生成一个新的文件并写入
# b: 以二进制的形式打开文件，可以用来操作非文本文件，如图片，视频等
# rb: 以二进制读取   wb：以二进制写入
# a：追加模式，会在最后追加内容，如果文件不能存在，会创建文件；如果文件存在，会追加
# r+: 可读写
# w+: 可读写
# t: 文本形式打开

# file = open('123.txt', encoding='utf8')  # 文件不存在时，会报错误
# print(file.read())
# file.write('hello')  # 不能执行写入操作，会报错
# file1 = open('456.txt', 'w')
# file1.read()  # 不能执行读取，会报错
# file1.write('hello')  # 可以执行写入的操作，只能写入字符串或二进制数据

# file.close()
# file1.close()


# file2 = open('123.txt', 'rb')
# print(file2.read())  # 读取的结果是二进制
# file2.write('大家好才是真的好')  # 报错，只能写入二进制
file2 = open('456.txt', 'wb')
file2.write('大家好才是真的好'.encode('utf8'))
file2.close()

file3 = open('yyy.txt', 'w+', encoding='utf8')
file3.write('小嘛小二郎呀')
file3.seek(0, 0)  # 写入之后，文件指针到最后，需要调用seek,文件指针，(0,0)表文件开头位置，(0,1)代表当前位置，(0,2)代表文件末尾位置
print(file3.read())
file3.close()
