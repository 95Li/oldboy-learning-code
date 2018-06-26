class DateButhday:
    def __init__(self,year,mon,day):
        self.year = year
        self.day = day
        self.mon = mon
    def get_buthday(self):
        print('出生日期为：%s-%s-%s'%(self.year,self.mon,self.day))

class Person:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        # self.year=year
        # self.day=day
        # self.mon=mon

    # def get_buthday(self):
    #     print('出生日期为：%s-%s-%s'%(self.year,self.mon,self.day))
class Teacher(Person):
    def __init__(self,name,age,sex,level):
        super().__init__(name,age,sex)
        self.level=level

class Student(Person):
    def __init__(self,name,age,sex,coures):
        super().__init__(name,age,sex)
        self.coures=coures


t1=Teacher('egon',18,'male',9)
t1.buthday=DateButhday(2000,2,3)
t1.buthday.get_buthday()

print(t1.__dict__)
print(t1.buthday.__dict__)