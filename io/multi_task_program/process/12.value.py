"""
共享内存
    通信原理
        在内存中开辟一块空间，进程可以写入内容和读取内容完成通信，但是每次写入内容会覆盖之前内容
    实现方法
        from multiprocessing import Value

        obj = Value(ctype, data)
            功能：开辟共享内存
            参数：ctype 表示共享内存空间类型 'i' 'f' 'c';data 共享内存空间初始数据
            返回值：共享内存对象
        obj.value 对该属性的修改查看即对共享内存读写
    注意：共享内存只能有一个值
"""

from multiprocessing import Process, Value
import time
import random

# 创建共享内存
money = Value('i', 5000)


# 操作共享内存
def man():
    for i in range(30):
        time.sleep(0.2)
        money.value += random.randint(1, 1000)


def girl():
    for i in range(30):
        time.sleep(0.15)
        money.value -= random.randint(100, 800)


p1 = Process(target=man)
p2 = Process(target=girl)
p1.start()
p2.start()
p1.join()
p2.join()

# 获取共享内存
print("一个月余额：", money.value)
