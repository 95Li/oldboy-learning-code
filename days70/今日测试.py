'''
1. 创建一个装饰器将下面函数输入的字符串首字母大写,其余字母小写。
'''
# def check(func):
#     def inner(*args,**kwargs):
#         args=[i.capitalize() for i in args]
#         func(*args,**kwargs)
#     return inner
#
# @check
# def f(a,b):
#     print(a,b)
#
# f('asdfasdas','sfdsd')
# #输出结果：  Asdfasdas Sfdsd

'''
2.请写一段python代码，替换掉目标字符串中的[北京市，技术，有限，公司]等字符，目标字符串：北京市麦达技术数字有限公司，要求替换输出 麦达数字。
'''
# s = '北京市麦达技术数字有限公司'
# li = ['北京市', '技术', '有限', '公司']
# for i in li:
#     print(i)
#     s=s.replace(i, '')
# print(s)

'''
3.*args,**kwargs的作用是什么？如何使用？      
  
  *args 位置参数 用于接收传进来的普通值
  **kwargs 关键字参数  用于接收传进来的字典类型的参数
  当两个一起使用的时候们可以接受任意类型的参数    
'''

'''
4.把字符串“HELLO PYTHON”从大写字母全部转换成小写字母并换行显示，然后输出到计算机c盘的hello.txt文件中保存。
'''
s = 'HELLO PYTHON'
new_s = s.lower().replace(' ', '/r/n')
print(new_s)
import os

path = 'F:\hello.txt'
with open(path, 'a') as f:
    f.write(new_s)

'''
5.python中如何拷贝一个对象？（赋值，浅拷贝，深拷贝的区别）

赋值： =  
  a='aaaaa'
  b=a
    赋值时 将a指向的地址 给了b  a b指向的地址是同一个

浅拷贝： 是关于字典，列表之类可变类型的  
        浅拷贝是指 当copy时 ，只拷贝改变了外层的地址，而内层仍然指向的是同一地址，原数据内层元素，拷贝数据的内层元素也改变，两个数据仍然是具有相关性
        浅拷贝有：  copy函数，list()函数等
深拷贝：与浅拷贝相对应 不仅拷贝了外层，内层元素也拷贝了，对原数据进行修改，不管怎么，都不会影响拷贝来的新数据
        deepcopy()函数
    
'''
