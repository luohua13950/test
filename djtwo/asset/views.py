# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from asset.script.read_yaml_file import read_yaml_file
from djtwo.settings import BASE_DIR
from learn.models import User
from django import forms
import os,sys
from asset.models import hostinfo
from asset.script import send_mails
sys.path.append("..")
# Create your views here.
class SearchHost(forms.Form):
    hostip = forms.CharField(label='主机IP',max_length=64)
    hostname = forms.CharField(label='主机名',max_length=64)
def upload_hosts(request):
    url_path = os.path.join(BASE_DIR,'upload')#先获得存放上传文件的目录
    if request.method == "POST":
        myfile = request.FILES.get("myfile",None)#获得上传的文件
        print url_path
        if not myfile:
            info = "文件不存在，请重新上传！"
            messages.add_message(request,messages.WARNING,info)
            response = HttpResponseRedirect('/asset/upload_hosts/')
            return response
        destnation = open(os.path.join(url_path,myfile.name),'wb+')#打开上传的文件
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
        #info = "方法不是POST"
        #messages.add_message(request,messages.WARNING,info)
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
'''
def send_email(requst):
            sendm = send_mails.sendmaill(subject = "dada",context ="dada",mail_to = ['luohua13950@163.com'])
            ret = sendm.send()
            if ret:
                info = "发送成功！"
                messages.add_message(requst,messages.SUCCESS,info)
                return render(requst,'sendemail.html')
            else:
                info = "发送失败！"
                messages.add_message(requst,messages.WARNING,info)
                respose = HttpResponseRedirect('/asset/sendemail/')
                return respose
'''
def sendmail(request):
    sendm = send_mails.sendmail(sub_info = "测试邮件",content_info ="这是一封测试邮件！",receive_addr = ['luohua13950@163.com'])
    ret = sendm.send()
    return  render(request,'sendemail.html',{'ret':ret})