"""
快速排序
    1.从数列中挑出一个元素，称为“基准(pivot)”；
    2.重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面(相同的数可以到任一边)。
    在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区(partition)操作；
    3.递归地(recursive)把小于基准值元素的子数列和大于基准值元素的子数列排序；
"""


# 完成一轮交换
def sub_sort(list_, low, high):
    # 选定基准
    pivot = list_[low]
    # low向后 high向前
    while low < high:
        # 后面的数往前放
        while list_[high] >= pivot and high > low:
            high -= 1
        list_[low] = list_[high]
        # 前面的数往后放
        while list_[low] < pivot and low < high:
            low += 1
        list_[high] = list_[low]
    list_[low] = pivot
    return low


def quick(list_, low, high):
    """
    快速排序
    :param list_:待排序的数列
    :param low:列表第一个元素索引
    :param high:列表最后一个元素索引
    :return:
    """
    if low < high:
        key = sub_sort(list_, low, high)
        quick(list_, low, key - 1)
        quick(list_, key + 1, high)


l = [56, 1, 78, 25, 5, 8, 3, 19]
quick(l, 0, len(l) - 1)
print(l)
