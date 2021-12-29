"""
socket -> bind<可选,一般不写> -> connect -> send/recv -> close

1.创建套接字
    注意：只有相同类型的套接字才能进行通信
2.请求连接
    sockfd.connect(server_addr)
        功能：连接服务器
        参数：元组   服务器地址
3.收发消息
    注意：防止两端都阻塞，recv send要配合
4.关闭套接字
"""

from socket import *

# 创建tcp套接字
sockfd = socket()  # 使用默认参数创建的就是tcp套接字

# 服务端地址
server_addr = ('127.0.0.1', 8888)

# 连接服务器
sockfd.connect(server_addr)

while True:
    # 发送消息
    data = input("Msg>>")
    if not data:
        break
    sockfd.send(data.encode())

    # 接收消息
    data = sockfd.recv(1024)
    print("Server:", data)  # 打印接收消息

# 关闭套接字
sockfd.close()
