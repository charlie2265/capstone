from django.urls import path

from employee import views

app_name = 'employee'

urlpatterns = [
    path('staff', views.staff_panel, name='staff_panel'),
    path('employee', views.employee_panel, name='employee_panel'),
]