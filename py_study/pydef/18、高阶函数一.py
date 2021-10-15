def tst():
    print('我是test函数')
    return 'hello'


def demo():
    print('我是demo函数')
    return tst


def bar():
    print('我是bar函数')
    return tst()


x = tst()
print(x)  # 'hello'

y = demo()  # y是test函数
print(y)  # <function tst at 0x0000020C2BF47310>
z = y()
print(z)  # 'hello'

a = bar()  # a是字符串'hello'
print(a)  # 'hello'
