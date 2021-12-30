"""
创建两个链表，两个链表中的值均为有序值
将两个链表合并为一个，合并后要求值仍为有序值
"""

from linklist import *

l1 = LinkList()
l2 = LinkList()

l1.init_list([2, 5, 7, 10, 13])
l2.init_list([3, 6, 9, 12])


# l1 = LinkList()
# l2 = LinkList()
# l3 = LinkList()
# l1.init_list([2, 5, 9, 13, 18, 20, 26])
# l2.init_list([3, 8, 10, 16, 25, 33, 42])
#
# p = l1.head
# q = l2.head.next
# while p.next:
#     if p.next.val > q.val:
#         temp = p.next
#         p.next = q
#         p = p.next
#         q = temp
#         l3.append(p.val)
#     else:
#         p = p.next
#         l3.append(p.val)
# while q:
#     p.next = q
#     l3.append(q.val)
#     q = q.next
#
# l3.show()


def merge(l1, l2):
    # 将l2合并到l1中
    p = l1.head
    q = l2.head.next
    while p.next is not None:
        if p.next.val < q.val:
            p = p.next
        else:
            temp = p.next
            p.next = q
            p = p.next
            q = temp
    p.next = q


merge(l1, l2)
l1.show()
