from django.http import HttpResponse
from django.shortcuts import render

def hello_view(request):
    return HttpResponse("hello")


def index(request):
    return render(request,'index.html')


def p_history(request):
    return render(request,'pHistory.html')