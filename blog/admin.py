from django.contrib import admin
from blog.models import Category, Tag, Article

# Register your models here.

class AritcleAdmin(admin.ModelAdmin):
    """ 定制admin后台,显示更详细的信息 """
    list_display = ['title', 'author', 'category', 'created_time', 'modified_time']

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article, AritcleAdmin)
