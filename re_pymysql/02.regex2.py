"""
re模块 功能函数演示
生成match对象的函数

re_pymysql.finditer(pattern, string, flags=0)
    功能：根据正则表达式匹配目标字符串内容
    参数：
        pattern 正则表达式
        string 目标字符串
        flags 功能标志位，扩展正则表达式的匹配
    返回值：匹配结果的迭代器

re_pymysql.fullmatch(pattern, string, flags=0)
    功能：完全匹配某个目标字符串
    参数：
        pattern 正则表达式
        string 目标字符串
    返回值：匹配内容match object

re_pymysql.match(pattern, string, flags=0)
    功能：匹配某个目标字符串开始位置
    参数
        pattern 正则表达式
        string 目标字符串
    返回值：匹配内容match object

re_pymysql.search(pattern, string, flags=0)
    功能：匹配目标字符串第一个符合内容
    参数：pattern 正则表达式；string 目标字符串
    返回值：匹配内容match object
"""

import re

s = "今年是2019年,建国70周年"
pattern = r'\d+'

# 返回迭代对象
it = re.finditer(pattern, s)

for i in it:
    print(i.group())  # 获取match对象对应内容

# 完全匹配一个字符串
m = re.fullmatch(r'\S+', s)
print(m.group())

# 匹配开始位置
m = re.match(r'\w+', s)
print(m.group())

# 匹配第一处符合正则表达式的内容
m = re.search(r'\d+', s)
print(m.group())
