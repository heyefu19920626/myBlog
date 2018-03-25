from django.db import models

# Create your models here.

class Category(models.Model):
    """ 分类模型 """
    name = models.CharField(max_length=100)

class Tag(models.Model):
    """ 标签模型 """
    name = models.CharField(max_length=100)

class Article(models.Model):
    """ 文章模型 """
    # 文章名称
    name = models.CharField(max_length=100)