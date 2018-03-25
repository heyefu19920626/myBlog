from django.db import models

# Create your models here.

class Category(models.Model):
    """ 分类模型 """
    name = models.CharField(max_length=100)
