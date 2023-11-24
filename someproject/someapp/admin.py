from django.contrib import admin
from django.contrib.admin import ModelAdmin
from someapp.models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    emp_details=['empno','empsal','empname']
    
    
admin.site.register(Employee,EmployeeAdmin)