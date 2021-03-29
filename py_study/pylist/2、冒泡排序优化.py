nums = [6, 5, 3, 1, 8, 7, 2, 4]

# 1、最初的方法：时间复杂度 O(n^2)
# j = 0
# count = 0
# while j < len(nums) - 1:
#     i = 0
#     while i < len(nums) - 1:
#         count += 1
#         if nums[i] > nums[i + 1]:
#             nums[i], nums[i + 1] = nums[i + 1], nums[i]
#         i += 1
#     j += 1
#
# print(nums)
# print(count)  # 次数为len(nums)-1 的平方

# 2、第一步优化
# j = 0
# count = 0
# while j < len(nums) - 1:
#     i = 0
#     while i < len(nums) - 1 - j:
#         count += 1
#         if nums[i] > nums[i + 1]:
#             nums[i], nums[i + 1] = nums[i + 1], nums[i]
#         i += 1
#     j += 1
#
# print(nums)
# print(count) # 次数为 len(nums)-1的平方 -0-1-2-3-4-5-6...-len(nums)-1

# 3、进一步优化
j = 0
count = 0
while j < len(nums) - 1:
    # 在每一趟里都定义一个flag
    flag = True  # 假设每一趟比较都没有交换
    i = 0
    while i < len(nums) - 1 - j:
        count += 1
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            flag = False  # 只要交换了，假设不成立
        i += 1
    if flag:
        # 这一趟走完以后，flag依然是True，说明这一趟没有进行过数据交换
        break
    j += 1

print(nums)
print(count)
