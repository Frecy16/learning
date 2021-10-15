def outer(x):
    m = 100
    print('我是outer函数')

    def inner():  # inner函数是定义在outer函数内部的一个函数
        n = 90
        print('我是inner函数')

    if x > 10:
        inner()
    return 'hello'


# inner()  # 在外部不能调用内部函数
outer(8)  # 只调用outer函数
outer(12)  # 调用了outer函数和inner函数
