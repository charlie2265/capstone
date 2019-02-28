from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import logout

# Create your views here.
def employee_panel(request):
    return render(request, 'employee/employee_panel.html')

def staff_panel(request):
    users = User.objects.all()
    # link to go to a submit user view 
    # link to remove users
    return render(request, 'employee/staff_panel.html', {'users': users})    

    
def add_employee(request):
    
    return render(request, 'add_remove/add_employee.html') 
    
def remove_employee(request):
    
    return render(request, 'add_remove/remove_employee.html')