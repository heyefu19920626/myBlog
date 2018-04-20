from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
# User = get_user_model()

# Create your models here.

class MyUser(AbstractUser):
    """ 自定义的用户模型 """
    # 用户头像的路径
    head_portrait = models.CharField(max_length=100)