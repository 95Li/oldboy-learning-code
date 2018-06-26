from django.db import models


# Create your models here.

class Dept(models.Model):
    name = models.CharField(max_length=32)


class Employee(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    salary = models.IntegerField()
    province = models.CharField(max_length=64)
    dept = models.ForeignKey(to=Dept)

    # def db_table(self):
    #     return 'employee'