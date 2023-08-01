from django.urls import path 
from . import views



urlpatterns = [
    path('',views.index,name="index"),
    path('hello/',views.hello_view,name="hello"),
    path('pescriptionhistory/',views.p_history,name="p_history"),
    path('appointment/',views.appointment,name="appointment"),
    path('contract/',views.contract,name="contract"),
    path('doctors/',views.doctors,name="doctors"),
    path('patients/',views.patients,name="patients"),
    path('Phco/',views.phco,name="phco"),
    path('pharmacy/',views.pharmacy,name="pharmacy"),
    path('results/',views.results,name="results"),

    



]
