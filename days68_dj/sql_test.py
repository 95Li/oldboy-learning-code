import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "days68_dj.settings")
    import django

    django.setup()

    from app01 import models

    # 查找所有书名里包含番茄的书
    books = models.Book.objects.filter(title__contains='番茄')

    # 查找出版日期是2017年的书
    books = models.Book.objects.filter(publish_date__year='2017')

    # 查找出版日期是2017年的书名
    books = models.Book.objects.filter(publish_date__year='2017').values('title')

    # 查找价格大于10元的书
    books = models.Book.objects.filter(price__gt=10)

    # 查找价格大于10元的书名和价格
    books = models.Book.objects.filter(price__gt=10).values('title', 'price')

    # 查找memo字段是空的书
    books = models.Book.objects.filter(memo__isnull=True)

    # 查找在北京的出版社
    books = models.Publisher.objects.filter(city='北京')

    # 查找名字以沙河开头的出版社
    books = models.Publisher.objects.filter(name__startswith='沙河')

    # 查找作者名字里面带“小”字的作者
    books = models.Author.objects.filter(name__contains='小')

    # 查找年龄大于30岁的作者
    books = models.Author.objects.filter(age__gt=30)

    # 查找手机号是155开头的作者
    books = models.Author.objects.filter(phone__startswith='155')

    # 查找手机号是155开头的作者的姓名和年龄
    books = models.Author.objects.filter(phone__startswith='155').values('name', 'age')

    # 查找书名是“番茄物语”的书的出版社
    books = models.Book.objects.get(title='番茄物语').publisher

    # 查找书名是“番茄物语”的书的出版社所在的城市
    # books = models.Book.objects.get(title='番茄物语').publisher.city
    books = models.Book.objects.filter(title='番茄物语').values('publisher__city')

    # 查找书名是“番茄物语”的书的出版社的名称
    # books = models.Book.objects.get(title='番茄物语').publisher.name
    books = models.Book.objects.filter(title='番茄物语').values('publisher__name')

    # 查找书名是“番茄物语”的书的所有作者
    # books = models.Book.objects.get(title='番茄物语').author.all()
    books = models.Book.objects.filter(title='番茄物语').values('author__name')

    # 查找书名是“番茄物语”的书的作者的年龄
    books = models.Book.objects.filter(title='番茄物语').values('author__age')

    # 查找书名是“番茄物语”的书的作者的手机号码
    books = models.Book.objects.filter(title='番茄物语').values('author__phone')

    # 查找书名是“番茄物语”的书的作者的地址
    books = models.Book.objects.filter(title='番茄物语').values('author__detail__addr')

    # 查找书名是“番茄物语”的书的作者的邮箱
    books = models.Book.objects.filter(title='番茄物语').values('author__detail__email')

    books = models.Author.objects.get(id=1).books.all()
    books = models.Author.objects.filter(id=1).values('book123__title')

    # print(books)

    from django.db.models import Avg, Sum, Max, Min, Count

    #统计每一本书的作者个数
    # res = models.Book.objects.annotate(count_author=Count('author__id')).values('title', 'count_author')
    # #统计出每个出版社买的最便宜的书的价格
    # res = models.Publisher.objects.annotate(min_price=Min('book__price')).values('name', 'book__title', 'min_price')
    # #统计不止一个作者的图书
    # res= models.Book.objects.annotate(author_num=Count('author__id')).filter(author_num__gt=1).values('title','author_num')
    # #根据一本图书作者数量的多少对查询集 QuerySet进行排序
    # res=models.Book.objects.annotate(author_num=Count('author__id')).values('title','author_num').order_by('-author_num')
    #查询各个作者出的书的总价格
    # res=models.Author.objects.annotate(sum_price=Sum('book123__price')).values('name','sum_price')
    # res=models.Author.objects.annotate(sum_price=Sum('book123__price'))
    # res = models.Author.objects.aggregate(sum_price=Sum('book123__price'))

    print(res)
