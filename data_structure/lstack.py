"""
lstack.py   链式栈
重点代码

思路分析：
    1.源于链表结构
    2.封装栈的操作方法（入栈，出栈，栈空，栈顶元素）
    3.链表开头作为栈顶（不用每次遍历）
"""


# 自定义栈异常
class StackError(Exception):
    pass


# 结点类
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# 链式栈操作
class LStack:
    def __init__(self):
        # 标记栈的栈顶位置
        self._top = None

    # 判断栈空
    def is_empty(self):
        return self._top is None

    # 入栈
    def push(self, val):
        # node = Node(val)
        # node.next = self._top
        # self._top = node
        self._top = Node(val, self._top)

    # 出栈
    def pop(self):
        if self.is_empty():
            raise StackError("LStack is empty")
        value = self._top.val
        self._top = self._top.next
        return value

    # 查看栈顶元素
    def top(self):
        if self.is_empty():
            raise StackError("LStack is empty")
        return self._top.val


if __name__ == '__main__':
    ls = LStack()
    ls.push(10)
    ls.push(20)
    ls.push(30)
    while not ls.is_empty():
        print(ls.pop())

