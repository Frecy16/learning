"""
1.用户名匹配
要求：1.用户名只能包含数字、字母、下划线
     2.不能以数字开头
     3.长度在6到16位范围内
"""
import re

# username = input('请输入用户名：')
# if re.search(r'^[a-zA-Z_][a-z0-9A-Z_]{5,15}$', username):
# # if re.fullmatch(r'[a-zA-Z_][a-z0-9A-Z_]{5,15}', username):
#     print(username)
# else:
#     print('用户名不符合规范')

# 2.密码匹配
# 要求：1.不能包含! @#￥%^&*这些特殊符号
#      2.必须以字母开头
#      3.长度 6 到 12 位范围内
# password = input('请输入密码：')
# if re.search(r'^[a-zA-Z][^!@#￥%^&*]{5,11}$', password):
#     print(password)
# else:
#     print('密码不合规范')
# from datetime import time

'''
3. 已知有文件test.txt里面的内容如下：
1000phone hello python
mobiletrain 大数据
1000phone java
mobiletrain html5
mobiletrain 云计算
查找文件中以1000phone开头的语句，并保存到列表中
'''
# result_list = []
# try:
#     with open('test.txt', 'r', encoding='utf8') as f:
#         # z = re.findall('1000phone.*', f.read())
#         # while True:
#         #     content = f.readline(1024)
#         #     if not content:
#         #         break
#         #     if re.search(r'^1000phone', content):
#         #         result_list.append(content.strip())
# except FileNotFoundError:
#     print('文件不存在')
#
# # print(result_list)
# print(z)

# 4. ipv4格式的 ip 地址匹配
# 提示：IP地址的范围是 0.0.0.0 ~ 255.255.255.255
# import random
# import datetime
# start_time = end_time = datetime.datetime.now()
#
# while (end_time - start_time).total_seconds()  < 10:  # 运行10秒钟
#     # ip = input('请输入ip：')
#     ip = (str(random.randint(0, 255)) + '.') * 3 + str(random.randint(0, 255))
#     if re.fullmatch(r'((\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])', ip):
#         # print(ip)
#         pass
#     else:
#         print('{} 不是ipv4地址'.format(ip))
#         break
#     end_time = datetime.datetime.now()

# 5.提取用户输入数据中的数值(数值包括正负数,还包括整数和小数在内) 并求和
# 例如： “-3.14good87nice19bye” ==> -3.14 + 87 + 19 = 102.86

# s = input('请输入数据：')
summer = 0
s = "af-2as3.ds--3.14good87nice19bye"
x = re.findall(r'-?\d+\.?\d*', s)
# x = re.finditer(r'-?(0|[1-9]\d*)(\.d+)?', s)
if x:
    for num in x:
        summer += float(num)
print(x)
print(summer)
