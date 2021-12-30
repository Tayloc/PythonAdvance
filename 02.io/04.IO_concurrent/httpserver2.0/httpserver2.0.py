"""
主要功能
    1.接收客户端(浏览器)请求
    2.解析客户端发送的请求
    3.根据请求组织数据内容
    4.将数据内容形成http响应格式返回给浏览器
升级点
    1.采用IO并发，可以满足多个客户端同时发起请求情况
    2.做基本的请求解析，根据具体请求返回具体内容，同时
    满足客户端简单的非网页请求情况
    3.通过类接口形式进行功能封装
技术分析
    1.使用tcp通信，基于http协议格式
    2.select io多路复用
"""

from socket import *
from select import *


# 具体功能实现
class HTTPServer:
    def __init__(self, host='0.0.0.0', port=8000, dir=None):
        self.host = host
        self.port = port
        self.dir = dir
        self.address = (host, port)
        # 多路复用列表
        self.rlist = []
        self.wlist = []
        self.xlist = []
        # 实例化对象时直接创建套接字
        self.create_socket()
        self.bind()

    # 创建套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)

    # 绑定地址
    def bind(self):
        self.sockfd.bind(self.address)

    # 启动服务
    def server_forever(self):
        self.sockfd.listen(3)
        print("Listen the port %d" % self.port)
        # IO多路复用接收客户端请求
        self.rlist.append(self.sockfd)
        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            for r in rs:
                if r is self.sockfd:  # 有客户端连接
                    c, addr = r.accept()
                    self.rlist.append(c)
                else:  # 有客户端发消息
                    # 处理请求
                    self.handle(r)

    def handle(self, connfd):
        # 接收http请求
        request = connfd.recv(4096)
        # 客户端断开
        if not request:
            self.rlist.remove(connfd)
            connfd.close()
            return
        # 提取请求内容
        request_line = request.splitlines()[0]  # 将字节串按行切割取第一个
        info = request_line.decode().split(' ')[1]  # 把请求行转化成字符串，按空格分割取第二项
        print(connfd.getpeername(), ':', info)

        # 根据请求内容进行数据整理
        # 分为两类：1.请求网页 2.其他
        if info == '/' or info[-5] == '.html':  # 如果请求内容是/或者请求网页
            self.get_html(connfd, info)
        else:  # 请求其他
            self.get_data(connfd, info)

    # 返回网页
    def get_html(self, connfd, info):
        if info == '/':
            # 请求主页
            filename = self.dir + "/index.html"
        else:
            filename = self.dir + info
        try:
            fd = open(filename)
        except Exception:
            # 网页不存在
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += "<h1>Sorry...</h1>"
        else:
            # 网页存在
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += fd.read()
        finally:  # 不管有无异常都发送过去
            # 将响应发送给浏览器
            connfd.send(response.encode())

    # 其他数据
    def get_data(self, connfd, info):
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        response += "<h1>Waitting for httpserver 3.0</h1>"
        connfd.send(response.encode())


# 用户使用HTTPServer
if __name__ == '__main__':
    """
    通过HTTPServer类快速搭建服务，展示自己的网页
    """
    # 用户决定的参数
    HOST = '0.0.0.0'
    PORT = 8000
    DIR = './static'  # 网页存储位置

    httpd = HTTPServer(HOST, PORT, DIR)  # 实例化对象
    httpd.server_forever()  # 启动服务
