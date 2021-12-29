"""
线程间通信方法
    线程间使用全局变量进行通信
共享资源争夺
    共享资源：多个进程或者线程都可以操作的资源称为共享资源。对共享资源的操作代码段称为临界区
    影响：对共享资源的无序操作可能会带来数据的混乱或者操作错误，此时往往需要同步互斥机制协调操作顺序
同步互斥机制
    同步：同步是一种协作关系，为完成操作，多进程或者线程间形成一种协调，按照必要的步骤有序执行操作
    互斥：互斥是一种制约关系，当一个进程或者线程占有资源时会进行加锁处理，此时其他进程线程就无法操
        作该资源，直到解锁后才能操作
线程同步互斥方法
    from threading import Event
    e = Event()
        创建线程event对象
    e.wait([timeout])
        阻塞等待e被set
    e.set()
        设置e，使wait结束阻塞
    e.clear()
        使e回到未被设置状态
    e.is_set()
        查看当前e是否被设置
"""

from threading import Thread, Event

s = None  # 用于通信
e = Event()  # 事件对象


def yang_zi_rong():
    print("杨子荣前来拜山头")
    global s
    s = "天王盖地虎"
    e.set()  # 操作完共享资源 e 设置


t = Thread(target=yang_zi_rong)
t.start()

print("说对口令就是自己人")
e.wait()  # 阻塞等待
if s == '天王盖地虎':
    print("宝塔镇河妖")
    print("你是对的人")
else:
    print("打死他...")

t.join()
