# class  Foo:
#     def __init__(self,name):
#         self.name=name
#
#     def __call__(self, *args, **kwargs):
#         print(*args)
# f=Foo('123')
# f(1,2,3,4)

class Mymeta(type):
    def __init__(self,class_name,class_bases,class_dic):
        if not class_name.istitle():
            raise  TypeError('类名首字母大写')
        if  not class_dic.get('__doc__'):
            raise TypeError('类中必须写好文档注视')
        super(Mymeta,self).__init__(class_name,class_bases,class_dic)


class Foo(object,metaclass=Mymeta):
    '''
       guanliyuan

     '''
    pass