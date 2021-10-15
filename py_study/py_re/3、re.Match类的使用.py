# 调用 re.match、re.search或者对re.finditer结果进行遍历
# 拿到的内容都是re.Match类型对象


import re

m = re.search(r'm.*j', 'o3sodmfijsxoij')
print(m)
# print(dir(m))  # ...  'end', 'endpos', 'expand', 'group', 'groupdict', 'groups', 'lastgroup', 'lastindex',
# 'pos', 're', 'regs', 'span', 'start', 'string'
# print(m.pos, m.endpos)  # 0 9   搜索开始和结束的位置
print(m.span())  # (5, 14) 匹配到的结果字符串的开始和结束下标

# 使用group方法可以获取匹配的字符串结果
# group 可以传参，表示第 n 个分组
print(m.group())  # mfij
print(m.group(0))  # mfij
# print(m.group(1))  # IndexError: no such group

# group 方法表示正则表达式的分组
# 1. 在正则表达式里使用()表示一个分组
# 2. 如果没有分组，默认只有一组
# 3. 分组的下标从0开始

m1 = re.search(r'(9.*)(0.*)(5.*7)', 'dad9fsfsd0wfsfd5asgdsgsdf7')
print(m1)
# 分组0：(9.*)(0.*)(5.*7) ,分组1：(9.*)，分组2：(0.*)，分组3：(5.*7)
print(m1.group(0))  # 9fsfsd0wfsfd5asgdsgsdf7 第 0 组就是把整个正则表达式当做一个整体
print(m1.group())  # 9fsfsd0wfsfd5asgdsgsdf7，不写默认是第0组
print(m1.group(1))  # 9fsfsd
print(m1.group(2))  # 0wfsfd
print(m1.group(3))  # 5asgdsgsdf7
print(m1.groups())  # ('9fsfsd', '0wfsfd', '5asgdsgsdf7') 把所有分组组成一个元组返回
# for i in range(4):
#     print(m1.group(i))

# (?P<name>表达式)  可以给分组起一个名字
m2 = re.search(r'(?P<abc>9.*)(0.*)(5.*7)', 'dad9fsfsd0wfsfd5asgdsgsdf7')
print(m2.groupdict())  # {'abc': '9fsfsd'}
print(m2.groupdict('abc'))  # {'abc': '9fsfsd'}

print(m2.group('abc'))  # 9fsfsd
print(m2.group(1))  # 9fsfsd
