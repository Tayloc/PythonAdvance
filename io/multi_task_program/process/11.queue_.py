"""
消息队列
    通信原理
        在内存中建立队列模型，进程通过队列将消息存入，或者从队列取出完成进程间通信
    实现方法
        from multiprocessing import Queue
        q = Queue(maxsize=0)
            功能：创建队列对象
            参数：最多存放消息个数
            返回值；队列对象
        q.put(data,[block,timeout])
            功能：向队列存入消息
            参数：data 要存入的内容
            block 设置是否阻塞 False为非阻塞
            timeout 超时检测
        q.get([block,timeout])
            功能：从队列取出消息
            参数：block 设置是否阻塞 False为非阻塞；timeout 超时检测
            返回值：返回获取到的内容
        q.full()    判断队列是否为满
        q.empty()   判断队列是否为空
        q.qsize()   获取队列中消息个数
        q.close()   关闭队列
"""
from multiprocessing import Queue, Process
from time import sleep
from random import randint

# 创建消息队列
q = Queue(5)


def handle():
    for i in range(6):
        x = randint(1, 33)
        q.put(x)
    q.put(randint(1, 16))


def request():
    l = []
    for i in range(6):
        l.append(q.get())
    l.sort()
    l.append(q.get())
    print(l)


p1 = Process(target=handle)
p2 = Process(target=request)
p1.start()
p2.start()
p1.join()
p2.join()
