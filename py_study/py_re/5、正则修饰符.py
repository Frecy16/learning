import re

# 正则修饰符是对正则表达式进行修饰
# .  表示除了换行以外的任意字符
# re.S: 让 . 匹配换行
# re.I: 使匹配对大小写不敏感
# re.M: 使 ^ 和 $ 能够匹配到换行的内容

m = re.search(r'm.*a', 'sdmfisd\nlkcxjao', re.S)
print(m)  # <re.Match object; span=(2, 14), match='mfisd\nlkcxja'>

x = re.search(r'x', 'sdlfXsdfs', re.I)
print(x)  # <re.Match object; span=(4, 5), match='X'>

y = re.findall(r'\w+$', 'i am boy\n you are girl\n he is man')
print(y)  # ['man']
y1 = re.findall(r'\w+$', 'i am boy\n you are girl\n he is man', re.M)
print(y1)  # ['boy', 'girl', 'man']
