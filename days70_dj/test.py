import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "days70_dj.settings")
    import django
    django.setup()

    from app01 import models

    data_list=[ models.Book(title ='第 {0} 本书'.format(i)) for i in range(100)]
    models.Book.objects.bulk_create(data_list)