# 列表推导式作用是使用简单的语法创建一个列表
# nums = [i for i in range(10)]
# print(nums)

# nums = []
# for i in range(10):
#     nums.append(i)
# print(nums)
#
# x = [i for i in range(10) if i % 2 == 0]
# print(x)

# points 是一个列表，这个列表里的额元素是元组
# points = [(x, y) for x in range(5, 9) for y in range(10, 20)]
# print(points)

# 请写一段python代码，实现分组一个list里面的元素，比如[1,2 ,3, 4, ...100], 变成[[1,2,3],[4,5,6]...]
m = [i for i in range(1, 101)]
n = [m[j:j + 3] for j in range(0, 100, 3)]  # range 第3个为步长
print(n)
