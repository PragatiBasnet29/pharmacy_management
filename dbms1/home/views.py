from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection

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
    print(', '.join(columns))

    # Print the data
    for row in rows:
        print(', '.join(str(value) for value in row))
    return render(request,'pHistory.html')