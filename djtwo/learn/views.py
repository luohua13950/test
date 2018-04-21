# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django import forms
from learn.models import User
from django.template import RequestContext,Context
from django.views.decorators.csrf import csrf_exempt
import  datetime
from django.contrib import messages
from asset.script import ssh_link,read_yaml_file
# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField(label='用户名:',max_length=100)
    password = forms.CharField(label='密码:',widget=forms.PasswordInput())

def login(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = User.objects.filter(username = username)
            if user:
                passwd = User.objects.filter(username = username,password = password)
                if passwd:
                    info = '登录成功！'
                    response = HttpResponseRedirect('/learn/index/')
                    response.set_cookie('username',username,3600)
                    last_login= datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    ##get的方式更新信息
                    user = User.objects.get(username = username)
                    user.username = username
                    user.password = password
                    user.last_login = last_login
                    user.save()
                    return response
                else:
                    info = '登录失败，请检查用户名和密码！'
                    messages.add_message(request,messages.WARNING,info)
                    response = HttpResponseRedirect('/learn/login/')
                   # return HttpResponse(info)
                    return response
            elif len(user) == 0:
                info = '输入是否正确？'
                messages.add_message(request,messages.WARNING,info)
            return HttpResponse(info)
    else:
        uf = UserForm()
    #return render_to_response('login.html',{'uf':uf},RequestContext(request))
    return render(request,'login.html',{'uf':uf})
def index(request):
    name = request.COOKIES.get('username')
    users = User.objects.filter(username = name).values('user_priority')#获取权限
    reprio = "管理员"
    for item in users:
       prio = item
    if item == '0':
       reprio = "普通用户"
    elif item == '1':
       reprio = "管理员"
    elif item == '2':
       reprio = "超级管理员"
    #context = ({'name':name})
    return render(request,'index.html',locals())

@csrf_exempt
def regist(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = User.objects.filter(username = username)
            print user
            if user:
                info = "用户已经存在！"
                messages.add_message(request,messages.WARNING,info)
            elif len(user) == 0:
                info = "注册成功！"
                user = User()
                user.username = username
                user.password = password
                user.last_login=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                user.save()
                messages.add_message(request,messages.SUCCESS,info)
                response = HttpResponseRedirect('/learn/login/')
                return response
    else:
        uf = UserForm()
    #c = ({'name':'luohua'})
    return render(request,'regist.html',{'uf':uf})

def changpass(request):
   users = User.objects.all()
   for u in (users):
    print (u)
    return render(request,"changpass.html",{'users':users})

def piant(request):
    #response = HttpResponseRedirect('/learn/piant/')
   # return response
    ssh = ssh_link.ssh_login_basetion()
    res = ssh_link.get_memory(ssh)
    host_name = ssh_link.HostIp
    user_mem = int(res[0])
    free_mem = int(res[1])
    avail_mem = int(res[2])
    ret = {'user_mem':user_mem,'free_mem':free_mem,'avail_mem':avail_mem,'host_name':host_name}
    ssh.close()
    return render(request,"piant.html",ret)
