"""
IO分类
    阻塞IO    非阻塞IO   IO多路复用  异步IO等
阻塞IO
    1.定义：在执行IO操作时如果执行条件不满足则阻塞。阻塞IO是IO的默认形态。
    2.效率：阻塞IO是效率很低的一种IO，但是由于逻辑简单所以是默认IO行为。
    3.阻塞情况
        因为某种执行条件没有满足造成的函数阻塞
            e.g. accept input recv
        处理IO的时间较长产生的阻塞状态
            e.g. 网络传输 大文件读写
非阻塞IO
    1.定义：通过修改IO属性行为，使原本阻塞的IO变为非阻塞的状态
        设置套接字为非阻塞IO
            sockfd.setblocking(bool)
                功能：设置套接字为非阻塞IO
                参数：默认为True,表示套接字IO阻塞；设置为False则套接字IO变为非阻塞
        超时检测：设置一个最长阻塞时间，超过该时间后则不再阻塞等待
            sockfd.settimeout(sec)
                功能：设置套接字的超时时间
                参数：设置的时间
"""

from socket import *
from time import ctime, sleep

# 日志文件
f = open('log.txt', 'a+')

# tcp套接字
sockfd = socket()
sockfd.bind(('127.0.0.1', 8888))
sockfd.listen(3)

# 设置套接字为非阻塞
# sockfd.setblocking(False)  # 将sockfd设置为非阻塞后通过sockfd调用的函数都会变为非阻塞的状态

# 设置超时检测
sockfd.settimeout(3)  # 通过sockfd所调用的所有函数都会最多阻塞3秒：在3秒内满足条件就不会阻塞，继续运行；没有满足条件最多也阻塞3秒

while True:
    print("Waiting for connect...")
    # 没有客户端连接每隔3秒写一条日志
    try:
        connfd, addr = sockfd.accept()
    except (BlockingIOError, TimeoutError) as e:
        sleep(3)
        f.write("%s : %s\n" % (ctime(), e))
        f.flush()
    else:
        print("Connect from:", addr)
        data = connfd.recv(1024).decode()
        print(data)
