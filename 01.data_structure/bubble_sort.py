def bubble_sort(target):
    # n个数比较n-1轮
    for i in range(len(target) - 1):
        for j in range(len(target) - 1 - i):
            if target[j] > target[j + 1]:
                target[j], target[j + 1] = target[j + 1], target[j]


list_ = [56, 1, 78, 25, 5, 8, 3, 19]

bubble_sort(list_)
print(list_)

