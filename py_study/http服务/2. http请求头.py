import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('192.168.61.1', 9000))
server_socket.listen(128)
# 获取的数据是一个元组，元组里有两个元素
# 第一个元素是客户端的socket连接
# 第二个元素是客户端的IP地址和端口号
client_socket, client_addr = server_socket.accept()

# 从客户端的 socket 里 获取数据
data = client_socket.recv(1024).decode('utf8')
print('接收到的数据：\n{}'.format(data))

# 返回内容之前，需要先设置 HTTP 响应头

# 设置一个响应头就换一行
client_socket.send('HTTP/1.1 200 OK\n'.encode('utf8'))

"""
接收到的数据：
# GET 请求方式， GET/POST/PUT/DELETE... ...
# /index.html?name=liming&age=18 请求路径及请求参数
# HTTP/1.1  HTTP版本号
GET / HTTP/1.1
Host: 192.168.61.130:9090  # 请求服务器地址
Connection: keep-alive
Upgrade-Insecure-Requests: 1
# UA 用户代理，最初目的是为了从请求头里辨识浏览器的类型
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9

"""

# 所有的响应头设置完成以后，再换行
client_socket.send('\n'.encode('utf8'))

# 给客户端返回消息
client_socket.send('hello world'.encode('utf8'))
