"""myfirstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
app_name='ratings'
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^firstpage/',include('firstpage.urls')),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^data_analysis/',include('data_analysis.urls')),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings')),
    url(r'^post/',include('post.urls')),]                                          
   #path('accounts/', include('django.contrib.auth.urls'))
