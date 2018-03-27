from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    """ 文章表单 """
    class Meta:
        """docstring for Meta"""
        model = Article
        fields = ['title', 'body',]
        labels = {'title': ''}
        widgets = {'body': forms.Textarea(attrs={'cols': 80})}
