from django.urls import path, include
from registration import views
from django.contrib.auth import urls as auth_urls

app_name = 'registration'

urlpatterns = [
    # path('', include(auth_urls)),
    # path('register', views.register, name='register'),
    path('login/', views.sign_in, name='sign_in'),
]