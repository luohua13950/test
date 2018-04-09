# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django import forms
from learn.models import User
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
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
            user = User.objects.filter(username = username,password = password)
            print username
            if user:
                passwd = User.objects.filter(username = username,password = password)
                if passwd:
                    info = '登录成功！'
                else:
                    info = '登录失败，请检查用户名和密码！'
            elif len(user) == 0:
                info = '输入是否正确？'
            return HttpResponse(info)
    else:
        uf = UserForm()
    #return render_to_response('login.html',{'uf':uf},RequestContext(request))
    return render(request,'login.html',{'uf':uf})
def index(request):
    return render(request,'login.html')

def regist(request):
    c = ({'name':'luohua'})
    return render(request,'regist.html',c)