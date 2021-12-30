"""
bitree.py   二叉树的简单实践
思路分析：
    1.使用链式存储，一个Node表示一个树的结点
    2.结点考虑使用两个属性变量分别表示左连接和右连接
"""

from data_structure.squeue import *


# 二叉树结点
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 二叉树遍历类
class BiTree:
    def __init__(self, root=None):
        self.root = root

    # 先序遍历
    def pre_order(self, node):
        if node is None:
            return
        print(node.val)
        self.pre_order(node.left)
        self.pre_order(node.right)

    # 中序遍历
    def mid_order(self, node):
        if node is None:
            return
        self.mid_order(node.left)
        print(node.val)
        self.mid_order(node.right)

    # 后续遍历
    def last_order(self, node):
        if node is None:
            return
        self.last_order(node.left)
        self.last_order(node.right)
        print(node.val)

    # 层次遍历
    def level_order(self, node):
        """
        让初始结点先入队，谁出队就遍历谁，并且让它的左右孩子分别入队，直到队列为空
        :param node:初始结点
        :return:
        """
        sq = Queue()
        sq.enqueue(node)  # 初始结点入队
        while not sq.is_empty():
            node = sq.dequeue()
            print(node.val, end=' ')  # 打印出队元素
            if node.left:
                sq.enqueue(node.left)
            if node.right:
                sq.enqueue(node.right)


if __name__ == '__main__':
    # 后续遍历顺序：B F G D I H E C A
    # 根据后续遍历构建二叉树
    b = Node('B')
    f = Node('F')
    g = Node('G')
    d = Node('D', f, g)
    i = Node('I')
    h = Node('H')
    e = Node('E', i, h)
    c = Node('C', d, e)
    a = Node('A', b, c)  # 树根

    # 将a作为遍历的起始位置
    bt = BiTree(a)
    bt.level_order(a)
