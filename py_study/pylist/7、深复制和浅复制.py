import copy

# 浅复制（拷贝）
nums = [1, 2, 3, 4, 5]
nums1 = nums  # 深拷贝/浅拷贝？都不是，是指向统一地址，是赋值

nums2 = nums.copy()  # 浅拷贝，两个内容一模一样，但是不是同一个对象

nums3 = copy.copy(nums)  # 和 nums.copy() 功能一样，都是浅拷贝

# 深拷贝，只能使用copy模块实现
words = ['hello', 'good', [100, 200, 300], 'yes', 'hi', 'ok']

# words1是words的浅拷贝
# words1 = words.copy()
# words[0] = '你好'
# print(words1)  # words1 不变，['hello', 'good', [100, 200, 300], 'yes', 'hi', 'ok']

# words[2][0] = 1
# print(words1)  # words1 也改变, ['hello', 'good', [1, 200, 300], 'yes', 'hi', 'ok']， 浅拷贝只拷贝了一层，嵌套的还是指向同一个值

# http://www.pythontutor.com  代码过程演示网站
words2 = copy.deepcopy(words)
words[2][1] = 2
print(words)  # ['hello', 'good', [100, 2, 300], 'yes', 'hi', 'ok']
print(words2)  # words2 不变，['hello', 'good', [100, 200, 300], 'yes', 'hi', 'ok']，深拷贝是完完全全的复制成独立的一份
