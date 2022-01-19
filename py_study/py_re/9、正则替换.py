# 正则表达式作用是用来对字符串进行检索和替换
# 检索：match  search  fullmatch  findall  finditer
# 替换：sub
import re

s = 'fas32sfdo2ioi0rejk4d09cl.a'

# print(re.sub(r'\d', 'x', s))  # fasxxsfdoxioixrejkxdxxcl.a 把每个数字替换成 x
# print(re.sub(r'\d+', 'x', s))  #  fasxsfdoxioixrejkxdxcl.a  把每一段连起来的数字替换为 x

p = 'hello34good23'  # 把字符串里的苏子 *2


# 第一个参数是正则表达式
# 第二个参数是新字符或者一个函数
# 第三个参数是需要被替换的原来的字符串
def test(x):
    y = int(x.group(0))
    y *= 2
    return str(y)


# sub内部在调用 test 方法时，会把每一个匹配到的数据以re.Match的格式传参
print(re.sub(r'\d+', test, p))  # test 函数时自动调用的
