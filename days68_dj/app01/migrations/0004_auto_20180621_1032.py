# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-21 02:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_book_memo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='authors', related_query_name='author123', to='app01.Author'),
        ),
    ]
