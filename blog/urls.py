from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name="index"),
    path('change_language/<language>/', views.change_language, name='change_language'),
    path('article/<article_id>/', views.article_details, name='article_details'),
]