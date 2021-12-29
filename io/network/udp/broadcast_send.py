"""
广播发送

1.创建UDP套接字
2.设置可以发送广播
3.循环向广播地址发送
"""

from socket import *
from time import sleep

# 广播地址
dest = ('172.40.91.255', 9999)

s = socket(AF_INET, SOCK_DGRAM)

s.setsockopt(SOL_SOCKET, SO_BROADCAST, True)

data = """
    HelloWorld
    HelloPython
    HelloJava
"""

while True:
    sleep(2)
    s.sendto(data.encode(), dest)  # 目标地址=广播地址

