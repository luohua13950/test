__author__ = 'luohua139'
from django.conf.urls import url
from learn import views
from djtwo import settings
urlpatterns=[
    url(r'^$',views.login,name='login'),
    url(r'^login/$',views.login,name='login'),
    url(r'^regist/$',views.regist,name='regist'),
    url(r'^index/$',views.index,name='index'),
    url(r'^changpass/$',views.changpass,name='changpass')
]