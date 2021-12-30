"""
IO多路复用
    1.定义：同时监控多个IO事件，当哪个IO事件准备就绪就执行哪个IO事件。以此形成可以
    同时处理多个IO的行为，避免一个IO阻塞造成其他IO均无法执行，提高了IO执行效率。
    2.具体方案
        select方法：windows linux unxi
        poll方法：linux unix
        epoll方法：linux


select方法
    rs, ws, xs = select(rlist, wlist, xlist[,timeout])
        功能：监控IO事件，阻塞等待IO发生
        参数：
            rlist 列表    存放关注的等待发生的IO事件
            wlist 列表    存放关注的要主动处理的IO事件
            xlist 列表    存放关注的出现异常要处理的IO
            timeout 超时时间
        返回值
            rs  列表  rlist中准备就绪的IO
            ws  列表  wlist中准备就绪的IO
            xs  列表  xlist中准备就绪的IO
"""

from select import select
from socket import *

s = socket()
s.bind(('0.0.0.0', 8889))
s.listen(3)

print("监控IO")
rs, ws, xs = select([s], [], [], 3)
print("rlist:", rs)
print("wlist:", ws)
print("xlist:", xs)
