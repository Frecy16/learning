import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('192.168.61.1', 8080))
f = open('../http服务/chat.txt', 'w', encoding='utf8')


def send_msg():
    while True:
        s.sendto(input().encode('gbk'), ("192.168.61.1", 9001))


def recv_msg():
    while True:
        data, addr = s.recvfrom(1024)
        print(data.decode('gbk'), addr[0], addr[1], file=f, flush=True)


t1 = threading.Thread(target=send_msg)
t2 = threading.Thread(target=recv_msg)

t1.start()
t2.start()
