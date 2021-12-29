"""
squeue.py   队列的顺序存储

思路分析：
    1. 基于列表完成数据存储
    2. 通过封装规定数据操作
"""


# 自定义队列异常
class QueueError(Exception):
    pass


# 队列操作
class Queue:
    # 初始化
    def __init__(self):
        # 空列表就是队列的存储空间
        self._elems = []

    # 判断队列空
    def is_empty(self):
        return self._elems == []

    # 入队    列表尾部定义为队尾
    def enqueue(self, val):
        self._elems.append(val)

    # 出队
    def dequeue(self):
        if self.is_empty():
            raise QueueError("Queue is empty")
        return self._elems.pop(0)


if __name__ == '__main__':
    sq = Queue()
    sq.enqueue(10)
    sq.enqueue(20)
    sq.enqueue(30)
    # from sstack import *
    # st = SStack()
    # while not sq.is_empty():
    #     st.push(sq.dequeue())
    # while not st.is_empty():
    #     sq.enqueue(st.pop())
    while not sq.is_empty():
        print(sq.dequeue())
