def add(a, b):
    c = a + b  # 变量C在外部是不可见的，只能在函数内部使用
    return c  # return 表示一个函数的执行结果


# 获取到 add 函数的结果，然后再求结果的 4 次方
result = add(1, 2)
print(result ** 4)

# 如果一个函数没有返回值，它的返回就是None

# print就是一个内置函数
x = print('hello')  # None

age = input('请输入您的年龄：')
print(age)
