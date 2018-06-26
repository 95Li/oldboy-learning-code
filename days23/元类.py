class_name='Chinese'
class_bases=(object,)
class_body="""
country="China"
def __init__(self,name,age,sex):
    self.name=name
    self.age=age
    self.sex=sex
def speak(self):
    print('%s speak Chinese' %self.name)
"""
class_dic={}
exec(class_body,{},class_dic)

# print(class_dic)

# 类的三大要素
print(class_name,class_bases,class_dic)

Chinese=type(class_name,class_bases,class_dic)
print(Chinese)

p=Chinese('egon',18,'male')
print(p.name,p.age,p.sex)

#
# # 3、储备知识__call__
# class Foo:
#     def __init__(self):
#         pass
#     def __str__(self):
#         return '123123'
#
#     def __del__(self):
#         pass
#
#     # 调用对象，则会自动触发对象下的绑定方法__call__的执行，
#     # 然后将对象本身当作第一个参数传给self，将调用对象时括号内的值
#     #传给*args与**kwargs
#     def __call__(self, *args, **kwargs):
#         print('__call__',args,kwargs)
#
#
# obj=Foo()
# # print(obj)

