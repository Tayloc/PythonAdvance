"""
poll方法
    p = select.poll()
        功能：创建poll对象
        返回值：poll对象

    p.register(fd, event)
        功能：注册关注的IO事件
        参数：
            fd 要关注的IO
            event 要关注的IO事件类型
                常用类型：POLLIN 读IO事件；POLLOUT 写IO事件；POLLERR 异常IO
        e.g. p.register(sockfd, POLLIN | POLLERR)

    p.unregister(fd)
        功能：取消对IO的关注
        参数：IO对象或者IO对象的fileno

    events = p.poll()
        功能：阻塞等待监控的IO事件发生
        返回值：返回发生的IO
              events格式  [(fileno,event),()...]
              每个元组为一个就绪IO，元组第一项是该IO的fileno，第二项是该IO就绪事件类型


poll_server
    1.创建套接字
    2.将套接字register
    3.创建查找字典，并维护
    4.循环监控IO发生
    5.处理发生的IO
"""

from socket import *
from select import *

# 创建监听套接字，作为关注的IO
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
s.bind(('0.0.0.0', 8888))
s.listen(3)

# 创建poll对象
p = poll()

# 建立查找字典，通过一个IO的fileno找到IO对象
# 始终跟register的IO保持一致
fdmap = {
    s.fileno(): s
}

# 关注s
p.register(s, POLLIN | POLLERR)

# 循环监控IO发生
while True:
    events = p.poll()
    # 循环遍历列表，查看哪个IO就绪，进行处理
    for fd, event in events:
        # 区分哪个IO就绪了
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print("Connect from:", addr)
            # 关注客户端连接套接字
            p.register(c, POLLIN | POLLERR)
            fdmap[c.fileno()] = c  # 维护字典
        elif event & POLLIN:  # POLLIN就绪
            data = fdmap[fd].recv(1024).decode()
            if not data:
                p.unregister(fd)  # 取消关注
                fdmap[fd].close()
                del fdmap[fd]
                continue  # 从字典删除
            print(data)
            fdmap[fd].send(b'OK')
