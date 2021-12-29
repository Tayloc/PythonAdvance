"""
ftp 文件服务，客户端
"""
import sys, time
from socket import *

# 服务器地址
ADDR = ('127.0.0.1', 8080)


# 客户端文件处理类
class FTPClient:
    """
    客户端处理，查看，上传，下载，退出
    """

    def __init__(self, sockfd):
        self.sockfd = sockfd

    # 获取文件库中文件列表
    def do_list(self):
        self.sockfd.send(b'L')  # 发送请求
        # 等待回复
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            # 一次性接收文件字符串
            data = self.sockfd.recv(4096)
            print(data.decode())
        else:
            print(data)

    # 退出
    def do_quit(self):
        self.sockfd.send(b'Q')  # 请求退出
        self.sockfd.close()
        sys.exit("谢谢使用")

    # 下载文件到当前目录
    def do_get(self, filename):
        # 发送请求
        self.sockfd.send(("G " + filename).encode())
        # 等待回复
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            f = open(filename, 'wb')
            # 循环接收写入文件
            while True:
                data = self.sockfd.recv(1024)  # 接收到的就是字节串
                if data == b'##':  # "##"表示服务端发送完成
                    break
                f.write(data)
            f.close()
        else:
            print(data)

    # 文件上传
    def do_put(self, filename):
        try:
            f = open(filename, 'rb')
        except Exception:
            print("该文件不存在")
            return
        # 获取文件名
        filename = filename.split('/')[-1]  # 按照/分隔取最后一个
        # 发送请求
        self.sockfd.send(('P ' + filename).encode())
        # 接收反馈
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            while True:
                data = f.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.sockfd.send(b'##')
                    break
                self.sockfd.send(data)
            f.close()
        else:
            print(data, )


# 连接服务器
def main():
    sockfd = socket()
    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print(e)
        return

    # 实例化对象，调用文件处理方法
    ftp = FTPClient(sockfd)

    # 循环发送请求
    while True:
        print("\n===========命令选项===========")
        print("*****       list       *****")
        print("*****     get file     *****")
        print("*****     put file     *****")
        print("*****       quit       *****")
        print("===========命令选项===========")

        cmd = input("输入命令：")
        if cmd.strip() == 'list':
            ftp.do_list()
        elif cmd.strip() == 'quit':
            ftp.do_quit()
        elif cmd[:3] == 'get':  # 前三个字母等于get
            filename = cmd.strip().split(' ')[-1]  # 获取要下载的文件名称：先去掉输入内容的两端空格然后按照空格切割取最后一项
            ftp.do_get(filename)
        elif cmd[:3] == 'put':  # 前三个字母等于get
            filename = cmd.strip().split(' ')[-1]  # 获取要上传的文件名称：先去掉输入内容的两端空格然后按照空格切割取最后一项
            ftp.do_put(filename)
        else:
            print("请输入其他命令")


if __name__ == '__main__':
    main()
