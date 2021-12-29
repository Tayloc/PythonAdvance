"""
套接字属性
    1、sockfd.type   套接字类型
    2、sockfd.family 套接字地址类型
    3、sockfd.getsockname()  获取套接字绑定地址
    4、sockfd.fileno()   获取套接字的文件描述符
    5、sockfd.getpeername()  获取连接套接字客户端地址
    6、sockfd.setsockopt(level,option,value)
        功能：设置套接字选项
        参数：level 选项类别SOL_SOCKET
             option 具体选项内容
             value 选项值
    7、sockfd.getsockopt(level,option)
        功能：获取套接字选项值
"""

from socket import *

# 创建套接字
s = socket()

# 当socket关闭后，本地端用于该socket的端口号立即就可以被重用。
# 通常来说，只有经过系统定义一段时间后，才能被重用。
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)

s.bind(('127.0.0.1', 8888))
s.listen(3)
c, addr = s.accept()

print("地址类型:", s.family)
print("套接字类型:", s.type)
print("绑定地址:", s.getsockname())
print("文件描述符:", s.fileno())

# 连接套接字调用，结果同accept返回的addr
print("连接端地址:", c.getpeername())
