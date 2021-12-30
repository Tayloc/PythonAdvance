"""
ubuntu安装gevent:sudo pip3 install gevent

gevent.spawn(func, argv)
    功能：生成协程对象
    参数
        func 协程函数
        argv 给协程函数传参(不定参)
    返回值：协程对象

gevent.joinall(list, [timeout])
    功能：阻塞等待协程执行完毕
    参数：
        list 协程对象列表
        timeout 超时时间

gevent.sleep(sec)
    功能：gevent睡眠阻塞
    参数:睡眠时间

gevent协程只有在遇到gevent指定的阻塞行为时才会自动在协程之间进行跳转
如gevent.joinall()，gevent.sleep()带来的阻塞
"""

import gevent


# 协程函数
def foo(a, b):
    print("Running foo...", a, b)
    gevent.sleep(2)
    print("Foo again...")


def bar():
    print("Running bar...")
    gevent.sleep(3)
    print("Bar again..")


# 生成协程对象
f = gevent.spawn(foo, 1, 2)
b = gevent.spawn(bar)

gevent.joinall([f, b])  # 阻塞等待f,b两个协程执行完毕
