"""
选择排序
    首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
    再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾
    重复第2步，直到所有元素均排序完毕
"""


def selection_sort(list_):
    for i in range(len(list_) - 1):
        min_index = i
        for j in range(i + 1, len(list_)):
            if list_[j] < list_[min_index]:
                min_index = j
        if min_index != i:
            list_[i], list_[min_index] = list_[min_index], list_[i]


list_target = [56, 1, 78, 25, 5, 8, 3, 19]

selection_sort(list_target)

print(list_target)
