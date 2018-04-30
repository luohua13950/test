__author__ = 'luohua139'
from django.conf.urls import url
from asset import views
urlpatterns=[
        url(r'^$',views.systeminfo,name='systeminfo'),
        url(r'^systeminfo/$',views.systeminfo,name='systeminfo'),
        url(r'^upload_hosts/$',views.upload_hosts,name='upload_hosts'),
        #url(r'^send_email/$',views.send_mail,name='sendemail')
        url(r'^sendmail/$',views.sendmail,name='sendmail')
        ]