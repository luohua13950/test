# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-17 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hostinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_ip', models.CharField(max_length=64, verbose_name='\u4e3b\u673aIP')),
                ('ssh_user', models.CharField(max_length=64, verbose_name='\u767b\u5f55\u7528\u6237')),
                ('ssh_passwd', models.CharField(max_length=64, verbose_name='\u767b\u5f55\u5bc6\u7801')),
                ('ssh_status', models.IntegerField(default=0, verbose_name='0-\u6210\u529f\uff0c1-\u5931\u8d25')),
                ('host_system', models.CharField(max_length=64, verbose_name='\u4e3b\u673a\u6240\u90e8\u7f72\u7684\u7cfb\u7edf')),
            ],
        ),
    ]
