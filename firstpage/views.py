from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse('Firstpage')
    return render(request,'firstpage/fp.html')
