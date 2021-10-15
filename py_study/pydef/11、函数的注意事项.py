# 函数的三要素：函数名、参数和返回值
# 在有一些编程语言（java，c）里，允许函数重名，在Python里不允许函数的重名
# 如果函数重名了，后一个函数会覆盖前一个函数
# python里，函数名也可以理解成一个变量名


def tst(a, b):
    print('hello, a = {}, b = {}'.format(a, b))


def tst(a):
    print('good, a = {}'.format(a))


tst(3, 4)

tst = 5
tst(3)  # tst 不再是一个函数，而是一个int变量，不能调用
