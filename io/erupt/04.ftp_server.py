"""
ftp文件服务器
    功能
        分为服务端和客户端，要求可以有多个客户端同时操作
        客户端可以查看服务器文件库中有什么文件
        客户端可以从文件库中下载文件到本地
        客户端可以上传一个本地文件到文件库
        使用print在客户端打印命令输入提示，引导操作
    技术点确定
        并发模型：多线程并发
        数据传输：tcp传输
    结构设计
        将基本文件操作功能封装为类
    功能模块
        搭建网络通信模型
        查看文件列表
        下载文件
        上传文件
        客户端退出
    协议确定
        L   请求文件列表
        Q   退出
        G   下载文件
        P   上传文件
"""
import sys, os, time
from socket import *
from threading import Thread

# 全局变量
HOST = '0.0.0.0'
PORT = 8080
ADDR = (HOST, PORT)
FTP = 'D:/code/AST/FTP/'  # 文件库位置


# 创建类实现服务器文件处理功能
class FTPServer(Thread):
    """
    查看列表，下载，上传，退出处理
    """

    def __init__(self, connfd):
        self.connfd = connfd
        super().__init__()

    def do_list(self):
        # 获取文件列表
        files = os.listdir(FTP)
        if not files:  # 文件库为空
            self.connfd.send("文件库为空".encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)  # 防止两次发送的消息粘在一块

        # 拼接文件
        filelist = ""
        for file in files:
            if file[0] != '.' and os.path.isfile(FTP + file):  # 不是隐藏文件但是普通文件
                filelist += file + '\n'
        self.connfd.send(filelist.encode())

    def do_get(self, filename):
        try:
            f = open(FTP + filename, 'rb')
        except Exception:  # 打开失败表示文件不存在
            self.connfd.send("文件不存在".encode())
            return
        else:  # 没有异常执行else
            self.connfd.send(b'OK')
            time.sleep(0.1)  # 防止发送的OK和发送的文件内容粘在一起
        # 发送文件
        while True:
            data = f.read(1024)  # 用rb方式打开，读到的是字节串
            if not data:  # 读到文件结尾
                time.sleep(0.1)  # 防止##和发送的内容粘包
                self.connfd.send(b'##')
                break
            self.connfd.send(data)

    # 实现文件上传
    def do_put(self, filename):
        if os.path.exists(FTP + filename):  # 文件库中文件已存在
            self.connfd.send("文件已存在".encode())
            return
        else:
            self.connfd.send(b'OK')
        # 接收文件
        f = open(FTP + filename, 'wb')
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break
            f.write(data)
        f.close()

    # 循环接收请求，分情况调用功能函数
    def run(self):
        while True:
            data = self.connfd.recv(1024).decode()
            if not data or data == 'Q':  # 客户端退出
                return  # run函数结束，对应的客户端的线程也结束
            elif data == 'L':
                self.do_list()
            elif data[0] == 'G':
                filename = data.split(' ')[-1]
                self.do_get(filename)
            elif data[0] == 'P':
                filename = data.split(' ')[-1]
                self.do_put(filename)


# 搭建网络服务端模型
def main():
    # 创建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
    s.bind(ADDR)
    s.listen(5)
    print("Listen the port 8080...")

    # 循环等待客户端连接
    while True:
        try:
            c, addr = s.accept()
            print("Connect from:", addr)
        except KeyboardInterrupt:
            sys.exit('退出服务器')
        except Exception as e:
            print(e)
            continue

        # 创建线程处理请求
        client = FTPServer(c)
        client.setDaemon(True)
        client.start()  # 启动线程运行run


if __name__ == '__main__':
    main()
