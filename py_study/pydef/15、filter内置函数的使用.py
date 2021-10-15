from functools import reduce

# filter 对可迭代对象进行过滤，得到的是一个filter对象，python2的时候是内置函数，python3修改成了一个内置类
# filter 可以给定两个参数，第一个参数是函数，第二个参数是可迭代对象

ages = [12, 23, 25, 30, 18, 22, 23, 30]
x = filter(lambda ele: ele > 18, ages)
# print(x)
# for i in x:
#     print(i)

# adult = list(x)
# print(adult)

nums = [12, 23, 25, 30, 18, 22, 23, 30]


# m  = map(lambda ele: ele + 2, nums)
# print(list(m))  # 把可迭代对象里的元素都执行函数里的动作

# reduce 以前是一个函数
# 内置函数和内置类都在 builtins.py文件里
# print(reduce(lambda ele1, ele2: ele1 + ele2, nums))  # 183

def foo(x, y):  # x=12,y=23;x=35,y=25;x=60,y-30;
    return x + y


# print(reduce(foo, nums))  # 183

students = [
    {'name': 'zhangsan', 'age': 18, 'score': 98, 'height': 180},
    {'name': 'lisi', 'age': 21, 'score': 97, 'height': 185},
    {'name': 'jone', 'age': 22, 'score': 100, 'height': 175},
    {'name': 'tony', 'age': 23, 'score': 90, 'height': 176},
    {'name': 'henry', 'age': 20, 'score': 95, 'height': 172}
]


def bar(x, y):
    return x + y['age']  # x = 0, y ={'name': 'zhangsan', 'age': 18, 'score': 98, 'height': 180}


# result = reduce(bar, students, 0)  # 0 是初始值
# print(result)
r1 = reduce(lambda x, y: x + y['age'], students, 0)
print(r1)
