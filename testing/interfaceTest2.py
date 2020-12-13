import flask, json
from flask import request
import requests

'''
flask: web框架，通过flask提供的装饰器@server.route()将普通函数转换为服务
登录接口，需要传url、username、passwd
'''

# 创建一个服务，吧当前这个python文件当做一个服务
server = flask.Flask(__name__)


@server.route('/user', methods=['get', 'post'])
def login():
    # 获取通过url请求传参的数据
    key_token = request.values.get('token')
    if key_token == '1651AS5a612q567':
        resu = {'code': 200, 'message': '你好', 'name': '大大'}
        return json.dumps(resu, ensure_ascii=False)  # 将字典转换为json串
    else:
        resu = {'code': 10001, 'token': '参数不能为空！'}
        return json.dumps(resu, ensure_asscii=False)


if __name__ == '__main__':
    server.run(debug=True, port=8889, host='127.0.0.1')
