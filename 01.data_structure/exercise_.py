"""
编写一个接口程序，获取一段文字，判断文字中括号是否匹配正确
如果正确则打印正确，不正确则指出出错的地方

思路分析：
    从前往后遍历这段文字，如果不是括号就不用管了；
    如果是左括号{，让其入栈，遇到有括号}，弹出栈顶元素，查看是否与其匹配，如果不匹配直接报错，如果匹配则继续往下遍历
    括号交叉：[入栈，{入栈，遇到右括号}，弹出栈顶元素{进行匹配，遇到右括号]，弹出栈顶元素[进行匹配
    考虑出错情况：{没有}与其匹配，没有[与]匹配
"""

text = "At Abridge, {our mission is to bring context and understanding to (every medical conversation) " \
       "so people can stay on top of their health.} We leverage groundbreaking machine learning (ML) " \
       "research to help [people] focus on (the) most important details from their health conversations. " \
       "{Python powers major aspects of [Abridge’s ML lifecycle, (including data annotation,) research and " \
       "experimentation,]}and ML model deployment to production."

from data_structure.lstack import *

# 将验证条件提前定义好
parens = "()[]{}"  # 需要特殊处理的字符集
left_parens = "([{"  # 入栈字符集

# 验证匹配关系
opposite = {'}': '{', ']': '[', ')': '('}

ls = LStack()  # 存储左括号的栈


def parent(text):
    # i遍历字符串的索引位置
    i, text_len = 0, len(text)

    # 开始遍历字符串
    while True:
        while i < text_len and text[i] not in parens:  # 没有遍历到结尾且字符不是括号
            i += 1
        if i >= text_len:  # 到字符串结尾了
            return
        else:  # 说明text[i]是括号
            yield text[i], i
            i += 1


# 功能函数判断提供的括号是否匹配
def ver():
    for pr, i in parent(text):
        if pr in left_parens:
            ls.push((pr, i))  # 左括号入栈
        elif ls.is_empty() or ls.pop()[0] != opposite[pr]:
            print("Unmatching is found at %d for %s" % (i, pr))
            break
    # for执行完了，没有遇到break，执行else
    else:
        if ls.is_empty():
            print("All parentheses are matched")
        else:
            # 左括号多了
            d = ls.pop()
            print("Unmatching is found at %d for %s" % (d[1], d[0]))


ver()
