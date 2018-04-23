from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name="index"),
    path('change_language/<language>/',
         views.change_language, name='change_language'),
    path('article/<int:article_id>/', views.article_details, name='article_details'),
    path('edit_article/<article_id>/', views.edit_article, name='edit_article'),
    path('new_article/', views.new_article, name='new_article'),
    path('article/preview_article/', views.preview_article, name='preview_article'),
]
