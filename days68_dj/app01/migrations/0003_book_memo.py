# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-21 01:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20180621_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='memo',
            field=models.TextField(null=True),
        ),
    ]
