#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/11/24

"""
Python全栈课前练习题
"""

s = "Alex SB 哈哈\r\nx:1\r\ny:2\r\nz:3\r\n\r\n自行车"

# 问题1：如何取到["Alex SB 哈哈\r\nx:1\r\ny:2\r\nz:3", "自行车"]?


# 问题2：如何在上面结果基础上拿到["Alex", "SB", "哈哈"]?


# 问题3：如何在上面结果基础上拿到"SB"?


# ------------------------------------------------------------------------------------------


# 有一个列表，他的内部是一些元祖，元祖的第一个元素是姓名，第二个元素是爱好。
# 现在我给你一个姓名，如"Egon",如果有这个姓名，就打印出他的爱好，没有就打印查无此人。

list1 = [
    ("Alex", "烫头"),
    ("Egon", "街舞"),
    ("Yuan", "喝茶")
]
def get_hobby(name):
    for i  in  list1:
        if i[0]==name:
            print(i[1])
            return
    print("查无此人")
get_hobby("Egon")



# ------------------------------------------------------------------------------------------

# 我有一个HTML文件"login.html"

# 问题1：我如何读取它的内容保存到变量html_s？
with open('login.html','r',encoding='utf-8')as f:
    html_s=f.read()

# 问题2：我如何读取它的二进制内容保存到变量html_b？
with open('login.html','rb')as f:
    html_b=f.read()

# ------------------------------------------------------------------------------------------

s2 = "Alex 花了一百万买了辆电动车，真@@xx@@。"

# 问题1：如何把上面的s2转变成"Alex 花了一百万买了辆电动车，真SB。"
s=s2.replace('@@xx@@','SB')
print(s)
