'''
4-17日作业
'''
'''
    1、判断一个对象是否属于str类型，判断一个类是否是另外一个类的子类
'''
a='123'
print(isinstance(a,str))
print(issubclass(str,object))

'''
    2、有俩程序员，一个lili，一个是egon，lili在写程序的时候需要用到egon所写的类(放到了另外一个文件中)，但是egon去跟女朋友度蜜月去了，还没有完成他写的类，
        class FtpClient:
            """
            ftp客户端,但是还么有实现具体的功能
            """
            def __init__(self,addr):
                print('正在连接服务器[%s]' %addr)
                self.addr=addr

            此处应该完成一个get功能
    lili想到了反射，使用了反射机制lili可以继续完成自己的代码，等egon度蜜月回来后再继续完成类的定义并且去实现lili想要的功能。
'''

class FtpClient:
    """
    ftp客户端,但是还么有实现具体的功能
    """

    def __init__(self, addr):
        print('正在连接服务器[%s]' % addr)
        self.addr = addr
f=FtpClient('egon')
addr=getattr(f,'addr')
print(addr)


'''

    3、定义一个老师类，定制打印对象的格式为‘<name:egon age:18 sex:male>’
'''
class Teacher:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def __str__(self):
        return '<name: %s  age: %s  sex: %s>'%(self.name,self.age,self.sex)
t=Teacher('egon',18,'male')
print(t)

'''
 4、定义一个自己的open类，控制文件的读或写，在对象被删除时自动回收系统资源
'''
class MyOpen:
    def __init__(self,file,io,encoding):
        self.file=file
        self.io=io
        self.encoding=encoding
        self.my_open=open(self.file,self.io,encoding=self.encoding)
    def __del__(self):
        self.my_open.close()
        print('guan bi wen jian')

mo=MyOpen(r'F:\python\object\days2\days23\setting.py','rt','utf-8')
del mo

'''
  5、自定义元类，把自定义类的数据属性都变成大写，必须有文档注释，类名的首字母必须大写
'''
class Mymeta(type):
    def __init__(self,class_name,class_base,class_dict):
        dict={}
        for name in class_dict:
            if not name.istitle():
                new_name=name.capitalize()
            dict.update({new_name:class_dict[name]})
        print(dict)
        super().__init__(class_name,class_base,dict)
        if not class_name.istitle():
            raise TypeError('类名必须首字母大写')
        if not class_dict.get('__doc__'):
            raise TypeError('类必须有文档注释')
class My(object,metaclass=Mymeta):
    '''
    MY 1233123
    '''
    char='123'
    def abc(self):
        print(self.char)
m=My()
print(My.__dict__)



'''

    6、用三种方法实现单例模式，参考答案:http://www.cnblogs.com/linhaifeng/articles/8029564.html#_label5
'''



class Mymeta(type):
    __obj = ''
    def __call__(self, *args, **kwargs):
        if self.__obj=='':
            self.__obj=self.__new__(self)
            self.__obj.__init__(*args, **kwargs)
        return self.__obj
class My(object,metaclass=Mymeta):
    '''
    MY 1233123
    '''
    char='123'
    def abc(self):
        print(self.char)
m = My()
m2 = My()
m3 = My()
print(m, m2, m3)



class My(object):
    __obj = None

    def __new__(cls, *args, **kwargs):
        print(cls.__obj)
        if cls.__obj == None:
            cls.__obj = cls
        else:
            cls = My.__obj


    '''
    MY 1233123
    '''
    char = '123'

    def abc(self):
        print(self.char)


m = My()
m2 = My()
m3 = My()
print(m, m2, m3)
