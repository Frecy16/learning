# 在程序运行过程中，由于编码不规范等造成程序无法正常执行，此时程序就会报错
# 健壮性: 很多编程语言里都有异常处理机制。


def div(a, b):
    return a / b


try:
    x = div(3, 1)
except Exception as e:  # 如果程序出错了，会立刻跳转到 except 语句
    print('除数不能为0')
else:  # 程序运行如果没有错误，会执行else语句里的代码
    print('结果是：', x)
