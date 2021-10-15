import time


def calc_time(fn):
    def inner(m, *args, **kwargs):
        start = time.time()
        y = fn(m)
        end = time.time()
        print('代码的运行耗时 {} 秒'.format(end - start))
        return y

    return inner


# 装饰器原理：1、调用cal_time；2、把被装饰的函数传递给fn ；3、当再次调用demo函数时已经不再是上面的demo，而是inner函数
@calc_time
def demo(n):
    x = 0
    for i in range(1, n):
        x += i
    return x


# @calc_time
# def foo():
#     print('hello')
#     time.sleep(1)
#     print('world')


z = demo(1000000, 'well', a='done')
print('装饰后的demo = {}'.format(z))
# foo()
