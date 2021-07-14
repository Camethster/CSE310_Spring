from django import forms
from django.shortcuts import render
from django.http import HttpResponse

from platinForm.form import platinForm

def hello(request):
    return render(request,'hello.html',{})

def platinPage(request,formAnswer={}):

    if request.method == 'POST':
        formAnswer = platinForm(request.POST)




    return render(request,'form.html',formAnswer)