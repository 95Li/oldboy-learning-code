
def war1(func):
    print("war1")
    def inner(*args, **kwargs):
        print("======war1 start=====")
        func(*args, **kwargs)
        print("======war1 end=====")
    return inner

def war2(func):
    print("war2")
    def inner(*args,**kwargs):
        print("======war2 start=====")
        func(*args,**kwargs)
        print("======war2 end=====")
    return inner

@war1
@war2
def f():
    print("****self****")
# 相当于 war1(war2(f))()

f()


