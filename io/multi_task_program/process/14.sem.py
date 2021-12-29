"""
信号量(信号灯集)
    通信原理
        给定一个数量对多个进程可见。多个进程都可以操作该数量增减，并根据数量值决定自己的行为
    实现方法
        from multiprocessing import Semaphore

        sem = Semaphore(num)
            功能：创建信号量对象
            参数：信号量的初始值
            返回值：信号量对象
        sem.acquire() 将信号量减1 当信号量为0时阻塞
        sem.release() 将信号量加1
        sem.get_value() 获取信号量数量
    信号量数量相当于资源，执行任务必须消耗资源
"""

from multiprocessing import Process, Semaphore
from time import sleep
import os

# 创建信号量(最多允许3个任务同时执行)
sem = Semaphore(3)


# 任务函数
def handle():
    sem.acquire()  # 想执行任务必须消耗一个信号量
    print("%s 执行任务" % os.getpid())
    sleep(2)
    print("%s 执行任务完毕" % os.getpid())
    sem.release()  # 归还信号量


# 10个任务需要执行
for i in range(10):
    p = Process(target=handle)
    p.start()
