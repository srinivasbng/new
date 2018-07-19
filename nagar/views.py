from django.shortcuts import render
from .forms import For
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request,'login.html')


def register(request):
    form=For(request.POST)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return render(request,'register.html',{'form':form})
        else:
            return HttpResponse('error occured')
    else:
        form=For()
        return render(request,'register.html',{'form':form})
