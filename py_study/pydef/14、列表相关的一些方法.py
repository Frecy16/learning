# 列表有几个内置函数和内置类，用了匿名函数
nums = [4, 8, 2, 1, 7, 6]
# nums.sort()
# print(nums)
tup = (5, 9, 2, 1, 3, 8, 7, 4)
# sorted内置函数，不会改变原有的数据，而是生成一个新的结果
# x = sorted(nums)
# print(x)
x1 = sorted(tup)
# print(x1)  # [1, 2, 3, 4, 5, 7, 8, 9]

students = [
    {'name': 'zhangsan', 'age': 18, 'score': 98, 'height': 180},
    {'name': 'lisi', 'age': 21, 'score': 97, 'height': 185},
    {'name': 'jone', 'age': 22, 'score': 100, 'height': 175},
    {'name': 'tony', 'age': 23, 'score': 90, 'height': 176},
    {'name': 'henry', 'age': 20, 'score': 95, 'height': 172}
]


# 字典和字典之间不能使用比较运算 <
# student.sort()

def foo(ele):
    # print("ele = {}".format(ele))
    return ele['height']


# 需要传递参数 key 指定比较规则
# key 参数类型是函数

# 在sort内部实现的时候，调用了foo方法，并且传入了一个参数，参数就是列表里的元素
# students.sort(key=foo)

students.sort(key=lambda ele: ele['score'])
print(students)
