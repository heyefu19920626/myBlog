from django.db import models

# Create your models here.


class Category(models.Model):
    """ 分类模型 """
    name = models.CharField(max_length=100)

    def __str__(self):
        """ 返回模型的字符串表示 """
        # 此处返回分类名称
        return self.name


class Tag(models.Model):
    """ 标签模型 """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    """ 文章模型 """
    # 文章名称
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
