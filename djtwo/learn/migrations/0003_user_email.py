# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-24 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0002_user_user_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='000', max_length=64),
        ),
    ]