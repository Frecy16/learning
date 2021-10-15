import json
from wsgiref.simple_server import make_server


def load_file(filename, **kwargs):
    try:
        with open(filename, 'r', encoding='utf8') as f:
            content = f.read()
            if kwargs:
                content = content.format(**kwargs)
            return content
    except FileNotFoundError:
        return '文件未找到'


def first_page():
    return '欢迎来到首页'


def login():
    return '欢迎进入登录页面'


def register():
    return '没有账号？请先进行注册'


def test():
    return json.dumps({'name': 'liming', 'age': 18, 'gender': 'male'})


def demo():
    return load_file('chat.txt')


def girlfriend():
    return load_file('ForGirlfriend.html')


def info():
    return load_file('info.html', username='至尊宝')


url = {
    '/': first_page,
    '/login': login,
    '/register': register,
    '/test': test,
    '/demo': demo,
    '/love': girlfriend,
    '/info': info
}


def demo_app(environ, start_respond):
    path = environ['PATH_INFO']
    # print(environ.get('QUERY_STRING'))  # QUERY_STRING ==> 获取到客户端GET请求方式传递的参数

    status_code = '200 OK'
    method = url.get(path)
    if method:
        response = method()
    else:
        status_code = '404 Not Found'
        response = '页面不存在'
    # if path == '/':
    #     response = '欢迎来到首页'
    # elif path == '/login':
    #     response = '欢迎进入登录页面'
    # elif path == '/register':
    #     response = '没有账号？请进行注册'
    # elif path == '/test':
    #     response = json.dumps({'name': 'liming', 'age': 18, 'gender': 'male'})
    # elif path == '/demo':
    #     response = open_file('chat.txt')
    # elif path == '/love':
    #     response = open_file('ForGirlfriend.html')
    # elif path == '/info':
    #     response = open_file('info.html', name='至尊宝')
    # else:
    #     status_code = '404 Not Found'
    #     response = '页面不存在'
    start_respond(status_code, [('Content-Type', 'text/html;charset=utf8'), ('Author', 'chenyang')])
    return [response.encode('utf8')]


if __name__ == '__main__':
    # demo_app 是一个函数，用来处理用户的请求
    httpd = make_server('', 8000, demo_app)
    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")
    import webbrowser

    webbrowser.open('http://localhost:8000/xyz?abc')
    while True:
        httpd.handle_request()  # serve one request, then exit
