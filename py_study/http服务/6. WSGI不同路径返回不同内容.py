from wsgiref.simple_server import make_server


def demo_app(environ, start_respond):
    path = environ['PATH_INFO']
    # 状态码： RESTFUL ==> 前后端分离
    # 2XX：请求响应成功
    # 3XX：重定向
    # 4XX：客户端的错误
    # 5XX：服务器的错误
    status_code = '200 OK'
    if path == '/':
        response = '欢迎来到首页'
    elif path == '/login':
        response = '欢迎进入登录页面'
    elif path == '/register':
        response = '没有账号？请进行注册'
    else:
        status_code = '404 Not Found'
        response = '页面不存在'
    start_respond(status_code, [('Content-Type', 'text/html;charset=utf8'), ('author', 'chenyang')])
    return [response.encode('utf8')]


if __name__ == '__main__':
    # demo_app 是一个函数，用来处理用户的请求
    httpd = make_server('', 8000, demo_app)
    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")
    # import webbrowser
    # webbrowser.open('http://localhost:8000/xyz?abc')
    while True:
        httpd.handle_request()  # serve one request, then exit
