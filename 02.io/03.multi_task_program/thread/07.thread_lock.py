"""
线程锁Lock
    from threading import Lock
    lock = Lock()
        创建锁对象
    lock.acquire()
        上锁  如果lock已经上锁再调用会阻塞
    lock.release()
        解锁
    with lock:  # 上锁,with代码块结束自动解锁
        ...
"""

from threading import Lock, Thread

a = b = 0
lock = Lock()  # 创建锁对象


def value():
    while True:
        lock.acquire()  # 上锁
        if a != b:
            print("a = %d, b = %d" % (a, b))
        lock.release()  # 解锁


t = Thread(target=value)

t.start()

while True:
    with lock:  # 上锁
        a += 1
        b += 1
        if a != b:
            break
            # with语句结束自动解锁

t.join()
