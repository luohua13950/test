# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from asset.script.read_yaml_file import read_yaml_file
from djtwo.settings import BASE_DIR
from learn.models import User
from django import forms
import os
from asset.models import hostinfo
# Create your views here.
class SearchHost(forms.Form):
    hostip = forms.CharField(label='主机IP',max_length=64)
    hostname = forms.CharField(label='主机名',max_length=64)
def upload_hosts(request):
    url_path = os.path.join(BASE_DIR,'upload')
    if request.method == "POST":
        myfile = request.FILES.get("myfile",None)
        print url_path
        if not myfile:
            info = "文件不存在，请重新上传！"
            messages.add_message(request,messages.WARNING,info)
            response = HttpResponseRedirect('/asset/upload_hosts/')
            return response
        destnation = open(os.path.join(url_path,myfile.name),'wb+')
        for chunk in myfile.chunks():
            destnation.write(chunk)
        destnation.close()
        info = "上传成功！"
        messages.add_message(request,messages.SUCCESS,info)
        response = HttpResponseRedirect('/asset/upload_hosts/')
        load_file_path = os.path.join(url_path,myfile.name)
        ret = read_yaml_file(load_file_path)
        ret_ip = ret['hosts']['ipadress']
        ret_user = ret['hosts']['user']
        ret_passwd = ret['hosts']['password']
        ret_system = ret['hosts']['ownsystem']
        len_ret = len(ret_ip)
        name = request.COOKIES.get('username')

        for item in range(len_ret):
            #hostinfo.objects.create(host_ip= ret_ip[item],ssh_user= ret_user[item],ssh_passwd = ret_passwd[item],host_system = ret_system[item])
            tmp_hostip = hostinfo.objects.filter(host_ip=ret_ip[item]).values('host_ip')
            if len(tmp_hostip) != 0:
                continue
            hosts = hostinfo(host_ip= ret_ip[item],ssh_user= ret_user[item],ssh_passwd = ret_passwd[item],host_system = ret_system[item],user_name = name)
            hosts.save()
        tt = hostinfo.objects.all()
        return response
    else:
        info = "方法不是POST"
        messages.add_message(request,messages.WARNING,info)
        response = HttpResponseRedirect('/asset/upload_hosts/')
    return render(request,'upload_hosts.html')

def systeminfo(request):
    Context = {}
    if request.method == "POST":
        uf = SearchHost(request.POST)
        if uf.is_valid():
            hostip = uf.cleaned_data['hostip']
            hostname = uf.cleaned_data['hostname']
            host = hostinfo.objects.filter(host_ip = hostip)
            print type(host)
            if host:
                Context['host'] = host
                #print type(host)
                return render(request,'systeminfo.html',Context)
    else:
        uf = SearchHost()
    return render(request,'systeminfo.html',{'uf':uf})