"""
基于fork的多进程网络并发模型
    实现步骤
        1.创建监听套接字
        2.等待接收客户端请求
        3.客户端连接创建新的进程处理客户端请求
        4.原进程继续等待其他客户端连接
        5.如果客户端退出，则销毁对应的进程
"""

from socket import *
import os
import signal

# 全部变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)

#  创建监听套接字
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
    # 循环处理客户端连接
    try:
        c, addr = s.accept()
        print("Connect from", addr)
    except KeyboardInterrupt:  # ctrl-c退出
        os._exit(0)
    except Exception as e:
        print(e)
        continue

    # 创建子进程处理客户端事务
    pid = os.fork()
    if pid == 0:
        s.close()  # 子进程中也有套接字s，但是对子进程无用
        handle(c)  # 处理具体事务
        os._exit(0)  # 子进程执行完后销毁
    else:
        c.close()  # 对父进程来说c是无用的
