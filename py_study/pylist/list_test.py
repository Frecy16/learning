# import datetime
#
# curtime = datetime.datetime.now().strftime("%Y%m%d")
# print(curtime)
import base64

str = "this is string example....wow!!!"
str = base64.b64encode(str.encode('utf-8', errors='strict'))

print("Encoded String: ", str)

m = [6, 5, 3, 1, 8, 7, 2, 4]
# m = ['b', 'a', 'd', 'e', 'a']
# x.pop()
# x.pop(3)
# x.remove('c')
# x.remove(1)  # 报错 1 not in list
# print(x.index('a', 2, 7))
# print(x.index(2))
# m.reverse()
# print(m)

# x[7] = 'life'
# print('d' in x)  # True
# # print(x)

# count = 0
# for i in range(len(m)):
#     for j in range(len(m)-i-1):
#         count += 1
#         if m[j+1] < m[j]:
#             m[j], m[j+1] = m[j+1], m[j]
#         j += 1
#         print(m)
# print(m)
# print(count)

# i = 0
# count = 0
# while i < len(m) -1:
#     j = 0
#     while j < len(m)-1-j:
#         count += 1
#         if m[j] > m[j + 1]:
#             m[j], m[j + 1] = m[j + 1], m[j]
#         j += 1
#     i += 1
# print(m)
# print(count)

# li = ['alex', 'eric', 'rain']
#
# # 1，计算列表长度并输出
# print(len(li))
#
# # 2，列表中追加元素“servn"，并输出添加后的列表
# li.append('servn')
# print(li)
#
# # 3，请在列表的第一个位置插入元素‘tony’，并输出添加后的列表
# li.insert(0, 'tony')
# print(li)

# 4，请修改列表第2个位置元素‘kelly’，并输出修改后的列表
# li[1] = 'kelly'
# print(li)

# 5，请在列表删除元素‘eric’，并输出删除后的列表
# li.remove('eric')
# print(li)

# 6，请删除列表中的第2个元素，并输出删除后的元素的值和删除元素后的列表
# print(li.pop(1), li)

# 7，请删除列表中的第三个元素，并输出删除后的列表
# li.pop(2)
# print(li)

# 8，请删除列表的第2到4个元素，并输出删除元素后的列表
# del li[1:4]
# for x in li[1:4]:
#     li.remove(x)
# print(li)

# 9，请用for len range输出列表的索引
# for i in range(len(li)):
#     print(i)

# 10，请使用enumrate输出列表元素和序号
# for i in enumerate(li):
#     print(i)

# 11，请使用for循环输出列表中的所有元素
# for i in li:
#     print(i)

# 有一个列表names，保存了一组姓名names=['zhangsan', 'lisi', 'chris', 'jerry', 'henry']
# 再让用户输入一个姓名，如果这个姓名在列表里存在，提示用户姓名已存在；
# 如果这个姓名在列表里不存在，就将这个姓名添加到列表里

names = ['zhangsan', 'lisi', 'chris', 'jerry', 'henry']

print(names.index('zhangsan'))

# while True:
#     username = str(input('请输入姓名：\n'))
#     if username in names:
#         print("用户名已存在")
#     else:
#         names.append(username)
#         break

# username = str(input('请输入姓名：\n'))
# for name in names:
#     if username == name:
#         print("用户名已存在")
#         break
# else:
#     names.append(username)

# counts = []
# for i in names:
#     num = names.count(i)
#     counts.append(num)
# print(counts)
