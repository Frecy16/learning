# person = {'name': 'zhangsan', 'age': 18, 'math': 98}

# print(person['name'])  # 'zhangsan'
# print(person['height'])  # KeyError,如果key不存在，会报错

# print(person.get('height'))
# print(person.get('gender', 'female'))
# print(person.get('name', 'lisi'))

# person = {'name': 'zhangsan', 'age': 18, 'gender': 'female'}

# x = person.pop('name')
# print(x)  # 'lisi'
# print(person)  #{'age': 18}

# result = person.popitem()
# # print(result)  # ('gender', 'female')
# # print(person)
# person1 = {'name': 'zhangsan', 'age': 18}
# person2 = {'addr': '襄阳', 'height': 180}
#
# # 字典之间不支持加法运算，字符串、元组、列表可以使用加法
# person1.update(person2)
# print(person1)  #
person = {'name': 'zhangsan', 'age': 18, 'gender': 'female'}

# 第一种遍历方式：直接for...in 循环字典
# for x in person  # for...in 循环获取的是key
#     print(x, '=', person[x])

# 第二种遍历方式：获取到所有的key，然后再遍历key，根据key获取value
# for k in person.keys():
#     print(k, '=', person[k])

# 第三种方式：获取到所有的value，一般不用
# 只能拿到值，不能拿key
# for v in person.valuse():
#     print(v)

# 第四种方式：
# for item in person.items():  # 列表里的元素是元组，把元组当做整体进行遍历
#    print(item[0], '=', item[1])

for k, v in person.items():
    print(k, '=', v)
