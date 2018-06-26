from django.db import models

# Create your models here.

from django.db import models


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    # 库存数
    kucun = models.IntegerField()
    # 卖出数
    maichu = models.IntegerField()

    def __str__(self):
        return "{}:{:,.2f}:{}:{}".format(self.name, self.price, self.kucun, self.maichu)
