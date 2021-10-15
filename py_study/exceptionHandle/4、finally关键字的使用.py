# file = open('D:/视频/VID_20191001_111726.mp4', 'rb')
#
# try:
#     while True:
#         content = file.read(1024)
#         if not content:
#             break
#         print(content)
#
# finally:  # 最终都会被执行的代码
#     print('文件被关闭了')
#     file.close()
#

def test(a, b):
    x = a + b
    return x  # 一旦return就表示函数结束
    return 'hello'  # 这段代码不会被执行，一般情况下，一个函数最多只能执行一个return语句


def demo(a, b):
    try:
        x = a / b
    except ZeroDivisionError:
        return '除数不能为0'
    else:
        return x
    finally:
        return 'good'  # 如果函数里面有finally， finally里的返回值会覆盖之前的返回值


# print(demo(1, 2))
print(demo(1, 0))  # 'good'
