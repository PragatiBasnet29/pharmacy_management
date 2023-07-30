from django.shortcuts import render
from django.urls import include ,path
from . import views




urlpatterns = [
    path("",views.index,name="index"),
    path("endpoint1/",views.endpoint1,name="enp1"),

    path("/endpoint2/",views.endpoint2,name="enp2"),
    ]
