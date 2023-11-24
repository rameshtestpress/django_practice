from django.db import models

class Employee(models.Model):
    empno=models.IntegerField(default=0)
    empsal=models.IntegerField(default=0)
    empname=models.CharField(max_length=50,default='ramesh')
    
    def __str__(self):
        return self.empname