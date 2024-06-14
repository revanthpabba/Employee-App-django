from django import forms
from .models import Employee

class Employee_form(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["empNo", "empName", "empSalary", "empAddress", ]
        #fields = "__all__"
        #labels = {"empNo": "EmpNo", "empName": "EmpName", "empSalary": "EmpSalary", "empAddress": "EmpAddress", }

        #We can specify all the fields from table like the above or the below(any one is specified.
        #Even we can specify the needed fields also
        