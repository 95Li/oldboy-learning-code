from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=64)
    publish_date = models.DateTimeField(auto_now=True)


class User(models.Model):
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
