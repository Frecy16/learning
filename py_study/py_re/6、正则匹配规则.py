# 1. 数字和字母都表示它本身
# 2. 很多字母前面添加 \ 会有特殊含义
# 3. 绝大多数标点符号都有特殊含义（重点）
# 4. 如果想要使用标点符号，需要在前面加 \
import re

# 字母x表示它本身
re.search(r'l', 'hello world')
re.search(r'5', '23423xdf5')

print(re.search(r'd', 'good'))  # 字母 d 是普通的字符
print(re.search(r'\d', 'good'))  # \d 有特殊含义，不再表示字母 d
print(re.search(r'\d', 'wsdfsdf23sdf'))

# re.search('+', '1+2')  # 不能直接使用， + 有特殊含义
print(re.search(r'\+', '1 + 2'))
