from django.urls import path
from django.contrib.auth.views import login
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'users'

urlpatterns = [
    path('users/login/', login,
         {'template_name': 'users/login.html'}, name='login'),
    path('users/logout/', views.logout_view, name='logout'),
    path('users/register/', views.register, name='register'),
    path('users/setting/profile/', views.head_pic_setting, name='head_pic'),
    path('users/settings/upload_head_pic/', views.upload_head_pic, name='upload_head_pic'),
    path('users/settings/change_head_pic/', views.change_head_pic, name='change_head_pic'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
