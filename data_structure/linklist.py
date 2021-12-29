"""
linklist.py
功能：实现单链表的构建和功能操作
重点代码
"""


# 创建结点类
class Node:
    """
    思路：将自定义的类视为结点的生成类，实例对象中包含数据部分和指向下一个结点next
    """

    def __init__(self, val, next=None):
        self.val = val  # 存储有用数据
        self.next = next  # 寻找下一个结点关系


class LinkList:
    """
    思路：单链表类，生成对象可以进行增删改查操作
        具体操作通过调用具体方法完成
    """

    def __init__(self):
        """
        初始化链表，标记一个链表的开端，以便于获取后续的结点
        """
        self.head = Node(None)

    # 通过list_为链表添加一组结点
    def init_list(self, list_):
        p = self.head  # p作为移动变量
        for item in list_:
            node = Node(item)
            p.next = node
            p = p.next

    # 遍历链表
    def show(self):
        p = self.head.next  # 第一个有效结点
        while p is not None:  # 判断对象是否相等时用is(not)，判断值是否相等用!(=)
            print(p.val)
            p = p.next  # p向后移动

    # 判断链表空
    def is_empty(self):
        """
        :return: True表示空链表
        """
        if not self.head.next:
            return True

    # 清空链表
    def clear(self):
        self.head.next = None

    # 尾部插入
    def append(self, val):
        p = self.head
        while p.next:
            p = p.next
        p.next = Node(val)

    # 头部插入
    def head_insert(self, val):
        node = Node(val)
        node.next = self.head.next
        self.head.next = node

    # 某个位置插入
    def insert(self, index, val):
        p = self.head
        for i in range(index):
            if p.next is None:
                break  # 超出位置最大范围结束循环
            p = p.next
        node = Node(val)
        node.next = p.next
        p.next = node

    # 删除结点
    # def delete(self, val):
    #     p = self.head
    #     while p.next:
    #         if p.next.val == val:
    #             p.next = p.next.next
    #             break
    #         else:
    #             p = p.next
    #     if p.next is None:
    #         print("没有要删除的结点值")

    # 删除结点
    def delete(self, val):
        p = self.head
        # 结束循环必然两个条件其一为假
        while p.next and p.next.val != val:
            p = p.next

        if p.next is None:
            raise ValueError("%d not in LinkList" % val)
        else:
            p.next = p.next.next

    # 获取某个位置结点值
    def get_index(self, index):
        if index < 0:
            raise IndexError("list index out of range")
        p = self.head.next
        for i in range(index):
            if p.next is None:
                raise IndexError("list index out of range")
            p = p.next

        print(p.val)


if __name__ == '__main__':
    l = LinkList()
