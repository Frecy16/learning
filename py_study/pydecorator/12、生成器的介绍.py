# 生成器其实就是迭代器，是一种比较特殊的迭代器
# 迭代器是一个对象，生成器是一个函数

# 最简单的生成器
x = [i for i in range(10)]  # 列表推导式，x是一个列表

y = (i for i in range(10))  # 生成器其实就是迭代器
print(y)
for n in y:
    print(n)
