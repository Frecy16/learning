import re

# \s  表示任意的非打印字符
print(re.search(r'\s', 'hello world'))  # 空格
print(re.search(r'\n', 'hello\nworld'))  # 换行
print(re.search(r'\t', 'hello\tworld'))  # 制表符

# \S  表示非空白字符
re.search(r'\S', '\t\n    x')

# 标点符号的使用
# (): 用来表示一个分组
m = re.search(r'h(\d+)x', 'sh908xklsjflk')
print(m.group())  # h908x
print(m.group(1))  # 908

m1 = re.search('\(.*\)', '(1+1)*3')
print(m1.group())  # (1+1)

# . 表示匹配除了换行以外的任意字符。如果想要匹配 . 需要使用 \.

# [] 用来表示可选项范围，[x-y] 从x到y区间，包含x和y, 只能选一个

# m2 = re.search(r'f[0-5]m', 'pdsf6m')  # None
# m2 = re.search(r'f[0-5]m', 'pdsf2m')  # f2m
# m2 = re.search(r'f[0-5]+m', 'pdsf212321m')  # f212321m
m2 = re.search(r'f[0-5a-z]+m', 'pdsf212321sfsam')  # f212321sfsam   0<=value<=5 或者 a<=value<=z
print(m2.group())

# | 用来表示或者
# | 和 [] 有一定的相似，但是有区别
# [] 里的值表示的是区间，而且是单个字符， | 就是可选值，可以出现多个值
m3 = re.search(r'f(x|pr|t)m', 'pdsfprm')  # fprm
print(m3)

# {} 用来限定前面元素出现的次数
# {n}: 表示前面的元素出现 n 次
print(re.search(r'go{2}d', 'good'))
# {n,}: 表示前面的元素出现 n 次以上
print(re.search(r'go{2,}d', 'gooooood'))
# {,n}: 表示前面的元素出现 n 次以下
print(re.search(r'go{,2}d', 'gd'))
# {m,n}: 表示前面元素出现m~n次
print(re.search(r'go{3,5}d', 'goood'))

# * 表示前面的元素出现任意次数（0次及以上） 等价于 {0，}
print(re.search(r'go*d', 'goooood'))

# + 表示前面的元素出现至少一次， 等价于 {1，}
print(re.search(r'go+d', 'good'))

# ? 两种用法：1.规定前面的元素最多只能出现一次，等价于 {,1}
#   2. 将贪婪模式转换成为非贪婪模式
print(re.search(r'go?d', 'good'))

# ^ 以指定内容开头  $ 以指定内容结尾
print(re.search(r'^a.*i$', 'asdfsjoi'))
