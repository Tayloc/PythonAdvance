"""
chat room
env: python3
socket udp & fork
"""

from socket import *
import os, sys

"""
全局变量：很多封装模块都要使用或者有一定的固定含义
"""

# 服务器地址
ADDR = ('0.0.0.0', 8888)

# 存储用户 {name:address}
user = {}


# 登录
def do_login(s, name, addr):
    if name in user or '管理员' in name:
        s.sendto('该用户已存在'.encode(), addr)
        return
    s.sendto(b'OK', addr)  # 可以进入聊天室

    # 通知其他人
    msg = "\n欢迎 '%s' 进入聊天室" % name
    for i in user:
        s.sendto(msg.encode(), user[i])
    user[name] = addr  # 将用户插入字典


# 聊天
def do_chat(s, name, text):
    msg = "\n%s: %s" % (name, text)
    for i in user:
        if i != name:
            s.sendto(msg.encode(), user[i])


# 退出
def do_quit(s, name):
    msg = "\n%s 退出聊天室" % name
    for i in user:
        if i != name:  # 其他人
            s.sendto(msg.encode(), user[i])
        else:  # 本人
            s.sendto(b'EXIT', user[i])
    del user[name]  # 删除用户


# 处理请求
def do_request(s):
    while True:
        data, addr = s.recvfrom(1024)
        tmp = data.decode().split(' ')  # 拆分请求
        # 根据不同的请求类型执行不同的事情
        if tmp[0] == 'L':
            do_login(s, tmp[1], addr)
        elif tmp[0] == 'C':
            text = ' '.join(tmp[2:])
            do_chat(s, tmp[1], text)
        elif tmp[0] == 'Q':
            do_quit(s, tmp[1])


# 搭建网路
def main():
    # udp服务端
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(ADDR)

    pid = os.fork()
    if pid == 0:
        while True:
            msg = input("管理员消息：")
            msg = "C 管理员 " + msg
            s.sendto(msg.encode(), ADDR)
    # 请求处理函数
    do_request(s)


main()
