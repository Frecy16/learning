nums = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
chars = ['a', 'c', 'x', 'd', 'p', 'a', 'p', 'a', 'c', 'c']
# 统计列表中元素出现的次数及元素值
# for i in set(nums):
#     # nums.count(i)
#     print('{} 出现的次数为：{}'.format(i, nums.count(i)))

# dict = {}
# for i in set(chars):
#     # print('{} 出现的次数为：{}'.format(i, chars.count(i)))
#     dict[i] = chars.count(i)
# print(dict)

char_count = {}
# for char in chars:
#     if char in char_count:
#         # print('字典已存在这个字符%s' % char)
#         char_count[char] += 1
#     else:
#         # print('字典中没有这个字符%s' % char)
#         char_count[char] = 1
#
# print(char_count)

# for char in chars:
#     if char not in char_count:
#         char_count[char] = chars.count(char)
# print(char_count)

vs = char_count.values()
# 可以使用内置函数max 取最大数
max_count = max(vs)
print(max_count)

# 打印最大数的key
for k, v in char_count.items():
    if v == max_count:
        print(k)

dict1 = {'a': 100, 'b': 200, 'c': 300}

dict2 = {v: k for k, v in dict1.items()}  # 字典推导式
print(dict2)
