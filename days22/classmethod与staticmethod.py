NAME='name'
AGE='age'


class People:
    def __init__(self,name,age):
         self.name=name
         self.age=age
    @classmethod
    def from_conf(cla):
        return cla(NAME,AGE)

p=People.from_conf()
print(p.name)
