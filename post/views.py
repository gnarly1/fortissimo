from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
def genre(request,genre):
    #return HttpResponse(genre)
    posts=Post.objects.filter(genre=genre)
    #posts=Post.objects.all()
    return render(request,'post/postgenrelist.html',{'posts':posts})
    
def completepost(request,slug):
    post=Post.objects.filter(slug=slug)
    return render(request,'post/completepost.html',{'post':post})
