import threading
import time

ticket_num = 20

# 锁的好处：确保了某段关键代码只能由一个线程从头到尾完整的执行
# 坏处：1.阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地降低了
#      2.由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的时间，可能会造成死锁

# 创建一把锁
lock = threading.Lock()


def sale_ticket():
    global ticket_num
    while True:
        lock.acquire()  # 加同步锁
        if ticket_num > 0:
            time.sleep(0.1)
            ticket_num -= 1
            lock.release()  # 解除同步锁
            print('{} 卖出一张票，还剩{}张'.format(threading.current_thread().name, ticket_num))
        else:
            lock.release()  # 解除同步锁
            print('不好意思，票已经卖完了')
            break


t1 = threading.Thread(target=sale_ticket, name='线程t1')
t2 = threading.Thread(target=sale_ticket, name='线程t2')

t1.start()
t2.start()
