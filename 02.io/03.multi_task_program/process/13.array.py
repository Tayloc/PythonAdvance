"""
共享内存
    通信原理
        在内存中开辟一块空间，进程可以写入内容和读取内容完成通信，但是每次写入内容会覆盖之前内容
    实现方法
        from multiprocessing import Array

        obj = Array(ctype, data)
            功能：开辟共享内存
            参数：ctype 表示共享内存数据类型;data 共享内存空间初始数据
            返回值：共享内存对象
        obj.value 对该属性的修改查看即对共享内存读写
    注意：共享内存只能有一个值
"""

from multiprocessing import Array, Process

# 创建共享内存
# shm = Array('i', 5) 与 shm = Array('i', [0, 0, 0, 0, 0])一致 ：初始开辟5个整形空间
# shm = Array('i', [1, 2, 3, 4])
shm = Array('c', b'hello')  # 初始值是hello的字节串


def fun():
    # array 创建共享内存对象可迭代
    for i in shm:
        print(i)
    # shm[1] = 1000
    shm[0] = b'H'


p = Process(target=fun)
p.start()
p.join()
for i in shm:
    print(i)

print(shm.value)  # 打印字节串
