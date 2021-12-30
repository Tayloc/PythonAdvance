"""
greenlet.greenlet(func)
    功能：创建协程对象
    参数：协程函数
g.switch()
    功能：选择要执行的协程函数
"""

from greenlet import greenlet


def fun1():
    print("执行fun1")
    gr2.switch()
    print("结束fun1")
    gr2.switch()


def fun2():
    print("执行fun2")
    gr1.switch()
    print("结束fun2")


# 将函数变为协程
gr1 = greenlet(fun1)
gr2 = greenlet(fun2)
gr1.switch()  # 选择执行哪个协程
