from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def rohit(request):
    return render(request,'rohit.html')

def sky(request):
    return HttpResponse('<h1>Sky Has No Limits When He Is In Form</h1>')