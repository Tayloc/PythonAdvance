"""
epoll方法
    使用方法：基本与poll相同
        生成对象改成epoll()
        将所有事件类型改为epoll类型
    epoll特点
        epoll效率比select poll要高
        epoll监控IO数量比select要多
        epoll的触发方式比poll要多(EPOLLET边缘触发)
"""

from socket import *
from select import *

# 创建监听套接字，作为关注的IO
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
s.bind(('0.0.0.0', 8888))
s.listen(3)

# 创建epoll对象
ep = epoll()

# 建立查找字典，通过一个IO的fileno找到IO对象
# 始终跟register的IO保持一致
fdmap = {
    s.fileno(): s
}

# 关注s
ep.register(s, EPOLLIN | EPOLLERR)

# 循环监控IO发生
while True:
    events = ep.poll()
    # 循环遍历列表，查看哪个IO就绪，进行处理
    for fd, event in events:
        # 区分哪个IO就绪了
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print("Connect from:", addr)
            # 关注客户端连接套接字
            ep.register(c, EPOLLIN | EPOLLERR)
            fdmap[c.fileno()] = c  # 维护字典
        elif event & EPOLLIN:  # POLLIN就绪
            data = fdmap[fd].recv(1024).decode()
            if not data:
                ep.unregister(fd)  # 取消关注
                fdmap[fd].close()
                del fdmap[fd]
                continue  # 从字典删除
            print(data)
            fdmap[fd].send(b'OK')
