from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def my_page(request):
    return render (request,"newpage.html")

def next_page(request):
    return render(request,"nextpage.html")

def third(request):
    return render (request,"third.html")


