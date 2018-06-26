# s=1
# result2 = (s == 2) and 'test_true' or 'test_false'
# print(result2)

# a=1
# b=2
#
#
# # a,b=b,a
#
# print(a,b)


# class Foo:
#     def __init__(self,x):
#         self.x=x
#
#     def __getattr__(self, item):
#         print('执行的是我')
#         # return self.__dict__[item]
#
# f1=Foo(10)
# print(f1.x)

class Foo:
    def __init__(self, x):
         self.a=x

    def __getattr__(self, item):
        print('执行的是我')

        # return self.__dict__[item]

    def __getattribute__(self, item):
        print('不管是否存在,我都会执行')
        raise AttributeError('哈哈')


f1 = Foo(10)
print(f1.a)
f1.xxxxxx
