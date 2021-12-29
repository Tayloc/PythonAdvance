"""
从终端输入一个单词
从单词本中找到该单词
打印该单词及其解释内容
如果找不到，则打印找不到
"""

# word = input("请输入单词：>>")
#
# f = open('dict.txt', 'r')
#
# data = f.readlines()
#
# for item in data:
#     if word == item.split(' ')[0]:
#         print(item)
#         break
#     elif item.split(' ')[0] > word:
#         print("没有找到")
#         break
# else:
#     print("没找到该单词")
#
# f.close()


word = input("Word:")

# 默认r打开
f = open('dict.txt')

# 每次获取一行
for line in f:
    w = line.split(' ')[0]
    # 如果遍历到的单词已经大于word就结束查找
    if w > word:
        print("没有找到该单词")
        break
    if w == word:
        print(line)
        break
else:
    print("没找到该单词")

f.close()