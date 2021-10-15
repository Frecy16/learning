# 将数据吸入到内存涉及到 StringIO 和 BytesIO 两个类
from io import StringIO, BytesIO

s_io = StringIO()
# s_io.write('hello')  # 把数据写入到内存里缓存起来
# s_io.write('kitty')
# print(s_io.getvalue())

# s = ''
# s += 'hello'
# s += 'world'
# print(s)

# file 需要的是一个文件流对象
# print('hello', file=open('sss.txt', 'w'))
# print('good', file=s_io)
# print('morning', file=s_io)
#
# print(s_io.getvalue())
s_io.close()

b_io = BytesIO()
b_io.write('你好'.encode('utf8'))  # 二进制形式写文件到内存并用utf8编码
print(b_io.getvalue().decode('utf8'))  # 二进制读取文件并用utf8解码
b_io.close()
