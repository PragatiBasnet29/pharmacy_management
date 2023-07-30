from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

# Create your views here.

def index(request):
    return HttpResponse("hello")

def endpoint1(request):
    return JsonResponse({"hello":"hello"})
    


def endpoint2(request):
    pass