def test(m):
    def inner(func):
        def warpper(*args,**kwargs):
            print(m)
            if m==1:
                print("start")
                func(*args,**kwargs)
                print("end")
        return warpper
    return inner

@test(m=1)
def f():
    print("2018-06-04")

f()