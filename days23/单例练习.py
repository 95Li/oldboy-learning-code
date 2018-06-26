'''
单例模式 练习
'''

NAME='name'
AGE=18
'''
1.加一个类方法 用于生成对象
'''
# class Mysingleton:
#     __instance=None
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     @classmethod
#     def singleton(cls):
#         if cls.__instance==None:
#             cls.__instance=cls(NAME,AGE)
#         return cls.__instance
#
# m1=Mysingleton.singleton()
# m2=Mysingleton.singleton()
# m3=Mysingleton('lyj',18)
#
# print(m1)
# print(m2)
# print(m3)

'''
2.元类 改init方法和call方法
'''
class Mymeta(type):
    # def __init__(self,name,base,dic):
    #     self.__instance=object.__new__(self)
    #     self.__init__(self.__instance,NAME,AGE)
    #     super().__init__(name,base,dic)
    def __new__(cls, name,base,dic):
        cls.__instance=type.__new__(cls)
        cls.__init__(cls.__instance,NAME,AGE)
        return super().__new__(cls,name,base,dic)

    def __call__(self, *args, **kwargs):
        if args or kwargs:
            obj=object.__new__(self)
            obj.__init__(*args, **kwargs)
            return obj
        else:
            return self.__instance
class Mysingleton(metaclass=Mymeta):
    def __init__(self,name,age):
        self.name=name
        self.age=age

m1=Mysingleton()
m2=Mysingleton()
m3=Mysingleton('lyj',18)

print(m1)
print(m2)
print(m3)

'''
3. 加装饰器
'''
# def singleton(cls):
#     __instance=cls(NAME,AGE)
#     def wrapper(*args,**kwargs):
#         if  args or kwargs:
#             obj=cls(*args,**kwargs)
#             return obj
#         return __instance
#     return wrapper
# @singleton
# class Mysingleton:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
# m1=Mysingleton()
# m2=Mysingleton()
# m3=Mysingleton('lyj',18)
#
# print(m1)
# print(m2)
# print(m3)
#

