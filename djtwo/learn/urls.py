__author__ = 'luohua139'
from django.conf.urls import url
from learn import views
urlpatterns=[
    url(r'^$',views.login,name='login'),
    url(r'^login/$',views.login,name='login'),
    url(r'^regist/$',views.regist,name='regist'),
]