from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views
app_name='data_analysis'
urlpatterns=[path('showimage.png',views.showimage,name='showimage'),path('imagebokeh',views.imagebokeh,name='imagbokeh'),
             
		]
