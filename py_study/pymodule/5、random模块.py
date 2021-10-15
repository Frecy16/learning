# random 模块用来生成一个随机数
import random

print(random.randint(2, 9))  # 用来生成[a, b]的随机整数,等价于randrange(a, b+1)
# random()  用来生成[0, 1)的随机浮点数
print(random.random())

# randrange(a, b)  用来生成[a, b)的随机整数
print(random.randrange(2, 9))

# chioce 用来在可迭代对象里随机抽取一个数据
print(random.choice([1, 2, 3, 4, 6, 2, 1, 6]))

# sample 用来在可迭代对象里随机抽取 n 个数据
print(random.sample(['zhangsan', 'lisi', 'jack', 'jerry', 'henry', 'tony'], 2))
