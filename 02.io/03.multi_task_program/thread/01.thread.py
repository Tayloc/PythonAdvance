"""
线程编程(Thread)
    什么是线程
        线程被称为轻量级的进程
        线程也可以使用计算机多核资源，是多任务编程方式
        线程是系统分配内核的最小单元
        线程可以理解为进程的分支任务
    线程特征
        一个进程中可以包含多个线程
        线程也是一个运行行为，消耗计算机资源
        一个进程中的所有线程共享这个进程的资源
        多个线程之间的运行互不影响各自运行
        线程的创建和销毁消耗资源远小于进程
        各个线程也有自己的ID等特征

    threading模块创建线程
        封装线程函数
        创建线程对象
            from threading import Thread
            t = Thread()
                功能：创建线程对象
                参数：target 绑定线程函数    args 元组，给线程函数位置传参   kwargs 字典，给线程函数键值传参
        启动线程
            t.start()
        回收线程
            t.join([timeout])
"""

import threading
from time import sleep
import os


# 线程函数
def music():
    for i in range(3):
        sleep(2)
        print(os.getpid(), "播放 : 黄河大合唱")


# 创建线程对象
t = threading.Thread(target=music)

# 启动线程
t.start()

for i in range(4):
    sleep(1)
    print(os.getpid(), "播放 : 葫芦娃")

# 回收线程
t.join()
