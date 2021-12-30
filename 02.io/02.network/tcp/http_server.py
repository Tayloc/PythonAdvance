"""
httpserver v1.0
基本要求：
    1.获取来自浏览器的请求
    2.判断如果请求内容是 / ,将index.html返回给客户端
    3.如果请求的是其他内容则返回404
"""
import socket
from socket import *


# 客户端处理
def request(connfd):
    # 获取请求将请求内容提取出来
    data = connfd.recv(4096)  # 接收请求
    # 防止浏览器异常退出
    if not data:
        return
    request_header = data.decode().split('\r\n')[0]  # 请求头
    info = request_header.split(' ')[1]  # 请求内容
    # 判断是 / 则返回index.html，不是则返回404
    if info == '/':
        with open('index.html', 'r') as f:
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += '\r\n'
            response += f.read()
    else:
        response = "HTTP/1.1 404 Not Found\r\n"
        response += "Content-Type:text/html\r\n"
        response += '\r\n'
        response += 'Sorry'
    connfd.send(response.encode())


# 搭建tcp网络
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
sockfd.bind(('0.0.0.0', 8888))
sockfd.listen(3)

while True:
    connfd, addr = sockfd.accept()
    request(connfd)  # 处理客户端请求
