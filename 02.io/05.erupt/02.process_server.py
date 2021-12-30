"""
基于process的多进程网络并发模型
    实现步骤
        1.创建监听套接字
        2.等待接收客户端请求
        3.客户端连接创建新的进程处理客户端请求
        4.原进程继续等待其他客户端连接
        5.如果客户端退出，则销毁对应的进程
"""

from multiprocessing import *
from socket import *
import os, signal

# 全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
s.bind(ADDR)
s.listen(5)

# 处理僵尸进程
signal.signal(signal.SIGCHLD, signal.SIG_IGN)
print("Listen the port 8888...")


def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()


while True:
    try:
        c, addr = s.accept()
        print("Connect from:", addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue

    # 创建子进程处理客户端事务
    p = Process(target=handle, args=(c,))
    p.daemon = True  # 父进程结束则所有服务终止
    p.start()
