from django.contrib import admin
from django.urls import path,include,re_path
from . import views
app_name='post'
urlpatterns= [ re_path(r'^(?P<genre>[\w]+)/$', views.genre,name="genre"),
               re_path(r'^(?P<slug>[\w-]+)/$',views.completepost,name="completepost"),]
    
