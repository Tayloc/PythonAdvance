"""
协程技术
    1、定义：纤程，微线程。是允许在不同入口点不同位置暂停或开始的计算机程序
    简单来说，协程就是可以暂停执行的函数
    2、协程原理：记录一个函数的上下文，协程调度切换时会将记录的上下文保存，
    在切换回来时进行调取，恢复原有的执行内容，以便从上一次执行位置继续执行

标准库协程的实现
    python3.5以后，使用标准库asyncio和async/await语法来编写并发代码。
    asyncio库通过对异步IO行为的支持完成python的协程。虽然官方说asyncio
    是未来的开发方向，但是由于其生态不够丰富，大量的客户端不支持awaitable
    需要自己去封装，所以在使用上存在缺陷。
"""

import asyncio


# 定义协程函数
async def fun1():
    print("start1")
    # 设置跳转阻塞点
    await asyncio.sleep(2)
    print("end1")


async def fun2():
    print("start2")
    await asyncio.sleep(3)
    print("end2")


# 生成协程对象
cor1 = fun1()
cor2 = fun2()

tasks = [asyncio.ensure_future(cor1), asyncio.ensure_future(cor2)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
