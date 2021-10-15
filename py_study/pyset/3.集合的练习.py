import json

# nums = [5, 8, 7, 6, 4, 1, 3, 5, 1, 8, 4]
#
# # 去重排序:
# nums1 = list(set(nums))
# nums1.sort()
# print(nums1)

n = '{"name": "list", "age": 20, "gender": "male"}'
# n = '["hello", "good"]'
# p = eval(n)
# print(type(p))
# s = json.loads(n) # loads可以将json字符串转换成Python里的数据
# print(s)
# print(type(s))

# print(json.dumps(['hello', 'good', 'yes', True]))
# print(json.dumps(('hello', 'good', 'yes', False)))

# nums = [5, 8, 7, 6, 4, 1]
# x = tuple(nums)
# print(x)
#
# y = set(nums)
# print(y)
#
# z = list({'name':'zhangsan', 'age':28, 'score':98})
# print(z)

names = {'zhangsan', 'tony', 'jack'}
names1 = {'zhangsan', 'lisi', 'tony', 'jack'}
print(names in names1)
