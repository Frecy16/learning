import re

# 字母表示它本身，很多字母前面 \ 会有特殊含义

# \n:表示换行  \t: 表示一个制表符  \s:空白字符  \S: 非空白字符
# \d:表示字符，等价于[0-9]
print(re.search(r'x\d+p', 'x23980p'))
print(re.search(r'[^0-9]+', 'he110'))

# \w:表示数字、字母以及 _ 以及中文等  等价于 [0-9a-zA-Z] 非标点符号
print(re.findall(r'\w+', 'h+E-12.6_X*'))  # ['h', 'E', '12', '6_X']
print(re.findall(r'\w+', '大,家+好'))  # ['大', '家', '好']

# \W: \w 取反 ，标点符号
print(re.findall(r'\W+', 'h+E-12.6_X*'))  # ['+', '-', '.', '*']
