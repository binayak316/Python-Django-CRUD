from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

# Create your views here.

def employee_list(request):
    emp = Employee.objects.all()
    #emp vanne euta variable declare gareko
    #Emlopyee.objects.all vaneko Employee database ko model vanta sab data taneko
    #emp variable lai context ma key pair value ma dinu parxa
    context = {
        'emp': emp,
    }
    return render(request, "CRUD_app/list.html", context)

def create_employee(request):
    form = EmployeeForm()
    # calling Employee form
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee-list')
    #     employee-list vaneko url ko namespace ho jun index ko ho index page ma list dekhaune vaneko
    context = {
        'form': form
    }
    return render(request, "CRUD_app/create.html", context)

def update_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)
    #

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee-list')

    context = {
        'employee': employee,
        'form': form,
    }
    return render(request, "CRUD_app/update.html", context)

def delete_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method =='POST':
        employee.delete()
        return redirect('employee-list')
    context = {
        'employee': employee,
    }

    return render(request, "CRUD_app/delete.html", context)
