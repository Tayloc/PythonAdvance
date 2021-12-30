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
