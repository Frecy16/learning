# ages = (18)  # 这种书写方式，ages是一个整数，并不是一个元组
# ages = (18,)  # 如果只有一个元素，要在最后面加 ,
# print(type(ages))

# tuple 内置类
# print(tuple(18))
# print(tuple('h'))  #  ('h',)

# heights = ('180', '172', '170')
#
# heights_list = list(heights)  #
# print(heights_list)
# print('*'.join(heights))  #

# 元组也可以遍历
nums = (9, 4, 3, 1, 7, 6, 9, 3, 9)
# for i in nums:
#     print(i)

# while循环进行遍历
j = 0
while j < len(nums):
    print(nums[j])
    j += 1
