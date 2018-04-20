from django import forms
from .models import MyUser
from django.contrib.auth.forms import UserCreationForm


class MyUserCreateForm(UserCreationForm):
    """ 自定义表单 """
    class Meta:
        model = MyUser
        fields = ("username",)
