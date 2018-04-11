# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django import forms
from learn.models import User
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
import  datetime
from django.contrib import messages
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
    return render(request,'index.html',{'name':name})

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