# 生成器的形式就相当于一个函数


def my_gen(n):
    i = 0
    while i < n:
        i += 1
        # return i  # return 表示一个函数的结束
        yield i  # 使用 yield 结果是一个生成器
        print('我是yield以后的代码')


m = my_gen(10)  # 获取一个生成器，不会调用 my_gen() 函数


# print(next(m))  # 当调用next方法，获取数据时，才会调用方法
# print(next(m))  # 再执行next方法，会从上一次yield出来的位置继续执行代码
# for j in m:
#     print(j)


def Fibonacci(n):
    num1 = num2 = 1
    count = 0
    while count < n:
        count += 1
        yield num1
        num1, num2 = num2, num1 + num2


f = Fibonacci(12)
for j in f:
    print(j)
