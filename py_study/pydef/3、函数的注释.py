def add(a: int, b: int):  # :int 只是一个建议

    """
    这个函数用来将两个数字相加
    :param a: 第一个数字
    :param b: 第二个数字
    :return: 两个数字相加的结果
    """
    return a + b


# help(add)  # 查看函数的详情
x = add(1, 2)
print(x)

y = add('hello', 'world')
print(y)

# z = add('hello', 5)
# print(z)
