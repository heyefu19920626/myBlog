from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    """ 文章表单 """
    class Meta:
        """docstring for Meta"""
        model = Article
        fields = ['title', 'body','category']
        TextInput = {'title': ''}
        Textarea = {'body': ''}
        ChoiceField = {'category': ''}
