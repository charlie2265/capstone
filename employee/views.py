from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.http import HttpResponse
from .forms import UserCreateForm, UploadFileForm
from .models import EmployeeProfile, UploadFile



# Create your views here.
def employee_panel(request):
    return render(request, 'employee/employee_panel.html')

def staff_panel(request):
    users = User.objects.all()
    return render(request, 'employee/staff_panel.html', {'users': users})    

    
def add_employee(request):
    
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            return render(request,'add_remove/success.html', {'user': user})
    else:
        form = UserCreateForm()
    
    return render(request, 'add_remove/add_employee.html', {'form': form}) 
        

class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('employee:staff_panel')
    template_name = 'employee/confirm_remove_employee.html'
    context_object_name = 'user'

@login_required
def employee_panel(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = request.user
            upload.save()
            return redirect('/')
    else:
        form = UploadFile()
    return render(request, 'employee/employee_panel.html', {'form': form})



    

    

     
            
    


        



    
