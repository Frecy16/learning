import time


# start = time.time() # time模块里的time方法，可以获取当前时间的时间戳
# # 时间戳是从1970-01-01 00:00:00 UTC 到现在的秒数
# # 从1970-01-01 00:00:00 ~ 2021-04-05 10:15 UTC  东八区 需要减8个小时
# print('start = {}'.format(start))
#
# x = 0
# for i in range(1, 1000000):
#     x += i
#
# print(x)
# end = time.time()
# print('end = {}'.format(end))
#
# print('代码的运行耗时 {} 秒'.format(end - start))


def calc_time(fn):
    start = time.time()
    fn()
    end = time.time()
    print('代码的运行耗时 {} 秒'.format(end - start))


def demo():
    x = 0
    for i in range(1, 1000000):
        x += i
    print(x)


def foo():
    print('hello')
    time.sleep(1)
    print('world')


calc_time(demo)
calc_time(foo)
