import socket


class Myserver(object):
    def __init__(self, ip, port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((ip, port))
        self.server_socket.listen(128)

    def start_server(self):
        while True:
            client_socket, client_addr = self.server_socket.accept()

            # 从客户端的 socket 里 获取数据
            data = client_socket.recv(1024).decode('utf8')
            print('接收到的数据：\n{}'.format(data))
            path = ''
            if data:
                respond_header = 'HTTP/1.1 200 OK\n'
                path = data.splitlines()[0].split()[1]
                # print('path=%s' % path)
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


server = Myserver("0.0.0.0", 9090)
server.start_server()
