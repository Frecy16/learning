# 1. 用代码实现将指定路径下的音频文件剪切到其他路径下
# 思路：1、剪切 --- 可以理解为拷贝一份到指定路径，然后把源文件删除
#      2、拷贝 --- 操作的是文件的数据：先从源文件中读取数据 --- 由于是音频文件，需要以字节形式进行操作，再将读取到文件写入到目的文件中
#      3、执行完上述操作之后，删除文件
# import os
#
# ori_name = 'C:/Users/frecy/Desktop/测试数据/Beyond - 喜欢你.mp3'
# des_name = 'C:/Users/frecy/Desktop/practice/Beyond - 喜欢你.mp3'
#
# ori_file = open(ori_name, 'rb')
# des_file = open(des_name, 'wb')
# while True:
#     content = ori_file.read(1024)
#     des_file.write(content)
#     if not content:
#         break
#
# ori_file.close()
# des_file.close()
# os.remove(ori_name)


# 2. 读取youbian.txt 文件中的数据，完成邮编查询的操作：输入邮编号，如果有此邮编号，输出对应的城市，否则提示，无此邮编
try:
    file = open('C:/Users/frecy/Desktop/practice/youbian.txt', 'r', encoding='GB2312')
    code = input("请输入邮编号：")

    while True:
        content = file.readline()
        if not content:
            print('无此邮编')
            break
        if code == content.split()[2]:
            s = content.split()[1] + " " + content.split()[0]
            print(s)
            break
    file.close()
except FileNotFoundError:
    print('文件不存在')


# 3. 将一个英文语句以单词为单位逆序排放到指定的文件中
#   例如： "I am a boy" 逆序排放后 "boy a am I" 将其写入到指定的文件中


def word_reverse(w):
    m = w.split()
    m.reverse()
    return ' '.join(m)

# s = word_reverse('I am a boy')
# print(s)
