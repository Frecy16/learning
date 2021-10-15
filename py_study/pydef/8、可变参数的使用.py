def add(a, b):
    return a + b


def add_many(n):
    m = 0
    for i in n:
        m += i

    return m


nums = [1, 2, 3, 4, 5, 6]
result = add_many(nums)
print(result)
print(add_many((1, 2, 3, 4, 5)))

# 一次input只能接收一次用户的输入
x = input("请输入多个数据，数据中间使用逗号分隔：")
innums = x.split(',')
nums2 = []
for i in innums:
    nums2.append(int(i))
print(nums2)

# nums1 = []
# while True:
#     num = input("请输入数字，输入exit退出输入：")
#     if num == 'exit':
#         break
#     nums1.append(int(num))
#
# print(nums1)
