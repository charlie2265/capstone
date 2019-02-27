from django.shortcuts import render

# Create your views here.
def employee_panel(request):
    return render(request, 'employee/employee_panel.html')

def staff_panel(request):
    # link to go to a submit user view 
    # show existing users 
    # link to remove users
    # logout
    return render(request, 'employee/staff_panel.html')    
    
def add_employee(request):
    
    pass

def remove_employee(request):
    pass