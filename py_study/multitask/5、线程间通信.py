import threading
import queue
import time


def produce():
    for i in range(1, 11):
        time.sleep(1)
        print('制作了++++++++面包{}{}'.format(threading.current_thread().name, i))
        q.put('{}{}'.format(threading.current_thread().name, i))


def consume():
    # while True:
    # q.get() 方法是一个阻塞的方法
    time.sleep(0.5)
    print('{}买到--------面包{}'.format(threading.current_thread().name, q.get()))


q = queue.Queue()  # 创建一个队列

p1 = threading.Thread(target=produce, name='pa')
c1 = threading.Thread(target=consume, name='pb')
p2 = threading.Thread(target=produce, name='pc')

# p1.start()
# p2.start()
c1.start()
