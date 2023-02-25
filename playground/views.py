from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def calcul():
    x=1
    y=2
    return x+y
def say_hello(request):
    x=calcul()
    return render(request,'hello.html')