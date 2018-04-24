# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class hostinfo(models.Model):
    host_ip = models.CharField(max_length=64,null=False,verbose_name='主机IP')
    ssh_user = models.CharField(max_length=64,null=False,verbose_name='登录用户')
    ssh_passwd = models.CharField(max_length=64,null=False,verbose_name='登录密码')
    ssh_status = models.IntegerField(default=0,verbose_name='0-成功，1-失败')
    host_system = models.CharField(max_length=64,null=False,verbose_name='主机所部署的系统')
    user_name = models.CharField(max_length=64,default='admin',verbose_name='添加机器的人名')
    ops_direct = models.CharField(max_length=64,default='no',verbose_name='该机器联系人')
    sytem_info = models.CharField(max_length=64,default='os',verbose_name='主机操作系统')
    class Meta:
        db_table = "hostinfo"