# with 语句后面的结果对象，需要重写 __enter__ 和 __exit__ 方法
# 当进入到with代码块，会自动调用 __enter__方法里的代码
# 当with 代码块执行完成以后，会自动调用 __exit__ 方法


class Demo(object):
    def __enter__(self):
        print('__enter__方法被执行了')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__方法被调用了')


def create_obj():
    x = Demo()
    return x


# d = create_obj().__enter__()
with create_obj() as d:  # as 变量名
    # 变量 d 不是 create_obj 的返回结果
    # 它是创建的对象 x 调用 __enter__ 之后的返回结果
    print(d)
