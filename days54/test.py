class Foo:
    __slots__=['name','age']

f1=Foo()
f1.name='alex'
f1.age=18
print(f1.__slots__)
print(f1.name)
print('=================')
f2=Foo()
f2.name='egon'
f2.age=19
print(f2.__slots__)
print(f1.name)
print(f2.name)
print('=================')


print(Foo.__dict__)
#f1与f2都没有属性字典__dict__了,统一归__slots__管,节省内存