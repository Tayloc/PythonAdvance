"""
udp客户端流程
    socket -> bind<可选，一般不写> -> sendto -> recvfrom -> close
1.创建套接字
2.收发消息
3.关闭套接字
"""

from socket import *

# 服务器地址
ADDR = ('127.0.0.1', 8888)

# 创建udp套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 循环收发消息
while True:
    data = input("Msg>>")
    if not data:
        break
    sockfd.sendto(data.encode(), ADDR)
    msg, addr = sockfd.recvfrom(1024)
    print("From server:", msg.decode())

sockfd.close()
