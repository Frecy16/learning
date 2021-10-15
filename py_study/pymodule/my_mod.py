# __all__ = ['m', 's', 'test']

m = 100
n = '123456'
s = 'hello'
_age = 19


def test():
    print("我是my_mod模块里的test函数")


def test_add(a, b):
    return a + b


def test_div(a, b):
    return a / b


# del _age

# __name__: 当直接运行这个py文件的时候，值是 __main__
# 如果这个py文件作为一个模块导入的时候，值是文件名
if __name__ == '__main__':
    print('my_mod里的name值是：', __name__)
    print('测试一下除法, 结果是', test_div(8, 2))
