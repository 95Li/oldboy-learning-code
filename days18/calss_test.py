import os
import json

class Campus:
    def __init__(self,name,city,area,courses,classs):
        self.name=name
        self.address={'city':city,'district':area}
        self.courses=courses
        self.classs=classs
    def create_class(self,name,campus,courses,teachers):
        get_class=Classs(name,campus,courses,teachers)
        self.classs.append(get_class.name)
        print(get_class.__dict__)
    def get_classs(self):
        print(self.classs)
    def create_course(self,name,cycle,price):
        get_course = Course(name,cycle,price)
        self.classs.append(get_course.name)
        return get_course
    def get_courses(self):
        print(self.courses)

class Classs:
    def __init__(self,name,campus,courses,teachers):
        self.name=name
        self.campus=campus
        self.courses=courses
        self.teachers=teachers
    def get_courses(self):
        print(self.courses)
    def get_teachers(self):
        print(self.teachers)

class Course:
    def __init__(self,name,cycle,price):
        self.name=name
        self.cycle=cycle
        self.price=price

    def get_course_info(self):
        print(self.__dict__)

class Student:
    def __init__(self,id,name,classs,score):
        self.id=id
        self.name=name
        self.classs=classs
        self.score=score

    def chose_classs(self,classs):
        self.classs.append(classs)
        print(self.classs)
    def register(self):
        path=os.path.join(os.path.dirname(__file__),'%s.json'%self.name)
        self=self.__dict__
        with open(path,'wt',encoding='utf-8')as f:
            json.dump(self,f)

class Teacher:
    def __init__(self,name,level):
        self.name = name
        self.level=level
    def update_score(self,student,score):
        student.score=score

courses=['XXX','YYY','ZZZ']
classs=['python','java','linux']
teachers=['egon','lqz','alex']

# beijing=Campus('北京校区','北京','朝阳区',courses,classs)
# shanghai=Campus('上海校区','上海','浦东新区',courses,classs)
# beijing.create_class('python','上海校区',courses,teachers)
# print(beijing.__dict__)
# print(shanghai.__dict__)

# pathon=Classs('python','上海校区',courses,teachers)
# pathon.get_courses()

student=Student(10,'lxx',classs,33)
# student.register()

teacher=Teacher('egon',2)
teacher.update_score(student,59)
print(student.score)