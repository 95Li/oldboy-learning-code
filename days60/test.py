def multipliers():
    list=(lambda x: i * x for i in range(4))
    return  list


print([m(2) for m in multipliers()])
'''
 结果是：  [6, 6, 6, 6]

m = [i * x for i in range(4)]
m(2)= [i * 2 for i in range(4)]
'''
#
#
# def hellocounter (name):
#     count=[0]
#     def counter():
#         count[0]+=1
#         print( 'Hello,',name,',',str(count[0])+' access!')
#     return counter
#
# hello = hellocounter('ma6174')
# hello()
# hello()
# hello()
