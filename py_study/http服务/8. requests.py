# requests 模块时第三方的模块，可以用来发送网络连接
# pip install requests


import requests

# r = requests.get('http://127.0.0.1:8000')
# print(r)  # 结果是一个Response 对象
# content 指的是返回结果，是一个二进制，可以用来传递图片
# print(r.content.decode('utf8'))
# print(r.text)
r1 = requests.get('http://127.0.0.1:8000/test')
print(r1.text, type(r1.text))
print(r1.json())  # 把 json 字符串解析成为python里对应的数据类型
