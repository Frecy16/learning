import sys

# sys.stdin  # 接收用户的输入，就是读取键盘里输入的数据
# sys.stdout  # 标准输出
# sys.stderr  # 错误输出

# s_in = sys.stdin
# while True:
#     content = s_in.readline().rstrip('\n')
#     if content =='':
#         break
#     print(content)

sys.stdout = open('info.log', 'a', encoding='utf8')
print('take me to your heart')
print('so many people, all the around world')

sys.stdout.close()

sys.stderr = open('error.log', 'a', encoding='utf8')
print(1 / 0)
sys.stderr.close()
