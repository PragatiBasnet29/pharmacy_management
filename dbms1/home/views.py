from django.http import HttpResponse,JsonResponse
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

    if request.method == 'GET':
        patientssn = request.GET.get('patients-SSN') 
        patientname=request.GET.get('patientsName')   
        if patientssn is None or patientname is None:
            print(patientssn)
            return render(request,'pHistory.html')
        raw_query =f'''
                        SELECT h.doctor_ssn,d.name, h.drug_tradename,h.Date,h.quantity 
                        FROM prescriptions as h,patients as p,doctors as d 
                        where
                        p.SSN=h.patient_ssn and p.ssn={patientssn} and d.SSN=h.Doctor_SSN and p.name like "{patientname}";

                    ''' 
        raw_query2 =f'''
                        SELECT h.patient_ssn,p.name,p.address,p.age
                        FROM prescriptions as h,patients as p,doctors as d 
                        where
                        p.SSN=h.patient_ssn and p.ssn={patientssn} and d.SSN=h.Doctor_SSN and p.name like "{patientname}";

                    '''
        
        with connection.cursor() as cursor:
            try:
                cursor.execute(raw_query2)
            except:
                 messages.info(request, 'Give proper SSN and PatientName!!')
                 return render(request,'pHistory.html')
                  
            pat_detail = cursor.fetchone()
            patientdetails={"ssn":pat_detail[0],
                            "name":pat_detail[1],
                            "address":pat_detail[2],
                            "age":pat_detail[3]
                            }
            cursor.execute(raw_query)
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()

        

            prescription_history_list = []

            for row in rows:
                    
                # Sample data for the prescription history
                    prescription_data = {
                        "DOCTORSSN": row[0],
                        "DOCTORNAME": row[1],
                        # "DATE": str(datetime.date(2023, 7, 1))
                        "DRUG": row[2],
                        "DATE": row[3],
                        "quantity": row[4],
                          }

                    # Append the current prescription_data dictionary to the list
                    prescription_history_list.append(prescription_data)
            

            print(str(prescription_history_list))
        return render(request,'pHistory.html',{'pre':prescription_history_list,"pat":patientdetails})


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
                    try:
                        cursor.execute(raw_query)
                    except:
                        messages.info(request, 'Write Data in Correct form!!')
                        return render(request,'contract.html')
                        

    return render(request,'contract.html')


def doctors(request):
    if request.method=="GET":
        
        name = request.GET.get('name')
        speciality = request.GET.get('speciality')
        years_of_experience = request.GET.get('years_of_experience')
 
        raw_query = f"INSERT INTO doctors ( Name, Specialty, YearsOfExp)  VALUES (  '{name}', '{speciality}','{years_of_experience}')"
        print(raw_query)
        if name is not None:
            with connection.cursor() as cursor:
                try:
                    cursor.execute(raw_query)
                except:
                    messages.info(request, 'Write Data in Correct form!!!!')
                    render(request,'contract.html')

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
                try:
                    cursor.execute(raw_query)
                except:
                    messages.info(request, 'Write Data in Correct form!!!')
                    return render(request,'patients.html')


    

    return render(request,'patients.html')

def phco(request):
     if request.method=="GET":
        company = request.GET.get('company')
        phone = request.GET.get('phone')
        
 
        raw_query = f"INSERT INTO PharmaceuticalCo ( CompanyName, Phone_Number)  VALUES (  '{company}', '{phone}')"
        print(raw_query)
        if company is not None:
            with connection.cursor() as cursor:
             try:
                cursor.execute(raw_query)
             except:
                 messages.info(request, 'Write Data in Correct form!!!!')
                 return render(request,'PharmaceuticalCo.html')

     


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
                try:
                    cursor.execute(raw_query)
                except:
                    messages.info(request, 'Write Data in Correct form!!!!')
                    return render(request,'pharmacy.html')


     return render(request,'pharmacy.html')

def results(request):
    if request.method == 'GET':
        sql = request.GET.get('search')  
        #print(sql)
        if sql is not None:
        #raw_query = "SELECT * FROM prescription_history"
            with connection.cursor() as cursor:
                try:
                    cursor.execute(sql)
                except:
                    messages.info(request, 'Write proper sql query!!!!')
                    return render(request,'result.html')
                columns = [col[0] for col in cursor.description]
                #print(columns)
                rows = cursor.fetchall()
            # for row in rows:
                prescription_history_list = []
                for row in rows:
                        prescription_data = {
                            columns[i]:row[i] for i in range(len(columns))
                            
                        }

                        # Append the current prescription_data dictionary to the list
                        prescription_history_list.append(prescription_data)
               

               # print(str(prescription_history_list))
                #print(columns)
            return render(request,'result.html',{'pre':prescription_history_list,"cols":columns,"sql":sql})

        return render(request,'result.html')
    

def admin_view(request):
    return render(request,"adminpage.html")

def patient(request):
    return render(request,"patientpage.html")
def update(request):
     if request.method=="GET":
         data = request.POST.get('data')
         return render(request,"makeupdate.html",{"sql":sql,"data":data})
     if request.method=="POST":
        data = request.POST.get('data')
        sql = request.POST.get('sql')
        data_dict = eval(data)
        print(data_dict)
        print(sql)
        return render(request,"makeupdate.html",{"sql":sql,"data":data_dict})
     return render(request,"makeupdate.html",{"data":"nodata"})

def endpoint_view(request):
    if request.method == 'GET':
            # Retrieve the variables from the POST request
            payload = request.GET
            
            # Process the payload data as needed
            variable1 = payload.get('var1')
            variable2 = payload.get('var2')
            a=variable1
            b=variable2

            print(variable1)
            print(variable2)
            print("hi")
                

                
                # Retrieve more variables as needed
                
                # Process the dataS
                
                # Return a JSON response
            response_data = {'message': 'Success',"var1":variable1,"var2":variable2}
            return JsonResponse(response_data)
            
    else:
            # Handle other HTTP methods if needed
        return HttpResponse("cannot get coordinates")

