from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Employee
from .forms import Employee_form


def index(request):
    return render(request, 'home.html')


def create_view(request):
    form = Employee_form()
    if request.method == "POST":
        form = Employee_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('./display')
    return render(request, 'insert.html', context={'form': form})


def retrieve_view(request):
    employee = Employee.objects.all()
    return render(request, "index.html", context={"employee": employee})


def update_view(request, uid):
    employee = Employee.objects.get(id=uid)
    if request.method == "POST":
        form = Employee_form(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../display')
    else:
        form = Employee_form(initial={'empNo': employee.empNo, 'empName': employee.empName, 'empSalary':employee.empSalary, 'empAddress':employee.empAddress})
    return render(request, 'update.html', content={"form": form})


def delete_view(request, did):
    employee = Employee.objects.get(id=did)
    employee.delete()
    return HttpResponseRedirect('../display')