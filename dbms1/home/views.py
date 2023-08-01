from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
import datetime
import json


def hello_view(request):
    return HttpResponse("hello")


def index(request):

    return render(request,'index.html')


def p_history(request):
    raw_query = "SELECT * FROM prescription_history"
    with connection.cursor() as cursor:
        cursor.execute(raw_query)
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()

    # Print the column names
    

    # Print the data
    for row in rows:
        
        

        

# Create an empty list to store prescription data for each row
        prescription_history_list = []

        for row in rows:
            # Sample data for the prescription history
                prescription_data = {
                    "PATIENTSSN": row[0],
                    "PATIENTNAME": row[1],
                    "PATIENTAGE": row[2],
                    "ADDRESS": row[3],
                    "DOCTORSSN": "1223",
                    "DOCTORNAME": 'DoctorName',
                    "SPECIALITY": 'General Physician',
                    "DATE": str(datetime.date(2023, 7, 1))
                }

                # Append the current prescription_data dictionary to the list
                prescription_history_list.append(prescription_data)
        

        print(str(prescription_history_list))
    return render(request,'pHistory.html',{'pre':prescription_history_list})


def appointment(request):
    if request.method=="GET":
        # values=request.GET.get()
        # print(values)
        print(request.GET.get('Date'))
        doctorssn = request.GET.get('DoctorSSN')
        patientssn = request.GET.get('PatientSSN')
        drugtardename = request.GET.get('DrugTradename')
        date = request.GET.get('Date')
        #date='2023-08-01'
        quantity = request.GET.get('Quantity')

        raw_query = f"INSERT INTO prescriptions ( Doctor_SSN, Patient_SSN, Drug_TradeName, Date, Quantity) VALUES ( '{doctorssn}', '{patientssn}', '{drugtardename}', '{date}', {quantity})"
        print(raw_query)
        with connection.cursor() as cursor:
            cursor.execute(raw_query)
        
    return render(request,'appointment.html')

def results(request):

    return render(request,'result.html')