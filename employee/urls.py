from django.urls import path
from employee import views
from .views import UserDeleteView, UserCreateForm


app_name = 'employee'

urlpatterns = [
    path('staff', views.staff_panel, name='staff_panel'),
    path('employee', views.employee_panel, name='employee_panel'),
    path('add_employee', views.add_employee, name='add_employee'),
    path('remove_employee/<str:pk>',UserDeleteView.as_view(), name='remove_employee'),
]