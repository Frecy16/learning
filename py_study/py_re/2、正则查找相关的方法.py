# 查找相关的方法
# match: 查找字符串，返回的结果是一个re.Match对象
# search: 查找字符串，返回的结果是一个re.Match对象
# match 和 search:
# 共同点：1. 只对字符串查询一次，只匹配一次  2. 返回值类型都是 re.Match类型的对象
# 不同点：match 是从头开始匹配，一旦匹配失败，就返回None；search是在整个字符串里匹配

# finditer: 查找到所有的匹配数据放到一个可迭代对象里
# findall: 把查找到的所有字符串结果放到一个列表里
# fullmatch: 完整匹配，字符串需要完全满足正则规则才会有结果，否则就是None


import re
from collections.abc import Iterable

m1 = re.match(r'hello', 'hello world good morning')
print(m1)  # <re.Match object; span=(0, 5), match='hello'>

m2 = re.search(r'good', 'hello world good morning good')
print(m2)  # <re.Match object; span=(12, 16), match='good'>

m3 = re.match(r'good', 'hello world good morning good')
print(m3)  # None

# finditer 返回的结果是一个可迭代对象
# 可迭代对象里的数据是匹配到的所有结果，是一个 re.Match 类型的对象
m4 = re.finditer(r's', 'sdfasfdsdfsdwesfdassvxcvvs')
print(isinstance(m4, Iterable))  # True

# for t in m4:
#     print(t)  # <re.Match object; span=(0, 1), match='s'> ......

m5 = re.findall(r'x\d+', 'sfdax23cxaoijvcx98oisdfsdfsxusoidu')
print(m5)  # ['x23', 'x98']

m6 = re.fullmatch(r'hello', 'hello world')
print(m6)  # None

m7 = re.fullmatch(r'h.*d', 'hkjsfhsfoisuiofhs d')
print(m7)  # <re.Match object; span=(0, 19), match='hkjsfhsfoisuiofhs d'>
