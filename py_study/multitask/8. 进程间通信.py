import os
import multiprocessing
import time


def create(m, x):
    for i in range(m):
        time.sleep(0.5)
        print('生产了++++++++pid: {} {}'.format(os.getpid(), i))
        x.put('pid: {} {}'.format(os.getpid(), i))


def consume(n, x):
    for i in range(n):
        time.sleep(0.5)
        print('消费了-------- {}'.format(x.get()))


if __name__ == '__main__':
    q = multiprocessing.Queue()  # 创建进程间的队列

    p1 = multiprocessing.Process(target=create, args=(10, q))  # 进程间不能共享全局变量，需要将队列作为参数传入进程中
    p2 = multiprocessing.Process(target=create, args=(10, q))
    c1 = multiprocessing.Process(target=consume, args=(10, q))
    p1.start()
    p2.start()
    c1.start()
