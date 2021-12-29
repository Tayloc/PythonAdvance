"""
将一个文件从客户端发送到服务端保存
文件可能是文本类型也可能是二进制文件
"""

from socket import *

# 创建tcp套接字
sockfd = socket()

# 绑定地址
sockfd.bind(('0.0.0.0', 8888))

# 设置监听
sockfd.listen(5)

# 阻塞等待客户端连接
connfd, addr = sockfd.accept()

f = open('new_note.txt', 'wb')

# 循环接收消息并写入新文件中
while True:
    data = connfd.recv(1024)
    if not data:
        break
    f.write(data)

f.close()
connfd.close()
sockfd.close()
