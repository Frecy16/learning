import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# IP地址只能通过ip地址访问
# server_socket.bing(("192l168.61.1", 9000))  # 能够通过127.0.0.1 和 localhost 来访问
# 0.0.0.0 表示所有的可用的地址

server_socket.bind(('192.168.61.1', 9002))
server_socket.listen(128)
while True:
    client_socket, client_addr = server_socket.accept()

    # 从客户端的 socket 里 获取数据
    data = client_socket.recv(1024).decode('utf8')
    print('接收到的数据：\n{}'.format(data))
    path = ''
    if data:
        respond_header = 'HTTP/1.1 200 OK\n'
        path = data.splitlines()[0].split()[1]
        print('path=%s' % path)
        if path == '/':
            respond_body = '欢迎您，这是首页'
        elif path == '/login':
            respond_body = '欢迎来到登录页面'
        elif path == '/register':
            respond_body = '欢迎进入注册页面'
        else:
            respond_header = 'HTTP/1.1 400 Page Not Found\n'
            respond_body = '请求页面不存在……'

        respond_header += 'content-type:text/html;charset=utf-8\n'
        respond_header += '\n'

        respond_data = respond_header + respond_body
        client_socket.send(respond_data.encode('utf8'))
