
class ParentClass:

    def __init__(self, name, sex, age):
        self.name = name
        self.age = age
        self.sex = sex

    def tell_info(self):
        print(self.__dict__)



class Teacher(ParentClass):
    def __init__(self, name, sex, age, level, salary):
        self.level = level
        self.salary = salary
        super().__init__(name, sex, age)

class Student(ParentClass):
    def learn(self):
        print('learning...')

class Course:
    def __init__(self,cname,period,price):
        self.cname=cname
        self.period=price
        self.price=price
    def tell_info(self):
        print(self.__dict__)