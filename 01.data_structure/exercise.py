"""
逆波兰表达式
"""

"""
from sstack import *

str_ = input("请输入>>")

operator = ("+", "-", "*", "/")

st = SStack()
for item in str_.split():
    if item.isdigit():
        st.push(item)
    elif item in operator:
        right = st.pop()
        left = st.pop()
        result = eval(str(left) + item + str(right))
        st.push(result)
    elif item == 'p':
        print(st.top())
"""

from sstack import *

st = SStack()

while True:
    exp = input()
    tmp = exp.split(' ')  # 按空格切割
    for i in tmp:
        if i not in ['+', '-', '*', '/', 'p']:
            st.push(float(i))
        elif i == '+':
            y = st.pop()
            x = st.pop()
            st.push(x + y)
        elif i == '-':
            y = st.pop()
            x = st.pop()
            st.push(x - y)
        elif i == '*':
            y = st.pop()
            x = st.pop()
            st.push(x * y)
        elif i == '/':
            y = st.pop()
            x = st.pop()
            st.push(x / y)
        elif i == 'p':
            print(st.top())
