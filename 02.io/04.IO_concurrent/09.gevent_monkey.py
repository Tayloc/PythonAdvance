"""
monkey脚本
    在gevent协程中，协程只有遇到gevent指定类型的阻塞才能跳转到其他协程，因此，
    我们希望将普通的IO阻塞行为转换为可以触发gevent协程跳转的阻塞，以提高执行效率

    转换方法：gevent提供了一个脚本程序monkey，可以修改底层解释IO阻塞行为，将
    很多普通阻塞转换为gevent阻塞

    使用方法
        1.导入monkey
            from gevent import monkey
        2.运行相应的脚本，例如转换socket中所有阻塞
            monkey.patch_socket()
        3.如果将所有可转换的IO阻塞全部转换则运行all
            monkey.patck_all()
        4.注意：脚本运行函数需要在对应模块导入前执行
"""

import gevent
from gevent import monkey

monkey.patch_time()  # 在time导入之前执行
from time import sleep


# 协程函数
def foo(a, b):
    print("Running foo...", a, b)
    # gevent.sleep(2)
    sleep(2)
    print("Foo again...")


def bar():
    print("Running bar...")
    # gevent.sleep(3)
    sleep(3)
    print("Bar again..")


# 生成协程对象
f = gevent.spawn(foo, 1, 2)
b = gevent.spawn(bar)

gevent.joinall([f, b])  # 阻塞等待f,b两个协程执行完毕
