"""
进程池实现
    必要性
        1.进程的创建和销毁过程消耗的资源较多
        2.当任务众多，每个任务在很短时间内完成时，需要频繁的创建和销毁进程。此时计算机压力较大
        3.进程池技术很好的解决了以上问题
    原理
        创建一定数量的进程来处理事件，事件处理完进程不退出而是继续处理其他事件，
        直到所有事件全都处理完毕统一销毁。增加进程的重复利用，降低资源消耗。
    进程池实现
        1.创建进程池对象，放入适当的进程
            pool = from multiprocessing import Pool
            Pool(int)
                功能：创建进程池对象
                参数：指定进程数量，默认根据系统自动判定
        2.将事件加入进程池队列执行
            pool.apply_async(func, args, kwargs)
                功能：使用进程池执行func事件
                参数：
                    func 事件函数
                    args 元组 给func按位置传参
                    kwargs 字典 给func按照键值传参
                返回值：返回函数事件对象
        3.关闭进程池
            pool.close()
                功能：关闭进程池
        4.回收进程池中进程
            pool.join()
                功能：回收进程池中进程
"""

from multiprocessing import Pool
from time import sleep, ctime


# 进程池事件,写在创建进程池之前
def worker(msg):
    sleep(2)
    print(ctime(), '--', msg)


# 创建进程池
pool = Pool()

# 向进程池队列添加事件
for i in range(10):
    msg = "Hello %d" % i
    pool.apply_async(func=worker, args=(msg,))

# 关闭进程池
pool.close()

# 回收进程池
pool.join()
