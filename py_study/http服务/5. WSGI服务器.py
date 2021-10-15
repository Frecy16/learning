from wsgiref.simple_server import make_server


# demo_app 需要两个参数
# 第 0 个参数，表示环境（电脑的环境；请求路径的环境）
# 第 1 个参数，是一个函数，用来返回响应头
# 这个函数需要一个返回值，返回值是一个列表
# 列表里只有一个元素，是一个二进制，表示返回给浏览器的数据
def demo_app(environ, start_respond):
    # environ是一个字典，保存了很多的数据
    # 其中重要的一个是 PATH_INFO 能够获取到用户的访问路径
    path = environ['PATH_INFO']
    print('path= {}'.format(path))
    start_respond('200 OK', [('Content-Type', 'text/html;charset=utf8'), ('author', 'chenyang')])
    return ['hello, welcome to this page, you are lucky fish!'.encode('utf8')]


if __name__ == '__main__':
    # demo_app 是一个函数，用来处理用户的请求
    httpd = make_server('', 8000, demo_app)  # '' 表示'0.0.0.0'
    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")
    import webbrowser

    webbrowser.open('http://localhost:8000/xyz?abc')
    httpd.handle_request()  # serve one request, then exit
