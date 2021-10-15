import threading
import time

# 多个线程可以同时操作一个全局变量（多个线程共享全局变量）
# 线程安全问题: 线程t1 卖出一张票，还剩-1张
ticket_num = 20


def sale_ticket():
    global ticket_num
    while True:
        if ticket_num > 0:
            time.sleep(0.1)
            ticket_num -= 1
            print('{} 卖出一张票，还剩{}张'.format(threading.current_thread().name, ticket_num))
        else:
            print('不好意思，票已经卖完了')
            break


t1 = threading.Thread(target=sale_ticket, name='线程t1')
t2 = threading.Thread(target=sale_ticket, name='线程t2')

t1.start()
t2.start()
