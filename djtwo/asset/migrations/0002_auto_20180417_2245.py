# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-17 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostinfo',
            name='user_name',
            field=models.CharField(default='admin', max_length=64, verbose_name='\u6dfb\u52a0\u673a\u5668\u7684\u4eba\u540d'),
        ),
        migrations.AlterModelTable(
            name='hostinfo',
            table='hostinfo',
        ),
    ]
