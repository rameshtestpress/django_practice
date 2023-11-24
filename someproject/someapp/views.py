from django.shortcuts import render
import datetime
from someapp.models import Employee

def display(request):
    emp_data=Employee.objects.all()
    emp_dict={'emp_list':emp_data}
    return render(request,'someapp/index.html',emp_dict)

# sending dynamic data to html by using dict{}

# def display(request):
#     date=datetime.datetime.now()
#     date_dict={'date':date}
#     return render(request,'someapp/index.html',context=date_dict)
    
# from django.http import HttpResponse

# def hello(response):
#     return HttpResponse('hello')

# Create your views here.
