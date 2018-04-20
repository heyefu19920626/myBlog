from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.

class MyUser(User):
    """ 自定义的用户模型 """
    # 用户头像的路径
    head_portrait = models.CharField(max_length=100)