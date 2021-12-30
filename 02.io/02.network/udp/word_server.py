"""
使用udp客户端查询单词，得到单词解释，如果没有该单词则得到"没有单词"，
客户端可以循环输入单词，直到输入空退出
"""

from socket import *

# 创建udp套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 绑定地址
sockfd.bind(('127.0.0.1', 8888))
f = open('dict.txt', 'r')


def search_word(word):
    for line in f:
        w = line.split(' ')[0]
        # 如果遍历到的单词已经大于word就结束查找
        if w > word:
            return "没找到该单词"
        if w == word:
            return line
    else:
        return "没找到该单词"


# 循环收发消息
while True:
    try:
        data, addr = sockfd.recvfrom(1024)
        if not data:
            break
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(e)
        continue
    result = search_word(data.decode())
    sockfd.sendto(result.encode(), addr)

f.close()
sockfd.close()
