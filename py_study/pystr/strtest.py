# from pydantic import BaseModel
#
#
# class AddressDate(BaseModel):
#     client_ip = "N/A"
#     client_port: int = 0
#     server_ip = "N/A"
#     server_port: int = 0

# str1 = 'hello world'

# print(str1.startswith('he', 1, 3))
# import base64
#
# str = "this is string example....wow!!!"
# str = base64.b64encode(str.encode('utf-8',errors = 'strict'))
#
# print ("Encoded String: " , str)

# x = '大家好，我是{}，我今年{}岁了'.format('李明', 18)
# print(x)
#
# # {数字} 根据数字的顺序来进行填入，数字从0开始
# y = '大家好，我是{1}，我今年{0}岁了'.format(16, 'lily')
# print(y)
#
# # {变量名}
# m = '大家好，我是{name}，今年{age}，我来自{addr}'.format(age=18, name='amy', addr='海南')
# print(m)
#
# # 混合使用  {数字} {变量}
# n = '大家好，我是{name}，我今年{1}岁了，我来自{0}'.format('北京', 24, name='tony')
# print(n)
#
# # {} 什么都不写 {数字} 不能混合使用
# lst = ['liuxing', 18, '上海', 180]
# # b = '大家好，我是{}，我今年{}岁了，我来自{}，身高{}cm'.format(lst[0], lst[1], lst[2], lst[3])
# b = '大家好，我是{}，我今年{}岁了，我来自{}，身高{}cm'.format(*lst)
# print(b)
#
# info = {'name': 'lilei', 'age': 24, 'addr': '北京', 'height': 190}
# c = '大家好，我是{name}，我来自{addr}，身高{height}cm，我今年{age}岁了'.format(**info)
# print(c)


# heros = ['阿珂', '嬴政', '韩信', '露娜', '后羿', '亚瑟']
# heros.append('黄忠')
# print(heros)  # ['阿珂', '嬴政', '韩信', '露娜', '后羿', '亚瑟', '黄忠']
#
# heros.insert(3, '李白')
# print(heros)  # ['阿珂', '嬴政', '韩信',  '李白', '露娜', '后羿', '亚瑟', '黄忠']
#
# x = ['马可波罗', '米莱迪', '狄仁杰']
# heros.extend(x)
# print(heros)
# print(x)
