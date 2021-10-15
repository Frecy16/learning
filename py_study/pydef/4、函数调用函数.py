def Test1():
    print("test1开始了")
    print("test1结束了")


def Test2():
    print("test2开始了")
    Test1()
    print("test2结束了")


# 定义函数求n~m之间所有整数之和
def sumInt(m, n):
    su = 0
    for i in range(m, n + 1):
        su += i
    return su


# 求一个n的阶乘
def factor(n):
    x = 1
    for i in range(1, n + 1):
        x *= i

    return x


def sumFac(m):
    sumf = 0
    for i in range(1, m + 1):
        sumf += factor(i)

    return sumf


# 计算m阶乘的和 m = 6 ==>  1！+2！+3！+4！+5！+6！
def sumFactor(m):
    sumf = 0
    for i in range(1, m + 1):
        x = 1
        for j in range(1, i + 1):
            x *= j
        sumf += x

    return sumf


# Test2()
# s = sumInt(1, 10)
# print(s)
y = factor(5)
print(y)
# sf = sumFactor(6)
# print(sf)
sf1 = sumFac(6)
print(sf1)
