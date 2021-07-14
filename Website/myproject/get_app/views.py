from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return render(request,'hello.html',{})

def form(request):

    forms =  {
        'number': request.user
    }



    return render(request,'form.html', forms)