from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
# User = get_user_model()

# Create your models here.

class MyUser(AbstractUser):
    """ 自定义的用户模型 """
    # 用户头像的路径
    head_portrait = models.CharField(max_length=100)
    # 用户昵称
    nick_name = models.CharField(max_length=20, default='')
    # 用户性别, 默认值为2,性别隐藏
    sex = models.IntegerField(default=2)
    # 用户简介
    bio = models.CharField(max_length=100, default='')
    # 关注人数
    following = models.IntegerField(default=0)
    # 粉丝数
    followers = models.IntegerField(default=0)
    # 博客数
    articles = models.IntegerField(default=0)
    # 评论数
    comments = models.IntegerField(default=0)