# x = '1111011'
# res = int(x,2)

# res=bin(18)

# v='011'
# res=int(v,8)


# v=30
# res=oct(v)

# v = '0x12'
# res=int(v,16)

# v = 87
# res = hex(v)


# res=bin(10)[2:]
# res=res.rjust(8,'0')
# print(res)  #输出： 00001010


# def tobin(str):
#     res_list = []
#     num_list = str.split('.')
#     for num in num_list:
#         res = bin(int(num))[2:]
#         res = res.rjust(8, '0')
#         res_list.append(res)
#     res = ' '.join(res_list)
#     return res
#
#

# inp = '10.3.9.12'
# res = tobin(inp)
# print(res)
import sys

a=0 or False and 1
print(a)
print((0 and 2 or 1 or 4))
print((0 and 2 or 1))
print((0 and 2 and 1))
print((1 or 3))
# sys.exit()
aaa=1 and 3

print(aaa)

print()

print((1 or 3))
