"""
socket -> bind -> listen -> accept -> send/recv -> close


1.创建套接字
    sockfd = socket.socket(socket_family=AF_INET,sock_type=SOCK_STREAM,proto=0)
        功能：
            创建套接字
        参数：
            socket_family    网络地址类型  AF_INET表示ipv4
            sock_type   套接字类型   SOCK_STREAM(流式) SOCK_DGRAM(数据报)
            proto   通常为0    选择子协议
        返回值：
            套接字对象

2.绑定地址
    本地地址    'localhost' '127.0.0.1'     客户端也要用'127.0.0.1'并且客户端和服务端在同一台主机上
    网络地址    '172.40.91.181'     客户端必须绑定服务端绑定的ip，本地主机和其他主机都可以访问
    自动获取地址  '0.0.0.0'       客户端可以绑定服务端绑定的ip地址或绑定'127.0.0.1'，本地主机和其他主机都可以访问

    sockfd.bind(addr)
        功能：绑定本机网络地址
        参数：二元元组 (ip,port) ('0.0.0.0',8888)

3.设置监听
通过调用listen，赋予这个套接字对象更加丰富的功能：把这个套接字变成监听套接字后，客户端就可以与其连接了
监听队列：一个监听实际上可以连接多个客户端，但是连接的过程要一个一个来，把要连接的客户端放在监听队列中
    sockfd.listen(n)
        功能：将套接字设置为监听套接字，确定监听队列大小
        参数：监听队列大小

4.等待处理客户端连接请求
每当连接上一个客户端后，服务端会创建一个专属的套接字，这个套接字是新的套接字，专门负责和客户端数据通信
    connfd, addr = sockfd.accept()
        功能：阻塞等待处理客户端请求
        返回值：
            connfd  客户端连接套接字
            addr    连接的客户端地址

5.消息收发
    data = connfd.recv(buffersize)
        功能：接收客户端消息
        参数：每次最多接收消息的大小
        返回值：接收到的内容

    n = connfd.send(data)
        功能：发送消息
        参数：要发送的内容   bytes格式
        返回值：发送的字节数

6.关闭套接字
    sockfd.close()
        功能：关闭套接字
"""

import socket

# 创建tcp套接字
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定地址
sockfd.bind(('127.0.0.1', 8888))

# 设置监听
sockfd.listen(5)
while True:
    # 阻塞等待处理连接
    print("Waiting for connect...")
    try:
        connfd, addr = sockfd.accept()
        print("Connect from", addr)  # 打印连接的客户端地址
    except KeyboardInterrupt:
        print("服务器退出")
        break
    except Exception as e:
        print(e)
        continue

    while True:
        # 收发消息
        data = connfd.recv(1024)
        if not data:
            break
        print("收到：", data.decode())
        n = connfd.send(b'Thanks')  # 发送字节串
        print("发送%d字节" % n)

    # 关闭套接字
    connfd.close()

sockfd.close()
