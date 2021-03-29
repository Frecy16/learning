# 1、判断用户名是已存在，存在则提示用户名已存在，不存在则添加到列表里

names = ['zhangsan', 'lisi', 'chris', 'jerry', 'july']

username = input("请输入用户名：\n")

# 使用列表的in方法实现
# while True:
#     for name in names:
#         if username == name:
#             print("用户名已存在")
#     else:
#         names.append(username)
#         break
# print(names)

# 不使用in方法
i = 0
while i < len(names):
    if username == names[i]:
        print("用户名已存在")
    i += 1
else:
    names.append(username)
print(names)
