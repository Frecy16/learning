# 在Python的正则表达式里，默认是贪婪模式，即尽可能多的匹配
import re

# 在贪婪模式后面添加 ? 可以将贪婪模式转换成为非贪婪模式
m = re.search(r'm.*a', 'osimi123aks987alsoda?')  # 贪婪匹配
m1 = re.search(r'm.*?a', 'osimi123aks987alsoda?')  # 非贪婪匹配
print(m.group())  # mi123aks987alsoda
print(m1.group())  # mi123a

x = re.match(r'aa(\d+?)ddd', 'aa2345ddd')
print(x.group(0))  # aa2345ddd  满足规则的前提下不贪婪，必须先满足规则
print(x.group(1))  # 2345

x1 = re.match(r'aa(\d??)(.*)', 'aa2345ddd')  # 第一个? 表示{0,1}匹配0~1次，第二个? 表示非贪婪匹配，那就匹配0次，即不匹配内容
print(x1.group(0))  # aa2345ddd
print(x1.group(1))  # 空
print(x1.group(2))  # 2345ddd
