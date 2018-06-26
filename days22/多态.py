import abc
class Animal:
    @abc.abstractmethod
    def bank(self):
        pass

class Pig(Animal):
    def bank(self):
        print('哼哼')
class Dog(Animal):
    def bank(self):
        print('旺旺')
p=Pig()
d=Dog()

def bank(Animal):
    Animal.bank()
p.bank()
bank(p)
bank(d)