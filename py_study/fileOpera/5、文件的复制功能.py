# sss.txt ==> sss.bak.txt
import os

file_name = input('请输入一个文件的路径：')
if os.path.isfile(file_name):
    name_list = file_name.rpartition('.')
    # names = os.path.splitext(file_name)  # ('xxx', '.txt')
    new_name = name_list[0] + '.bak.' + name_list[2]
    ori_file = open(file_name, 'rb')  # 以二进制文件写入
    new_file = open(new_name, 'wb')  # 以二进制文件写入
    while True:
        content = ori_file.read(1024)  # 每次读取1024个字节
        new_file.write(content)
        if not content:  # 判断内容是否为空
            break

    ori_file.close()
    new_file.close()
else:
    print('您输入的文件不存在')
