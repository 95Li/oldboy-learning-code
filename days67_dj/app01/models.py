from django.db import models


# Create your models here.

class MyCharField(models.Field):
    def __init__(self, max_length, *args, **kwargs):
        self.max_length = max_length
        super(MyCharField, self).__init__(max_length=max_length, *args, **kwargs)

    def db_type(self, connection):
        return 'char(%s)' % self.max_length


class test(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    test = MyCharField(max_length=32)
