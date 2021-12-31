"""
WebFrame部分  模拟后端应用工作流程
    从httpserver接收具体请求
    根据请求进行逻辑处理和数据处理
    将需要的数据反馈给httpserver
"""
import json
from socket import *
from settings import *
from select import select
from urls import *


# 应用类，处理某一方面的请求
class Application:
    def __init__(self):
        self.rlist = []
        self.wlist = []
        self.xlist = []
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, DEBUG)
        self.sockfd.bind((frame_ip, frame_port))

    # 启动服务
    def start(self):
        self.sockfd.listen(5)
        print("Start app listen %s" % frame_port)
        self.rlist.append(self.sockfd)
        # select 监控请求
        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            for r in rs:
                if r is self.sockfd:  # 有客户端发起连接
                    connfd, addr = r.accept()
                    self.rlist.append(connfd)
                else:  # 有httpserver发消息
                    self.handle(r)
                    self.rlist.remove(r)

    # 处理具体的httpserver请求
    def handle(self, connfd):
        request = connfd.recv(1024).decode()
        request = json.loads(request)
        # request --> {'method':'GET','info':'/'}
        if request['method'] == 'GET':
            if request['info'] == '/' or request['info'][-5:] == '.html':
                response = self.get_html(request['info'])
            else:
                response = self.get_data(request['info'])
        elif request['method'] == 'POST':
            pass
        # 将数据发送给httpserver
        # response->{'status':'200','data':'xxx'}
        response = json.dumps(response)
        connfd.send(response.encode())
        connfd.close()

    # 处理网页
    def get_html(self, info):
        if info == '/':
            filename = STATIC_DIT + "/index.html"
        else:
            filename = STATIC_DIT + info
        try:
            fd = open(filename)
        except Exception as e:
            fd = open(STATIC_DIT + '/404.html')
            return {'static': '404', 'data': fd.read()}
        else:
            return {'static': '200', 'data': fd.read()}

    # 处理数据
    def get_data(self, info):
        for url, func in urls:
            if url == info:
                return {'status': '200', 'data': func()}
        return {'status': '404', 'data': 'Sorry...'}


app = Application()
app.start()  # 启动服务
