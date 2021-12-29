"""
服务端流程
    socket -> bind -> recvfrom -> sendto -> close

1.创建数据报套接字
    sockfd = socket(AF_INET, SOCK_DGRAM)
2.绑定地址
    sockfd.bind(addr)
3.消息收发
    data, addr = sockfd.recvfrom(buffersize)
        功能：接收UDP消息
        参数：每次最多接收多少字节
        返回值：data 接收到的内容   addr 消息发送方地址
    n = sockfd.sendto(data, addr)
        功能：发送UDP消息
        参数：data 发送的内容 bytes格式   addr 目标地址
        返回值：发送的字节数
4.关闭套接字
    sockfd.close()
"""
import socket
from socket import *

# 创建套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 绑定地址
server_addr = ('127.0.0.1', 8888)
sockfd.bind(server_addr)

# 循环收发消息
while True:
    data, addr = sockfd.recvfrom(1024)
    print("收到消息:", data.decode())
    n = sockfd.sendto(b'Thanks', addr)

# 关闭套接字
socket.close()
