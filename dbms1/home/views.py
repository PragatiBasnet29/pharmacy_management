from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.db import connection
import datetime
import json
from django.contrib import messages


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
        if doctorssn is None:
            return render(request,'appointment.html')

        raw_query = f"INSERT INTO prescriptions ( Doctor_SSN, Patient_SSN, Drug_TradeName, Date, Quantity) VALUES ( '{doctorssn}', '{patientssn}', '{drugtardename}', '{date}', {quantity})"
        print(raw_query)
        with connection.cursor() as cursor:
            try:
                cursor.execute(raw_query)
            except:
                messages.info(request, 'The doctor or patient has not been added please add them First!!')
                print("wronginfo")
                return render(request,'appointment.html')

    return render(request,'appointment.html')

def contract(request):
        
    if request.method=="GET":
        
            name = request.GET.get('name')
            pharmacy_id = request.GET.get('pharmacy_id')
            start_date = request.GET.get('start_date')
            end_date = request.GET.get('end_date')
            contract_text = request.GET.get('contract_text')
            raw_query = f"INSERT INTO contract (PharmaceuticalCo,Pharmacy_ID,Start_Date,End_Date ,Contract_Text  )  VALUES (  '{name}', '{pharmacy_id}','{start_date}', '{end_date}', {contract_text})"
            print(raw_query)
            if name is not None:
                with connection.cursor() as cursor:
                    cursor.execute(raw_query)

    return render(request,'contract.html')


def doctors(request):
    if request.method=="GET":
        
        name = request.GET.get('name')
        speciality = request.GET.get('speciality')
        years_of_experience = request.GET.get('start_date')
 
        raw_query = f"INSERT INTO doctors ( Name, Specialty, YearsOfExp)  VALUES (  '{name}', '{speciality}','{years_of_experience}')"
        print(raw_query)
        if name is not None:
            with connection.cursor() as cursor:
             cursor.execute(raw_query)

    return render(request,'Doctors.html')

def patients(request):
    if request.method=="GET":
        name = request.GET.get('name')
        address = request.GET.get('address')
        age = request.GET.get('age')
 
        raw_query = f"INSERT INTO patients ( Name, Address, Age)  VALUES (  '{name}', '{address}','{age}')"
        print(raw_query)
        if name is not None:
            with connection.cursor() as cursor:
                cursor.execute(raw_query)

    

    return render(request,'patients.html')

def phco(request):
     if request.method=="GET":
        company = request.GET.get('company')
        phone = request.GET.get('phone')
        
 
        raw_query = f"INSERT INTO PharmaceuticalCo ( CompanyName, Phone_Number)  VALUES (  '{company}', '{phone}')"
        print(raw_query)
        if company is not None:
            with connection.cursor() as cursor:
             cursor.execute(raw_query)


     return render(request,'PharmaceuticalCo.html')

def pharmacy(request):
     if request.method=="GET":
        name = request.GET.get('name')
        address = request.GET.get('address')
        phone= request.GET.get('phone')
 

        if name is not None:
 
            raw_query = f"INSERT INTO pharmacy (Name, Address,Phone_Number)  VALUES (  '{name}', '{address}','{phone}')"
            print(raw_query)
            with connection.cursor() as cursor:
                cursor.execute(raw_query)

     return render(request,'pharmacy.html')

def results(request):
    if request.method == 'GET':
        sql = request.GET.get('search')  
        print(sql)
        if sql is not None:
        #raw_query = "SELECT * FROM prescription_history"
            with connection.cursor() as cursor:
                cursor.execute(sql)
                columns = [col[0] for col in cursor.description]
                print(columns)
                rows = cursor.fetchall()
            # for row in rows:
                prescription_history_list = []
                for row in rows:
                        prescription_data = {
                            columns[i]:row[i] for i in range(len(columns))
                            
                        }

                        # Append the current prescription_data dictionary to the list
                        prescription_history_list.append(prescription_data)
                col_dict={
                    "col":columns
                    }
                

                print(str(prescription_history_list))
                print(str(col_dict))
            return render(request,'result.html',{'pre':prescription_history_list,"cols":'1'})

        return render(request,'result.html')
