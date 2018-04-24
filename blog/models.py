from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


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
    # 文章标题
    title = models.CharField(max_length=100)
    # 文章内容
    body = models.TextField()
    # 文章分类
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # 创建时间
    created_time = models.DateTimeField(auto_now_add=True)
    # 修改时间
    modified_time = models.DateTimeField(auto_now=True)
    # 作者
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 标签
    tags = models.ManyToManyField(Tag)
    # 访问量
    page_view = models.IntegerField(default=0)
    # 称赞量
    praise = models.IntegerField(default=0)
    # 谴责量
    censure = models.IntegerField(default=0)
    # 评论量
    comments = models.IntegerField(default=0)


    def __str__(self):
        return self.title
