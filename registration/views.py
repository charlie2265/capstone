from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        if user.is_staff:
            return redirect('employee:staff_panel')
        else:
            return redirect('employee:employee_panel')

def sign_in(request):
    if request.method == 'POST':
        return login_user(request)
    else:
        return render(request, 'registration/login.html')