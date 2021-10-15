def add(a, b):
    return a + b


# x = add(4, 5)  # 函数名(实参) 作用是调用函数，获取到函数的执行结果，并赋值给变量x
# print(x)

# print("0x%X" % id(add))
# fn = add  # 相当于给函数add起了一个别名fn
# print("0x%X" % id(fn))
# print(fn(3, 4))

# 除了使用def 关键字定义一个函数以外，还可以使用 lambda 表达式定义一个函数
# 调用匿名函数两种方式：
# 1.给它定义一个名字（很少这样使用）
# 2.把这个函数当做参数传给另一个函数使用
# lambda a, b: a * b  # 匿名函数


def calc(a, b, fn):
    c = fn(a, b)
    return c


def addi(a, b):
    return a + b


def minus(a, b):
    return a - b


# x1 = calc(1, 2, addi)  # a=1,b=2,fn=addi
# x2 = calc(10, 5, minus)  # a=10,b=5,fn=minus
# print(x1, x2)

x3 = calc(5, 11, lambda x, y: x + y)
x4 = calc(16, 4, lambda x, y: x - y)
x5 = calc(4, 5, lambda x, y: x * y)
x6 = calc(12, 4, lambda x, y: x / y)
print(x3, x4, x5, x6)
