import os
# from days66_dj
if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "days67_dj.settings")
    import django
    django.setup()

    from app01 import models

    # books = models.test.objects.all()
    # print(books)

    # test=models.test.objects.extra(
    #     select={'newid': 'select * from app01_test '},
    #     # select_params=[1, ],
    #     # where=['age>%s'],
    #     # params=[18, ],
    #     # order_by=['-age'],
    #     tables=['app01_test']
    # )

    from django.db import connection,connections

    cursor=connection.cursor()
    cursor.execute('select * from app01_test')
    res =cursor.fetchone()

    print(res)