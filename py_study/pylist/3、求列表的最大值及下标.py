nums = [3, 1, 9, 8, 4, 2, 0, 7, 5]

# 使用列表的sort方法
# nums.sort()
# print(nums[-1])

# 不使用sort方法
maxNum = nums[0]
maxIndex = 0
for i in range(len(nums) - 1):
    i += 1
    if maxNum < nums[i]:
        maxNum = nums[i]
        maxIndex = i

print(maxNum, maxIndex)
