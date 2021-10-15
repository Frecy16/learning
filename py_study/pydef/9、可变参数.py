# *args 表示可变位置参数
# **kwargs 表示可变的关键字参数
def add(a, b, *args, mul=1, **kwargs):  # 缺省参数要放在可变参数的后面
    # print('a = {}, b = {}'.format(a, b))
    # print('args = {}'.format(args))  # 多出来的可变参数会以元组的形式保存到args里
    print('kwargs = {}'.format(kwargs))  # 多出来的关键字参数会以字典的形式保存
    s = a + b
    for arg in args:
        s += arg

    print(s + mul)


add(1, 3)
add(9, 5, 4, 2, 0)
add(1, 3, 5, 7, mul=2, x=0, y=4)  # kwargs = {'x': 0, 'y': 4}，18
