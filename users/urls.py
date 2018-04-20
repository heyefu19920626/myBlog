from django.urls import path
from django.contrib.auth.views import login

from . import views

app_name = 'users'

urlpatterns = [
    path('users/login/', login, {'template_name': 'users/login.html'}, name='login'),
    path('users/logout/', views.logout_view, name='logout'),
    path('users/register/', views.register, name='register'),
    path('users/setting/profile/', views.profile_setting, name='profile_setting'),
]
