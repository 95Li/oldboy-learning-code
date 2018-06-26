dic={'1':'a','2':'b'}
# k=list(dic)
# print(k)

a='a'
def foo(*a):
    print(a)

def f(**w):
    print(w)

f(a='a',b='b')
# f(dic)

foo(a)
foo(dic)
foo(a='a',b='b')
# foo()










