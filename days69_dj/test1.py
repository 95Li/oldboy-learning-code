import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "days69_dj.settings")

    import django

    django.setup()

    from app01 import models
    from django.db.models import F

    res = models.Product.objects.filter(maichu=F('kucun'))
    # res= models.Product.objects.filter(maichu__gt=F("kucun"))

    from django.db.models import Value
    from django.db.models.functions import Concat
    # models.Product.objects.update(price=F('price')+30)
    # models.Product.objects.update(name=Concat(F('name'),Value('特价')))

    from django.db.models import Q

    res = models.Product.objects.filter(Q(kucun=60) | Q(kucun=100))
    res = models.Product.objects.filter(Q(kucun=60), ~Q(price=60))

    # print(res)

    # from django.db import transaction
    # try:
    #     with transaction.atomic():
    #         models.Product.objects.update(price=F('price') + 30)
    #         # res=models.Product.objects.get(maichu=F('kucun'))
    #         res=models.Product.objects.get(maichu=F('kucun')).values()
    #         print(res)
    # except Exception as e:
    #     print(e)
    res = models.Product.objects.filter(name__contains='新款').extra(
        {'res': 'select count(id) from app01_product GROUP BY kucun '}).values('res', 'kucun')
    print(res)
