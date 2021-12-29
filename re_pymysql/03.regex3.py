"""
match 对象属性演示

group(n=0)
    功能：获取match对象匹配内容
    参数：默认为0表示获取整个match对象内容，如果是序列号或者组名则表示获取对应子组内容
    返回值：匹配字符串
"""

import re

pattern = r"(ab)cd(?P<pig>ef)"
regex = re.compile(pattern)
obj = regex.search('abcdefghi')  # match对象

# 属性变量
print(obj.pos)  # 打印匹配目标字符串的开始位置
print(obj.endpos)  # 打印匹配目标字符串的结尾位置
print(obj.re)  # 正则表达式
print(obj.string)  # 目标字符串
print(obj.lastgroup)  # 最后一组组名
print(obj.lastindex)  # 最后一组序列号

print("================")

# 属性方法
print(obj.span())  # 匹配内容在字符串中位置
print(obj.start())
print(obj.end())
print(obj.groupdict())  # 捕获组字典
print(obj.groups())  # 子组对应内容元组
print(obj.group())  # 获取match对象对应内容
