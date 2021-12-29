"""
使用udp客户端查询单词，得到单词解释，如果没有该单词则得到"没有单词"，
客户端可以循环输入单词，直到输入空退出
"""

from socket import *

# 服务端地址
ADDR = ('127.0.0.1', 8888)

# 创建udp套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 循环发送接收消息
while True:
    word = input("请输入要查询的单词：")
    if not word:
        break
    sockfd.sendto(word.encode(), ADDR)
    data, addr = sockfd.recvfrom(1024)
    print(data.decode())

sockfd.close()
