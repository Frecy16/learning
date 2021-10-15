# 递归简单来说，就是函数内部自己调用自己
# 递归最重要的就是找到出口（停止的条件


def tst():
    print('test')
    tst()


count = 0


def tell_story():
    global count
    count += 1
    print("从前有座山")
    print("山里有座庙")
    print("庙里有个老和尚")
    print("还有一个小和尚")
    print("老和尚在小和尚讲故事")
    print("故事的内容是")
    if count < 5:  # 设定递归停止的条件，5次以后停止
        tell_story()


# 求 1 ~ n 的和
def get_sum(n):
    if n == 0:
        return 0
    return get_sum(n - 1) + n


# 使用递归求 n!
def get_factor(n):
    if n == 0:
        return 1
    return get_factor(n - 1) * n


# 使用递归求斐波那契数列的第 n 个数字  1,1,2,3,5,8,13,21,34,55,89,144,233……
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# tell_story()
# print(get_sum(5))
# print(get_factor(6))  # 720
print(fibonacci(6))  # 8
