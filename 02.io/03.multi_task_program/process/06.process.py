"""
multiprocessing模块创建进程
    流程特点
        1、将需要子进程执行的事件封装为函数
        2、通过模块的Process类创建进程对象，关联函数
        3、【可以通过进程对象设置进程信息及属性】
        4、通过进程对象调用start启动进程
        5、通过进程对象调用join回收进程
    基本接口使用
        Process()
            功能：创建进程对象
            参数
                target 绑定要执行的目标函数
                args 元组，用于给target函数位置传参
                kwargs 字典，给target函数键值传参
        p.start()
            功能：启动进程
        注意：启动进程此时target绑定函数开始执行，该函数作为子进程执行内容，此时进程真正被创建
        p.join([timeout])
            功能：阻塞等待回收进程
            参数：超时时间
        注意：
            使用multiprocessing创建进程同样是子进程复制父进程空间代码段，父子进程运行互不影响
            子进程只运行target绑定的函数部分，其余内容均是父进程执行内容
            multiprocessing中父进程往往只用来创建子进程回收子进程，具体事件由子进程完成
            multiprocessing创建的子进程中无法使用标准输入
"""

import multiprocessing as mp
from time import sleep


# 进程函数
def fun():
    print("开始一个进程")
    sleep(5)
    print("子进程结束")


# 创建进程对象
p = mp.Process(target=fun)

# 启动进程
p.start()

# 回收进程
p.join()
