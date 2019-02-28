from django.urls import path

from employee import views

app_name = 'employee'

urlpatterns = [
    path('staff', views.staff_panel, name='staff_panel'),
    path('employee', views.employee_panel, name='employee_panel'),
    path('add_employee', views.add_employee, name='add_employee'),
    path('remove_employee',views.remove_employee, name='remove_employee')
]