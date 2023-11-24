from django import forms

class EmployeeInfoForm(forms.Form):
    name=forms.CharField()
    salary=forms.IntegerField()
    