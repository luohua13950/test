# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-24 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0002_auto_20180417_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostinfo',
            name='ops_direct',
            field=models.CharField(default='no', max_length=64, verbose_name='\u8be5\u673a\u5668\u8054\u7cfb\u4eba'),
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='sytem_info',
            field=models.CharField(default='os', max_length=64, verbose_name='\u4e3b\u673a\u64cd\u4f5c\u7cfb\u7edf'),
        ),
    ]
