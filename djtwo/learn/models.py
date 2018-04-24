# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    TYPE_CHIOCE = (
     ('0','commuser'),
     ('1','admin'),
     ('2','superadmin'),
    )
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    last_login = models.DateTimeField(blank=True)
    user_priority=models.IntegerField(default=0)
    email = models.CharField(max_length=64,default='000')
    def __unicode__(self):
        return self.username