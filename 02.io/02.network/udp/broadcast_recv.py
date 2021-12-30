"""
UDP套接字广播
    广播定义：一端发送多点接收
    广播地址：每个网络的最大地址为发送广播的地址，向该地址发送，则网段内所有主机都能接收。

步骤
    1.创建udp套接字
    2.设置套接字可以发送接收广播（setsockopt）
    3.选择接收的端口
    4.接收广播
"""

from socket import *

# 创建udp套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 设置套接字接收广播
sockfd.setsockopt(SOL_SOCKET, SO_BROADCAST, True)

# 绑定地址
sockfd.bind(('0.0.0.0', 9999))

while True:
    msg, addr = sockfd.recvfrom(1024)
    print(msg.decode())

