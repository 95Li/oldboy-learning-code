import setting
# class Mymeta(type):
#     def __init__(self,name,base,dict):
#         self.__instance=object.__new__(self)
#         self.__init__(self.__instance,setting.HOST,setting.PORT)
#         super().__init__(name,base,dict)
#     def __call__(self, *args, **kwargs):
#         if args or kwargs:
#             obj=object.__new__(self)
#             self.__init__(obj,*args, **kwargs)
#             return obj
#             # super().__call__(*args, **kwargs)
#         return self.__instance
#
# class MySql(metaclass=Mymeta):
#     def __init__(self,host,port):
#         self.host=host
#         self.port=port


# class MySql:
#     __instance=None
#     def __init__(self,host,port):
#         self.host=host
#         self.post=port
#     @classmethod
#     def singleton(cls):
#         if cls.__instance==None:
#             obj=cls(setting.HOST,setting.PORT)
#             return obj
#         else:return cls.__instance

def single(cls):
    __instance=cls(setting.HOST,setting.PORT)
    def wrapper(*args,**kwargs):
        if args or kwargs:
            obj=cls(*args,**kwargs)
            return obj
        else: return __instance
    return wrapper
@single
class MySql:
    def __init__(self,host,port):
        self.host=host
        self.port=port

obj1=MySql()
obj2=MySql()
# obj2=MySql.singleton()

obj3=MySql('qwe','asd')
print(obj1,obj1.__dict__)
print(obj2,obj2.__dict__)
print(obj3,obj3.__dict__)