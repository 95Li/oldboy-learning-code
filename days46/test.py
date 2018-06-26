def addBinary(a, b):
    a, b = int('0b' + a, 2), int('0b' + b, 2)
    return bin(a + b)[2:]

a = "1010"
b = "1011"
print(addBinary(a, b))
# 还有另外长一点但比我短的代码，是将a,b反转过来，这样列表切片方便。
# int()函数用于将一个字符串或数字转换为整型。语法：
# class int(x, base)
# x–字符串或数字
# base–进制数，默认十进制。
# bin()函数返回一个整型int或者长整数long int的二进制表示。