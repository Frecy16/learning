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

# 所有的响应头设置完成以后，再换行
client_socket.send('\n'.encode('utf8'))

# 给客户端返回消息
client_socket.send('hello world'.encode('utf8'))
