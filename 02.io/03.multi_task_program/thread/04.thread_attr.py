"""
t.name  线程名称
t.setName() 设置线程名称
t.getName() 获取线程名称
t.is_alive()    查看线程是否在生命周期
t.daemon    设置主线程和分支线程的退出关系
"""

from threading import Thread
from time import sleep


def fun():
    sleep(3)
    print("线程属性测试")


t = Thread(target=fun, name="Dec")

t.setDaemon(True)  # 主线程退出分支线程也退出,要求在start前设置，一般不和join同时使用

t.start()

t.setName("twenty-two")
print("name:", t.getName())

print("is alive:", t.is_alive())

print("daemon:", t.isDaemon())
