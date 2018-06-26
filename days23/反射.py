# class People:
#     country='china'
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#
# p=People('egon',18)
# print(hasattr(People,'country'))
# print(getattr(People,'country',None))
# print(getattr(People,'age',None))
# print(setattr(People,'country','CHINA'))
# print(delattr(People,'country'))
#
# print(hasattr(p,'country'))
# print(getattr(p,'country',None))
# print(getattr(p,'age',None))
#

class Foo:
    def run(self):
        while True:
            cmd=input('cmd>>:').strip()
            if hasattr(self,cmd):
                func=getattr(self,cmd)
                func()
    def download(self):
        print('dowonload...')

    def upload(self):
        print('upload...')

obj=Foo()
obj.run()
