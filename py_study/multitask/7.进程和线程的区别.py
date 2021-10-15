"""
功能：
    进程：能够完成多任务，比如在一台电脑上能够同时运行多个QQ
    线程：能够完成多任务，比如一个QQ中的多个聊天窗口

定义：
    同一进程间的不同线程可以共享全局变量
    不同的进程间不能共享全局变量

区别：
    一个程序至少有一个进程，一个进程至少有一个线程
    线程的划分尺度小于进程（资源比进程少），使得多线程程序的并发性高
    进程在执行过程中拥有独立的内存单元，而多个线程共享内存，从而极大地提高了程序的运行效率
    线程不能够独立执行，必须依存在进程中
    可以将进程理解为工厂中的一条流水线，而其中的线程就是这个流水线上的工人

优缺点：
    线程和进程在使用上各有缺点：线程执行开销小，但不利于资源的管理和保护；而进程正相反。
"""
import os
import threading
import multiprocessing

n = 100


def test():
    global n
    n += 1
    print('{}n的值是{}'.format(os.getpid(), n))


def demo():
    global n
    n += 1
    print('{}里n的值是{}'.format(os.getpid(), n))


# test()  # 101
# demo()  # 102

# 同一个进程里的两个子线程，线程之间可以共享同一进程的全局变量
# t1 = threading.Thread(target=test)
# t2 = threading.Thread(target=demo)
# t1.start()
# t2.start()


if __name__ == '__main__':
    # 不同的进程访问全局变量，不同进程各自保存一份全局变量，不会共享全局变量
    p1 = multiprocessing.Process(target=test)
    p2 = multiprocessing.Process(target=demo)
    p1.start()
    p2.start()
