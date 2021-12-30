"""
将一个文件从客户端发送到服务端保存
文件可能是文本类型也可能是二进制文件
"""

from socket import *

# 创建tcp套接字
sockfd = socket()

# 连接服务器
sockfd.connect(('127.0.0.1', 8888))

# 打开文件
f = open('note', 'rb')
# 循环读取目标文件并发送
while True:
    data = f.read(1024)
    if not data:
        break
    sockfd.send(data)

f.close()
sockfd.close()
