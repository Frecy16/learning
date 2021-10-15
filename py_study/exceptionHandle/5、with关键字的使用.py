# try:
#     file = open('123.txt', 'r', encoding='utf8')
# except FileNotFoundError:
#     print('文件不存在')
# else:
#     try:
#         file.read()
#     finally:
#         file.close()


try:
    with open('123.txt', 'r', encoding='utf8') as file:
        file.read()  # 不需要手动的关闭文件
        # print(file.read())
    # file.close()  # with 关键字会帮助我们关闭文件
except FileNotFoundError:
    print('未找到文件')

# with 称之为上下文管理器，很多需要手动关闭的连接
# 比如，文件连接，socket连接，数据库的连接， 都能使用with关键字自动关闭连接
# with 关键字后面对象，需要实现 __enter__ 和 __exit__ 魔法方法
