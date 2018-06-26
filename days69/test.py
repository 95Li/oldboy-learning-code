# # a=[1,4,3,2]
# a=[1,2,3,4]
# # b=sorted(a)
# # b=a
# # print(b)
# if a==sorted(a):
#     print('T')

# a='{:,.2f}'.format(50080.33)
# print(a)

# from collections import Counter
# l=['a','b','c','a','a']
# l_dic=Counter(l)
# print(l_dic)
#

# v = dict.fromkeys(['k1', 'k2'], [])
# print(v)
# v['k1'].append(666)
# print(v)
# v['k1'] = 777
# print(v)
#
# def num():
#     return [lambda x:x*i for i in range(4)]
#
# print([m(2) for m in num()])

#
# a = [1, 2, 3]
# b = sorted(a, reverse=True)
# print(b)
# if a == b:
#     print('++++++')

#
# res=['%d * %d = %d' %(i,j,i*j ) for i in range(1,10) for j in range(1,10)]
# print(res)

# print( i % 2 for i in range(10) )
# print([ i % 2 for i in range(10) ])

# res=1 < 2==2
# print(res)
# print(1==True)

# a='1,2,3'
# b=a.split(',')
# print(b)

a=['1', '2', '3']
b=[int(i) for i in a]
print(b)
