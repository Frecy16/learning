# 1. 一个函数作为另一个函数的参数
# 2. 一个函数作为另一个函数的返回值
# 3. 函数内部再定义一个函数

def foo():
    print('我是foo，我被调用了')
    return 'foo'


def bar():
    print('我是bar，我被调用了')
    # return foo()
    return foo


x = bar()
print(x)

y = bar()()
print(y)  # 'foo'


def outer():
    m = 100

    def inner():
        n = 90
        print('我是inner函数')

    print('我是outer函数')
    return inner


outer()
outer()()  # 调用内部函数
