"""
二分查找方法训练
"""


def search(list_, key):
    """
    二分查找
    :param list_: 有序数列
    :param key: 要查找的关键值
    :return: 关键值的索引位置,None表示没找到
    """
    # low第一个数index，high最后一个数index
    low, high = 0, len(list_) - 1
    while low <= high:
        mid = (low + high) // 2
        if key == list_[mid]:
            return mid
        elif key > list_[mid]:
            low = mid + 1
        elif key < list_[mid]:
            high = mid - 1


l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Key index:", search(l, 5))
