from django import forms
from django.shortcuts import render
from django.http import HttpResponse

from platinForm.form import platinForm

def hello(request):
    return render(request,'hello.html',{})

def platinPage(request,formAnswer={}):

    if request.method == 'POST':
        formAnswer = platinForm(request.POST)
        if formAnswer.is_valid():
            value = request.POST.get("platin","")
            wlist = value.split(" ")
            evalue = ''
            for nvalue in wlist:
                evalue += nvalue[-3:-2] + nvalue[:-3] + ' '
                print(evalue)   
    else:   
        formAnswer = platinForm()
        evalue = ""

    return render(request,'pform.html',{'evalue': evalue,'form' : formAnswer,'header': request.headers})

def englishPage(request,formAnswer={}):
        
    if request.method == 'POST':
        formAnswer = platinForm(request.POST)
        if formAnswer.is_valid():
            value = request.POST.get("english","")
            wlist = value.split(' ')
            pvalue = ''
            for nvalue in wlist:
                pvalue += nvalue[1:] + nvalue[:1] + 'ay '
                print(pvalue)   
    else:
        formAnswer = platinForm()
        pvalue = ""

    return render(request,'eform.html',{'pvalue':pvalue,'form' : formAnswer})