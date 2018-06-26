class People:
    def __init__(self,name):
        self.__name=name
    @property
    def names(self):
        return self.__name
    @names .setter
    def names (self,x):
        self.__name=x
    @names .deleter
    def names (self):
        del self.__name
p=People('egon')
print(p.names )
p.names='qwe'
print(p.names )
del p.names
print(p.names)



