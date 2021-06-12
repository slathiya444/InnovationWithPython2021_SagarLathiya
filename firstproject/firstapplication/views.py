from django.shortcuts import render
# from django.http import HttpResponse
from .forms import firstform
from .models import firstmodel

# Create your views here.

def function(request):
    context = {}
    form = firstform(request.POST or None)
    if form.is_valid():
        form.save()
        form = firstform()
    context['form'] = form
    return render(request,'home.html',context)

def result(request):
    dataset = firstmodel.objects.all()
    return render(request,'display.html',{'dataset' : dataset})